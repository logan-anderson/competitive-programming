#include <iostream>
using namespace std;

class ent
{
public:
    ent(char type_in);
    ~ent();
    char type;
};

ent::ent(char type_in)
{
    type = type_in;
}

ent::~ent()
{
}


int main()
{
    /* code */
    ent thing = ent('o');
    cout << thing.type << '\n';

    return 0;
}
