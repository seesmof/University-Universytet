using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace three_source
{
    public class User
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Admin { get; set; } = 0;
    }
    public class Estate
    {
        public int ID { get; set; }
        public string Title { get; set; }
        public string Kind { get; set; }
        public User Owner { get; set; }
    }
    public class Meeting
    {
        public int ID { get; set; }
        public string Score { get; set; }
        public string Status { get; set; } = "Wait";
        public Estate Target { get; set; }
        public User Sender { get; set; }
    }
    public class UserHandler
    {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        public UserHandler(MySqlConnection connection) { this.connection = connection; }
        public User create(string name, int admin = 0)
        {
            query = $"INSERT INTO user (name,admin) VALUES ('{name}',{admin});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var user = new User();
            while (reader.Read())
            {
                user.ID = reader.GetInt32(0);
                user.Name = name;
                user.Admin = admin;
            }
            reader.Close();
            return user;
        }
        public User read(int id)
        {
            query = $"SELECT id,name,admin FROM user WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                reader.Close();
                return user;
            }
            reader.Close();
            return null;
        }
        public List<User> readAll()
        {
            query = "SELECT id,name,admin FROM user;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var users = new List<User>();
            while (reader.Read())
            {
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                users.Add(user);
            }
            reader.Close();
            return users;
        }
        public void update(User user)
        {
            query = $"UPDATE user SET name='{user.Name}',admin={user.Admin} WHERE id={user.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public void delete(int id)
        {
            query = $"DELETE FROM user WHERE id={id};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
    }
    public class EstateHandler
    {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        List<string> kinds = new List<string>{
            "Home",
            "Flat",
            "New",
        };
        public EstateHandler(MySqlConnection connection) { this.connection = connection; }
        public Estate create(string name, string kind, User owner)
        {
            var correctKind = kinds.Contains(kind);
            if (!correctKind)
            {
                return null;
            }

            query = $"INSERT INTO estate (title,kind,owner_id) VALUES ('{name}','{kind}',{owner.ID});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var estate = new Estate();
            while (reader.Read())
            {
                estate.ID = reader.GetInt32(0);
                estate.Title = name;
                estate.Kind = kind;
                estate.Owner = owner;
            }
            reader.Close();
            return estate;
        }
        public Estate read(int id)
        {
            query = $"SELECT id,title,kind,owner_id FROM estate WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            int tempOwner = 0;
            var estate = new Estate();
            while (reader.Read())
            {
                estate.ID = reader.GetInt32(0);
                estate.Title = reader.GetString(1);
                estate.Kind = reader.GetString(2);
                tempOwner = reader.GetInt32(3);
            }
            reader.Close();
            estate.Owner = new UserHandler(connection).read(tempOwner);
            return estate;
        }
        public List<Estate> readAll()
        {
            query = "SELECT id,title,kind,owner_id FROM estate;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var estates = new List<Estate>();
            var owners = new List<int>();
            while (reader.Read())
            {
                var estate = new Estate();
                estate.ID = reader.GetInt32(0);
                estate.Title = reader.GetString(1);
                estate.Kind = reader.GetString(2);
                owners.Add(reader.GetInt32(3));
                estates.Add(estate);
            }
            reader.Close();
            for (int i = 0; i < estates.Count; i++)
            {
                estates[i].Owner = new UserHandler(connection).read(owners[i]);
            }
            return estates;
        }
        public void update(Estate estate)
        {
            query = $"UPDATE estate SET title='{estate.Title}',kind='{estate.Kind}',owner_id={estate.Owner.ID} WHERE id={estate.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public void delete(int id)
        {
            query = $"DELETE FROM estate WHERE id={id};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
    }
    public class MeetingHandler
    {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        List<string> statuses = new List<string>{
            "Wait",
            "Done",
            "Skip",
        };
        List<string> scores = new List<string>{
            "Bad",
            "Okay",
            "Fine",
        };
        public MeetingHandler(MySqlConnection connection) { this.connection = connection; }
        public Meeting create(Estate viewable, User viewer, string score = "Okay", string status = "Wait")
        {
            var correctStatus = statuses.Contains(status);
            var correctScore = scores.Contains(score);
            if (!correctScore || !correctStatus)
            {
                return null;
            }

            query = $"INSERT INTO meeting (score,status,target_id,sender_id) VALUES ('{score}','{status}',{viewable.ID},{viewer.ID});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var meeting = new Meeting();
            while (reader.Read())
            {
                meeting.ID = reader.GetInt32(0);
                meeting.Score = score;
                meeting.Status = status;
                meeting.Target = viewable;
                meeting.Sender = viewer;
            }
            reader.Close();
            return meeting;
        }
        public Meeting read(int id)
        {
            query = $"SELECT id,score,status,target_id,sender_id FROM meeting WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var meeting = new Meeting();
            var tempViewable = 0;
            var tempViewer = 0;
            while (reader.Read())
            {
                meeting.ID = reader.GetInt32(0);
                meeting.Score = reader.GetString(1);
                meeting.Status = reader.GetString(2);
                tempViewable = reader.GetInt32(3);
                tempViewer = reader.GetInt32(4);
            }
            reader.Close();
            meeting.Target = new EstateHandler(connection).read(tempViewable);
            meeting.Sender = new UserHandler(connection).read(tempViewer);
            return meeting;
        }
        public List<Meeting> readAll()
        {
            query = "SELECT id,score,status,target_id,sender_id FROM meeting;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var meetings = new List<Meeting>();
            var viewables = new List<int>();
            var viewers = new List<int>();
            while (reader.Read())
            {
                var meeting = new Meeting();
                meeting.ID = reader.GetInt32(0);
                meeting.Score = reader.GetString(1);
                meeting.Status = reader.GetString(2);
                viewables.Add(reader.GetInt32(3));
                viewers.Add(reader.GetInt32(4));
                meetings.Add(meeting);
            }
            reader.Close();
            for (int i = 0; i < meetings.Count; i++)
            {
                meetings[i].Target = new EstateHandler(connection).read(viewables[i]);
                meetings[i].Sender = new UserHandler(connection).read(viewers[i]);
            }
            return meetings;
        }
        public void update(Meeting meeting)
        {
            query = $"UPDATE meeting SET score='{meeting.Score}',status='{meeting.Status}',target_id={meeting.Target.ID},sender_id={meeting.Sender.ID} WHERE id={meeting.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public void delete(int id)
        {
            query = $"DELETE FROM meeting WHERE id={id};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
    }
    public class Test
    {
        MySqlConnection connection;
        public Test(MySqlConnection connection) { this.connection = connection; }
        public void testUser(string userName = "Luke")
        {
            // Create
            var handler = new UserHandler(connection);
            var user = handler.create(userName);
            Console.WriteLine($"Created user {user.ID} name {user.Name} manager {Convert.ToBoolean(user.Admin)}");

            // Read
            user = handler.read(user.ID);
            Console.WriteLine($"Read user {user.ID} name {user.Name} manager {Convert.ToBoolean(user.Admin)}");

            // Update 
            user.Admin = 1;
            handler.update(user);

            user = handler.read(user.ID);
            Console.WriteLine($"Updated user {user.ID} name {user.Name} manager {Convert.ToBoolean(user.Admin)}");

            // Delete
            handler.delete(user.ID);
            Console.WriteLine($"Deleted user {user.ID}");

            // Show all
            var users = handler.readAll();
            Console.WriteLine($"All users ({users.Count}):");
            foreach (var u in users)
            {
                Console.WriteLine($"- User {u.ID} name {u.Name} manager {Convert.ToBoolean(u.Admin)}");
            }
        }
        public void testEstate(string estateName = "Quiet House in the Countryside", string kind = "Home", User owner = null)
        {
            // Create
            var handler = new EstateHandler(connection);
            var estate = handler.create(estateName, kind, owner);
            Console.WriteLine($"Created estate {estate.ID} name {estate.Title} kind {estate.Kind} owner {estate.Owner.Name}");

            // Read
            estate = handler.read(estate.ID);
            Console.WriteLine($"Read estate {estate.ID} name {estate.Title} kind {estate.Kind} owner {estate.Owner.Name}");

            // Update 
            estate.Title = "Modern Appartament near Court";
            estate.Kind = "New";
            handler.update(estate);

            estate = handler.read(estate.ID);
            Console.WriteLine($"Updated estate {estate.ID} name {estate.Title} kind {estate.Kind} owner {estate.Owner.Name}");

            // Delete
            handler.delete(estate.ID);
            Console.WriteLine($"Deleted estate {estate.ID}");

            // Show all
            var estates = handler.readAll();
            Console.WriteLine($"All estates ({estates.Count}):");
            foreach (var l in estates)
            {
                Console.WriteLine($"- Estate {l.ID} name {l.Title} kind {l.Kind} owner {l.Owner.Name}");
            }
        }
        public void testMeeting(Estate viewable = null, User viewer = null)
        {
            // Create
            var handler = new MeetingHandler(connection);
            var meeting = handler.create(viewable, viewer);
            Console.WriteLine($"Created meeting {meeting.ID} score {meeting.Score} status {meeting.Status} viewable {meeting.Target.Title} viewer {meeting.Sender.Name}");

            // Read
            meeting = handler.read(meeting.ID);
            Console.WriteLine($"Read meeting {meeting.ID} score {meeting.Score} status {meeting.Status} viewable {meeting.Target.Title} viewer {meeting.Sender.Name}");

            // Update 
            meeting.Score = "Fine";
            meeting.Status = "Done";
            handler.update(meeting);

            meeting = handler.read(meeting.ID);
            Console.WriteLine($"Updated meeting {meeting.ID} score {meeting.Score} status {meeting.Status} viewable {meeting.Target.Title} viewer {meeting.Sender.Name}");

            // Delete
            handler.delete(meeting.ID);
            Console.WriteLine($"Deleted meeting {meeting.ID}");

            // Show all
            var meetings = handler.readAll();
            Console.WriteLine($"All meetings ({meetings.Count}):");
            foreach (var m in meetings)
            {
                Console.WriteLine($"- Meeting {m.ID} score {m.Score} status {m.Status} viewable {m.Target.Title} viewer {m.Sender.Name}");
            }
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(conStr);
            connection.Open();

            var handler = new UserHandler(connection);
            handler
            
            connection.Close();
        }
    }
}
