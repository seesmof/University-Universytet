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
                user.id = int.Parse(reader[0].ToString());
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
                user.id = int.Parse(reader[0].ToString());
                user.name = reader[1].ToString();
                user.manager = int.Parse(reader[2].ToString());
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

            // insert new user 
            var handler = new UserHandler(connection);
            var user = handler.create("Mark");
            Console.WriteLine($"user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");

            // update user status 
            user.manager = 1;
            handler.update(user);
            user = handler.read(user.id);
            Console.WriteLine($"user {user.id} name {user.name} manager {Convert.ToBoolean(user.manager)}");

            // delete user
            handler.delete(user.id);
            var findUser = handler.read(user.id);
            if (findUser == null)
            {
                Console.WriteLine("No user found");
            } else {
                Console.WriteLine($"user {findUser.id} name {findUser.name} manager {Convert.ToBoolean(findUser.manager)}");
            }
            Console.ReadKey();

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
