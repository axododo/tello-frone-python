#mael et maathias
import keyboard # pour détecter les touches du clavier
from djitellopy import Tello    # importe tello depuis DJITelloPy
import time

# créer une instance de Tello
drone = Tello()

# se connecter au drone
drone.connect()

# décoller
batterie=drone.get_battery()
temperature=drone.get_temperature()
# initialiser les variables de commande
a_r = 0
t = 0
m_d = 0

def video():

# définir la taille de la fenêtre de la vidéo
    drone.streamon()

# boucle infinie pour afficher la vidéo
    while True:
        frame = drone.get_frame_read()
        if frame is None or frame.stopped:
            break
            cv2.imshow("Tello Video", frame.frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# libérer les ressources
        cv2.destroyAllWindows()
        frame.stop()
        drone.streamoff()
        drone.end()


while True:
    video()
    # détecter les touches du clavier
    if keyboard.is_pressed('a'): # avancer
        drone.takeoff()
    elif keyboard.is_pressed('e'): # avancer
        drone.land()
    elif keyboard.is_pressed('z'): # avancer
        a_r = 50
    elif keyboard.is_pressed('s'): # reculer
        a_r = -50
    elif keyboard.is_pressed('q'): # atterir
        t = 50
    elif keyboard.is_pressed('q'): # atterir
        t = -50
    elif keyboard.is_pressed('up'): # monter
        m_d = 50
    elif keyboard.is_pressed('down'): # descendre
        m_d = -50
    elif keyboard.is_pressed('left'): # tourner à gauche
        t = 50
    elif keyboard.is_pressed('right'): # tourner à droite
        t = -50
        # détecter les touches du clavier
    elif keyboard.is_pressed('a'): # avancer
        drone.takeoff()
    elif keyboard.is_pressed('e'): # avancer
        drone.land()
    elif keyboard.is_pressed('space'): # atterir
        drone.flip_forward()
    elif keyboard.is_pressed('t'): # atterir
        print(temperature)
    elif keyboard.is_pressed('b'): # atterir
        print(batterie)
        break
    else:
        drone.send_rc_control(t,a_r,m_d, 0)
        time.sleep(0.5)
        a_r = 0
        t = 0
        m_d = 0
        if batterie < 10 or temperature > 800000:
                print("ALERTE CRITIQUE")
                drone.land()


    # détecter les touches du clavier


# se déconnecter du drone
drone.end()
