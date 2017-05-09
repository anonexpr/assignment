#!/usr/bin/env python
"""
This programs works in python version 3.5.2
This program checks the macbook battery status
Generate a voice alert when laptop battery charge is below 40%,
the alert should be triggered every 15 minutes in beginning and
when the charge is below 10%, trigger alert every 2 minutes
"""
import shlex
import subprocess
import time

def battery_status():
    """
    This function returns the percentage of charge remaining in laptop
    """
    battery_comm = 'pmset -g batt'
    args = shlex.split(battery_comm)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout = process.communicate()[0].decode("utf-8").replace("\n", "")
    batt_status = stdout.split()
    return batt_status[6].replace('%;', '')

def alert():
    """
    This function makes voice alerts based on laptop battery status
    """
    high_threshold = 40
    low_threshold = 10

    voice_alert_high_threshold = 'say battery charge below %s' % (high_threshold)
    voice_alert_low_threshold = 'say battery charge below %s' % (low_threshold)

    args_high = shlex.split(voice_alert_high_threshold)
    args_low = shlex.split(voice_alert_low_threshold)

    while True:
        charge = int(battery_status())
        if charge <= high_threshold and charge > low_threshold:
            subprocess.run(args_high)
            time.sleep(900)
        elif charge <= low_threshold:
            subprocess.run(args_low)
            time.sleep(120)

if __name__ == "__main__":
    alert()
