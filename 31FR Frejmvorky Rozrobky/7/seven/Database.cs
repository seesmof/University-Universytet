using MySql.Data.MySqlClient;
using System.Collections.Generic;
using System.Linq;

namespace seven {
    public class Database {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        public const string LastCreatedID="SELECT LAST_INSERT_ID();";

        // SYSTEM
        public Database(MySqlConnection connection){ this.connection = connection; }
        public MySqlDataReader read(string query){
            command=new MySqlCommand(query,connection);
            return command.ExecuteReader();
        }
        public void write(string query){
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }

        // CREATE
        public User createUser(string name, int admin = 0, int balance=0){
            write($"INSERT INTO user (name,admin,balance) VALUES ('{name}',{admin},{balance});");
            reader=read(LastCreatedID);
            var user = new User();
            while (reader.Read()){
                user.ID = reader.GetInt32(0);
                user.Name = name;
                user.Admin = admin;
                user.Balance=balance;
            }
            reader.Close();
            return user;
        }
        public Estate createEstate(string title, string kind, User owner, int price){
            write($"INSERT INTO estate (title,kind,owner_id,price) VALUES ('{title}','{kind}',{owner.ID},{price});");
            reader=read(LastCreatedID);
            var estate = new Estate();
            while (reader.Read()){
                estate.ID = reader.GetInt32(0);
                estate.Title = title;
                estate.Kind = kind;
                estate.Owner = owner;
                estate.Price=price;
            }
            reader.Close();
            return estate;
        }
        public Meeting createMeeting(User sender,Estate target){
            write($"INSERT INTO meeting (sender_id,target_id) VALUES ({sender.ID},{target.ID});");
            reader=read(LastCreatedID);
            var meeting = new Meeting();
            while (reader.Read()){
                meeting.ID = reader.GetInt32(0);
                meeting.Sender=sender;
                meeting.Target=target;
            }
            reader.Close();
            return meeting;
        }

        // READ
        public List<User> getUsers(){
            reader=read("SELECT id,name,admin,balance FROM user;");
            var users=new List<User>();
            while (reader.Read()){
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                user.Balance=reader.GetInt32(3);
                users.Add(user);
            }
            reader.Close();
            return users;
        }
        public User getUser(int id){
            return getUsers().Where(u=>u.ID==id).ToList().ElementAtOrDefault(0);
        }
        public List<Estate> getEstates(){
            reader=read("SELECT id,owner_id,title,kind,price FROM estate;");
            var estates=new List<Estate>();
            var owners=new List<int>();
            while (reader.Read()){
                var estate=new Estate();
                estate.ID=reader.GetInt32(0);
                owners.Add(reader.GetInt32(1));
                estate.Title=reader.GetString(2);
                estate.Kind=reader.GetString(3);
                estate.Price=reader.GetInt32(4);
                estates.Add(estate);
            }
            reader.Close();
            for (int i=0;i<estates.Count;i++){
                estates[i].Owner=getUser(owners[i]);
            }
            return estates;
        }
        public Estate getEstate(int id){
            return getEstates().Where(e=>e.ID==id).ToList().ElementAtOrDefault(0);
        }
        public List<Meeting> getMeetings(){
            reader=read("SELECT id,sender_id,target_id,score,status FROM meeting;");
            var meetings=new List<Meeting>();
            var senders = new List<int>();
            var targets = new List<int>();
            while (reader.Read()){
                var meeting = new Meeting();
                meeting.ID = reader.GetInt32(0);
                senders.Add(reader.GetInt32(1));
                targets.Add(reader.GetInt32(2));
                meeting.Score = reader.GetString(3);
                meeting.Status = reader.GetString(4);
                meetings.Add(meeting);
            }
            reader.Close();
            for (int i = 0; i < meetings.Count; i++){
                meetings[i].Sender = getUser(senders[i]);
                meetings[i].Target = getEstate(targets[i]);
            }
            return meetings;
        }
        public Meeting getMeeting(int id){
            return getMeetings().Where(m=>m.ID==id).ToList().ElementAtOrDefault(0);
        }

        // UPDATE
        public void updateUser(User user){
            write($"UPDATE user SET name='{user.Name}',admin={user.Admin},balance={user.Balance} WHERE id={user.ID};");
        }
        public void updateEstate(Estate estate){
            write($"UPDATE estate SET owner_id={estate.Owner.ID},title='{estate.Title}',kind='{estate.Kind}',price={estate.Price} WHERE id={estate.ID};");
        }
        public void updateMeeting(Meeting meeting){
            write($"UPDATE meeting SET sender_id={meeting.Sender.ID},target_id={meeting.Target.ID},score='{meeting.Score}',status='{meeting.Status}' WHERE id={meeting.ID};");
        }

        // DELETE
        public void deleteUser(int id){
            write($"DELETE FROM user WHERE id={id};");
        }
        public void deleteEstate(int id){
            write($"DELETE FROM estate WHERE id={id};");
        }
        public void deleteMeeting(int id){
            write($"DELETE FROM meeting WHERE id={id};");
        }
    }
}
