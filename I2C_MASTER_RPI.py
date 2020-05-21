import time
import subprocess

#our address of the device
ADDRESS = 0x08
RESCODE = "0x41\n" ##hex code UTF-8 for A, B, C, D
RES2CODE = "0x42\n" ## for F
RES3CODE = "0x43\n"
RES4CODE = "0x44\n"

try:
    while True:
        ##value = os.system("i2cget -y 1 " + str(ADDRESS))
        ##val = subprocess.run(['i2cget', '-y', '1', str(ADDRESS)], stdout=subprocess.PIPE)
        value = subprocess.check_output(['i2cget', '-y', '1', str(ADDRESS)])
        ##str_val = val.stdout.decode('utf-8')
        str_value = value.decode('utf-8')
        
        if str_value == RESCODE:
            print("TOO CLOSE")
        elif str_value == RES2CODE:
            print("Close enough")
        elif str_value == RES3CODE:
            print("Far enough")
        elif str_value == RES4CODE:
            print("FARRRR")
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit requested")
