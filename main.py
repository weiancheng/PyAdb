from pyadb import PyAdb


def main():
    devices = PyAdb.get_devices()
    if len(devices) == 0:
        print('please plugin a device...')
        exit(-1)

    dev = PyAdb(devices[0])
    if not dev.is_connected():
        print('device is not connected')
        exit(-1)

    packages = dev.get_apk_list()
    if not packages:
        print('catch the list of package from device failed')

    ''' test reboot device '''
    if dev.is_connected():
        dev.reboot()
        if dev.is_connected():
            print('reboot failed')
            exit(-1)

    print("test adb success")
    exit(0)


if __name__ == '__main__':
    main()
