from machine import Pin,ADC, PWM,Timer
import _thread
import utime



# Speaker GPIO Pin
speaker = PWM(Pin(0))

#GPIO Pins for different songs
song1=Pin(20, Pin.IN, Pin.PULL_DOWN)
song2=Pin(21, Pin.IN, Pin.PULL_DOWN)
song3=Pin(22, Pin.IN, Pin.PULL_DOWN)
song4=Pin(26, Pin.IN, Pin.PULL_DOWN)
song5=Pin(27, Pin.IN, Pin.PULL_DOWN)

#PWM(GPIO) Pins for 7 seg display
seg_a = PWM(Pin(14))
seg_b = PWM(Pin(15))
seg_c = PWM(Pin(17))
seg_d = PWM(Pin(18))
seg_e = PWM(Pin(19))
seg_f = PWM(Pin(13))
seg_g = PWM(Pin(12))

#Timer for song callbacks
tim = Timer()

# Different Freq for used notes 
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

# Times
SX = 0.125;
ET = 0.25;
ETex = 0.375;
Q = 0.5;
H = 1;
EX = 1.5;
FULL = 2;
EXH = 2.5;


# Timer for callbacks
timer = Timer()


# notes and durations for tones
twinkle_note=  [C, C, G, G, A, A, G, F, F, E, E, D, D, C, G, 
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

bday_note= [C, C, D, C, F, E, C, C, D, C, G, F, C, C, CH, A, F, E, D, Bf, Bf, A, F, G, F
                ]
bday_duration = [ETex, SX, Q, Q, Q, H, ETex, SX, Q, Q, Q, H, ETex, SX, Q, Q, Q, Q, Q, ETex, SX, 
                Q, Q, Q, H]
LED_ON = 35000
LED_OFF = 0
vol = 2000

def displaySegments(value):
    a = LED_ON
    b = LED_ON
    c = LED_ON
    d = LED_ON
    e = LED_ON
    f = LED_ON
    g = LED_ON
    
    value == 0 and toSegments(a=a,b=b,c=c,d=d,e=e,f=f) 
    value == 1 and toSegments(e=e,f=f)
    value == 2 and toSegments(a=a,b=b,d=d,e=e,g=g)    
    value == 3 and toSegments(a=a,b=b,c=c,d=d,g=g)
    value == 4 and toSegments(b=b,c=c,f=f,g=g)
    value == 5 and toSegments(a=a,c=c,d=d,f=f,g=g)
    value == 6 and toSegments(a=a,c=c,d=d,e=e,f=f,g=g)
    value == 7 and toSegments(a=a,b=b,c=c)
    value == 8 and toSegments(a=a,b=b,c=c,d=d,e=e,f=f,g=g)
    value == 9 and toSegments(a=a,b=b,c=c,f=f,g=g)
    value == 10 and toSegments(a=a,b=b,c=c,e=e,f=f,g=g)
    value == 11 and toSegments(c=c,d=d,e=e,f=f,g=g)
    value == 12 and toSegments(a=a,d=d,e=e,f=f)
    value == 13 and toSegments(b=b,c=c,d=d,e=e,g=g)
    value == 14 and toSegments(a=a,d=d,e=e,f=f,g=g)
    value == 15 and toSegments(a=a,e=e,f=f,g=g)
    
def toSegments(a=LED_OFF,b=LED_OFF,c=LED_OFF,d=LED_OFF,e=LED_OFF,f=LED_OFF,g=LED_OFF):
        seg_a.duty_u16(a)
        seg_b.duty_u16(b)
        seg_c.duty_u16(c)
        seg_d.duty_u16(d)
        seg_e.duty_u16(e)
        seg_f.duty_u16(f)
        seg_g.duty_u16(g)
displaySegments(1)

# Interrupt function for volume up button
def checkVolUpInput(t):
    global vol
    if vol<(15000+1000):
        vol +=1000
        displaySegments(0 if vol == 0 else (vol-1000)/1000)
# Interrupt function for volume down button
def checkVolDownInput(t):
    global vol
    if vol>(1000):
        vol -=1000
        displaySegments(0 if vol == 0 else (vol-1000)/1000)
i = 0
limit = 0
notes = []
notes_duration = []
playing = False
def playsong(timer):
    
    global  i
    global playing
    if i == limit:
        speaker.duty_u16(0)
        playing = False
    else:
        speaker.duty_u16(0)
        utime.sleep(0.015)
        speaker.duty_u16(int(vol))
        speaker.freq(int(int(notes[i])))
        i+=1
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)

# GPIO Pin for volume UP
volUP=Pin(1, Pin.IN, Pin.PULL_DOWN)
volUP.irq(trigger=Pin.IRQ_FALLING, handler=checkVolUpInput)
#GPIO Pin for volume down
volDown=Pin(2, Pin.IN, Pin.PULL_DOWN)
volDown.irq(trigger=Pin.IRQ_FALLING, handler=checkVolDownInput)

while 1:
    if song1.value() and (not playing or not notes == twinkle_note) :
        notes = twinkle_note
        notes_duration = twinkle_duration
        i = 0
        limit = len(twinkle_note)-1
        playing = True
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)
    elif song2.value() and (not playing or not notes == damned_note) :
        notes = damned_note
        notes_duration = damned_duration
        i = 0
        limit = len(damned_note)-1
        playing = True
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)
    elif song3.value() and (not playing or not notes == letit_note) :
        notes = letit_note
        notes_duration = letit_duration
        i = 0
        limit = len(letit_duration)-1
        playing = True
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)
    elif song4.value()and (not playing or not notes == hedwig_note) :
        notes = hedwig_note
        notes_duration = hedwig_duration
        i = 0
        limit = len(hedwig_note)-1
        playing = True
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)
    elif song5.value()and (not playing or not notes == bday_note) :
        notes = bday_note
        notes_duration = bday_duration
        i = 0
        limit = len(bday_note)-1
        playing = True
        timer.init(freq=1/notes_duration[i], mode=Timer.ONE_SHOT, callback=playsong)
            
    # Shuts off the song if none of the led(s) are on. aka reset 
    if not (song1.value() or song2.value() or  song3.value() or song4.value() or song5.value()):
        speaker.duty_u16(0)
        playing = False
        pass
    if (vol == 1000):
        speaker.duty_u16(0)

        
