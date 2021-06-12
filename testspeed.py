import serial
from adaptOS import get_nano_port
import time

script_path = os.path.join("nano", "script", "ReadAccelerometer", "ReadAccelerometer.ino")
upload(script_path)
start = time.perf_counter()
with serial.Serial(get_nano_port(), 115200, timeout=1) as ser:
    old = time.perf_counter_ns()
    while (time.perf_counter() - start < 2):
        line = ser.readline()
        new = time.perf_counter_ns()
        print(new-old, line.decode('UTF-8'))
        old = new
