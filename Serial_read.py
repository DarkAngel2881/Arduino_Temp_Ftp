import time as t
from ftp import *
import serial
from datetime import datetime
from numpy import average

#time of temp measurement
def time():
    now = datetime.now()
    today = datetime.today()
    current_time = now.strftime(" %H_%M_%S ") + today.strftime("%d-%m-%Y")
    return current_time


#create a new file named "city" + "time of measurement".txt
def new_file(city):
    filename = city + time() + ".txt"
    f = open(filename, "w")
    f.write("")
    f.close
    return filename


arduino = serial.Serial('COM10', 9600, timeout=0)
city_measurement = input("Enter the city you are measuring from (firt capital letter no spaces): ")

while True:
    filename = new_file(city_measurement)
    temps = []
    
    #take 10 temp measurements and write them in the file
    for i in range(1, 11):
        with open(filename, "a") as f:
            temp = arduino.readline().decode().rstrip()
            #temp = input(">>> ")
            temps.append(float(temp))
            print("Temp " + str (i) + ": \t" + temp + " \tC°\n")
            f.write("Temp " + str (i) + ": \t" + temp + " \tC°\n")
            if i==10:
                f.write("\n--Average temp = " + str(round(average(temps), 2)) + " C°--")
            t.sleep(2)
            f.close

    #ftp file
    send_temps(filename, city_measurement)

    
