Class_Library
  currentUser.cs
    string name
    string password
    bool isAdmin
  user.cs
    string name
    string password
    bool isAdmin
  flight.cs
    string name
    int price
    string date
    int seats
  ticket.cs
    string userName
    string flightName
    int price
    string date
    int seatRow
    bool isMiddle
    bool isWindow
    bool isPrivate
    bool isBaggage
    bool isMeal
  flightsDataManager.cs
    interface IFlightsDataManager
    List<flight> loadFlights()
    flight getFlight(string name)
  ticketsDataManager.cs
    interface ITicketsDataManager
    List<ticket> loadTickets()
    ticket GetTicket(string flightName)
    List<ticket> GetOwnTickets(string userName)
    void AddTicket(string userName, string flightName, int price, string date, int seatRow, bool isMiddle, bool isWindow, bool isPrivate, bool isBaggage, bool isMeal)
  userDataManager.cs
    interface IuserDataManager
    List<user> loadUsers()
    void addUser(string name, string password, bool isAdmin)
    user getUser(string name)
    bool isAdmin(string name)
    bool validateCredentials(string name, string password)
App
  ... all the forms and data files ...
  flights.txt
    ... rows of data ...
    flight_name,price,date,seats
  tickets.txt
    ... rows of data ...
    user_name,flight_name,price,date,seat_row,is_middle,is_window,is_private,is_baggage,is_meal
  users.txt
    ... rows of data ...
    name,password,is_admin
  flights.cs
    flights.Designer.cs
  login.cs
    login.Designer.cs
  menu.cs
    menu.Designer.cs
  signup.cs
    signup.Designer.cs
  tickets.cs
    tickets.Designer.cs