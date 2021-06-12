from src.communication.read import export_measurements, monitor
from src.communication.upload_script import upload
import os

# script_path = os.path.join("nano", "script", "ReadAccelerometer", "ReadAccelerometer.ino")
# upload(script_path)
path = os.path.join("nano_33", "measurements")
# export_measurements(60*60*8, path, "114Hz_2g.csv")
monitor()

