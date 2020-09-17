import pandas as pd
import Tool.config.model as config
import logging

date_formate = '%Y-%m-%d %H:%M:%S'
msg_format = '%(asctime)-15s %(filename)s :%(lineno)d'
logging.basicConfig(level=logging.INFO, format=msg_format, datefmt=date_formate)

setting = config.SettingProperty().fileSetting.get('clock')


def main():
    local = setting.get('localPath')
    remote = setting.get('remotePath')

    df = pd.read_table(local + '20200511.txt', sep=' ', index_col=None, header=None,
                       converters={0: lambda x: '20' + x, 1: str})
    # df.dropna(how='any')
    # logging.info(df.shape)
    df.shape
    # 去Nan資料
    dfdrop = df.dropna()
    dfdrop[1] = dfdrop[0] + dfdrop[1]
    dfdrop[0] = dfdrop[5]
    df2 = dfdrop.drop(columns=[2, 3, 4, 5])
    # df2 = df2.sort_values(by=[0, 1], ascending=(True, True))
    # print(df)
    # print('---------')
    # print(dfdrop)
    # print(dfdrop.iloc[0])
    # dfdrop.iloc[]
    # print(dfdrop.shape[0])
    # print(dfdrop.shape[1])
    print(df2)
    row = dfdrop.shape[0]
    col = dfdrop.shape[1]
    # 命名欄位
    df2 = df2.rename(columns={0: 'employeeId', 1: 'date'})
    # ecport csv
    df2.to_csv('export.txt', index=False, header=False)
    # export json
    df2.to_json('export2.txt', orient='index')
    df2.head()


if __name__ == '__main__':
    main()
