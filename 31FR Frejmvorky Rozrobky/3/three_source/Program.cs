using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace three_source
{
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public int manager { get; set; } = 0;
    }
    public class Listing
    {
        public int id { get; set; }
        public string name { get; set; }
        public int price { get; set; }
        public string kind { get; set; }
        public User owner { get; set; }
    }
    public class Meeting
    {
        public int id { get; set; }
        public int score { get; set; }
        public string status { get; set; } = "Pending";
        public Listing viweable { get; set; }
        public User viewer { get; set; }
    }
    public class UserHandler
    {
        MySqlConnection connection;
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        public UserHandler(MySqlConnection connection) { this.connection = connection; }
        public User create(string name, int manager = 0)
        {
            query = $"INSERT INTO user (name,manager) VALUES ('{name}','{manager}');";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var user = new User();
            while (reader.Read())
            {
                user.id = reader.GetInt32(0);
                user.name = name;
                user.manager = manager;
            }
            reader.Close();
            return user;
        }
        public User read(int id)
        {
            query = $"SELECT id,name,manager FROM user WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                var user = new User();
                user.id = reader.GetInt32(0);
                user.name = reader.GetString(1);
                user.manager = reader.GetInt32(2);
                reader.Close();
                return user;
            }
            reader.Close();
            return null;
        }
        public void update(User user)
        {
            query = $"UPDATE user SET name='{user.name}',manager='{user.manager}' WHERE id={user.id};";
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
    public static class Test
    {
        public static void testUser(MySqlConnection connection, string userName = "Luke")
        {
            // Create
            var handler = new UserHandler(connection);
            var user = handler.create(userName);
            Console.WriteLine($"Created user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");

            // Read
            user = handler.read(user.id);
            Console.WriteLine($"Read user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");

            // Update 
            user.manager = 1;
            handler.update(user);

            user = handler.read(user.id);
            Console.WriteLine($"Updated user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");

            // Delete
            handler.delete(user.id);

            user = handler.read(user.id);
            if (user != null)
            {
                Console.WriteLine($"Deleted user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");
            }
            else
            {
                Console.WriteLine($"Deleted user not found");
            }
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(conStr);
            string query;
            MySqlCommand command;
            MySqlDataReader reader;
            connection.Open();

            Test.testUser(connection);

            // read all users 
            query = $"SELECT id,name,manager FROM user;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var users = new List<User>();
            while (reader.Read())
            {
                var u = new User();
                u.id = int.Parse(reader[0].ToString());
                u.name = reader[1].ToString();
                u.manager = int.Parse(reader[2].ToString());
                users.Add(u);
            }
            reader.Close();
            foreach (var u in users)
            {
                Console.WriteLine($"User {u.id} name {u.name} manager {u.manager}");
            }

            connection.Close();
        }
    }
}
