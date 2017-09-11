#importing the modules
from sense_hat import SenseHat
from time import sleep, gmtime, strftime
import time 

SH = SenseHat()

SH.clear()

F = open('II project - data.csv', 'w') #creating a .csv file
F.write('DATE;TEMP;HUMID;PRES;G\n') #header of .csv file

x = 179 #number of measurements
#################
#humidity average
i = int(20) 
ic = int(i) 
il = int(i - 1)
ca = int(i) 
a = float(0)
n = int(i-1)
cm= float(0) 
hum_base = []
delta_h = float(0) 

#temperature average
ic_t = int(i) 
il_t = int(i - 1)
a_t = float(0)
n_t = int(i-1)
cm_t= float(0) 
tem_base = []
delta_t = float(0)

#pressure average
ic_p = int(i) 
il_p = int(i - 1) 
a_p = float(0)
n_p = int(i-1)
cm_p= float(0)
press_base = []
delta_p = float(0) 

#from: http://www.stuffaboutcode.com/search?q=CPU+Temperature
## Thanks to Martin O'Hanlon for sharing his code!
class CPUTemp:
 def __init__(self, tempfilename = "/sys/class/thermal/thermal_zone0/temp"):
  self.tempfilename = tempfilename
 def __enter__(self):
  self.open()
  return self
 def open(self):
  self.tempfile = open(self.tempfilename, "r")
 def read(self):
  self.tempfile.seek(0)
  return self.tempfile.read().rstrip()
 def get_temperature(self):
  return self.get_temperature_in_c()
 def get_temperature_in_c(self):
  tempraw = self.read()
  return float(tempraw[:-3] + "." + tempraw[-3:])
 def __exit__(self, type, value, traceback):
  self.close()
 def close(self):
  self.tempfile.close()

#waiting for the start (warm up)
time.sleep(0)

##taking measurements for control measurement
while i > 0: #loop

    pu = SH.get_temperature_from_pressure() #temperature's measurement from pressure sensor
    hu = SH.get_temperature_from_humidity() #temperature's measurement from humidity sensor
    t = SH.get_temperature() #temperature's measurement

    #Next part of Mr. Martin's code. Thank YOU again!
    with CPUTemp() as cpu_temp: 
     c = cpu_temp.get_temperature()
     
    #temperature measurements to the average (used for alarm)     
    #Thans for Kieran, Watch-Dogs's creator. You inspired us to create this code!
    T = ((pu+t+hu)/3) - c/5 #final temperature's value (including the heat emited by CPU)
    tem_base.append(T) #adding measurement to the list
    
    #humidity measurements to the average (used for alarm)
    H = SH.get_humidity() #temperature's measurement
    hum_base.append(H) #adding measurement to the list
    i = i-1 #loop's counter

    
    #preassure measurements to the average (used for alarm)
    P = SH.get_pressure() #pressure's meansurement
    press_base.append(P) #adding measurement to the list
    
    time.sleep(1)
    
hum_base.sort() #sorting variables

while ca > 0: #loop
    
    a = a + hum_base[n] #adding measurement to measurement's sum 
    ca = ca-1 #loop's counter
    n = n-1 #measurement's counter

    a_t = a_t + tem_base[n_t] #adding measurement to mensurment's sum 
    n_t = n_t -1 #measurement's counter

    a_p = a_p + press_base[n_p] #adding measurement to mensurment's sum 
    n_p = n_p -1 #measurement's counter

    
#creating averages    
last = hum_base[il] #the highest measurment [humidity]
cm = a/ic #calculating average of humidity

last_t = tem_base[il_t] #the highest mensurment [temperature]
cm_t = a_t/ic_t #calculating average of temperature

last_p = press_base[il_p] #the highest mensurment [pressure]
cm_p = a_p/ic_p #calculating average of pressure



#numbers on the display
       
  ## UP LEFT ##

#1 up - left
def ul1():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)     
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, 0, 0, 0)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, 0, 0, 0)   
      SH.set_pixel(1, 3, 0, 0, 0)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, ko)   
      SH.set_pixel(2, 2, ko)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, 0, 0, 0)   
      SH.set_pixel(3, 3, 0, 0, 0)
            
#2 up - left
def ul2():
      SH.set_pixel(0, 0, ko)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, ko)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, 0, 0, 0)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, ko)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, ko)   
      SH.set_pixel(2, 2, 0, 0, 0)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, 0, 0, 0)   
      SH.set_pixel(3, 3, 0, 0, 0)
      
#3 up - left
def ul3():
    SH.set_pixel(0, 0, ko)   
    SH.set_pixel(0, 1, 0, 0, 0)   
    SH.set_pixel(0, 2, 0, 0, 0)   
    SH.set_pixel(0, 3, ko)
    SH.set_pixel(1, 0, ko)
    SH.set_pixel(1, 1, ko)   
    SH.set_pixel(1, 2, 0, 0, 0)   
    SH.set_pixel(1, 3, ko)
    SH.set_pixel(2, 0, ko)   
    SH.set_pixel(2, 1, ko)   
    SH.set_pixel(2, 2, ko)   
    SH.set_pixel(2, 3, ko)
    SH.set_pixel(3, 0, 0, 0,0 )
    SH.set_pixel(3, 1, 0, 0, 0)
    SH.set_pixel(3, 2, 0, 0, 0)
    SH.set_pixel(3, 3, 0, 0, 0)
#4 up - left
def ul4():
      SH.set_pixel(0, 0, ko)   
      SH.set_pixel(0, 1, ko)   
      SH.set_pixel(0, 2, ko)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, 0, 0, 0)   
      SH.set_pixel(1, 1, 0, 0, 0)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, 0, 0, 0)
      SH.set_pixel(2, 0, 0, 0, 0)   
      SH.set_pixel(2, 1, ko)  
      SH.set_pixel(2, 2, ko)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, 0, 0, 0)
      
#5 up - left   
def ul5():
      SH.set_pixel(0, 0, ko)   
      SH.set_pixel(0, 1, ko)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, ko)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, 0, 0, 0)   
      SH.set_pixel(1, 3, ko)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, 0, 0, 0)   
      SH.set_pixel(2, 2, ko)  
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, 0, 0, 0)   
      SH.set_pixel(3, 3, 0, 0, 0)

#6 up - left
def ul6():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, ko)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, 0, 0, 0)   
      SH.set_pixel(2, 2, ko)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, ko)
#7 up - left	
def ul7():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, 0, 0, 0)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, 0, 0, 0)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, ko)   
      SH.set_pixel(2, 2, ko)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, 0, 0, 0)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, 0, 0, 0)
	
#8 up - left
def ul8():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, ko)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, 0, 0, 0)   
      SH.set_pixel(2, 2, ko)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, ko)   
      SH.set_pixel(3, 1, ko)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, ko)
#9 up - left	
def ul9():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, ko)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, 0, 0, 0)   
      SH.set_pixel(1, 3, ko)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, ko)   
      SH.set_pixel(2, 2, 0, 0, 0)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, ko)   
      SH.set_pixel(3, 1, ko)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, ko)
	
# 0 up - left 
def ul0():
      SH.set_pixel(0, 0, 0, 0, 0)   
      SH.set_pixel(0, 1, 0, 0, 0)   
      SH.set_pixel(0, 2, 0, 0, 0)   
      SH.set_pixel(0, 3, 0, 0, 0)
      SH.set_pixel(1, 0, 0, 0, 0)   
      SH.set_pixel(1, 1, ko)   
      SH.set_pixel(1, 2, ko)   
      SH.set_pixel(1, 3, 0, 0, 0)
      SH.set_pixel(2, 0, ko)   
      SH.set_pixel(2, 1, 0, 0, 0)   
      SH.set_pixel(2, 2, 0, 0, 0)   
      SH.set_pixel(2, 3, ko)
      SH.set_pixel(3, 0, 0, 0, 0)   
      SH.set_pixel(3, 1, ko)   
      SH.set_pixel(3, 2, ko)   
      SH.set_pixel(3, 3, 0, 0, 0)

      
		  
      ## UP RIGHT ##
# 1 up - right
def ur1(): 
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, 0, 0, 0)   
      SH.set_pixel(5, 1, ko)   
      SH.set_pixel(5, 2, 0, 0, 0)   
      SH.set_pixel(5, 3, 0, 0, 0)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, ko)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, 0, 0, 0)   
      SH.set_pixel(7, 1, 0, 0, 0)   
      SH.set_pixel(7, 2, 0, 0, 0)   
      SH.set_pixel(7, 3, 0, 0, 0)
#2 up - right
def ur2():
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, 0, 0, 0)   
      SH.set_pixel(5, 2, 0, 0, 0)   
      SH.set_pixel(5, 3, ko)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, 0, 0, 0)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, ko)   
      SH.set_pixel(7, 1, ko)   
      SH.set_pixel(7, 2, 0, 0, 0)   
      SH.set_pixel(7, 3, ko)


#3 up - right
def ur3():    
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, 0, 0, 0)   
      SH.set_pixel(5, 2, 0, 0, 0)   
      SH.set_pixel(5, 3, ko)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, ko)   
      SH.set_pixel(6, 2, 0, 0, 0)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, ko)   
      SH.set_pixel(7, 1, ko)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, ko)

#4 up - right
def ur4():
      SH.set_pixel(4, 0, ko)   
      SH.set_pixel(4, 1, ko)   
      SH.set_pixel(4, 2, ko)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, 0, 0, 0)   
      SH.set_pixel(5, 1, 0, 0, 0)   
      SH.set_pixel(5, 2, ko)   
      SH.set_pixel(5, 3, 0, 0, 0)
      SH.set_pixel(6, 0, 0, 0, 0)   
      SH.set_pixel(6, 1, ko)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, 0, 0, 0)   
      SH.set_pixel(7, 1, 0, 0, 0)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, 0, 0, 0)

#5 up - right
def ur5():
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, ko)   
      SH.set_pixel(5, 2, 0, 0, 0)   
      SH.set_pixel(5, 3, ko)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, ko)   
      SH.set_pixel(6, 2, 0, 0, 0)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, ko)   
      SH.set_pixel(7, 1, 0, 0, 0)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, ko)

#6 up - right
def ur6():
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, ko)   
      SH.set_pixel(5, 2, ko)   
      SH.set_pixel(5, 3, ko)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, 0, 0, 0)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, 0, 0, 0)   
      SH.set_pixel(7, 1, 0, 0, 0)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, ko)
        

#7 up - right
def ur7():
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, 0, 0, 0)   
      SH.set_pixel(5, 2, ko)   
      SH.set_pixel(5, 3, 0, 0, 0)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, ko)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, 0, 0, 0)   
      SH.set_pixel(7, 1, 0, 0, 0)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, 0, 0, 0)

#8 up - right
def ur8():
      SH.set_pixel(4, 0, 0, 0, 0)   
      SH.set_pixel(4, 1, 0, 0, 0)   
      SH.set_pixel(4, 2, 0, 0, 0)   
      SH.set_pixel(4, 3, 0, 0, 0)
      SH.set_pixel(5, 0, ko)   
      SH.set_pixel(5, 1, ko)   
      SH.set_pixel(5, 2, ko)   
      SH.set_pixel(5, 3, ko)
      SH.set_pixel(6, 0, ko)   
      SH.set_pixel(6, 1, 0, 0, 0)   
      SH.set_pixel(6, 2, ko)   
      SH.set_pixel(6, 3, ko)
      SH.set_pixel(7, 0, ko)   
      SH.set_pixel(7, 1, ko)   
      SH.set_pixel(7, 2, ko)   
      SH.set_pixel(7, 3, ko)

#9 up - right
def ur9():
        SH.set_pixel(4, 0, 0, 0, 0)   
        SH.set_pixel(4, 1, 0, 0, 0)   
        SH.set_pixel(4, 2, 0, 0, 0)   
        SH.set_pixel(4, 3, 0, 0, 0)
        SH.set_pixel(5, 0, ko)   
        SH.set_pixel(5, 1, ko)   
        SH.set_pixel(5, 2, 0, 0, 0)   
        SH.set_pixel(5, 3, ko)
        SH.set_pixel(6, 0, ko)   
        SH.set_pixel(6, 1, ko)   
        SH.set_pixel(6, 2, 0, 0, 0)   
        SH.set_pixel(6, 3, ko)
        SH.set_pixel(7, 0, ko)   
        SH.set_pixel(7, 1, ko)   
        SH.set_pixel(7, 2, ko)   
        SH.set_pixel(7, 3, ko)

#0 up - right
def ur0():
        SH.set_pixel(4, 0, 0, 0, 0)   
        SH.set_pixel(4, 1, 0, 0, 0)   
        SH.set_pixel(4, 2, 0, 0, 0)   
        SH.set_pixel(4, 3, 0, 0, 0)
        SH.set_pixel(5, 0, 0, 0, 0)   
        SH.set_pixel(5, 1, ko)   
        SH.set_pixel(5, 2, ko)   
        SH.set_pixel(5, 3, 0, 0, 0)
        SH.set_pixel(6, 0, ko)   
        SH.set_pixel(6, 1, 0, 0, 0)   
        SH.set_pixel(6, 2, 0, 0, 0)   
        SH.set_pixel(6, 3, ko)
        SH.set_pixel(7, 0, 0, 0, 0)   
        SH.set_pixel(7, 1, ko)   
        SH.set_pixel(7, 2, ko)   
        SH.set_pixel(7, 3, 0, 0, 0)

    
## DOWN LEFT ## 

# 1 down - left
def dl1():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, 0, 0, 0)   
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, 0, 0, 0)   
    SH.set_pixel(1, 7, 0, 0, 0)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, ko)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0, 0)   
    SH.set_pixel(3, 5, 0, 0, 0)   
    SH.set_pixel(3, 6, 0, 0, 0)   
    SH.set_pixel(3, 7, 0, 0, 0)
    
#2 down - left
def dl2():
      SH.set_pixel(0, 4, ko)   
      SH.set_pixel(0, 5, 0, 0, 0)   
      SH.set_pixel(0, 6, 0, 0, 0)   
      SH.set_pixel(0, 7, ko)
      SH.set_pixel(1, 4, ko)   
      SH.set_pixel(1, 5, 0, 0, 0)   
      SH.set_pixel(1, 6, ko)   
      SH.set_pixel(1, 7, ko)
      SH.set_pixel(2, 4, ko)   
      SH.set_pixel(2, 5, ko)   
      SH.set_pixel(2, 6, 0, 0, 0)   
      SH.set_pixel(2, 7, ko)
      SH.set_pixel(3, 4, 0, 0, 0)   
      SH.set_pixel(3, 5, 0, 0, 0)   
      SH.set_pixel(3, 6, 0, 0, 0)   
      SH.set_pixel(3, 7, 0, 0, 0)
    
#3 down - left
def dl3():
    SH.set_pixel(0, 4, ko)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, ko)
    SH.set_pixel(1, 4, ko)
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, 0, 0, 0)   
    SH.set_pixel(1, 7, ko)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, ko)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0,0 )
    SH.set_pixel(3, 5, 0, 0, 0)
    SH.set_pixel(3, 6, 0, 0, 0)
    SH.set_pixel(3, 7, 0, 0, 0)

#4 down - left
def dl4():
    SH.set_pixel(0, 4, ko)   
    SH.set_pixel(0, 5, ko)   
    SH.set_pixel(0, 6, ko)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, 0, 0, 0)   
    SH.set_pixel(1, 5, 0, 0, 0)   
    SH.set_pixel(1, 6, ko)   
    SH.set_pixel(1, 7, 0, 0, 0)
    SH.set_pixel(2, 4, 0, 0, 0)   
    SH.set_pixel(2, 5, ko)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0, 0)   
    SH.set_pixel(3, 5, 0, 0, 0)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, 0, 0, 0)

#5 down - left
def dl5():
      SH.set_pixel(0, 4, ko)   
      SH.set_pixel(0, 5, ko)   
      SH.set_pixel(0, 6, 0, 0, 0)   
      SH.set_pixel(0, 7, ko)
      SH.set_pixel(1, 4, ko)   
      SH.set_pixel(1, 5, ko)   
      SH.set_pixel(1, 6, 0, 0, 0)   
      SH.set_pixel(1, 7, ko)
      SH.set_pixel(2, 4, ko)   
      SH.set_pixel(2, 5, 0, 0, 0)   
      SH.set_pixel(2, 6, ko)  
      SH.set_pixel(2, 7, ko)
      SH.set_pixel(3, 4, 0, 0, 0)   
      SH.set_pixel(3, 5, 0, 0, 0)   
      SH.set_pixel(3, 6, 0, 0, 0)   
      SH.set_pixel(3, 7, 0, 0, 0)
    
#6 down - left
def dl6():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, ko)   
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, ko)   
    SH.set_pixel(1, 7, ko)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, 0, 0, 0)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0, 0)   
    SH.set_pixel(3, 5, 0, 0, 0)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, ko)

#7 down - left
def dl7():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, ko)   
    SH.set_pixel(1, 5, 0, 0, 0)   
    SH.set_pixel(1, 6, ko)   
    SH.set_pixel(1, 7, 0, 0, 0)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, ko)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0, 0)   
    SH.set_pixel(3, 5, 0, 0, 0)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, 0, 0, 0)

#8 down - left 
def dl8():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, ko)   
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, ko)   
    SH.set_pixel(1, 7, ko)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, 0, 0, 0)   
    SH.set_pixel(2, 6, ko)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, ko)   
    SH.set_pixel(3, 5, ko)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, ko)

#9 down - left
def dl9():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, ko)   
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, 0, 0, 0)   
    SH.set_pixel(1, 7, ko)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, ko)   
    SH.set_pixel(2, 6, 0, 0, 0)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, ko)   
    SH.set_pixel(3, 5, ko)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, ko)

#0 down - left
def dl0():
    SH.set_pixel(0, 4, 0, 0, 0)   
    SH.set_pixel(0, 5, 0, 0, 0)   
    SH.set_pixel(0, 6, 0, 0, 0)   
    SH.set_pixel(0, 7, 0, 0, 0)
    SH.set_pixel(1, 4, 0, 0, 0)   
    SH.set_pixel(1, 5, ko)   
    SH.set_pixel(1, 6, ko)   
    SH.set_pixel(1, 7, 0, 0, 0)
    SH.set_pixel(2, 4, ko)   
    SH.set_pixel(2, 5, 0, 0, 0)   
    SH.set_pixel(2, 6, 0, 0, 0)   
    SH.set_pixel(2, 7, ko)
    SH.set_pixel(3, 4, 0, 0, 0)   
    SH.set_pixel(3, 5, ko)   
    SH.set_pixel(3, 6, ko)   
    SH.set_pixel(3, 7, 0, 0, 0)



## DOWN RIGHT ## 
  
#1 down - right 
def dr1():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, 0, 0, 0)   
    SH.set_pixel(5, 5, ko)   
    SH.set_pixel(5, 6, 0, 0, 0)   
    SH.set_pixel(5, 7, 0, 0, 0)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, ko)   
    SH.set_pixel(6, 6, ko)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, 0, 0, 0)   
    SH.set_pixel(7, 5, 0, 0, 0)   
    SH.set_pixel(7, 6, 0, 0, 0)   
    SH.set_pixel(7, 7, 0, 0, 0)

#2 down - right
def dr2():
      SH.set_pixel(4, 4, 0, 0, 0)   
      SH.set_pixel(4, 5, 0, 0, 0)   
      SH.set_pixel(4, 6, 0, 0, 0)   
      SH.set_pixel(4, 7, 0, 0, 0)
      SH.set_pixel(5, 4, ko)   
      SH.set_pixel(5, 5, 0, 0, 0)   
      SH.set_pixel(5, 6, 0, 0, 0)   
      SH.set_pixel(5, 7, ko)
      SH.set_pixel(6, 4, ko)   
      SH.set_pixel(6, 5, 0, 0, 0)   
      SH.set_pixel(6, 6, ko)   
      SH.set_pixel(6, 7, ko)
      SH.set_pixel(7, 4, ko)   
      SH.set_pixel(7, 5, ko)   
      SH.set_pixel(7, 6, 0, 0, 0)   
      SH.set_pixel(7, 7, ko)
			  


#3 down - right 
def dr3():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, ko)   
    SH.set_pixel(5, 5, 0, 0, 0)   
    SH.set_pixel(5, 6, 0, 0, 0)   
    SH.set_pixel(5, 7, ko)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, ko)   
    SH.set_pixel(6, 6, 0, 0, 0)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, ko)   
    SH.set_pixel(7, 5, ko)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, ko)
    
#4 down - right
def dr4():
    SH.set_pixel(4, 4, ko)   
    SH.set_pixel(4, 5, ko)   
    SH.set_pixel(4, 6, ko)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, 0, 0, 0)   
    SH.set_pixel(5, 5, 0, 0, 0)   
    SH.set_pixel(5, 6, ko)   
    SH.set_pixel(5, 7, 0, 0, 0)
    SH.set_pixel(6, 4, 0, 0, 0)   
    SH.set_pixel(6, 5, ko)   
    SH.set_pixel(6, 6, ko)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, 0, 0, 0)   
    SH.set_pixel(7, 5, 0, 0, 0)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, 0, 0, 0)

#5 down - right 
def dr5():
      SH.set_pixel(4, 4, 0, 0, 0)   
      SH.set_pixel(4, 5, 0, 0, 0)   
      SH.set_pixel(4, 6, 0, 0, 0)   
      SH.set_pixel(4, 7, 0, 0, 0)
      SH.set_pixel(5, 4, ko)   
      SH.set_pixel(5, 5, ko)   
      SH.set_pixel(5, 6, 0, 0, 0)   
      SH.set_pixel(5, 7, ko)
      SH.set_pixel(6, 4, ko)   
      SH.set_pixel(6, 5, ko)   
      SH.set_pixel(6, 6, 0, 0, 0)   
      SH.set_pixel(6, 7, ko)
      SH.set_pixel(7, 4, ko)   
      SH.set_pixel(7, 5, 0, 0, 0)   
      SH.set_pixel(7, 6, ko)   
      SH.set_pixel(7, 7, ko)
			  
    
#6 down - right
def dr6():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, ko)   
    SH.set_pixel(5, 5, ko)   
    SH.set_pixel(5, 6, ko)   
    SH.set_pixel(5, 7, ko)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, 0, 0, 0)   
    SH.set_pixel(6, 6, ko)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, 0, 0, 0)   
    SH.set_pixel(7, 5, 0, 0, 0)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, ko)

#7 down - right
def dr7():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, ko)   
    SH.set_pixel(5, 5, 0, 0, 0)   
    SH.set_pixel(5, 6, ko)   
    SH.set_pixel(5, 7, 0, 0, 0)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, ko)   
    SH.set_pixel(6, 6, ko)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, 0, 0, 0)   
    SH.set_pixel(7, 5, 0, 0, 0)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, 0, 0, 0)
    
#8 down - right
def dr8():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, ko)   
    SH.set_pixel(5, 5, ko)   
    SH.set_pixel(5, 6, ko)   
    SH.set_pixel(5, 7, ko)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, 0, 0, 0)   
    SH.set_pixel(6, 6, ko)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, ko)   
    SH.set_pixel(7, 5, ko)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, ko)
    
#9 down - right
def dr9():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, ko)   
    SH.set_pixel(5, 5, ko)   
    SH.set_pixel(5, 6, 0, 0, 0)   
    SH.set_pixel(5, 7, ko)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, ko)   
    SH.set_pixel(6, 6, 0, 0, 0)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, ko)   
    SH.set_pixel(7, 5, ko)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, ko)

#0 down - right 
def dr0():
    SH.set_pixel(4, 4, 0, 0, 0)   
    SH.set_pixel(4, 5, 0, 0, 0)   
    SH.set_pixel(4, 6, 0, 0, 0)   
    SH.set_pixel(4, 7, 0, 0, 0)
    SH.set_pixel(5, 4, 0, 0, 0)   
    SH.set_pixel(5, 5, ko)   
    SH.set_pixel(5, 6, ko)   
    SH.set_pixel(5, 7, 0, 0, 0)
    SH.set_pixel(6, 4, ko)   
    SH.set_pixel(6, 5, 0, 0, 0)   
    SH.set_pixel(6, 6, 0, 0, 0)   
    SH.set_pixel(6, 7, ko)
    SH.set_pixel(7, 4, 0, 0, 0)   
    SH.set_pixel(7, 5, ko)   
    SH.set_pixel(7, 6, ko)   
    SH.set_pixel(7, 7, 0, 0, 0)


##taking current measurements
while x > 0: #loop
  x = x - 1 #loop's counter
  
  pu = SH.get_temperature_from_pressure() #temperature's measurement from pressure sensor
  hu = SH.get_temperature_from_humidity() #temperature's measurement from humidity sensor
  t = SH.get_temperature() #temperature's measurement

  with CPUTemp() as cpu_temp:
    c = cpu_temp.get_temperature()
    
  T = ((pu+t+hu)/3) - c/5 #final temperature's value (including the heat emited bu CPU)
  
  T = round (T, 0) #rounding variables
  T = str(T) #changing type of variable to string
  
  H = SH.get_humidity() # humidity's measurement
  H = round (H, 0) #rounding variables
  H = str(H) #changing type of variable to string

  P = SH.get_pressure() #pressure's measurement
  P = round(P, 0) #rounding variables
  P = int(P) #changing type of variable to string
  
  G = SH.get_accelerometer_raw() #getting accelerometer's data
  
  #Humidity
  H_dzi = H[0] #getting tens from number
  H_jed = H[1] #getting ones from number
  
  H_dzi = int(H_dzi) #changing variable's type to interger
  H_jed = int(H_jed) #changing variable's type to interger

  #Temperature
  T_dzi = T[0] #getting tens from number
  T_jed = T[1] #getting ones from number
  
  T_dzi = int(T_dzi) #changing variable's type to interger
  T_jed = int(T_jed) #changing variable's type to interger

  
  SH.load_image("ht.png") #loading image [humidity] to display on the LED
  sleep (1) #time of displaying image


  #Temperature's displaying
  ko = (204, 0, 204) #color's variable

  #displaying temperature's value on the screen
  if (T_dzi == 1):
    dl1()
        
  elif (T_dzi == 2):
    dl2()
                
  elif (T_dzi == 3):
    dl3()
             
  elif (T_dzi == 4):
    dl4()
		
  elif (T_dzi == 5):
    dl5()
	
  elif (T_dzi == 6):
    dl6()
		
  elif (T_dzi == 7):
    dl7()
	
  elif (T_dzi == 8):
    dl8()
		
  elif (T_dzi == 9):
    dl9()

  elif (T_dzi == 0):
    dl0()
  #######
  if (T_jed == 1):
    dr1()
        
  elif (T_jed == 2):
    dr2()
                
  elif (T_jed == 3):
    dr3()
             
  elif (T_jed == 4):
    dr4()
		
  elif (T_jed == 5):
    dr5()
	
  elif (T_jed == 6):
    dr6()
	
  elif (T_jed == 7):
    dr7()
	
  elif (T_jed == 8):
    dr8()
		
  elif (T_jed == 9):
    dr9()

  elif (T_jed == 0):
    dr0()
  #displaying humidity's value on the screen
  
  ko = (250, 250, 0) #color's variable
    
  if (H_dzi == 1):
    ul1()
    
        
  elif (H_dzi == 2):
    ul2()
                
  elif (H_dzi == 3):
    ul3()
             
  elif (H_dzi == 4):
    ul4()
		
  elif (H_dzi == 5):
    ul5()
	
  elif (H_dzi == 6):
    ul6()
		
  elif (H_dzi == 7):
    ul7()
	
  elif (H_dzi == 8):
    ul8()
		
  elif (H_dzi == 9):
    ul9()

  elif (H_dzi == 0):
    ul0()
######
  if (H_jed == 1):
    ur1()
      
  if (H_jed == 2):
    ur2()
                
  elif (H_jed == 3):
    ur3()
             
  elif (H_jed == 4):
    ur4()
		
  if (H_jed == 5):
    ur5()
	
  elif (H_jed == 6):
    ur6()
		
  elif (H_jed == 7):
    ur7()
	
  elif (H_jed == 8):
    ur8()
		
  elif (H_jed == 9):
    ur9()
    
  elif (H_jed == 0):
    ur0()

#work with .csv file
  xt = strftime("%a %d %b %Y %H:%M", gmtime()) #getting date and time
  F.write(xt + ';' + str(T) + ';' + str(H) + ';' + str(P) +';' + str(G) +'\n') #writing measurements to .csv file
  sleep(3)
  
  SH.load_image("preassure.png" ) #loading pressure's image that appears on the LED display
  sleep(1)
  SH.show_message(str(P), text_colour=[0, 255, 255]) #displaying preassure's value on the screen

##values for the alarm
  #Humidity
  H = float (H) #changing variable's type to string
  delta_h = H - cm #difference between actual measurement and measurement's average

  #Temperature
  T = float (T) #changing variable's type to string
  delta_t = T - cm_t #difference between actual measurement and measurement's average

  #Preassure
  P = float (P) #changing variable's type to string
  delta_p = P - cm_p #difference between actual measurement and measurement's average

  #checking if measurements are in norm
  #Humidity
  if delta_h > 5 or delta_h < -5:
      F.write('^^ Alarm - Humidity ^^ \n')
      for kns in range(5):
        
        SH.show_letter('H', text_colour=[250, 0, 0])
        time.sleep (0.2)
        SH.show_letter('H', text_colour=[255, 255, 0])
        time.sleep (0.2)
        
  #Temperature      
  if delta_t >= 4 or delta_t <= -4:
      F.write('^^ Alarm - Temperature ^^ \n')
      for kns_t in range(5):
        
        SH.show_letter('T', text_colour=[250, 0, 0])
        time.sleep (0.2)
        SH.show_letter('T', text_colour=[204, 0, 204])
        time.sleep (0.2)
        
  #Pressure
  if delta_p > 5 or delta_p < -5:
      F.write('^^ Alarm - Pressure ^^ \n') 
      for kns_p in range(5):
        
        SH.show_letter('P', text_colour=[250, 0, 0])
        time.sleep (0.2)
        SH.show_letter('P', text_colour=[0, 255, 225])
        time.sleep (0.2)
        
#end of program
if x == 0:
  SH.clear()
  F.close()
  exit()


      








