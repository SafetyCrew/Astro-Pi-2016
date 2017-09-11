#imprting modules:
from sense_hat import SenseHat
from time import sleep, gmtime, strftime
import time

SH = SenseHat()
F = open('I project - data.csv', 'w') #creating the .csv file

#Variables:
p = int(400) #measurements number
humid = float(0)
i = int(20)
ic = int(i) 
il = int(i - 1)
c = int(i) 
a = float(0)
n = int(i-1)
cm= float(0) 
hum_base = []
h = float(0) 
A = int(0) 
delta = float(0) 
white = (250,250,250) #white color [display]

#Waiting (warm up)
time.sleep(120)

#taking control measurements and calculating the average from them
while i > 0: #loop
    h = SH.get_humidity() #humidity's measurement
    hum_base.append(h) #adding measurement to the list
    i = i-1 #loop's iterator
    time.sleep(1)
hum_base.sort() #sorting variables [list]
while c > 0:
    a = a + hum_base[n] #adding measurement to measurement's sum 
    c = c-1 #loop's counter
    n = n-1 #measurement's counter
    
last = hum_base[il] #the highest measurement
cm = a/ic #average

#writing the average of control measurements to file
F.write('mensurment [humidity] ' + str(hum_base) +' average: ' + str(cm) + '\n')

time.sleep(0)

#Program's start:
while p > 0:
    humid = SH.get_humidity() #getting humidity from humidity sensor
    delta = humid - cm
    if (delta > 0.7) :

        B = (50, 50, 50) #gray
        W = (250, 250, 250) #white
        X = (250, 0, 0) #color of background
        A = A + 1 #to write 'astro' to file later
        G = 5 # iterator for loop [emulating gif file]

        #setting and displaying pixels to make the astronaut's image:
        while (G > 0):
            #HAPPY ASTRONAUT :D=> BY KRYSTIAN
            x = [
                X, X, X, W, W, X, X, X,
                X, X, W, B, B, W, X, X,
                X, X, W, B, B, W, X, X,
                X, X, X, W, W, X, X, X,
                X, X, W, W, W, W, X, X,
                X, X, W, W, W, W, X, X,
                X, W, X, W, W, X, W, X,
                X, X, X, W, W, X, X, X
            ]
                  
            SH.set_pixels(x)
                  
            time.sleep(1)
                  
            x = [
                X, X, X, W, W, X, X, X,
                X, X, W, B, B, W, X, X,
                X, X, W, B, B, W, X, X,
                W, X, X, W, W, X, X, W,
                X, W, W, W, W, W, W, X,
                X, X, X, W, W, X, X, X,
                X, X, X, W, W, X, X, X,
                X, X, W, X, X, W, X, X
            ]
                    
            SH.set_pixels(x)
                    
            time.sleep (1)
            
            G = G - 1 #loop's iterator
            t = 0 #time = 0 [no waiting]
    else:

        green = (0, 250, 0) #green color [display]
        white = (0, 0, 0) #black color [alpha]
        
    #copied part of code from Raspberry Pi Sense HAT emulator
        humidity_value = 64 * humid / 100
        pixels = [green if i < humidity_value else white for i in range(64)]
        SH.set_pixels(pixels)

        
        A = 0 #clearing variable's value
        t = 10
        
    #Writing to .csv file
    F.write(strftime("%a %d %b %Y %H:%M:%S", gmtime()) +' humidity:;' + str(humid) + '\n')
    if A > 0 :
        F.write('^^ ASTR ^^''\n') #log written when astronaut appears    
    A = 0 #clearing variable's value   
    p = p - 1 #main iterator
    time.sleep(t)

 #end of the program   
else:
    SH.clear()
    F.close()
    exit()


    
