user
  id INT PRIMARY_KEY AUTO_INCREMENT
  name VARCHAR(127) NOT_NULL
  manager TINYINT DEFAULT 0

listing
  id INT PRIMARY_KEY AUTO_INCREMENT
  title VARCHAR(127) NOT_NULL
  price INT Unsigned NOT_NULL
  kind VARCHAR(12) DEFAULT "House" <House | Flat | New>
  owner INT FOREIGN_KEY NOT_NULL <user.id>

meeting
  id INT PRIMARY_KEY AUTO_INCREMENT
  score INT DEFAULT 0
  status VARCHAR(12) DEFAULT "Pending" <Pending | Viewed | Canceled>
  home INT FOREIGN_KEY NOT_NULL <listing.id>
  looker INT FOREIGN_KEY NOT_NULL <user.id>