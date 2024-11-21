class Listing:
  int id:
  string kind<'Private'|'Flat'|'New'>:
  int owner<User>:
  string name:
  int price:

  void addListing(string kind, string name, int price):
  Listing viewListing(Listing):
  void deleteListing(Listing):
  void editListing(Listing):
  void makeChosen(Listing, User):

class User:
  int id:
  string name:
  bool manager:
  list[Listing] listings:
  list[Listing] chosen:
  list[Meeting] meetings:

  void editUser(User):

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