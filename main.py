from pyadb import PyAdb


def main():
    for dev in PyAdb.get_devices():
        print(dev)


if __name__ == '__main__':
    main()
