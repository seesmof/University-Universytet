# aвтоматизована система купівлі авіаквитків
## вступ

Ландшафт авіаперевезень суттєво змінився з появою автоматизованих систем продажу авіаквитків, які спростили процес бронювання та покращили якість обслуговування клієнтів. Незважаючи на значний прогрес, що призвів до ефективних процесів бронювання та оплати, залишаються проблеми з інтеграцією цих систем з динамічними моделями ціноутворення та багатоканальними мережами дистрибуції.

Провідні компанії в цій галузі, такі як Amadeus, Sabre і Travelport, продовжують впроваджувати інновації, спираючись на ідеї таких експертів галузі, як Алекс Кремер і Генрі Хартевельдт. Світові тенденції свідчать про перехід до більш персоналізованих і зручних інтерфейсів, використання штучного інтелекту для прогнозування поведінки споживачів та оптимізації продажів.

Актуальність цього дослідження полягає в тому, що воно може заповнити існуючі прогалини, пропонуючи систему, яка не тільки спрощує транзакції, але й пропонує предиктивну аналітику для управління запасами. Метою цієї роботи є розробка комплексного рішення, яке задовольнить потреби як авіакомпаній, так і мандрівників, і може бути застосоване на різних платформах і пристроях.

Ця робота ґрунтується на попередніх дослідженнях у цій галузі, спрямованих на синтез найкращих практик та впровадження нових підходів до дизайну та функціональності системи. Вона є свідченням постійного розвитку технологій авіаперевезень, спрямованих на значний прогрес у цій галузі.

## основна частина
### проєктування системи
- вимоги до програмного забезпечення
- вхідні та вихідні дані
- спосіб роботи з даними (структура бази даних) з використанням відповідної діаграми
- прототип графічного інтерфейсу користувача
- система об'єктів, які використовуються в предметній області що аналізується з описом основних атрибутів і методів цих об'єктів та використанням відповідної діаграми
- функціональні моделі основних процесів

Software Requirements:
- Середовище розробки: Visual Studio
- Мова програмування: C#
- Фреймворк: .NET для WinForms
- База даних: Текстові файли (flights.txt, tickets.txt, users.txt)

Input and Output Data:
- Вхідні: Дані, введені користувачем через форми графічного інтерфейсу.
- Вихідні: Відображення даних у графічному інтерфейсі, оновлені текстові файли.

Database Structure:
Спосіб роботи з даними є прямолінійним: користувач взаємодіє з графічним інтерфейсом, в залежності від виконаних дій до бази даних надходять запити про створення об'єктів на основі класів даних. Після створення об'єкти заносяться у базу даних, а файли зберігаються. При потребі, в залежності від виконаних дій, до бази даних надходять запити на вибірку даних, а ці дані подаються через форми графічного інтерфейсу до користувача.
Структура бази даних виглядає наступним чином (Рис. 1.1):
- Структура бази даних (Рис. 1.1)
- flights.txt: `flight_name,price,date,seats`
- tickets.txt: `user_name,flight_name,price,date,seat_row,is_middle,is_window,is_private,is_baggage,is_meal`
- users.txt: `name,password,is_admin`

GUI Prototype:
Схематичний прототип графічного інтерфейсу користувача:
- Login Form
- Signup Form
- Menu Form
- Flights Form
- Tickets Form
Нижче наведено графічні форми прототипи графічного інтерфейсу користувача (Рис. 1.2-7):
- Прототип форми  (Рис. 1.)

System of Objects:
All the data classes and data handlers with their interfaces are located in a separate classes library called Class_Library, from which we import a compiled .dll file to then use them in the UI of our program.
Всі класи даних та обробники даних з їх інтерфейсами знаходяться в окремій бібліотеці класів Class_Library, з якої ми імпортуємо скомпільований .dll файл, аби потім використовувати їх в інтерфейсі нашої програми.
Вміст Class_Library виглядає наступним чином:
```csharp
Class_Library
  currentUser.cs
    string name
    string password
    bool isAdmin
  flight.cs
    string name
    int price
    string date
    int seats
  flightsDataManager.cs
    interface IFlightsDataManager
    List<flight> loadFlights()
    flight getFlight(string name)
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
  ticketsDataManager.cs
    List<ticket> loadTickets()
    ticket GetTicket(string flightName)
    List<ticket> GetOwnTickets(string userName)
    void AddTicket(string userName, string flightName, int price, string date, int seatRow, bool isMiddle, bool isWindow, bool isPrivate, bool isBaggage, bool isMeal)
  user.cs
    string name
    string password
    bool isAdmin
  userDataManager.cs
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
```
1. currentUser.cs:
- Attributes: name, password, isAdmin
1. flight.cs:
- Attributes: name, price, date, seats
1. flightsDataManager.cs:
- Methods: loadFlights(), getFlight(name)
1. ticket.cs:
- Attributes: userName, flightName, price, date, seatRow, isMiddle, isWindow, isPrivate, isBaggage, isMeal
1. ticketsDataManager.cs:
- Methods: loadTickets(), GetTicket(flightName), GetOwnTickets(userName), AddTicket(...)
1. user.cs:
- Attributes: name, password, isAdmin
1. userDataManager.cs:
- Methods: loadUsers(), addUser(...), getUser(name), isAdmin(name), validateCredentials(name,password)

Functional Models of Main Processes:
- signup 
- booking a ticket 
- viewing tickets

1. User Authentication Process:
- Use userDataManager to validate credentials.
1. Flight Booking Process:
- Select flight using flightsDataManager.
- Book ticket using ticketsDataManager.
### опис програми
- функціональну схему програмного забезпечення
  - just all the data classes and data handlers scattered and connected
- структурну схему програмного забезпечення у вигляді діаграми компонентів
  - root then Class_Library and App, then all the classes there 
- опис модулів реалізованого програмного забезпечення з визначенням основних функцій

Структуру проєкту можна умовно поділити на чотири секції:
- обробники даних 
- класи даних 
- файли даних 
- форми інтерфейсу користувача
Де обробники даних та класи даних належать до окремої бібліотеки Class_Library, а файли даних та форми користувацького інтерфейсу лежать в основній теці App.

Обробники даних 
ticketsDataManager.cs
```csharp
List<ticket> loadTickets(); // loads the list of all tickets
ticket GetTicket(string flightName); // returns a ticket by its flight name
List<ticket> GetOwnTickets(string userName); // return a ticket given a user name
void AddTicket(string userName, string flightName, int price, string date, int seatRow, bool isMiddle, bool isWindow, bool isPrivate, bool isBaggage, bool isMeal); // adds a new ticket given all the data
```

userDataManager.cs
```csharp
List<user> loadUsers(); // loads the list of all users
void addUser(string name, string password, bool isAdmin); // adds a new user given all the data
user getUser(string name); // returns a user by its name
bool isAdmin(string name); // returns true if the user is an admin
bool validateCredentials(string name, string password); // returns true if the credentials are valid
```

flightsDataManager.cs
```csharp
List<flight> loadFlights(); // loads the list of all flights
flight getFlight(string name); // returns a flight by its name
```

Класи даних 
currentUser.cs
```csharp
string name; // user name
string password; // user password
bool isAdmin; // true if the user is an admin
```

user.cs
```csharp
string name; // user name
string password; // user password
bool isAdmin; // true if the user is an admin
```

flight.cs
```csharp
string name; // flight name
int price; // ticket default price
string date; // flight date
int seats; // number of seats
```

ticket.cs
```csharp
string userName; // user name
string flightName; // flight name
int price; // ticket total price
string date; // flight date
int seatRow; // seat row
bool isMiddle; // true if the seat is in the middle row
bool isWindow; // true if the seat is near the window
bool isPrivate; // true if the seat is private
bool isBaggage; // true if extra baggage is needed
bool isMeal; // true if extra meal is needed
```

Файли даних 
flights.txt 
```csv
flight_name,price,date,seats
```

tickets.txt
```csv
user_name,flight_name,price,date,seat_row,is_middle,is_window,is_private,is_baggage,is_meal
```

users.txt
```csv
name,password,is_admin
```

Форми користувацького інтерфейсу
flights.cs
```csharp
const int collapsedHeight = 190; // the height of the collapsed window
const int expandedHeight = 560; // the height of the expanded window
flight selectedFlight; // the currently selected flight
int totalPrice; // the total price of the selected ticket
int seatTypePrice = 0; // the price of the selected seat type
int mealPrice = 0; // the price of the selected meal
int luggagePrice = 0; // the price of the selected baggage
int privatePrice = 0; // the price of the selected private seat

public flights(); // constructor, collapses the window height and loads the list of all flights
void updateTotal(); // updates the total price label
renderFlightNames(List<flight> flights); // renders the list of flight names
menuButton_Click(object sender, EventArgs e); // closes the window and opens the menu
flightsList_SelectedValueChanged(object sender, EventArgs e); // handles the selection of a flight, fetched the flight info from the database, updates all the labels and the total price
middleRadio_CheckedChanged(object sender, EventArgs e); // unchecks other radio buttons and updates the total price
randomRadio_CheckedChanged(object sender, EventArgs e); // unchecks other radio buttons and updates the total price
windowRadio_CheckedChanged(object sender, EventArgs e); // unchecks other radio buttons and updates the total price
mealBox_CheckedChanged(object sender, EventArgs e); // updates the total price based on the status
luggageBox_CheckedChanged(object sender, EventArgs e); // updates the total price based on the status
privateBox_CheckedChanged(object sender, EventArgs e); // updates the total price based on the status
bookButton_Click(object sender, EventArgs e); // forms a new ticket, adds it to the database, shows the success message and closes the window 
```

login.cs
```csharp
public login(); // constructor
void loginButton_Click(object sender, EventArgs e); // validates the credentials, opens the menu if valid or shows an error if not
void registerButton_Click(object sender, EventArgs e); // opens the signup window and closes the login window
```

menu.cs
```csharp
public menu(); // constructor
void signoutButton_Click(object sender, EventArgs e); // signs out the user and closes the menu
void flightsButton_Click(object sender, EventArgs e); // opens the flights window and closes the menu
void ticketsButton_Click(object sender, EventArgs e); // opens the tickets window and closes the menu
```

signup.cs
```csharp
public signup(); // constructor
void loginButton_Click(object sender, EventArgs e); // opens the login window and closes the signup window
void signupButton_Click(object sender, EventArgs e); // creates a new user and closes the signup window
```

tickets.cs
```csharp
public tickets(); // constructor, loads the list of tickets
void loadTickets(); // loads the list of tickets and renders it
void backButton_Click(object sender, EventArgs e); // closes the window and opens the menu
```

- опис роботи з програмним забезпеченням з наведенням усіх необхідних скріншотів

Робота з програмою завжди починається з вікна входу (Рис. 3.1):

Вікно входу до програми (Рис. 3.1)

У вікні входу користувач може зайти у свій обліковий запис. Якшо користувач облікового запису не має, він може перейти до вікна реєстрації (Рис. 3.2)

Вікно реєстрації нового користувача (Рис. 3.2)

У вікні реєстрації користувач може створити обліковий запис, зазначивши всі поля (Рис. 3.2)

Після входу або реєстрації, користувач потрапляє до головного меню (Рис. 3.3)

Головне меню програми (Рис. 3.3)

У головному меню користувач може вийти з облікового запису, що перенесе його назад до вікна входу (Рис. 3.4)

Кнопка виходу з облікового запису (Рис. 3.4)

У головному меню користувач може переглянути список польотів (Рис. 3.5)

Список доступних польотів (Рис. 3.5)

У списку польотів користувач може обрати підходящий польот, змінити параметри та замовити квиток (Рис. 3.6)

Кнопка замовлення квитка (Рис. 3.6)

Після замовлення квитка користувача переносить до головного меню, де він може переглянути свої квитки (Рис. 3.7)

Список квитків користувача (Рис. 3.7)

Якщо користувач є адміністратором, йому будуть доступні квитки всіх користувачів (Рис. 3.8)

Список квитків для адміністратора (Рис. 3.8)

- опис повідомлень та оброблення критичних ситуацій

Програма містить наступні повідомлення (Рис. 4.1-4):
### управління ризиками
У підрозділі з аналізу ризиків повинно бути для кожного ризику визначено ймовірність його настання, рівень впливу на розклад проєкту, рівень впливу на витрати проєкту та рівень впливу на досягнення результатів проєкту, а також співставлена зона критичності. Усі ці значення мають бути приведені для стану до застосування управління даним ризиком («до управління», тобто фактично під час аналізу) та після завершення реалізації ризику або заходу з управління («після управління»).
Для оцінювання ймовірності та рівня впливу може використовуватися або числове значення (кількісні ризики), або категорія (якісні ризики). Категорії можуть належати наступному набору: дуже низький, низький, помірний, сильний, дуже сильний.
У випадку використання категорій наступні ситуації можна вважати такими, що відносяться до зони некритичних:
- вплив загалом є дуже низьким;
- вплив є низьким, а ймовірність не вище помірної;
- ймовірність є дуже низькою, а вплив не є дуже сильним.
Наступні ситуації, не включаючи описані некритичні, потребують додаткової уваги і належать до зони важливих:
- за сильної (високої) або дуже сильної ймовірності вплив є низьким або помірним;
- за помірної або низької ймовірності вплив є помірним або високим;
- за дуже низької ймовірності вплив є дуже сильним.
Наступні ситуації, не включаючи описані вище, належать до зони критичних:
- ймовірність настання і одночасно вплив є дуже сильними (високими) або сильними (високими);
- вплив є дуже сильним (високим), а ймовірність настання помірною або низькою.
Для кількісних ризиків може використовуватися наступна система перетворення значення ймовірності у відповідні категорії:
- не більше 10% для дуже низької;
- більше 70% для дуже сильної (високої);
- більше 50% для сильної;
- більше 30% для помірної;
- більше 10% для низької.
Переведення конкретних значень впливу кількісного ризику в категорії для подальшого визначення зони критичності залежить від відповідних запланованих показників проєкту (витрат, тривалост і, результатів).

Виявлення ризиків

Виявимо ризики у проєкті:
- Корупція бази даних:
 - Опис: База даних, що зберігає інформацію про рейси та квитки, може бути пошкоджена через апаратні збої, програмні помилки або інші проблеми.
 - Сфери впливу: Цілісність даних, доступність системи.
- Зміни обсягу робіт:
 - Опис: Зміни у вимогах або обсязі проєкту можуть призвести до додаткової роботи, затримок або невідповідності початковим цілям.
 - Сфери впливу: План-графік проєкту, зусилля з розробки.
- Економічна нестабільність:
 - Опис: Економічні коливання (наприклад, інфляція, девальвація валюти) можуть вплинути на витрати та фінансування проєкту.
 - Сфери впливу: Бюджет проєкту, фінансова стабільність.

Ймовірність ризиків

Оцінимо ймовірність кожного ризику:
- Корупція бази даних:
  - Якісний: Помірний (завдяки регулярному резервному копіюванню та надійному управлінню базою даних).
- Зміни обсягу робіт:
  - Якісний: Високий (зміни обсягу робіт є поширеним явищем у програмних проєктах).
- Економічна нестабільність:
  - Якісний: Дуже високий (зовнішні фактори поза контролем людей).

Вплив ризиків

Оцінимо вплив на аспекти проєкту:
- Корупція бази даних:
  - Якісний: Помірний (зусилля з відновлення даних, простої системи).
- Зміни обсягу робіт:
  - Якісний: Високий (доопрацювання, затримки).
- Економічна нестабільність:
  - Якісний: Високий (коригування бюджету, розподіл ресурсів).

Оцінка до управління

Поєднаємо ймовірності та вплив:
- Корупція бази даних: Важливий (помірна ймовірність, помірний вплив).
- Зміни обсягу робіт: Критичний (висока ймовірність, високий вплив).
- Економічна нестабільність: Критичний (дуже висока ймовірність, високий вплив).

Оцінка після управління

Оцінимо ризики після управлінню:
- Корупція бази даних: Мінімізований (стратегії резервного копіювання, моніторинг).
- Зміни обсягу робіт: Заходи в разі непередбачуваних ситуацій (процес управління змінами).
- Економічна нестабільність: Моніторинг та адаптація (фінансові резерви).
## висновки
Висновки вміщують безпосередньо після викладення суті записки, починаючи з нової сторінки: у висновках наводять найбільш важливі результати, одержані в розрахунково-графічному завданні, виконують оцінку одержаних результатів роботи з урахуванням світових тенденцій вирішення поставленої задачі; можливі галузі використання результатів роботи; наукову, соціальну значущість роботи, у висновках необхідно наголосити на якісних та кількісних показниках отриманих результатів, обґрунтувати достовірність результатів, викласти рекомендації щодо їх використання

На закінчення, розробка передової автоматизованої системи продажу квитків являє собою значний стрибок вперед в індустрії авіаперевезень. Система, розроблена в цій роботі, використовуючи описану структуру проекту, пропонує надійне рішення, яке вирішує поточні проблеми у сфері бронювання та ціноутворення, забезпечуючи при цьому предиктивну аналітику для управління запасами.

Інтеграція зручного інтерфейсу з можливостями прогнозування на основі штучного інтелекту гарантує, що авіакомпанії зможуть пропонувати персоналізований досвід для мандрівників, оптимізуючи продажі та задоволеність клієнтів. Наукова та соціальна значущість цієї роботи полягає в тому, що вона може революціонізувати спосіб взаємодії авіакомпаній та мандрівників, зробивши авіаперевезення більш доступними та ефективними.

Якісні та кількісні показники успіху цієї системи включають покращення простоти транзакцій, підвищення точності управління запасами та покращення користувацького досвіду. Надійність цих результатів ґрунтується на комплексному підході, застосованому при розробці системи, що відображено в структурі проекту.

Рекомендації щодо впровадження включають поетапне розгортання системи на різних платформах з постійним моніторингом та механізмами зворотного зв'язку для забезпечення адаптивності до мінливих потреб ринку. Ця робота не тільки сприяє розширенню знань у галузі технологій повітряних перевезень, але й створює прецедент для майбутніх інновацій, спрямованих на покращення глобального досвіду подорожей.