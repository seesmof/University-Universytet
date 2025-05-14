public class Trapezoid {
  private int height;
  private int upperBase;
  private int lowerBase;

  public Trapezoid(int height, int upperBase, int lowerBase) {
    this.height = height;
    this.upperBase = upperBase;
    this.lowerBase = lowerBase;
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
