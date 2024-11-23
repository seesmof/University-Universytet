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
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        public UserHandler(MySqlConnection connection) { this.connection = connection; }
        public User create(string name, int manager = 0)
        {
            query = $"INSERT INTO user (name,manager) VALUES ('{name}',{manager});";
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
        public List<User> readAll()
        {
            query = "SELECT id,name,manager FROM user;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var users = new List<User>();
            while (reader.Read())
            {
                var user = new User();
                user.id = reader.GetInt32(0);
                user.name = reader.GetString(1);
                user.manager = reader.GetInt32(2);
                users.Add(user);
            }
            reader.Close();
            return users;
        }
        public void update(User user)
        {
            query = $"UPDATE user SET name='{user.name}',manager={user.manager} WHERE id={user.id};";
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
    public class ListingHandler
    {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        List<string> kinds = new List<string>{
            "House",
            "Flat",
            "New",
        };
        public ListingHandler(MySqlConnection connection) { this.connection = connection; }
        public Listing create(string name, int price, string kind, User owner)
        {
            var correctKind = kinds.Contains(kind);
            if (!correctKind)
            {
                return null;
            }

            query = $"INSERT INTO listing (name,price,kind,owner) VALUES ('{name}','{price}','{kind}','{owner.id}');";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
            
            query = "SELECT LAST_INSERT_ID();";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var listing = new Listing();
            while (reader.Read())
            {
                listing.id = reader.GetInt32(0);
                listing.name = name;
                listing.price = price;
                listing.kind = kind;
                listing.owner = owner;
            }
            reader.Close();
            return listing;
        }
        public Listing read(int id)
        {
            query = $"SELECT id,name,price,kind,owner FROM listing WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                var listing = new Listing();
                listing.id = reader.GetInt32(0);
                listing.name = reader.GetString(1);
                listing.price = reader.GetInt32(2);
                listing.kind = reader.GetString(3);
                listing.owner = new UserHandler(connection).read(reader.GetInt32(4));
                reader.Close();
                return listing;
            }
            reader.Close();
            return null;
        }
        public List<Listing> readAll()
        {
            query = "SELECT id,name,price,kind,owner FROM listing;";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var listings = new List<Listing>();
            while (reader.Read())
            {
                var listing = new Listing();
                listing.id = reader.GetInt32(0);
                listing.name = reader.GetString(1);
                listing.price = reader.GetInt32(2);
                listing.kind = reader.GetString(3);
                listing.owner = new UserHandler(connection).read(reader.GetInt32(4));
                listings.Add(listing);
            }
            reader.Close();
            return listings;
        }
        public void update(Listing listing)
        {
            query = $"UPDATE listing SET name='{listing.name}',price={listing.price},kind='{listing.kind}',owner={listing.owner.id} WHERE id={listing.id};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public void delete(int id)
        {
            query = $"DELETE FROM listing WHERE id={id};";
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

            // Show all
            var users = handler.readAll();
            Console.WriteLine($"All users ({users.Count}):");
            foreach (var u in users)
            {
                Console.WriteLine($"User {u.id} name {u.name} manager {Convert.ToBoolean(u.manager)}");
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

            Test.testUser(connection);

            connection.Close();
        }
    }
}
