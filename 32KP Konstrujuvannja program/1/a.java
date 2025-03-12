class a {
  public static void main(String[] args) {
    int a = 7;
    int b = 3;
    System.out.println("a: " + Integer.toBinaryString(a));
    System.out.println("b: " + Integer.toBinaryString(b));

    int left = a << b;
    int right = a >> b;
    int unsignedRight = a >>> b;
    System.out.println("Left << " + Integer.toBinaryString(left));
    System.out.println("Right >> " + Integer.toBinaryString(right));
    System.out.println("Unsigned right >>> " + Integer.toBinaryString(unsignedRight));
  }
}