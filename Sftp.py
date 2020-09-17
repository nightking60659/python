import sys
import pysftp as sftp
import logging
import config.model as config
import time

print('test')
print(sys.argv[1])
print(sys.argv)

date_formate = '%Y-%m-%d %H:%M:%S'
msg_format = '%(asctime)-15s %(filename)s :%(lineno)d'
logging.basicConfig(level=logging.INFO, format=msg_format, datefmt=date_formate, filename='test.txt')
connection = config.SettingProperty().conntion
setting = config.SettingProperty().fileSetting


def processUpload(platform):
    if platform == 'clock':
        clock()
    elif platform == 'gp':
        gp()
    elif platform == 'mr':
        mr()
    else:
        print('error')


def clock():
    logging.info('clock process')

    connSftp(setting.get('clock'))


def gp():
    print('gp process')
    connSftp(setting.get('gp'))


def mr():
    print('mr process')
    connSftp(setting.get('mr'))


# 設定順序
def connSftp(setting):
    print(setting)
    print(setting.get('localPath'))
    print(setting.get('remotePath'))

    ip = connection.get('IP')
    user = connection.get('userName')
    pwd = connection.get('pwd')

    time.gmtime()
    print(time.gmtime())
    print(time.strftime('%Y%m%d', time.gmtime()))
    date = time.strftime('%Y%m%d', time.gmtime())
    local = setting.get('localPath')
    remote = setting.get('remotePath')

    fileName = setting.get('FileName')
    sf = sftp.Connection(ip, username=user, password=pwd)
    try:
    # 取遠端資料
        sf.get(remote + 'TimeClockInbound.xlsx', local + 'test.xlsx')
    # 放本地端資料
        sf.put(local + '20200511.txt', remote + fileName + '_' + date + '.txt')
    except FileNotFoundError:
        print('File is not Found')
    sf.close()


if __name__ == '__main__':
    processUpload(str(sys.argv[1]))
