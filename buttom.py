import sys
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
CURRENT_STATE = False
  
SEQUENCE = [[1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]]

def my_callback(channel):
    global CURRENT_STATE
    CURRENT_STATE = not CURRENT_STATE
   
STEPPER_PINS = [17,18,27,22]
for pin in STEPPER_PINS:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(23, GPIO.RISING, callback=my_callback, bouncetime=300)
               
SEQUENCE_COUNT = len(SEQUENCE)
PINS_COUNT = len(STEPPER_PINS)
                
sequence_index = 0
direction = 1
                 
if len(sys.argv)>1:
    wait_time = int(sys.argv[1])/float(1000)
else:
    wait_time = 1/float(1000)

try:
    while True:
        if CURRENT_STATE:
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])
            sequence_index = (sequence_index + direction) % SEQUENCE_COUNT
        else:
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], 0)
            sequence_index = 0
        time.sleep(wait_time)
except KeyboardInterrupt:
    print('Exit')
finally:
    GPIO.cleanup()
