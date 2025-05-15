public class Trapezoid {
  public Coordinate a;
  public Coordinate b;
  public Coordinate c;
  public Coordinate d;
  public double height;

  private double _lowerBase;
  private double _upperBase;

  public Trapezoid(int height, Coordinate a, Coordinate b, Coordinate c, Coordinate d) {
    this.a = a;
    this.b = b;
    this.c = c;
    this.d = d;
    this.height = height;

    this._lowerBase = Math.abs(c.x - d.x);
    this._upperBase = Math.abs(b.x - a.x);
  }

  public double getArea() {
    return (_upperBase + _lowerBase) * height / 2;
  }

  public double getRadiusOfInscribedCircle(double sideLength, double cornerToCatenary) {
    double squared = Math.pow(sideLength, 2) - Math.pow(cornerToCatenary, 2);
    double regular = Math.sqrt(squared);
    return regular / 2;
  }
}
