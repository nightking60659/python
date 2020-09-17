import os


class SettingProperty:

    @property
    def conntion(self):
        return {
            'IP': ip,
            'userName': account,
            'pwd': password
        }

    @property
    def fileSetting(self):
        return {'clock': {
            'remotePath': remotePath,
            'localPath': local,
            'year': 2,
            'month': 2,
            'day': 2,
            'empId': 5,
            'FileName':'TimeClock'
        }, 'other': {  # Gp
            'remotePath': remotePath,
            'localPath': local
        }}
