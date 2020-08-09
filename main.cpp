#include <iostream>
#include <string>
#include <iterator>
#include <map>
#include <functional>
#include <queue>
#include <vector>

using namespace std;

int main()
{
    struct prescription
    {
        int droppedOff;
        char type;
        int secondsToFill;
    };
    struct CustomCompare
    {
        bool operator()(const prescription &first, const prescription &second)
        {
            return first.droppedOff < second.droppedOff;
        }
    };

    int numOfpre, numOfWorkers, currentTime;

    priority_queue <prescription, vector<prescription>, CustomCompare> pQueue;
    prescription p;
    p.droppedOff =1;
    

    prescription z;
    p.droppedOff = 2;

    pQueue.push(p);
    pQueue.push(z);

    prescription out = pQueue.top();

    cout << out.droppedOff;


    return 0;
}