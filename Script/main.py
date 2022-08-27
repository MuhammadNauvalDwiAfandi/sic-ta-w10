import time
import numpy as np

from temperature import read_temp
from Oksi import Oksi, shutDownOksi
from sendUbidots import sendData
from location import getLocation, buildLocation


def logic(temp, spo2, bpm):
    '''
    Check condition using temperature, spo2, and bpm
    Take argument temp, spo2, bpm
    '''
    if spo2 <= 90:
        return 'Sakit parah'
    
    elif 90 < spo2 <= 95:
        if 36.5 <= temp <= 38.5:
            return 'Sakit'

        elif temp > 38.5:
            return 'Sakit parah'

        else:
            return 'Sakit'

    elif 95 < spo2 <= 100:
        if 36.5 <= temp <= 37.5:
            if bpm < 60:
                return 'Sakit'

            elif 60 <= bpm <= 100:
                return 'Normal'

            else:
                return 'Sakit parah'

        elif 37.5 < temp <= 38.5:
            return 'Sakit'

        elif temp > 38.5:
            return 'Sakit parah'

        else:
            return 'Sakit'

def averageOksi2(statusPrint=True, banyak=20):
    '''
    Find average hearth rate and spo2 measurment, accept bol int
    Take minimum 100 value by default
    Returning (averagehr, averagesp2)
    '''
    hr =[]
    sp2 = []
    
    while len(hr) <= banyak or len(sp2) <= banyak:
        dta = Oksi(statusPrint)

        if dta[2]:
            if dta[0] < 40:
                hr.append(40)
            elif dta[0] > 130:
                hr.append(130)
            else:
                hr.append(dta[0])

        if dta[3]:
            sp2.append(dta[1])

    avhr = int(np.average(hr))
    avsp2 = int(np.amax(sp2))

    return avhr, avsp2

def startSensor():
    '''
    Starting sensor, measure temperature, BPM, and SPO2
    Return (temperature, bpm, spo2)
    '''
    print('Mengukur...')

    oks = averageOksi2()
    time.sleep(5)

    temp = read_temp()

    return temp[0], oks[0], oks[1]

def main(name):
    dta = startSensor()
    status = logic(dta[0], dta[2], dta[1])
    location = getLocation()
    loc = buildLocation(location[0], location[1])


    print(f"Temperature     : {dta[0]}")
    print(f'BPM             : {dta[1]}')
    print(f'SPO2            : {dta[2]}')
    print(f'Health status   : {status}')
    print(f'Location        : {loc}')

    sendData(dta[1], name, dta[2], status, dta[0], loc)

if __name__ == '__main__':
    name = input('Enter name: ')
    main(name)

    time.sleep(1)
    shutDownOksi()
