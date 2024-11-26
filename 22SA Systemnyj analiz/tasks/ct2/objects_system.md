```csharp
Class_Library // бібліотека класів даних та класів обробників даних
  currentUser.cs // клас даних поточного користувача
    string name; // ім'я користувача
    string password; // пароль користувача
    bool isAdmin; // чи є користувач адміністратором
  flight.cs // клас даних рейсу
    string name; // назва рейсу
    int price; // стандартна ціна рейсу
    string date; // дата рейсу
    int seats; // кількість місць
  flightsDataManager.cs // клас обробник даних рейсів
    List<flight> loadFlights(); // завантажує дані рейсів
    flight getFlight(string name); // повертає рейс за назвою
  ticket.cs // клас даних квитка
    string userName; // ім'я користувача
    string flightName; // назва рейсу
    int price; // загальна ціна квитка
    string date; // дата рейсу
    int seatRow; // обраний ряд місця
    bool isMiddle; // чи місце у середньому ряду 
    bool isWindow; // чи місце біля вікна 
    bool isPrivate; // чи місце приватне
    bool isBaggage; // чи потрібне додаткове місце для багажу
    bool isMeal; // чи потрібне харчування на борту
  ticketsDataManager.cs // клас обробник даних квитків
    List<ticket> loadTickets(); // завантажує дані квитків
    ticket GetTicket(string flightName); // повертає квиток за назвою рейсу
    List<ticket> GetOwnTickets(string userName); // повертає квитки користувача
    void AddTicket(string userName, string flightName, int price, string date, int seatRow, bool isMiddle, bool isWindow, bool isPrivate, bool isBaggage, bool isMeal); // додає новий квиток за всіма даними
  user.cs // клас даних користувача
    string name; // ім'я користувача
    string password; // пароль користувача
    bool isAdmin; // чи є користувач адміністратором
  userDataManager.cs // клас обробник даних користувачів
    List<user> loadUsers(); // завантажує дані користувачів
    void addUser(string name, string password, bool isAdmin); // додає нового користувача
    user getUser(string name); // повертає користувача за ім'ям
    bool isAdmin(string name); // повертає чи є користувач адміністратором
    bool validateCredentials(string name, string password); // повертає чи валідні дані користувача
App // містить форми користувацького інтерфейсу та файли даних 
  flights.txt // дані рейсів
    flight_name,price,date,seats // назва рейсу, ціна, дата, кількість місць
    // продовжується з нового рядку так само
  tickets.txt // дані квитків
    user_name,flight_name,price,date,seat_row,is_middle,is_window,is_private,is_baggage,is_meal // ім'я користувача, назва рейсу, ціна, дата, ряд місця, чи середній ряд, чи місце біля вікна, чи місце приватне, чи потрібен додатковий багаж, чи потрібне харчування
    // продовжується з нового рядку так само
  users.txt // дані користувачів
    name,password,is_admin // ім'я користувача, пароль, чи є адміністратором
    // продовжується з нового рядку так само
  flights.cs // форма перегляду рейсів
  login.cs // форма входу
  menu.cs // форма меню
  signup.cs // форма реєстрації
  tickets.cs // форма перегляду квитків
```