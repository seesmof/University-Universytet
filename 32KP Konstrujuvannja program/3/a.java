public class a {
  public static void main(String[] args) {
    int radius = 3;
    int height = 5;
    Cylinder cylinder = new Cylinder(radius, height);

    double area = cylinder.area();
    double volume = cylinder.volume();

    System.out.println("Area: " + area);
    System.out.println("Volume: " + volume);
  }
}
