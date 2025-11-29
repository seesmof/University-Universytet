class Listing: об'єкт нерухомості
  int id: унікальний ідентифікатор
  User owner: користувач власник
  string name: назва
  int price: вартість
  enum['Private' | 'Flat' | 'New'] kind: тип

  void addListing(string kind, string name, int price): додати до бази даних
  Listing viewListing(Listing listing): переглянути
  void editListing(Listing listing): змінити
  void deleteListing(Listing listing): видалити
  void makeChosen(Listing listing, User user): додати до обраних

class User: користувач застосунком
  int id: унікальний ідентифікатор
  string name: ім'я
  bool manager: статус
  list[Listing] listings: виставлені об'єкти нерухомості
  list[Listing] chosen: обрані об'єкти нерухомості
  list[Meeting] meetings: зустрічі

  void addUser(string name, bool manager): додати до бази даних
  User viewUser(User user): переглянути
  void editUser(User user): змінити
  void deleteUser(User user): видалити

class Meeting: об'єкт зустрічі
  int id: унікальний ідентифікатор
  Listing listing: об'єкт нерухомості для перегляду
  User viewer: користувач переглядач
  int score: оцінка
  enum['Pending' | 'Viewed' | 'Canceled'] status: статус

  void addMeeting(Listing listing, User viewer): додати до бази даних
  Meeting viewMeeting(Meeting meeting): переглянути
  void editMeeting(Meeting meeting): змінити
  void deleteMeeting(Meeting meeting): видалити