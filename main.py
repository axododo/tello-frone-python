from djitellopy import tello    # importe tello depuis DJITelloPy
import time                     # pour utiliser sleep

drone = tello.Tello()           #crée un objet drone de classe tello

# definie les actions du drone
def start__drone():                              # deffinie une fonction
    i = 0                                        # declare une variable
    drone.takeoff()                              # decollage
    time.sleep(2)
    drone.send_rc_control(0,25,30,0)             # controle les mouvement du drone
    time.sleep(2)
    drone.send_rc_control(0,0,0,0)
    while i != 3:                                # declare une boucle qui s execute jusqu'a que i s incremente a 3
        drone.flip_back()                        # fait un backflip
        time.sleep(2)
        i += 1                                   # incremente i de 1
        pass
    drone.send_rc_control(0,-25,-30,0)
    time.sleep(2)
    drone.send_rc_control(0,0,0,0)
    drone.end()
    pass

# commence a executer les actions du drone 
drone.connect()                                  # se connecte au drone
battery = drone.get_battery()                    # recupere la batterie pour l'assigner a la variable
if battery > 55:                                 # verifie la battery
    start__drone()                               # execute la fonction start__drone()
else:
    print("batterie inssufisante")               # retourne si la batterie n'est pas suffisante
