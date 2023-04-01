class GeometricShape
{
protected:
    int x, y;    // coordinates of the center of the figure
    float angle; // angle of rotation (in degrees)
    float scale; // scale factor
public:
    virtual void show() = 0;               // show the figure on the screen
    virtual void hide() = 0;               // make the figure invisible (destroy its image)
    virtual void rotate(float angle) = 0;  // rotate the figure by a given angle (the angle is given in degrees)
    virtual void move(int dx, int dy) = 0; // move the figure to the given vector
};

class Circle : public GeometricShape
{
private:
    int radius;

public:
    Circle(int x, int y, int radius)
    {
        this->x = x;
        this->y = y;
        this->radius = radius;
        this->angle = 0.0f;
        this->scale = 1.0f;
    }
    void show()
    {
        // implementation for showing a circle on the screen
    }
    void hide()
    {
        // implementation for hiding a circle on the screen
    }
    void rotate(float angle)
    {
        // implementation for rotating a circle on the screen
    }
    void move(int dx, int dy)
    {
        this->x += dx;
        this->y += dy;
    }
};

int main()
{
    Circle c(100, 100, 50);
    c.show();        // show the circle on the screen
    c.rotate(45.0f); // rotate the circle by 45 degrees
    c.move(50, 0);   // move the circle 50 pixels to the right
    c.hide();        // hide the circle from the screen
    return 0;
}
