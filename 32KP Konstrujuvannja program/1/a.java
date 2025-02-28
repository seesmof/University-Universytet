class a {
  public static void main(String[] args) {
    // Якщо написати i<=2, j<=3 працювати не буде
    for (int i = 0, j = 1; i <= 2 && j <= 3; i++, j++) {
      System.err.println(i + " and " + j);
    }
  }
}