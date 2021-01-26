from gpiozero import Button
from signal import pause

button = Button(4, hold_time = 3.0)

def buttonPressed():
    print("Button was pressed.")
def buttonHeld():
    print("Button was held.")
def buttonReleased():
    print("Button was released.")

button.when_pressed = buttonPressed
button.when_held = buttonHeld
button.when_released = buttonReleased

pause()
    