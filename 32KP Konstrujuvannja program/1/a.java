class Car {
  public boolean isLoaded = false;
}

class Account {
  public boolean isDeleted = false;
  public int balance = 0;
}

class User {
  public boolean isLoggedIn = false;
  public boolean isRegistered = false;
}

class a {
  public static void main(String[] args) {
    Account account = new Account();
    User user = new User();
    Car car = new Car();

    // АБО
    if (account.isDeleted || account.balance == 0)
      System.out.println("Cannot perform");
    // ТА
    if (user.isLoggedIn && user.isRegistered)
      System.out.println("Welcome");
    // НІ
    if (!car.isLoaded)
      System.out.println("Not loaded");
  }
}