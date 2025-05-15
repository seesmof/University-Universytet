public class a {
  public static void main(String[] args) {
    int height = 5;
    Coordinate a = new Coordinate(3, 0);
    Coordinate b = new Coordinate(7, 0);
    Coordinate d = new Coordinate(4, height);
    Coordinate c = new Coordinate(10, height);
    Trapezoid trapezoid = new Trapezoid(height, a, b, c, d);

    double area = trapezoid.getArea();
    double sideLength = 5;
    double cornerToCatenary = 3;
    double circleRadius = trapezoid.getRadiusOfInscribedCircle(sideLength, cornerToCatenary);

    System.out.println("Area: " + area);
    System.out.println("Circle radius: " + circleRadius);
  }
}
