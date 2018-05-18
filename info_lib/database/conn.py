from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from InformationManager.info_lib.parse import base
from sqlalchemy.exc import OperationalError

BaseModel = declarative_base()


class Conn(object):
    def __init__(self):
        self.initialize()

    def __del__(self):
        if self.flag:
            self.engine.dispose()

    def initialize(self,
                   pwd=base.MYS_PASSWD,
                   ip='localhost',
                   port=base.MYS_PORT,
                   database=base.MYS_BASIC_DATABASE):
        try:
          #  conn_str = 'mysql://root:%s@%s:%s/%s?charset=utf8&unix_socket=%s' % (pwd, ip,
          #                                                                       port,
          #                                                                       database,
          #                                                                       base.ALA_MYSQL_UNIX_SOCKET)
            conn_str = 'mysql+pymysql://root:%s@%s:%s/%s?charset=utf8' % (pwd, ip,
                                                                       port,
                                                                       database)
            self.engine = create_engine(
                conn_str,
                pool_recycle=3600,
                isolation_level="READ UNCOMMITTED")
            Session = sessionmaker(autoflush=False, bind=self.engine)
            self.session = Session()
            self.metadata = MetaData(self.engine)
            self.session.execute("show databases;")
        except Exception, e:
            self.flag = False
            return (base.DAT_DB_CONNECT_ERROR, e.message)
        else:
            self.flag = True
            return (base.SUCCESS, self)

    def commit(self, session):
        try:
            session.commit()
        except Exception, e:
            session.rollback()
            return (base.DAT_DB_COMMIT_ERROR, e.message + "db commit error")
        else:
            return (base.SUCCESS, "")
        finally:
            session.close()


if __name__ == "__main__":
    conn = Conn()
