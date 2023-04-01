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
    GeometricFigure() : centerX(0), centerY(0), angle(0), scale(0) {}

    GeometricFigure(ll centerX, ll centerY, ll angle, ll scale) : centerX(centerX), centerY(centerY), angle(angle), scale(scale) {}

    virtual void show() = 0;
    virtual void hide() = 0;
    virtual void rotate(ll angle) = 0;
    virtual void move(ll x, ll y) = 0;

    // declare a default virtual desctructor
    virtual ~GeometricFigure() {}
};

class Rectangle : public GeometricFigure
{
private:
    ll width, height;
    string color;
    string symbol;

public:
    Rectangle(ll centerX, ll centerY, ll angle, ll scale, string color) : GeometricFigure(centerX, centerY, angle, scale), color(color), symbol("") {}

    void show() override
    {
        if (color == "orange")
        {
            if (angle != 90 || angle != 180 || angle != 270 || angle != 360 || angle != 0)
                symbol = "🟧";
            else
                symbol = "🔶";
        }
        else
        {
            if (angle != 90 || angle != 180 || angle != 270 || angle != 360 || angle != 0)
                symbol = "🟦";
            else
                symbol = "🔷";
        }

        for (ll k = 0; k < centerY; k++)
            cout << "\n";

        for (ll i = 0; i < scale; i++)
        {
            for (ll k = 0; k < centerX; k++)
                cout << "    ";
            for (ll j = 0; j < scale; j++)
                cout << symbol;
            cout << endl;
        }
    }

    void hide() override
    {
        symbol = " ";
    }

    void rotate(ll angle) override
    {
        angle += angle;
    }

    void move(ll x, ll y) override
    {
        centerX += x;
        centerY += y;
    }
};

void createRectangle(vector<unique_ptr<Rectangle>> &rectangles)
{
    int centerX, centerY, angle, scale;
    string color;
    cout << "Enter center X: ";
    cin >> centerX;
    cout << "Enter center Y: ";
    cin >> centerY;
    cout << "Enter angle: ";
    cin >> angle;
    cout << "Enter scale: ";
    cin >> scale;
    cout << "Enter color (orange/blue): ";
    cin >> color;
    auto rectangle = make_unique<Rectangle>(centerX, centerY, angle, scale, color);
    rectangles.push_back(move(rectangle));
    cout << "Rectangle created!" << endl;
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