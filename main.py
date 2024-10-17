import RPi.GPIO as GPIO
import time

relay_pin = 21  # = GPIO 21 = Pin 40
temp = 2 # temps en secondes

# setup des broches GPIO
GPIO.setwarnings(False)  # désactive les messages d'alerte
GPIO.setmode(GPIO.BCM)  # Utilisation de la numérotation BCM
GPIO.setup(relay_pin, GPIO.OUT)  # initialise la broche en sortie

try:
    while True:
        GPIO.output(relay_pin, GPIO.HIGH)  # allume le relais
        time.sleep(temp)  # attendre x secondes

        GPIO.output(relay_pin, GPIO.LOW)  # eteint le relais
        time.sleep(temp)  # attendre x secondes

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.cleanup()  # nettoie les broches GPIO
