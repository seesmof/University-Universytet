public class Cylinder {
  private int radius;
  private int height;

  public Cylinder(int radius, int height) {
    this.radius = radius;
    this.height = height;
  }

  public double area() {
    double circlesArea = 2 * Math.PI * Math.pow(radius, 2);
    double rectanglesArea = 2 * Math.PI * this.radius * this.height;
    return circlesArea + rectanglesArea;
  }

  public double volume() {
    return Math.PI * Math.pow(this.radius, 2) * this.height;
  }
}