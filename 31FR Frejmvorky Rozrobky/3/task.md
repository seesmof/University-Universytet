# MySQL Data

var USER = "root";
var PASSWORD = "1313";
var HOST = "localhost";
var PORT = "3306";
var NAME = "data";

# Planning

add all those mysql data as variables that users can change to meet the remote connection requirement

use the assert() method to meet the modular testing requirement

# Detailed Task

1. Виконати аналіз ТЗ та розробленої архітектури системи щодо вимог до організації даних.
2. Прийняти рішення про систему збереження даних та обґрунтувати її.
3. Розробити структуру бази даних, необхідної для збереження даних системи. Додатково (не є обов’язковою вимогою) для зберігання деяких даних можуть використовуватися XML-файли або вони можуть бути створені як паралельне сховище.
4. Реалізувати функціональність програмного забезпечення, пов’язану зі взаємодією з даними. Під час реалізації взаємодії має обов’язково враховуватися можливість роботи з даними з віддалених пристроїв, що мінімально має підтримуватися на рівні відповідної системи керування базами даних.
5. Виконати тестування розробленого програмного забезпечення. У процесі тестування має обов’язково застосовуватись модульне тестування.
6. Тестування має виконуватися шляхом взаємодії з різними файлами (в яких зберігаються дані) визначеної структури на пристроях з різними апаратними хараткеристиками під керуванням різних операційних систем або версій операційних систем.
7. Виконати аналіз отриманих результатів тестування. У процесі аналізу отриманих результатів має бути порівняно результати, отримані під керуванням різних операційних систем (або їх версій) та на різних пристроях.

## Database Structure 

Listing
  INT id PrimaryKey AutoIncrement
  VARCHAR(127) name
  INT price Unsigned
  VARCHAR(12) kind <Private|Flat|New>
  INT owner ForeignKey <User.id>

User
  INT id PrimaryKey AutoIncrement
  VARCHAR(127) name
  BOOLEAN manager

Meeting
  INT id PrimaryKey AutoIncrement
  INT score
  VARCHAR(12) status <Pending|Viewed|Canceled>
  INT viewable ForeignKey <Listing.id>
  INT viewer ForeignKey <User.id>

## Program Functions 

Listing
  addListing(string kind, string name, int price)
    if kind=='New' check if owner.manager
  viewListing(Listing listing)
  editListing(Listing listing)
  deleteListing(Listing listing)
  makeChosen(Listing listing, User user)

User
  addUser(string name, bool manager)
  viewUser(User user)
  editUser(User user)
  deleteUser(User user)

Meeting
  addMeeting(Listing listing, User viewer)
  viewMeeting(Meeting meeting)
  editMeeting(Meeting meeting)
  deleteMeeting(Meeting meeting)