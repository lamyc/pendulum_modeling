import subprocess
import os

def upload(file_path, port, timeout=60):
    '''function to upload .ino script to chip within python

    Parameters:
    ------------
    file_path: string
                absolute path or relative path of the script to be uploaded.
    port: string
            usb port to connect to the arduino chip.
    timeout: int, optional
            timeout in seconds, default is 60.
    '''

    ret = subprocess.run(["arduino", "--upload", "--port", port, file_path],
                         shell=False,
                         encoding="utf-8",
                         timeout=timeout)

    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)



if __name__ == "__main__":
    fpath = os.path.join("..","..", "nano_33", "script", "ReadAccelerometer",
            "ReadAccelerometer.ino")
    upload(fpath, "/dev/ttyACM0")

