#include "mbed.h"
class displaySegmentNum{
    public:
    displaySegmentNum(PinName A,PinName B,PinName C,PinName D,PinName E,PinName F,PinName G):_A(A),_B(B),_C(C),_D(D),_E(E),_F(F),_G(G){
        }
    void displayNum(int val){
        switch(val){
            case 1:
            _A = 0.0;
            _B = 0.5;
            _C = 0.5;
            _D = 0.0;
            _E = 0.0;
            _F = 0.0;
            _G = 0.8;
                break;
            case 2:
            _A = 0.8;
            _B = 0.8;
            _C = 0.0;
            _D = 0.8;
            _E = 0.8;
            _F = 0.0;
            _G = 0.8;
                break;
            case 3:
            _A = 0.8;
            _B = 0.8;
            _C = 0.8;
            _D = 0.8;
            _E = 0.8;
            _F = 0.0;
            _G = 0.8;
                break;
            case 4:            
            _A = 0.0;
            _B = 0.8;
            _C = 0.8;
            _D = 0.0;
            _E = 0.0;
            _F = 0.8;
            _G = 0.8;
                break;
            case 5:
            _A = 0.8;
            _B = 0.0;
            _C = 0.8;
            _D = 0.0;
            _E = 0.8;
            _F = 0.8;
            _G = 0.8;
                break;
            case 6:
            _A = 0.0;
            _B = 0.0;
            _C = 0.8;
            _D = 0.8;
            _E = 0.8;
            _F = 0.8;
            _G = 0.8;
                break;
            case 7:
            _A = 0.8;
            _B = 0.8;
            _C = 0.8;
            _D = 0.0;
            _E = 0.0;
            _F = 0.0;
            _G = 0.0;
                break;
            case 8:
            _A = 0.8;
            _B = 0.8;
            _C = 0.8;
            _D = 0.8;
            _E = 0.8;
            _F = 0.8;
            _G = 0.8;
                break;
            case 9:
            _A = 0.8;
            _B = 0.8;
            _C = 0.8;
            _D = 0.0;
            _E = 0.0;
            _F = 0.8;
            _G = 0.8;
                break;
            
            }
        }
    private:
    PwmOut _A;
    PwmOut _B;
    PwmOut _C;
    PwmOut _D;
    PwmOut _E;
    PwmOut _F;
    PwmOut _G;
    };