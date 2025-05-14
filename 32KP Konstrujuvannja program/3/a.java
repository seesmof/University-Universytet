public class a {
  public static void main(String[] args) {
    Cylinder c = new Cylinder(7, 5);
    System.out.println(c.area());
    System.out.println(c.volume());

    Tetrahedron t = new Tetrahedron(10);
    System.out.println(t.area());
    System.out.println(t.volume());
  }
}
