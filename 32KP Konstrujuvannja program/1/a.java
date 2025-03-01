class a {
  public static void main(String[] args) {
    // Оголошення
    String[] texts;
    // Встановлення
    texts = new String[3];
    // Ініціаліація
    texts[0] = "One";
    texts[1] = "Two";
    texts[2] = "Three";
    // Вивід
    for (String text : texts) {
      System.err.println(text);
    }
  }
}