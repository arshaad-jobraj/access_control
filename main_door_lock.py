import io
import os
import sys
import time
import requests
from datetime import datetime
from gpiozero import OutputDevice
import logging
import sys

main_door_relay = 26


main_door_lock = OutputDevice(main_door_relay,active_high=False)
main_door_lock.off()

def open_lock():
    main_door_lock.on()
    time.sleep(5)
    main_door_lock.off()
    print(datetime.now().isoformat(), 'Main Door opened by API')
    sys.stdout.flush()