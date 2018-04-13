import re
import os
import adb


class PyAdb(object):
    def __init__(self, device_name):
        self.__dev_name = device_name

    def is_connected(self):
        ret = adb.adb_devices()
        pattern = self.__dev_name + '\s'
        r = re.search(pattern, ret)
        if r:
            return True
        return False

    def get_apk_list(self):
        if not self.is_connected():
            return None

        cmd = 'pm list packages'
        ret = adb.adb_shell(cmd, self.__dev_name)
        return ret.replace('package:', '').split("\n")

    def install_apk(self, path, package_name):
        if not self.is_connected():
            return False

        if not os.path.exists(path):
            print('file ' + path + ' is not exist')
            return False

        adb.adb_install(path, self.__dev_name)

        for package in self.get_apk_list():
            if package == package_name:
                return True
        return False

    def uninstall_apk(self, apk):
        if not self.is_connected():
            return False

        ''' remove package'''
        for package in self.get_apk_list():
            if package == apk:
                adb.adb_uninstall(apk, self.__dev_name)

        ''' check again'''
        for package in self.get_apk_list():
            if package == apk:
                ''' package is still exist'''
                return False

        return True

    def reboot(self):
        if not self.is_connected():
            return
        adb.adb_reboot(self.__dev_name)

    @staticmethod
    def get_devices():
        ret = adb.adb_devices()
        return re.findall("\n([\d\w]+)\s+device", ret)
