import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_json(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

    def add_ini(self,file_path,NewSection,new_key,new_value):
        config = MyConfigParser()
        # 读取现有的配置文件
        config.read(file_path, encoding="UTF-8")
        # 增加新的配置部分
        config.add_section(NewSection)
        config.set(NewSection, new_key, new_value)
        # 写回到配置文件
        with open(file_path, 'w') as configfile:
            config.write(configfile)

    def modify_ini(self, file_path,SectionName,key,new_value):
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        # 修改现有配置项
        config.set(SectionName, key, new_value)
        # 写回到配置文件
        with open('example.ini', 'w') as configfile:
            config.write(configfile)

    def remove_ini(self, file_path,SectionName,key):
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        # 删除配置项
        config.remove_option(SectionName, key)

        # 如果需要删除整个部分
        # config.remove_section(SectionName)

        # 写回到配置文件
        with open('example.ini', 'w') as configfile:
            config.write(configfile)


data = ReadFileData()