class a {
  public static void main(String[] args) {
    int a = 7;
    int b = 3;
    System.out.println("a: " + Integer.toBinaryString(a));
    System.out.println("b: " + Integer.toBinaryString(b));
    int and = a & b;
    System.out.println(and + " AND in bin: " + Integer.toBinaryString(and));
    int or = a | b;
    System.out.println(or + " OR in bin: " + Integer.toBinaryString(or));
    int eor = a ^ b;
    System.out.println(eor + " EOR in bin: " + Integer.toBinaryString(eor));
    int com = ~a;
    System.out.println(com + " COM in bin: " + Integer.toBinaryString(com));
  }
}