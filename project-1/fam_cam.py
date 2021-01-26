from datetime import datetime
from gpiozero import Buzzer, LED, MotionSensor
from signal import pause
from text_me import texter

buzzer = Buzzer(4)
led = LED(14)
motion_sensor = MotionSensor(18)

def start_motion():
    detection = datetime.now()
    led.blink(0.5, 0.5)
    buzzer.beep(0.5, 0.5) 
    print(f"Motion detected at {detection}")
    texter(detection)

def end_motion():
    led.off() # Method to turn off the LED light
    buzzer.off() # Method to turn off the buzzer

print("Starting up the sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor ready")
motion_sensor.when_motion = start_motion
motion_sensor.when_no_motion = end_motion


pause()