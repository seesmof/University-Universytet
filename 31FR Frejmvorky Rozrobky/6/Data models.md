user 
  id int primaryKey autoIncrement 
  name string 
  admin bool 
estate 
  id int primaryKey autoIncrement
  owner_id int foreignKey <user.id>
  title string 
  kind string [Home | Flat | New]
meeting
  id int primaryKey autoIncrement
  sender_id int foreignKey <user.id>
  target_id int foreignKey <estate.id>
  status string [Wait | Done | Skip]
  score string [Bad | Okay | Fine]