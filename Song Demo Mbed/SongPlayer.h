#include "mbed.h"
#include <iostream>

// new class to play a note on Speaker based on PwmOut class
class SongPlayer
{
public:
    SongPlayer(PinName pin) : _pin(pin) {
// _pin(pin) means pass pin to the constructor
    }
// class method to play a note based on PwmOut class
    void PlaySong(float frequency[], float duration[], float& volume) {
        vol = &volume;
        notecount = 0;
        _pin.period(1.0/frequency[notecount]);
        _pin = 1/((float)volume);
        noteduration.attach(callback(this,&SongPlayer::nextnote), duration[notecount]);
        // setup timer to interrupt for next note to play
        frequencyptr = frequency;
        durationptr = duration;
        //returns after first note starts to play
    }
    void pause(){
//        noteduration.stop();
        }
    void nextnote();
private:
    Timeout noteduration;
    PwmOut _pin;
    int notecount;
    float *  vol;
    float * frequencyptr;
    float * durationptr;
    float pauseDuration;
};
//Interrupt Routine to play next note
void SongPlayer::nextnote()
{
    _pin = 0.0;
    notecount++; //setup next note in song
    if (durationptr[notecount]!=0.0) {
        _pin.period(1.0/frequencyptr[notecount]);
        noteduration.attach(callback(this,&SongPlayer::nextnote), durationptr[notecount]);
        float volume = *vol;
        _pin = (float)(1/volume);

    } else{
        _pin = 0.0; //turn off on last note
                noteduration.detach();
}
}
