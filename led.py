import time
import Adafruit_PCA9685

# Initialize the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 10  # Min pulse length out of 4096
servo_max = 4090  # Max pulse length out of 4096

# Set the frequency of pulses for red leds
def set_red_freq(pwm, freq):
    pwm.set_pwm(0, 0, freq)
    pwm.set_pwm(1, 0, freq)

# Set the frequency of pulses for red leds
def set_yellow_freq(pwm, freq):
    pwm.set_pwm(13, 0, freq)
    pwm.set_pwm(12, 0, freq)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    set_red_freq(pwm, servo_max)
    set_yellow_freq(pwm, servo_min)
    time.sleep(1)
    set_red_freq(pwm, servo_min)
    set_yellow_freq(pwm, servo_max)
    time.sleep(1)
