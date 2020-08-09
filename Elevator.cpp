#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int canIGetThere(int currentFloor, int steps, int goalFloor);
int stepsToGetThere(int currentFloor, int totalFloors, int goalFloor, int upSteps, int downSteps);
int main() {
    int f,s,g,u,d;
    cin >> f >> s >> g >> u >> d;
    cout <<   stepsToGetThere(s,f,g,u,d) << endl;
    return 0;
}
int stepsToGetThere(int currentFloor, int totalFloors, int goalFloor, int upSteps, int downSteps) {
    if(currentFloor > totalFloors || currentFloor < 1) {
        cout << "use the stairs\n";
        exit(0);
    }
    int stepsToTake = goalFloor - currentFloor;
    if(stepsToTake == 0) {
        return 0;
    }
    else if( (currentFloor + upSteps >  totalFloors  || upSteps == 0 ) && (currentFloor - upSteps < 1  || downSteps == 0) ){
        cout << "use the stairs\n";
        exit(0);
    }
    // if you can not step up step up
    else if(currentFloor + upSteps >  totalFloors || upSteps == 0) {
         // make a step down
        currentFloor = currentFloor - downSteps;
        return 1 + stepsToGetThere(currentFloor, totalFloors, goalFloor, upSteps, downSteps);
    }
    else if(currentFloor - upSteps < 1 || downSteps == 0) {
        //make a step up
        currentFloor = currentFloor + upSteps;
        return 1 + stepsToGetThere(currentFloor, totalFloors, goalFloor, upSteps, downSteps);
    }
    else if(stepsToTake > 0){
        // we gotta go up
        int iCan = canIGetThere(currentFloor, goalFloor, upSteps); 
        if(iCan) {
            return iCan;
        }
        else {
            // make a step down
            currentFloor = currentFloor - downSteps;
            return 1 + stepsToGetThere(currentFloor, totalFloors, goalFloor, upSteps, downSteps);
            
        }
    } 
    else {
        // we need to go down
        int iCan = canIGetThere(currentFloor, goalFloor, downSteps);
        if(iCan) {
            return iCan;
        }
        else {
            //make a step up
            currentFloor = currentFloor + upSteps;
            return 1 + stepsToGetThere(currentFloor, totalFloors, goalFloor, upSteps, downSteps);
            
        }
    }
}
int canIGetThere(int currentFloor, int goalFloor, int steps) {
    if(steps == 0) {
        return 0;
    }
    int total_steps = abs(currentFloor - goalFloor);
    if( ( total_steps % steps) == 0) {
        return total_steps/steps;
    }
    else {
        return 0;
    }
}