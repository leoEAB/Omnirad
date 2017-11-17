#Hauptklasse fuer die Bewegung des Roboters
#Durch Benutzereingaben, welche ueber eine GUI ausgewaehlt werden, wird der Roboter in Bewegung gesetzt 
import RPi.GPIO as GPIO
from time import sleep

#Namensdefinition GPIO-Pins, BOARD = Pins 1 - 40
GPIO.setmode(GPIO.BOARD)

#Zuweisungen
M1in1 = 13 #Motor 1 Input 1 Motortreiber 1
M1in2 = 15 #Motor 1 Input 2 Motortreiber 1
M2in3 = 16 #Motor 2 Input 3 Motortreiber 1
M2in4 = 18 #Motor 2 Input 4 Motortreiber 1
M3in1 = 38 #Motor 3 Input 1 Motortreiber 2
M3in2 = 40 #Motor 3 Input 2 Motortreiber 2

M1_pwm = 11 #Motor 1 Enable A Motortreiber 1
M2_pwm = 12 #Motor 2 Enable B Motortreiber 1
M3_pwm = 36 #Motor 3 Enable A Motortreiber 2

Enc1A = 35 #Encoder an Motor 1 Kanal A
Enc1B = 37 #Encoder an Motor 1 Kanal B
Enc2A = 31 #Encoder an Motor 2 Kanal A
Enc2B = 33 #Encoder an Motor 2 Kanal B
Enc3A = 29 #Encoder an Motor 3 Kanal A
Enc3B = 32 #Encoder an Motor 3 Kanal B

#GPIO-Pins als Output-Pins initialisieren
GPIO.setup(M1in1, GPIO.OUT)
GPIO.setup(M1in2, GPIO.OUT)
GPIO.setup(M2in3, GPIO.OUT)
GPIO.setup(M2in4, GPIO.OUT)
GPIO.setup(M3in1, GPIO.OUT)
GPIO.setup(M3in2, GPIO.OUT)

#Initialisierung der drei PWM-Kanaele fuer jeden Motor einzeln
GPIO.setup(M1_pwm, GPIO.OUT)
GPIO.setup(M2_pwm, GPIO.OUT)
GPIO.setup(M3_pwm, GPIO.OUT)

#GPIO-Pins als Input-Pins initialisieren
GPIO.setup(Enc1A, GPIO.IN) #Encoder 1 Kanal A
GPIO.setup(Enc1B, GPIO.IN) #Encoder 1 Kanal B
GPIO.setup(Enc2A, GPIO.IN) #Encoder 2 Kanal A
GPIO.setup(Enc2B, GPIO.IN) #Encoder 2 Kanal B
GPIO.setup(Enc3A, GPIO.IN) #Encoder 3 Kanal A
GPIO.setup(Enc3B, GPIO.IN) #Encoder 3 Kanal B

#Pulsweitenmodulation Zuweisung und Maximalgrenze
PWM1 = GPIO.PWM(M1_pwm, 100)
PWM2 = GPIO.PWM(M2_pwm, 100)
PWM3 = GPIO.PWM(M3_pwm, 100)

#Pulsweitenmodulation starten
PWM1.start(0)
PWM2.start(0)
PWM3.start(0)

#Startgeschwindigkeit Initialiserung
speed = 50
length = 0

#----- Motor 1 - PWM, Wahrheitstabelle ----

#Motor 1 Drehung links
def M1_left(speed):
	PWM1.ChangeDutyCycle(speed)
	GPIO.output(M1_pwm, 1)
	GPIO.output(M1in1, 1)
	GPIO.output(M1in2, 0)

#Motor 1 Drehung rechts
def M1_right(speed):
	PWM1.ChangeDutyCycle(speed)
	GPIO.output(M1_pwm, 1)
	GPIO.output(M1in1, 0)
	GPIO.output(M1in2, 1)

#Motor 1 Stopp
def M1_stop():
	GPIO.output(M1_pwm, 1)
	GPIO.output(M1in1, 1)
	GPIO.output(M1in2, 1)

#----- Motor 2 - PWM, Wahrheitstabelle ----

#Motor 2 Drehung links
def M2_left(speed):
	PWM2.ChangeDutyCycle(speed)
	GPIO.output(M2_pwm, 1)
	GPIO.output(M2in3, 1)
	GPIO.output(M2in4, 0)

#Motor 2 Drehung rechts
def M2_right(speed):
	PWM2.ChangeDutyCycle(speed)
	GPIO.output(M2_pwm, 1)
	GPIO.output(M2in3, 0)
	GPIO.output(M2in4, 1)

#Motor 2 Stopp
def M2_stop():
	GPIO.output(M2_pwm, 1)
	GPIO.output(M2in3, 1)
	GPIO.output(M2in4, 1)


#----- Motor 3 - PWM, Wahrheitstabelle ----

#Motor 3 Drehung links
def M3_left(speed):
	PWM3.ChangeDutyCycle(speed)
	GPIO.output(M3_pwm, 1)
	GPIO.output(M3in1, 1)
	GPIO.output(M3in2, 0)

#Motor 3 Drehung rechts
def M3_right(speed):
	PWM3.ChangeDutyCycle(speed)
	GPIO.output(M3_pwm, 1)
	GPIO.output(M3in1, 0)
	GPIO.output(M3in2, 1)

#Motor 3 Stopp
def M3_stop():
	GPIO.output(M3_pwm, 1)
	GPIO.output(M3in1, 1)
	GPIO.output(M3in2, 1)


#------------------------
#Motor 1 und 2: Vorwaerts (Norden)
def forward_12(speed):
	M1_left(speed)
	M2_right(speed)

#Motor 1 und 2: Rueckwaerts (Sueden)
def back_12(speed):
	M1_right(speed)
	M2_left(speed)	

#Motor 1 und 2 gemeinsames stoppen
def stop_12():
	M1_stop()
	M2_stop()
	sleep(0.5)	#Anhalten der Anwendung, damit stoppen sichergestellt wird

#Drehung aller Motoren aus dem Stand nach links
def pivot_left(speed):
	M1_left(speed)
	M2_left(speed)
	M3_left(speed)

#Drehung aller Motoren aus dem Stand nach rechts
def pivot_right(speed):
	M1_right(speed)
	M2_right(speed)
	M3_right(speed)

#alle Motoren gemeinsam stoppen
def stop_all():
	M1_stop()
	M2_stop()
	M3_stop()
	sleep(0.5)

#Input-Funktion fuer Benutzereingaben
#Testen auf fehlerhafte Eingabe, da Integer-Wert erwartet wird
#Parameterliste: String, Int, Int
#String: Benutzerhinweis fuer Grenzen
#Int: min- und max-Werte fuer Grenzen
def get_int(prompt, min, max):
	while True:
		antwort = raw_input(prompt)
		try:
			antwort = int(antwort)
			if min <= antwort <= max:
				return antwort
			else:
				print("Bitte Bereich einhalten!")
		except ValueError:
			print("Bitte eine Zahl eingeben!")

#Encoder-Messungen 
#Paramaterliste: length=Pulse
def measure_encoder(length):
	Enc1A_state = 0
	Enc1A_state_old = 0
	counter = 0
	while True: 									#Dauerschleife
		Enc1A_state = GPIO.input(Enc1A)             #Zustand am Encoder-Pins
		if ((not Enc1A_state_old) and Enc1A_state): #sobald Zustandsaenderungen am Encoder-Pin, hochzaehlen der Zaehlvariable
			counter += 1
		Enc1A_state_old = Enc1A_state               #alten Zustand mit neuem Zustand ueberschreiben

		if counter == length: 						#Abbruchbedingung fuer Dauerschleife, sobald Encoderpulse mit vorgegebener Streckenlaenge uebereinstimmt 
			counter = 0   							#Ruecksetzen des Zaehlers
			stop_all()    							#Stoppen aller Motoren
			sleep(0.5)    							#Anhalten der Anwendung fuer 0,5 Sekunden, damit gestoppt werden kann
			break         							#Verlassen der Dauerschleife

#Set: Bewegung 
#Benutzereingabe: Funktionsaufruf Bewegungsart
MOVE = {
	1: forward_12,
	2: back_12
}
	
#Set: Streckenlaenge   
#Benutzereingabe: Pulse
LENGTH = {
	1: 95,
	2: 190,
	3: 285,
	4: 380,
	5: 475
}

#PWM-Geschwindigkeiten 
#Benutzereingabe: langsam, mittel, schnell
SPEED = {
	1: 10,
	2: 50,
	3: 100
}

#Hauptfunktion
def main():
	#Initialisierung der Encoderzustaende
	Enc1A_state = 0
	Enc1A_state_old = 0
	Enc2A_state = 0
	Enc2A_state_old = 0
	Enc3A_state = 0
	Enc3A_state_old = 0
	
	#Initialisierung der Zaehlvariable
	counter = 0
	
	#Variablen fuer Benutzereingaben
	move_in = 0
	length_in = 0
	speed_in = 0
	
	#Initialisierung der Streckenlaenge und Geschwindigkeit
	length = 0
	speed_value = 0
	
	#GUI
	print("\nSteuerung der Omnirad Plattform\n")

	#Dauerschleife, Abbruchbedingung bei Eingabe von Zahlenwert Null
	while True: 
		print("Bitte Bewegungsart eingeben oder Programm beenden: ")
		print("0 = Beenden\n\n1 = Vorwaerts\n2 = Rueckwearts\n3 = Linksdrehung 45Grad\n4 = Rechtsdrehung 45Grad")
		auswahl = get_int("Auswahl: ", 0, 4) #Benutzereingabe
		if auswahl == 0: break               #Anwendung beenden, sobald 0 gewaehlt
		
		#sobald Benutzer Richtung auswaehlt, stehen Geschwindigkeit und Streckenlaenge zur Auswahl
		if auswahl == 1 or auswahl == 2:					
			print("Bitte Geschwindigkeit eingeben: ")
			print("1 = langsam\n2 = mittel\n3 = schnell")
			speed_in = get_int("Auswahl: ", 1, 3) 
		
			print("Bitte Streckenlaenge eingeben: ")
			print("1 = 10cm\n2 = 20cm\n3 = 30cm\n4 = 40cm\n5 = 50cm")
			length_in = get_int("Auswahl: ", 1, 5)
			length = LENGTH[length_in]
		 
 			#Aufruf des Geschwindigkeits-Sets
			if speed_in in SPEED: 
				speed_value = SPEED[speed_in]
				MOVE[auswahl](speed_value)	#Bewegungsauswahl des Benutzers, vorwarts oder rueckwaerts		
			
			measure_encoder(length) 		#Funktionsaufruf: Encodermessungen
		
		#45 Grad Linksdrehung, sobald Benutzer 3 eingibt, vordefinierte Geschwindigkeit und Streckenlaenge			
		elif auswahl == 3:
			pivot_left(100)
			measure_encoder(90)
		
		#45 Grad Rechtsderhung, sobald Benutzer 4 eingibt, vordefinierte Geschwindigkeit und Streckenlaenge
		elif auswahl == 4:
			pivot_right(100)
			measure_encoder(90)	

#Stoppen aller Motoren, GPIO-Pins freigeben		
def quit():
	stop_all()
	GPIO.cleanup()

#Aufruf der Mainfunktion, sobald abgeschlossen, wird quit-Funktion aufgerufen
main()
quit()

