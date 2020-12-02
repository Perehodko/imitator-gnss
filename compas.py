import serial


HDT = '$GPHDT,65.000,T*32'
HDG = '$GPHDG,65.0,,,0.1,T*15'
THS = '$GPTHS,338.01,A*1C'

# для проверки расчета Истинного курса тлько по HDG
# приоритет: HDG
# на нав виджете KK
HDG_KK = '$GPHDG,65.0,1,,0.5,T*09'

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

l = [HDT, HDG_WITHOUT_MV, THS]
sent = []

for i in l:
    sent.append(i)

for i in range(1, 100000):
    for i in range(len(l)):
        with serial.Serial() as ser:
            ser.port = '/dev/ttyMXUSB4'
            ser.open()
            ser.write(l[i].encode('utf-8'))
            # sleep(1)
            print(l[i])
