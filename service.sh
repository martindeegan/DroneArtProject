#!/bin/bash
# To be run on raspberry pi

# Runs the led.py script on power up
sudo cp led.service /lib/systemd/system/led.service

sudo systemctl daemon-reload
sudo systemctl enable led.service
sudo reboot

