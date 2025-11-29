public class Tetrahedron {
  private int _edge;

  public Tetrahedron(int edge) {
    this._edge = edge;
  }

  public double area() {
    return Math.pow(_edge, 2) * Math.sqrt(3);
  }

  public double volume() {
    double up = Math.pow(_edge, 3) * Math.sqrt(2);
    return up / 12;
  }
}
