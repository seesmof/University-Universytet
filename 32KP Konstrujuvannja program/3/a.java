public class a {
  public static void main(String[] args) {
    Coordinate a = new Coordinate(0, 0);
    Coordinate b = new Coordinate(7, 0);
    Coordinate c = new Coordinate(2, 5);
    Coordinate d = new Coordinate(5, 5);
    Trapezoid g = new Trapezoid(3, a, b, c, d);
    System.out.println(g.getArea());
  }
}
