import subprocess

def excuteCommand(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    status = process.wait(timeout=10 * 1000)
    process.kill()
    print("cmd in:", cmd)
    print("cmd out: ", out)
    return out


if __name__ == '__main__':
    excuteCommand("ls *.py")
    # excuteCommand('sudo airodump-ng wlan0')
