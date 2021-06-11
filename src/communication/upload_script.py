import subprocess
import os

def upload(file_path, port, timeout=1):
    ret = subprocess.run(["arduino", "--upload", "--port", port, "-v", file_path],
                         shell=True,
                         encoding="utf-8",
                         timeout=timeout)

    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)



if __name__ == "__main__":
    fpath = os.path.join("..", "..", "nano_33", "script", "ReadAccelerometer",
            "ReadAccelerometer.ino")
    upload(fpath, "/dev/ttyS4")

