import serial
from src.communication.adaptOS import get_nano_port
from src.communication.upload_script import upload
import time
import os

# script_path = os.path.join("nano_33", "script", "ReadAccelerometer", "ReadAccelerometer.ino")
# script_path = os.path.join("nano_33", "script", "print", "print.ino")
upload(script_path)
start = time.perf_counter()
with serial.Serial(get_nano_port(), 2000000, timeout=1) as ser:
    old = time.perf_counter_ns()
    while (time.perf_counter() - start < 2):
        line = ser.readline()
        new = time.perf_counter_ns()
        print(new-old, line.decode('UTF-8'))
        old = new
