#coding=utf-8
from appium import webdriver
import yaml
import logging
import logging.config


file=open('../ymal/desired_caps.yaml','r')
data=yaml.load(file)
file.close()

# 该放在作用是从ConfigParser格式的文件中读取日志配置，同时如果当前脚本有配置log参数，则覆盖当前log配置选项。
CON_LOG='../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    file = open('../ymal/desired_caps.yaml','r')
    data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()
