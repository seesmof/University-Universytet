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

User
  id INT PRIMARY_KEY AUTO_INCREMENT
  name VARCHAR(127) NOT_NULL
  manager BOOLEAN DEFAULT False

Listing
  id INT PRIMARY_KEY AUTO_INCREMENT
  name VARCHAR(127) NOT_NULL
  price INT Unsigned NOT_NULL
  kind VARCHAR(12) NOT_NULL <Private|Flat|New>
  owner INT FOREIGN_KEY NOT_NULL <User.id>

Meeting
  id INT PRIMARY_KEY AUTO_INCREMENT
  score INT
  status VARCHAR(12) DEFAULT "Pending" <Pending|Viewed|Canceled>
  viewable INT FOREIGN_KEY NOT_NULL <Listing.id>
  viewer INT FOREIGN_KEY NOT_NULL <User.id>

## Program Functions 

User
  createUser(string name, bool manager)
  readUser(id, name[optional])
    get by id
    if not id: get first one by name 
  updateUser(User user)
  deleteUser(User user)

Listing
  createListing(name, price, kind)
    if kind=='New' check if owner.manager
    check kind enum
  readListing(id, name[optional])
    get by id 
    if not id: get first one by name 
  updateListing(Listing listing)
  deleteListing(Listing listing)
  makeChosen(Listing listing, User user)

Meeting
  createMeeting(Listing listing, User viewer)
  readMeeting(id, name[optional])
    get by id
    if not id: get first one by name 
  updateMeeting(Meeting meeting)
  deleteMeeting(Meeting meeting)

