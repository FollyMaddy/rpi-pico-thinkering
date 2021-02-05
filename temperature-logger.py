import uos
from machine import Pin
import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    f = open('data.txt', 'a')
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    #convert a variable in to string, otherwise it will not save
    writetemp = repr(temperature)
    f.write(writetemp + '\n' )
    f.close()
    utime.sleep(1)
    led.value(0)
    utime.sleep(59)
    #these are testlines to see if the data is saved
    #r = open('data.txt')
    #print(r.read())
    #r.close()
    #print(uos.listdir())
    #print(uos.statvfs('data.txt'))
    
