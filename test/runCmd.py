import subprocess

def excuteCommand(com):
    ex = subprocess.Popen(com, stdout=subprocess.PIPE, shell=True)
    out, err  = ex.communicate()
    status = ex.wait(timeout=10*1000)
    print("cmd in:", com)
    print("cmd out: ", out)
    return out

if __name__ == '__main__':
    excuteCommand('sudo airodump-ng wlan0')