class a {
  public static void main(String[] args) {
    boolean check = false;
    outer: while (!check) {
      System.err.println("False");
      boolean other = false;
      inner: while (!other) {
        System.err.println("False" + " False");
        // Множення рядків не працює. Якщо писати "False"*2, видасть помилку
        other = true;
        if (other) {
          break outer;
        }
      }
    }
  }
}