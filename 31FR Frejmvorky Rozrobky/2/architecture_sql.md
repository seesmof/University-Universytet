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
  AUTONUM id: унікальний ідентифікатор
  VARCHAR status: статус зустрічі Private або Flat або New

TABLE Meeting: об'єкт зустрічі
  AUTONUM id: унікальний ідентифікатор
  FOREIGN KEY listing: об'єкт нерухомості для перегляду
  FOREIGN KEY viewer: користувач переглядач
  INT score: оцінка
  FOREIGN KEY status: статус