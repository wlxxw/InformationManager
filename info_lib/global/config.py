# -*- coding: utf-8 -*-

import ConfigParser

CONFIG_DEF_FILE_NAME = "../etc/define.conf"
CONFIG_SET_FILE_NAME = "../etc/setting.conf"


class HyhiveConfig():
    def __init__(self):
        pass

    @staticmethod
    def load_config(file_name=CONFIG_DEF_FILE_NAME):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(file_name)
            sec_list = cf.sections()
            ret_dict = {}
            for sec_list_item in sec_list:
                item_list = cf.items(sec_list_item)
                prefix = sec_list_item[0:3] + "_"
                if prefix == "GLO_":
                    prefix = ""
                for item_element in item_list:
                    if str(item_element[1]).isdigit():
                        ret_dict[prefix + item_element[0].upper()] = eval(
                            item_element[1])
                    else:
                        ret_dict[prefix + item_element[0].upper()] = eval(
                            str(item_element[1]))
            return (0, ret_dict)
        except Exception as e:
            return (-1, e)


class CaptainConfig(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


if __name__ == "__main__":
    print HyhiveConfig().load_config()
    print HyhiveConfig().load_config(CONFIG_SET_FILE_NAME)
