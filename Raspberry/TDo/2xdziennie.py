from time import sleep
 
# bibioteka do raspberyPi dla GPIO
# https://forbot.pl/blog/kurs-raspberry-pi-podstawy-pythona-gpio-id26099
import RPi.GPIO as GPIO
 
# Numertyczne zarządzanie GPIO
GPIO.setmode(GPIO.BCM)
# Ustawiamy wyjście na tych pinach
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
 
 
#512 krokow to pelen obot
stepMotor_moves = 512
#szybkosc zmiany magnesow w ms
stepMotor_sleep = 0.003
#tablica z pinami IN1, IN2, IN3, IN4
stepMotor_pins = [26, 19, 13, 6]
 
def stepMotor_resetMagnets():
  GPIO.output(stepMotor_pins[0], GPIO.LOW)
  GPIO.output(stepMotor_pins[1], GPIO.LOW)
  GPIO.output(stepMotor_pins[2], GPIO.LOW)
  GPIO.output(stepMotor_pins[3], GPIO.LOW)
 
 
def stepMotor_moveForward():
  stepMotor_resetMagnets() # reset magnets before looping step motor
  for j in range(stepMotor_moves):
    # Forward - power on magnets in 1, 2, 3, 4 config with sleep every change
    for i in range(4):
      if i == 0:
        GPIO.output(stepMotor_pins[3], GPIO.LOW)
        GPIO.output(stepMotor_pins[0], GPIO.HIGH)
      elif i == 1:
        GPIO.output(stepMotor_pins[0], GPIO.LOW)
        GPIO.output(stepMotor_pins[1], GPIO.HIGH)
      elif i == 2:
        GPIO.output(stepMotor_pins[1], GPIO.LOW)
        GPIO.output(stepMotor_pins[2], GPIO.HIGH)
      elif i == 3:
        GPIO.output(stepMotor_pins[2], GPIO.LOW)
        GPIO.output(stepMotor_pins[3], GPIO.HIGH)
      sleep(stepMotor_sleep)
stepMotor_resetMagnets()
# release magnets
def stepMotor_moveBackward():
  stepMotor_resetMagnets() # reset magnets before looping step motor
  for j in range(stepMotor_moves):
     # Forward - power on magnets in 4, 3, 2, 1 config with sleep every change
    for i in range(4):
      if i == 0:
        GPIO.output(stepMotor_pins[0], GPIO.LOW)
        GPIO.output(stepMotor_pins[3], GPIO.HIGH)
      elif i == 1:
        GPIO.output(stepMotor_pins[3], GPIO.LOW)
        GPIO.output(stepMotor_pins[2], GPIO.HIGH)
      elif i == 2:
        GPIO.output(stepMotor_pins[2], GPIO.LOW)
        GPIO.output(stepMotor_pins[1], GPIO.HIGH)
      elif i == 3:
        GPIO.output(stepMotor_pins[1], GPIO.LOW)
        GPIO.output(stepMotor_pins[0], GPIO.HIGH)
      sleep(stepMotor_sleep)

  stepMotor_resetMagnets() # release magnets

while True:
  stepMotor_moveForward()
  print("Sleep 3s!")
  sleep(3)
  print("Moving backward!")
  stepMotor_moveBackward()
  sleep(43200)