import sys
import pysftp as sftp
import logging as logger
import config.model as config
import time

date_format = '%Y-%m-%d %H:%M:%S'
msg_format = '%(asctime)-15s %(filename)s :%(lineno)d'
logger.basicConfig(level=logger.INFO, format=msg_format, datefmt=date_format, filename='test.txt')
connection = config.SettingProperty().conntion
setting = config.SettingProperty().fileSetting

# 上傳平台
def processUpload(platform):
    if platform == 'paltfrom1':
        paltfrom1()
    elif platform == 'paltfrom2':
        paltfrom2()
    elif platform == 'paltfrom3':
        paltfrom3()
    elif platform == 'paltfrom4':
        paltfrom4()
    elif platform == 'paltfrom5':
        paltfrom5()
    else:
        print('error')


def paltfrom1():
    logger.info('paltfrom1 process')

    connSftp(setting.get('paltfrom1'))


def paltfrom2():
    logger.info('paltfrom2 process')

    connSftp(setting.get('paltfrom2'))


def paltfrom3():
    logger.info('paltfrom3 process')

    connSftp(setting.get('paltfrom3'))


def paltfrom4():
    print('paltfrom4 process')
    connSftp(setting.get('paltfrom4'))


def paltfrom5():
    print('paltfrom5 process')
    connSftp(setting.get('paltfrom5'))


# 設sftp連線
def connSftp(setting):
    print(setting)
    print(setting.get('localPath'))
    print(setting.get('remotePath'))
    # 連線資訊
    ip = connection.get('IP')
    user = connection.get('userName')
    pwd = connection.get('pwd')
    # date Format
    date = time.strftime('%Y%m%d%H%M%S', time.gmtime())
    local = setting.get('localPath')
    remote = setting.get('remotePath')
    id = setting.get('id')

    fileName = setting.get('destFileName')
    # 連線
    sf = sftp.Connection(ip, username=user, password=pwd)
    # try:               #TimeClockInbound.xlsx
    logger.info(remote + 'TimeClockInbound.xlsx' + ' to ' + local + 'test.xlsx')
    # 取遠端資料
    sf.get(remote + 'TimeClockInbound.xlsx', local + 'test.xlsx')
    # 放本地端資料
    sf.put(local + '20200511.txt', remote + fileName + '_' + date + '-' + id + '.txt')
    # except FileNotFoundError:
    #     print('File is not Found')
    sf.close()


if __name__ == '__main__':
    processUpload(str(sys.argv[1]))
