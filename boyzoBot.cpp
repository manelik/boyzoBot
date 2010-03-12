#include <iostream>
#include <cstdlib>

using namespace std;


class rantBot{
public:
  string name;
  float mood; //if mood reaches zero, rantBot goes to sleep

  rantBot(){name="";mood=0.0;};
  rantBot(string,float);
  void RandomRant();

};

rantBot::rantBot(string botNom,float initmood){
  name=botNom;
  mood=initmood;
}

void rantBot::RandomRant(){
  cout <<" Rant!"<<endl;
}

int main(){
  rantBot boyzoBot("boyzo",10.0);
  int timestep;
  int flag=1;

  srand(time(NULL));

  while(flag){
    timestep=rand()%10;
    sleep(timestep);
    boyzoBot.RandomRant();
    boyzoBot.mood-=1;
    if(boyzoBot.mood<=0.0)flag=0;
  }

  cout <<"boyzoBot cansado RANT! a dormir"<<endl;

  return 0;
}
