import keyboard # pour détecter les touches du clavier
from djitellopy import Tello    # importe tello depuis DJITelloPy
import time

# créer une instance de Tello
drone = Tello()

# se connecter au drone
drone.connect()

# initialiser les variables de commande
roll = 0
pitch = 0
yaw = 0
throttle = 0

# initialize drone state as "not_flying"
drone_state = "not_flying"

while True:
    try:
        # check if drone is connected
        if not drone.send_command("command"):
            print("Trying to reconnect...")
            drone.connect()
            time.sleep(1)
            continue

        # check drone state and battery level
        battery = drone.get_battery()
        temperature = drone.get_temperature()
        if battery < 50 or temperature > 30:
            print("Critical warning: battery low or temperature high")
            if drone_state == "flying":
                drone.land()
                drone_state = "not_flying"
                break

        # detect keyboard inputs
        if keyboard.is_pressed('a'): # take off
            if drone_state == "not_flying":
                drone.takeoff()
                drone_state = "flying"
        elif keyboard.is_pressed('e'): # land
            if drone_state == "flying":
                drone.land()
                drone_state = "not_flying"
        elif keyboard.is_pressed('z'): # move forward
            pitch = 50
        elif keyboard.is_pressed('s'): # move backward
            pitch = -50
        elif keyboard.is_pressed('q'): # move left
            roll = 50
        elif keyboard.is_pressed('d'): # move right
            roll = -50
        elif keyboard.is_pressed('up'): # move up
            throttle = 50
        elif keyboard.is_pressed('down'): # move down
            throttle = -50
        elif keyboard.is_pressed('left'): # rotate left
            yaw = 50
        elif keyboard.is_pressed('right'): # rotate right
            yaw = -50
        elif keyboard.is_pressed('space'): # perform flip
            drone.flip_front()
        elif keyboard.is_pressed('t'): # get temperature
            print(temperature)
        elif keyboard.is_pressed('b'): # get battery level
            print(battery)
            break
        else:
            # send movement commands
            drone.send_rc_control(roll, pitch, yaw, throttle)
            time.sleep(0.5)
            roll = 0
            pitch = 0
            yaw = 0
            throttle = 0
    except Exception as e:
        print("Error: ", e)
        break

# se déconnecter du drone
drone.end()
