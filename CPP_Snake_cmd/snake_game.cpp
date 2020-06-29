#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;


bool gameOver;
const int width = 20;
const int height = 20;
int x,y,fruitX,fruitY,score;
int tailX[100], tailY[100];
int ntail;

enum direction{STOP=0,UP,DOWN,LEFT,RIGHT};
direction dir;

void setup(){
    gameOver = false;
    dir = STOP;
    score = 0;
    x=width/2; y=height/2;
    fruitX=rand()%width;
    fruitY=rand()%height;
}

void draw(){
    system("cls");
    //Generate upper border
    for(int i=0;i<width+2;++i){
        cout<<"#";
    }
    cout<<endl;
    //Generate the map
    for(int i=0;i<height;++i){
        for(int j=0;j<width;++j){
            if(j==0) cout<<"#";
            if (i==y && j==x) cout<<"O";
            else if (i==fruitY && j==fruitX) cout<<"F";
            else{
                bool isPrinted = false;
                for(int k=0;k<ntail;++k){
                    if(tailX[k] == j && tailY[k] == i){
                        cout<<"o";
                        isPrinted = true;
                    }
                }
                if(!isPrinted)
                cout<<" ";
            }
            if(j==width-1) cout<<"#";
        }
        cout<<"\n";
    }
    //Generate lower border
    for(int i=0;i<width+2;++i){
        cout<<"#";
    }
    cout<<endl;
    cout<<"\nSCORE: "<<score<<endl;
}

void input(){
    if(_kbhit()){
        switch(_getch()){
            case 'a':
                dir=LEFT;
                break;
            case 's':
                dir=DOWN;
                break;
            case 'd':
                dir=RIGHT;
                break;
            case 'w':
                dir=UP;
                break;
            case 'x':
                gameOver=true;
                break;
            default:
                break;
        }
    }
}

void logic(){
    //Win game when max tail size is reached
    if(ntail==100){
        gameOver=true;
        cout<<"\n\n\nYOU WON!!!\n\n\n";
        return;
    }
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = x;
    tailY[0] = y;
    for(int i=1;i<ntail;++i){
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }
    switch(dir){
            case LEFT:
                --x;
                break;
            case DOWN:
                ++y;
                break;
            case RIGHT:
                ++x;
                break;
            case UP:
                --y;
                break;
            default:
                break;
        }
    //if(x>width || x<01 || y>height || y<0) gameOver=true;
    if(x>=width) x=0;
    else if(x<0) x=width-1;
    if(y>=height) y=0;
    else if(y<0) y=height-1;

    for(int i=0;i<ntail;++i){
        if(tailX[i] == x && tailY[i] == y) gameOver = true;
    }
    if(x==fruitX && y==fruitY){
        ++ntail;
        score+=10;
        fruitX=rand()%width;
        fruitY=rand()%height;
    }
}

int main(){
    setup();
    while(!gameOver){
        draw();
        input();
        logic();
        Sleep(5);
    }
}

