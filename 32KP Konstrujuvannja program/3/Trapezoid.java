public class Trapezoid {
  private int height;
  private Coordinate a;
  private Coordinate b;
  private Coordinate c;
  private Coordinate d;

  private int lowerBase;
  private int upperBase;

  public Trapezoid(int height, Coordinate a, Coordinate b, Coordinate c, Coordinate d) {
    this.height = height;
    this.a = a;
    this.b = b;
    this.c = c;
    this.d = d;

    this.lowerBase = c.x - d.x;
    this.upperBase = b.x - a.x;
  }

  public double getArea() {
    return (upperBase + lowerBase) * height / 2;
  }

  public double getRadiusOfInscribedCircle(double sideLength, double cornerToCatenary) {
    double squared = Math.pow(sideLength, 2) - Math.pow(cornerToCatenary, 2);
    double regular = Math.sqrt(squared);
    return regular / 2;
  }
}
