import serial

# positive
HDT = '$GPHDT,65.000,T*32'
HDG = '$GPHDG,65.0,,,0.1,T*16'
THS = '$GPTHS,338.01,A*1C'

# для проверки расчета Истинного курса тлько по HDG
# приоритет: HDG
# на нав виджете KK --> 66,5
HDG_KK = '$GPHDG,65.0,1,,0.5,T*23'

# для проверки расчета Истинного курса, когда в HDG нет MV
# значение берется из RMC
HDG_WITHOUT_MV = '$GPHDG,65.0,1,,,T*08'

# Нет данных о магнитном склонении
HDG_MAGN_EMPTY = '$GPHDG,65.0,,,,T*15'

# Режим cчисления курса
THS_E = '$GPTHS,338.01,E*0A'
# Режим симуляции курса
THS_S = '$GPTHS,338.01,S*1C'

GSA_TRASH = '$GNGSA,F,3,80,71,73,79,69,,,,,,,,1.83,4.0,1.47*2C'
TRASH = '��ܔE#���n�Dhh��#���k���n�-f�-k��n��#����DnDJKk��n�Kk�-�#�����-�#���Jk��Jk�n�N�#���Jk�n�D�)��#��'
HDG_E = '$GPHDG,,,,,'

list_s = [HDT, HDG, THS]
sent = []

for i in list_s:
    sent.append(i)

while True:
    try:
        for i in range(len(list_s)):
            with serial.Serial() as ser:
                ser.port = '/dev/ttyMXUSB4'
                ser.open()
                ser.write(list_s[i].encode('utf-8'))
                print(list_s[i])
    except Exception as e:
        print("Такого устройства нет", e)
        break
