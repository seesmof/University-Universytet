class Listing:
  int id:
  User owner:
  string name:
  int price:
  enum['Private' | 'Flat' | 'New'] kind:

  void addListing(string kind, string name, int price):
  Listing viewListing(Listing listing):
  void editListing(Listing listing):
  void deleteListing(Listing listing):
  void makeChosen(Listing listing, User user):
  void setKind(string kind):

class User:
  int id:
  string name:
  bool manager:
  list[Listing] listings:
  list[Listing] chosen:
  list[Meeting] meetings:

  void addUser(string name, bool manager):
  User viewUser(User user):
  void editUser(User user):
  void deleteUser(User user):
  void changeStatus(User user, bool manager):

class Meeting:
  int id:
  Listing listing:
  User viewer:
  int score:
  enum['Private' | 'Flat' | 'New'] status:

  void addMeeting(Listing listing, User viewer):
  Meeting viewMeeting(Meeting meeting):
  void editMeeting(Meeting meeting):
  void deleteMeeting(Meeting meeting):
  void setScore(int score):
  void setStatus(string status):

Listing
  type: private OR flat OR new 
  owner: User

  viewDetails()
  editDetails()
  deleteListing()
  addListing()
User 
  manager: bool
  meetings: list[Meeting]
  listings: list[Listing]
  chosen: list[Listing]

  viewDetails()
  editDetails()
  viewListings()
  viewChosenListings()
  viewMeetings()
Meeting 
  status: pending OR visited OR canceled
  score: int 1 to 10
  listing: Listing

  scheduleMeeting()
  viewDetails()
  editDetails()
  rateMeeting()