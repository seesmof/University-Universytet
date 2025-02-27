class a {
  public static void main(String[] args) {
    outer: for (int i = 0; i < 3; i++) {
      inner: for (int j = 1; j <= 3; j++) {
        if (i == 2)
          continue outer;
        else
          System.err.println(i + " and " + j);
      }
    }
  }
}