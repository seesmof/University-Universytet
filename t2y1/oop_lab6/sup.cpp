#include "sup.h"
#include "../../lib.h"
using namespace std;

/*
Варіант 5. Для класу «Геометрична фігура» з варіанту 2, створити похідний клас для роботи з фігурою типу «прямокутник». Визначити інтерфейсну частину у класах, застосувати атрибути доступу.

Варіант 2. Створити абстрактний клас для роботи з геометричними фігурами на екрані. Передбачити такі компоненти–властивості класу: координати центра фігури; кут повороту (у градусах); масштабний фактор; і такі функції–методи: показати фігуру на екрані; зробити фігуру невидною (знищити її зображення); повернути фігуру на заданий кут (кут надається у градусах); пересунути фігуру на наданий вектор.
*/

class GeometricFigure
{
protected:
    ll centerX;
    ll centerY;
    ll angle;
    ll scale;

public:
    // declare default constructor
    GeometricFigure() : centerX(0), centerY(0), angle(0), scale(0) {}

    // declare parameterized constructor
    GeometricFigure(ll centerX, ll centerY, ll angle, ll scale) : centerX(centerX), centerY(centerY), angle(angle), scale(scale) {}

    // declare pure virtual functions
    virtual void show() = 0;
    virtual void hide() = 0;
    virtual void rotate(ll angle) = 0;
    virtual void move(ll x, ll y) = 0;

    // declare a default virtual desctructor
    virtual ~GeometricFigure() {}
};

// declare derived class
class Rectangle : public GeometricFigure
{
private:
    string color;
    string symbol;

public:
    // declare default constructor
    Rectangle() : color(""), symbol("") {}

    // declare parameterized constructor
    Rectangle(ll centerX, ll centerY, ll angle, ll scale, string color) : GeometricFigure(centerX, centerY, angle, scale), color(color), symbol("") {}

    // declare show method
    void show() override
    {
        // check for angle for both colors
        if (color == "orange")
        {
            if (angle == 90 || angle == 180 || angle == 270 || angle == 360 || angle == 0)
                symbol = "🟧";
            else
                symbol = "🔶";
        }
        else
        {
            if (angle == 90 || angle == 180 || angle == 270 || angle == 360 || angle == 0)
                symbol = "🟦";
            else
                symbol = "🔷";
        }

        // output Y offset
        for (ll k = 0; k < centerY; k++)
            cout << "\n";

        // output rectangle
        for (ll i = 0; i < scale; i++)
        {
            // with X offset
            for (ll k = 0; k < centerX; k++)
                cout << "  ";
            // and rectangles themselves
            for (ll j = 0; j < scale; j++)
                cout << symbol;
            // end current line
            cout << endl;
        }
    }

    // declare hide method
    void hide() override
    {
        // replace symbol with whitespace
        symbol = " ";
    }

    // declare rotate method
    void rotate(ll angle) override
    {
        // modify by given angle
        angle += angle;
    }

    // declare move method
    void move(ll x, ll y) override
    {
        // move figure by given values
        centerX += x;
        centerY += y;
    }
};

// declare function for creating rectangle
void createRectangle(vector<unique_ptr<Rectangle>> &rectangles)
{
    cout << "How many rectangles to create: ";
    ll amount = getNum();

    if (amount < 0)
    {
        bad("Cannot create that many rectangles. Try again later...");
        return;
    }

    for (ll i = 0; i < amount; i++)
    {
        cout << "(" << i + 1 << ") Creating rectangle...\n";

        cout << "    "
             << "Enter rectangles's X offset: ";
        ll centerX = getNum();

        cout << "    "
             << "Enter rectangles's Y offset: ";
        ll centerY = getNum();

        cout << "    "
             << "Enter rectangles's angle: ";
        ll angle = getNum();

        cout << "    "
             << "Enter rectangles's scale: ";
        ll scale = getNum();

        string color;
        cout << "    "
             << "Enter rectangles's color ( orange | blue ): ";
        cin >> color;

        rectangles.push_back(make_unique<Rectangle>(centerX, centerY, angle, scale, color));
    }

    if (rectangles.size() == amount)
        good("All rectangles were created successfully!");
    else
        bad("There was some problem creating rectangles");
    return;
}

void showRectangles(const vector<unique_ptr<Rectangle>> &rectangles)
{
    for (const auto &rectangle : rectangles)
    {
        rectangle->show();
    }
}

void deleteRectangle(vector<unique_ptr<Rectangle>> &rectangles)
{
    int index;
    cout << "Enter index of rectangle to delete: ";
    cin >> index;
    if (index >= 0 && index < rectangles.size())
    {
        rectangles.erase(rectangles.begin() + index);
        cout << "Rectangle deleted!" << endl;
    }
    else
    {
        cout << "Invalid index!" << endl;
    }
}

void modifyRectangle(vector<unique_ptr<Rectangle>> &rectangles)
{
    int index;
    cout << "Enter index of rectangle to modify: ";
    cin >> index;
    if (index >= 0 && index < rectangles.size())
    {
        int option;
        cout << "1. Move rectangle" << endl;
        cout << "2. Rotate rectangle" << endl;
        cout << "Enter option: ";
        cin >> option;
        if (option == 1)
        {
            int x, y;
            cout << "Enter X offset: ";
            cin >> x;
            cout << "Enter Y offset: ";
            cin >> y;
            rectangles[index]->move(x, y);
            cout << "Rectangle moved!" << endl;
        }
        else if (option == 2)
        {
            int angle;
            cout << "Enter angle: ";
            cin >> angle;
            rectangles[index]->rotate(angle);
            cout << "Rectangle rotated!" << endl;
        }
        else
        {
            cout << "Invalid option!" << endl;
        }
    }
    else
    {
        cout << "Invalid index!" << endl;
    }
}