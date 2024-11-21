TABLE ListingKind: тип нерухомості
  AUTONUM id: унікальний ідентифікатор
  VARCHAR kind: тип нерухомості Private або Flat або New

TABLE Listing: об'єкт нерухомості
  AUTONUM id: унікальний ідентифікатор
  FOREIGN KEY owner: користувач власник
  VARCHAR name: назва
  INT price: вартість
  FOREIGN KEY kind: тип

TABLE User: користувач застосунком
  AUTONUM id: унікальний ідентифікатор
  VARCHAR name: ім'я
  BOOL manager: статус
  FOREIGN KEY listings: виставлені об'єкти нерухомості
  FOREIGN KEY chosen: обрані об'єкти нерухомості
  FOREIGN KEY meetings: зустрічі

TABLE MeetingStatus: статус зустрічі

TABLE Meeting: об'єкт зустрічі
  AUTONUM id: унікальний ідентифікатор
  FOREIGN KEY listing: об'єкт нерухомості для перегляду
  FOREIGN KEY viewer: користувач переглядач
  INT score: оцінка
  enum['Private' | 'Flat' | 'New'] status: статус



TABLE Listing: об'єкт нерухомості
  AUTONUM: унікальний ідентифікатор
  FOREIGN KEY owner: користувач власник
  CHAR name: назва
  INT price: вартість
  CHAR kind: тип

TABLE User: користувач застосунком
  AUTONUM id: унікальний ідентифікатор
  VARCHAR name:
  BOOL manager:


  list[Listing] listings:
  list[Listing] chosen:
  list[Meeting] meetings:

class Meeting: об'єкт зустрічі
  AUTONUM id: унікальний ідентифікатор
  Listing listing:
  User viewer:
  INT score:
  CHAR status: