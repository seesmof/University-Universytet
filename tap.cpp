class Point
{
private:
    int x;
    int y;

public:
    // Constructor for initializing x and y values

    Point(int xVal, int yVal)
    {

        x = xVal;

        y = yVal;
    }

    // Getter methods for retrieving x and y values

    int getX() { return x; }

    int getY() { return y; }
};