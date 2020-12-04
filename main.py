import serial
from time import sleep

DTM = '$GNDTM,,,,,,,,' #
ZDA = '$GPZDA,160012.71,11,03,2004,-1,00*7D'
# DTM = '$GNDTM,P90,,,,,,,W84*56'  # WGS84
RMC = '$GPRMC,225446,A,4916.45,N,12311.12,W,,054.7,191194,3,E*5F' # VALID
GSA = '$GNGSA,A,3,80,71,73,79,69,,,,,,,,1.83,4.0,1.47*2B'

GNS = '$GNGNS,112257.00,3844.24011,N,00908.43828,W,AN,03,5.5,,,,*7D'
VTG = '$GPVTG,220.86,T,,M,2.550,N,4.724,K,A*34'


GSA_TRASH = '$GNGSA,F,3,80,71,73,79,69,,,,,,,,1.83,4.0,1.47*2C'
GSA_EMPTY = '$GNGSA,,,,,,,,,,,,,,,,,*70'
TRASH = '��ܔE#���n�Dhh��#���k���n�-f�-k��n��#����DnDJKk��n�Kk�-�#�����-�#���Jk��Jk�n�N�#���Jk�n�D�)��#��'
#TRASH = "#%$%(*&#"
l = [ZDA, DTM, RMC, GSA]
sent = []

for i in l:
    sent.append(i)

while True:
    for i in range(len(l)):
        with serial.Serial() as ser:
            # ser.baudrate = 9600
            ser.port = '/dev/ttyMXUSB0'
            ser.open()
            ser.write(l[i].encode('utf-8'))
            # sleep(1)
            print(l[i])
