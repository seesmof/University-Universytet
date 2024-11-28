using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace four_source
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
        public User Owner { get; set; }
        public string Title { get; set; }
        public string Kind { get; set; }
    }
    public class Meeting
    {
        public int ID { get; set; }
        public string Score { get; set; }
        public string Status { get; set; } = "Wait";
        public User Sender { get; set; }
        public Estate Target { get; set; }
    }
    public static class EstateKind
    {
        public const string Home = "Home";
        public const string Flat = "Flat";
        public const string New = "New";
    }
    public static class MeetingStatus
    {
        public const string Wait = "Wait";
        public const string Done = "Done";
        public const string Skip = "Skip";
    }
    public static class MeetingScore
    {
        public const string Bad = "Bad";
        public const string Okay = "Okay";
        public const string Fine = "Fine";
    }
    public static class Query
    {
        public const string LastCreatedID = "SELECT LAST_INSERT_ID();";
    }
    public class Session
    {
        public bool Entered { get; set; } = false;
        public User Client { get; set; }
        public List<Estate> Owned { get; set; }
        public List<Meeting> Plan { get; set; }
    }
    public class Database
    {
        MySqlConnection connection;
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        public Database(MySqlConnection connection) { this.connection = connection; }
        public User getUserByName(string userName)
        {
            query = $"SELECT id,name,admin FROM user WHERE name='{userName}';";
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
        public User createUser(string userName,int admin = 0)
        {
            query = $"INSERT INTO user (name,admin) VALUES ('{userName}',{admin});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();

            query = Query.LastCreatedID;
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var user = new User();
            while (reader.Read())
            {
                user.ID = reader.GetInt32(0);
                user.Name = userName;
                user.Admin = admin;
            }
            reader.Close();
            return user;
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            const string connectionString = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(connectionString);
            var database = new Database(connection);
            connection.Open();
            var session = new Session();
            while (true)
            {
                if (!session.Entered)
                {
                    Console.WriteLine("User name:");
                    var userName = Console.ReadLine();
                    User foundUser = database.getUserByName(userName);
                    if (foundUser!=null)
                    {
                        session.Client = foundUser;
                    }
                    else
                    {
                        session.Client = database.createUser(userName);
                    }
                    session.Entered=true;
                }
                else
                {

                }
            }
            connection.Close();
        }
    }
}
