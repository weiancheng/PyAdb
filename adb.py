import subprocess


def adb_reboot(device=''):
    if 0 == len(device):
        cmd = 'adb reboot'
    else:
        cmd = 'adb -s ' + device + ' reboot'
    subprocess.call(cmd, shell=True)


def adb_devices():
    cmd = 'adb devices'
    return subprocess.getoutput(cmd)


def adb_install(apk_path, device=''):
    if len(device) == 0:
        cmd = 'adb install ' + apk_path
    else:
        cmd = 'adb -s ' + device + ' install -r ' + apk_path

    subprocess.call(cmd, shell=True)


def adb_uninstall(package, device=''):
    if len(device) == 0:
        cmd = 'adb uninstall ' + package
    else:
        cmd = 'adb -s ' + device + ' uninstall ' + package

    subprocess.call(cmd, shell=True)


def adb_shell(cmd, device=''):
    if len(device) == 0:
        adb_cmd = 'adb shell ' + cmd
    else:
        adb_cmd = 'adb -s ' + device + ' shell ' + cmd
    return subprocess.getoutput(adb_cmd)
