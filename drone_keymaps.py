import keyboard # pour détecter les touches du clavier
from djitellopy import Tello    # importe tello depuis DJITelloPy
import time
# créer une instance de Tello
drone = Tello()

# se connecter au drone
drone.connect()
t = 0
a_r = 0
m_d = 0
# décoller
drone.takeoff()

while True:
    # détecter les touches du clavier
    if keyboard.wait('z'): # avancer
        a_r = (50)
        time.sleep(0,5)
    elif keyboard.wait('s'): # reculer
        a_r = -50
        time.sleep(0,5)
    elif keyboard.wait('a'): # tourner à gauche
        t = 50
        time.sleep(0,5)
    elif keyboard.wait('q'): # tourner à droite
        t = -50
        time.sleep(0,5)
    elif keyboard.wait('d'): # monter
        m_d = 50
        time.sleep(0,5)
    elif keyboard.wait('e'): # descendre
        m_d = -50
        time.sleep(0,5)
    elif keyboard.wait('space'): # atterir
        drone.land()
        break
    else:
        drone.send_rc_control(t,a_r,m_d, 0)

# se déconnecter du drone
drone.end()
