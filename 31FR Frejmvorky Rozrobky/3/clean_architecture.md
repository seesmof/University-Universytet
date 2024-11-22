class Listing
  int id
  User owner
  string name
  int price
  enum['Private' | 'Flat' | 'New'] kind

  void addListing(string kind, string name, int price)
  Listing viewListing(Listing listing)
  void editListing(Listing listing)
  void deleteListing(Listing listing)
  void makeChosen(Listing listing, User user)

class User
  int id
  string name
  bool manager
  list[Listing] listingsнерухомості
  list[Listing] chosenнерухомості
  list[Meeting] meetings

  void addUser(string name, bool manager)
  User viewUser(User user)
  void editUser(User user)
  void deleteUser(User user)

class Meeting
  int id
  Listing listingперегляду
  User viewer
  int score
  enum['Private' | 'Flat' | 'New'] status

  void addMeeting(Listing listing, User viewer)
  Meeting viewMeeting(Meeting meeting)
  void editMeeting(Meeting meeting)
  void deleteMeeting(Meeting meeting)