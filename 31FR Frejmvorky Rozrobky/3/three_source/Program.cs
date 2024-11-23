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
        public int create(User user)
        {
            query = $"INSERT INTO user (name,manager) VALUES ('{user.name}','{user.manager}');";
            return user.id;
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(conStr);
            connection.Open();

            // insert new user 
            var user = new User();
            user.name = "John";
            var query = $"INSERT INTO user (name,manager) values ('{user.name}','{user.manager}');";
            var command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            Console.WriteLine($"Inserted user id {null} name {user.name} manager {user.manager}");
            Console.ReadKey();

            // get user id
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                var id = reader[0];
                user.id = int.Parse(id.ToString());
            }
            Console.WriteLine($"Read user {user.id} name {user.name} manager {user.manager}");
            Console.ReadKey();
            reader.Close();

            // get user data by id 
            query = $"SELECT id, name, manager FROM user WHERE id = {user.id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var readUser = new User();
            while (reader.Read())
            {
                readUser.id = int.Parse(reader[0].ToString());
                readUser.name = reader[1].ToString();
                readUser.manager = int.Parse(reader[2].ToString());
            }
            Console.WriteLine($"Read user {readUser.id} name {readUser.name} manager {readUser.manager}");
            Console.ReadKey();
            reader.Close();

            // update user status 
            user.manager = 1;
            query = $"UPDATE user SET name = '{user.name}', manager = '{user.manager}' WHERE id = {user.id}";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();

            // read updated user 
            query = $"SELECT id, name, manager FROM user WHERE id = {user.id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                readUser.id = int.Parse(reader[0].ToString());
                readUser.name = reader[1].ToString();
                readUser.manager = int.Parse(reader[2].ToString());
            }
            Console.WriteLine($"Read user {readUser.id} name {readUser.name} manager {readUser.manager}");
            Console.ReadKey();
            reader.Close();

            // delete user
            query = $"DELETE FROM user WHERE id = {user.id}";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            Console.WriteLine($"Deleted user {user.id} name {user.name} manager {user.manager}");
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
