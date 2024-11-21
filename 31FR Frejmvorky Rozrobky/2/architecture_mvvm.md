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
  string name:
  bool manager:
  list[Listing] listings:
  list[Listing] chosen:
  list[Meeting] meetings:

  void addUser(string name, bool manager): додати до бази даних
  User viewUser(User user): переглянути
  void editUser(User user): змінити
  void deleteUser(User user): видалити

class Meeting: об'єкт зустрічі
  int id: унікальний ідентифікатор
  Listing listing:
  User viewer:
  int score:
  enum['Private' | 'Flat' | 'New'] status:

  void addMeeting(Listing listing, User viewer): додати до бази даних
  Meeting viewMeeting(Meeting meeting): переглянути
  void editMeeting(Meeting meeting): змінити
  void deleteMeeting(Meeting meeting): видалити