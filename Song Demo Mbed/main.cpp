#include "mbed.h"
#include "SongPlayer.h"
#include "SevenSegmentDisplay.h"

// Song test program - plays a song using PWM and timer interrupts
// for documentation see http://mbed.org/users/4180_1/notebook/using-a-speaker-for-audio-output/
// can be used to play a song, if you have the notes and durations
// for musical note frequencies see http://en.wikipedia.org/wiki/Piano_key_frequencies

// Set up notes and durations for sample song to play
// A 0.0 duration note at end terminates song play

// Version 2.0: Added note variables for easier song translation as well as
// beat variables for easier time/duration translation - Group 6, ELCT 201

// Notes
float AL = 880.000;
float BL = 987.7666;
float C = 1046.502;
float D = 1174.659;
float Ef = 1244.508;
float E = 1318.510;
float F = 1396.913;
float G = 1567.982;
float A = 1760.000;
float Bf = 1864.655;
float B = 1975.533;
float CH = 2093.005;
float CHs = 2217.461;
float DH = 2349.318;
float EHf = 2489.016;
float EH = 2637.020;
float FH = 2793.826;
float FHs = 2959.955;
float GH = 3135.963;

// Beats
float SX = 0.125;
float ET = 0.25;
float ETex = 0.375;
float Q = 0.5;
float H = 1;
float EX = 1.5;
float FULL = 2;
float EXH = 2.5;

int numSongs = 5;
int currentSong = 5;

    // Twinkle Twinkle Little Start
    float twinkle_note[43]= {C, C, G, G, A, A, G, F, F, E, E, D, D, C, G, 
                G, F, F, E, E, D, G, G, F, F, E, E, D, C, C, 
                G, G, A, A, G, F, F, E, E, D, D, C, 0.0
                };
    float twinkle_duration[43]= {Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H, 
                Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H, 
                Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, Q, H, 0.0
                };
    
    // Damned
    float damned_note[65]= {B, E, BL, B, E, BL, B, E, B, E, BL, B, E, BL, B, //15
                E, CH, E, C, CH, E, C, CH, E, DH, E, C, CH, E, C, B, E, B, //33
                E, BL, B, E, BL, B, E /*40*/, B, E, BL, B, E, BL, B, E, CH, E, C, CH, E, //53
                C, CH, E, DH, E, C, CH, E, C, B, A, 0.0 //65
                };
    float damned_duration[65]= {ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, 
                ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, 
                ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, 
                ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, ET, 0.0
                };
                
    // Let It Be

    float letit_note[59]= {G, G, G, G, A, E, G, G, CH, DH, CH, CH, CH, B, A, CH, A, EH, EH, FH, EH,  //21 
                EH, DH, EH, DH, DH,CH, G, F, E, G, G, G, A, CH, G, G, CH, DH, CH, CH, CH, B, A, CH, 
                A, EH, EH, FH, EH, EH, DH, EH, DH, DH, CH, G, F, 0.0
                };
    float letit_duration[59]= {ET, ET, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, Q, H, //23
                ET, ET, Q, Q, Q, Q, EX, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, Q, H, Q, Q, Q, Q, //50
                Q, H, ET, ET, Q, Q, Q, Q, 0.0
                };
    // Happy Birthday    
    float bday_note[26]= {C, C, D, C, F, E, C, C, D, C, G, F, C, C, CH, A, F, E, D, Bf, Bf, A, F, G, F, 0.0
                };
    float bday_duration[26]= {ETex, SX, Q, Q, Q, H, ETex, SX, Q, Q, Q, H, ETex, SX, Q, Q, Q, Q, Q, ETex, SX, 
                Q, Q, Q, H, 0.0
                };
    
    // Hedwig's Theme
    float hedwig_note[32]= {E, A, CH, B, A, EH, DH, B, A, CH, B, G, Bf, E, E, A, CH, B, A, EH, GH, FHs, F, 
                CHs, F, EH, EHf, Ef, CH, A, CH, 0.0
                };
    float hedwig_duration[32]= {Q, Q, Q, Q, H, Q, EX, EX, Q, Q, Q, H, Q, EXH, Q, Q, Q, Q, H, Q, H, Q, H, 
                Q, Q, Q, Q, H, Q, EXH, Q, 0.0
                };
                int currentVolumeLevel = 1;
                float volumeLevel = 10*(20-currentVolumeLevel*2);

displaySegmentNum displayVolumeNumber(A1,A0,A4,A5,PTE20,A3,A2);
//InterruptIn vol_1(PTA17);
//DigitalIn vol_2(PTA16);
DigitalIn musiButton_1(PTD7);
DigitalIn musiButton_2(PTD6);
DigitalIn musiButton_3(PTD4);
DigitalIn musiButton_4(PTD5);
DigitalIn musiButton_5(PTD0);

InterruptIn volume_Up(PTA17);
InterruptIn volume_Down(PTA16);

SongPlayer mySpeaker(PTE29);

void changeSong(){
    //currentSong++;
    if(currentSong == 0)
        mySpeaker.PlaySong(twinkle_note,twinkle_duration,volumeLevel);
    else if(currentSong == 1)
        mySpeaker.PlaySong(damned_note,damned_duration,volumeLevel);
    else if(currentSong == 2)
        mySpeaker.PlaySong(letit_note,letit_duration,volumeLevel);
    else if(currentSong == 3)
        mySpeaker.PlaySong(bday_note,bday_duration,volumeLevel);
    else if(currentSong == 4)
        mySpeaker.PlaySong(hedwig_note,hedwig_duration,volumeLevel);
}      

void setMusic_1(){

   if(currentSong!=0){
    currentSong = 0;
    changeSong();}
    }
void setMusic_2(){

    if(currentSong!=1){
    currentSong = 1;
    changeSong();}
    }
    void setMusic_3(){
    if(currentSong!=2){
    currentSong = 2;
    changeSong();}
        }
            void setMusic_4(){
    if(currentSong!=3){
    currentSong = 3;
    changeSong();}
        }    void setMusic_5(){
    if(currentSong!=4){
    currentSong = 4;
    changeSong();}
        }
void volUP(){
    if(currentVolumeLevel!=9){
    ++currentVolumeLevel; 
    volumeLevel = 10*(20-currentVolumeLevel*2);
    displayVolumeNumber.displayNum(currentVolumeLevel);
    }
 
}  
void volDown(){
    if(currentVolumeLevel!=1){
    --currentVolumeLevel; 
    volumeLevel = 10*(20-currentVolumeLevel*2);
    displayVolumeNumber.displayNum(currentVolumeLevel);
    }
    }
int main(){
    volume_Up.rise(&volUP);
    volume_Down.rise(&volDown);
    while(1) {   
        if(musiButton_1){
            setMusic_1();
        }
          else  if(musiButton_2){
            setMusic_2();
        }
         else   if(musiButton_3){
            setMusic_3();
        }
        else    if(musiButton_4){
            setMusic_4();
        }
        else    if(musiButton_5){
            setMusic_5();
        }
    }
}