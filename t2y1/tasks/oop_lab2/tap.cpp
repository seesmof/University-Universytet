#include "../lib.h"
using namespace std;

// define the Stop struct, which represents a stop on the route
struct Stop
{
    string name;     // name of the stop
    double distance; // distance from previous stop
    Stop *prev;      // pointer to previous stop in route
    Stop *next;      // pointer to next stop in route
};

// define the Route class, which represents a route composed of stops
class Route
{
private:
    Stop *head; // pointer to first stop in route
    Stop *tail; // pointer to last stop in route
public:
    // constructor initializes empty route with head and tail set to nullptr
    Route() : head(nullptr), tail(nullptr) {}

    // destructor deletes all stops in route
    ~Route()
    {
        Stop *curr = head;
        while (curr != nullptr)
        {
            Stop *next = curr->next;
            delete curr;
            curr = next;
        }
    }

    // adds a new stop with the given name and distance from previous stop to the end of the route
    void add_stop(string name, double distance)
    {
        Stop *stop = new Stop();
        stop->name = name;
        stop->distance = distance;
        stop->prev = tail;
        stop->next = nullptr;
        if (tail != nullptr)
        {
            tail->next = stop;
        }
        tail = stop;
        if (head == nullptr)
        {
            head = stop;
        }
    }

    // returns the length of the route by summing the distance between each pair of adjacent stops
    double len_route()
    {
        double length = 0.0;
        Stop *curr = head;
        while (curr != nullptr && curr->next != nullptr)
        {
            length += curr->distance;
            curr = curr->next;
        }
        return length;
    }

    // returns the time required to travel the route assuming a fixed speed of 50 km/h
    double time_route()
    {
        double time = len_route() / 50.0;
        return time;
    }
};

// main function creates a new route and adds stops to it, then prints the length and travel time of the route
int main()
{
    Route route;
    route.add_stop("New York", 20.5);
    route.add_stop("Chicago", 15.0);
    route.add_stop("Denver", 10.5);
    route.add_stop("San Francisco", 30.0);
    double length = route.len_route();
    double time = route.time_route();
    cout << "Route length: " << length << " km" << endl;
    cout << "Travel time: " << time << " hours" << endl;
    return 0;
}
