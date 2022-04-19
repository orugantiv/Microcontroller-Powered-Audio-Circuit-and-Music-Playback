from machine import Pin,ADC, PWM,Timer
import _thread
import utime

from utime import sleep
buzzer = PWM(Pin(0))
tim = Timer()

AL = 880;
BL = 987;
C = 1046;
D = 1174;
Ef = 1244;
E = 1318;
F = 1396;
G = 1567;
A = 1760;
Bf = 1864;
B = 1975;
CH = 2093;
CHs = 2217;
DH = 2349.;
EHf = 2489;
EH = 2637;
FH = 2793;
FHs = 2959;
GH = 3135;


SX = 0.125;
ET = 0.25;
ETex = 0.375;
Q = 0.5;
H = 1;
EX = 1.5;
FULL = 2;
EXH = 2.5;

twinkle_note= [C, C, G, G, A, A, G, F, F, E, E, D, D, C, G, 
                G, F, F, E, E, D, G, G, F, F, E, E, D, C, C, 
                G, G, A, A, G, F, F, E, E, D, D, C]
twinkle_duration= [Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H, 
                Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H, 
                Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H]

damned_note= [B, E, BL, B, E, BL, B, E, B, E, BL, B, E, BL, B, E, CH, E, C, CH, E, C, CH, E, DH, E, C,
              CH, E, C, B, E, B, E, BL, B, E, BL, B, E , B, E, BL, B, E, BL, B, E, CH, E, C, CH, E, C, CH, E, DH, E, C, CH, E, C, B, A]
damned_duration= [ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET,
                  ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET,
                  ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET,
                  ET, ET, ET, ET]

letit_note= [G, G, G, G, A, E, G, G, CH, DH, CH, CH, CH, B, A, CH, A, EH, EH, FH, EH,  
                EH, DH, EH, DH, DH,CH, G, F, E, G, G, G, A, CH, G, G, CH, DH, CH, CH, CH, B, A, CH, 
                A, EH, EH, FH, EH, EH, DH, EH, DH, DH, CH, G, F
                ]
letit_duration= [ET, ET, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, H,
                ET, ET, Q, Q, Q, Q, EX, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, 
                Q, H, ET, ET, Q, Q, Q, Q
                ]
hedwig_note= [E, A, CH, B, A, EH, DH, B, A, CH, B, G, Bf, E, E, A, CH, B, A, EH, GH, FHs, F, 
                CHs, F, EH, EHf, Ef, CH, A, CH
                ]
hedwig_duration= [Q, Q, Q, Q, H, Q, EX, EX, Q, Q, Q, H, Q, EXH, Q, Q, Q, Q, H, Q, H, Q, H, 
                Q, Q, Q, Q, H, Q, EXH, Q]

# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.

# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.

from machine import Timer
seg_a = PWM(Pin(14))
seg_b = PWM(Pin(15))
seg_c = PWM(Pin(17))
seg_d = PWM(Pin(18))
seg_e = PWM(Pin(19))
seg_f = PWM(Pin(13))
seg_g = PWM(Pin(12))
#seg_h = Pin()

LED_ON = 35000
LED_OFF = 0
def displaySegments(value):
    if value == 0:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON)
    elif value == 1:
        toSegments(e=LED_ON,f=LED_ON)
    elif value == 2:
        toSegments(a=LED_ON,b=LED_ON,d=LED_ON,e=LED_ON,g=LED_ON)    
    elif value == 3:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON,d=LED_ON,g=LED_ON)
    elif value == 4:
        toSegments(b=LED_ON,c=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 5:
        toSegments(a=LED_ON,c=LED_ON,d=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 6:
        toSegments(a=LED_ON,c=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 7:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON)
    elif value == 8:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 9:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 10:
        toSegments(a=LED_ON,b=LED_ON,c=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 11:
        toSegments(c=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 12:
        toSegments(a=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON)
    elif value == 13:
        toSegments(b=LED_ON,c=LED_ON,d=LED_ON,e=LED_ON,g=LED_ON)
    elif value == 14:
        toSegments(a=LED_ON,d=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
    elif value == 15:
        toSegments(a=LED_ON,e=LED_ON,f=LED_ON,g=LED_ON)
def toSegments(a=LED_OFF,b=LED_OFF,c=LED_OFF,d=LED_OFF,e=LED_OFF,f=LED_OFF,g=LED_OFF):
        seg_a.duty_u16(a)
        seg_b.duty_u16(b)
        seg_c.duty_u16(c)
        seg_d.duty_u16(d)
        seg_e.duty_u16(e)
        seg_f.duty_u16(f)
        seg_g.duty_u16(g)
displaySegments(1)
def handle_interrupt(pin):
    checkVolUpInput()
   #vol = 1000
    return
vol = 1000
def playtone(frequency):
    buzzer.duty_u16(int(vol))
    buzzer.freq(frequency)
def checkVolUpInput(p):
    global vol
    if vol<15000:
        vol +=1000
        tmpSeg = 1
        if vol == 0:
            tmpSeg = 0
        else:
            tmpSeg =vol/1000
        displaySegments(tmpSeg)
    print(vol)
def bequiet():
    buzzer.duty_u16(0)
def checkVolDownInput(p):
    global vol
    if vol>0:
        vol -=1000
        tmpSeg = 1
        if vol == 0:
            tmpSeg = 0
        else:
            tmpSeg =vol/1000
        displaySegments(tmpSeg)
    print(vol)

def playsong(notes,notes_duration):
    for i in range(len(notes)):
        playtone(int(notes[i]))      
        sleep(notes_duration[i])
    bequiet()

volUP=Pin(1, Pin.IN, Pin.PULL_DOWN)
volUP.irq(trigger=Pin.IRQ_FALLING, handler=checkVolUpInput)
volDown=Pin(2, Pin.IN, Pin.PULL_DOWN)
volDown.irq(trigger=Pin.IRQ_FALLING, handler=checkVolDownInput)

song1=Pin(20, Pin.IN, Pin.PULL_DOWN)
song2=Pin(21, Pin.IN, Pin.PULL_DOWN)
song3=Pin(22, Pin.IN, Pin.PULL_DOWN)
song4=Pin(26, Pin.IN, Pin.PULL_DOWN)
song5=Pin(27, Pin.IN, Pin.PULL_UP)
#song5.irq(trigger=Pin.IRQ_RISING, h200andler=checkVolUpInput) 
while 1:
#    playsong(hedwig_note,hedwig_duration)
    if song1.value():
        playsong(twinkle_note,twinkle_duration)
    elif song2.value():
        playsong(damned_note,damned_duration)
    elif song3.value():
        playsong(letit_note,letit_duration)
    elif song4.value():
        playsong(hedwig_note,hedwig_duration)

    #print("down")

    #song1.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt) 
