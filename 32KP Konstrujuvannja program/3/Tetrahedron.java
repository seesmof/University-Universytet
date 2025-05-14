public class Tetrahedron {
  private int edge;

  public Tetrahedron(int edge) {
    this.edge = edge;
  }

  public double area() {
    return Math.pow(edge, 2) * Math.sqrt(3);
  }

  public double volume() {
    double up = Math.pow(edge, 3) * Math.sqrt(2);
    return up / 12;
  }
}
