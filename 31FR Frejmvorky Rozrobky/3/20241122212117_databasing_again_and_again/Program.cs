using System;
using System.Collections.Generic;
using System.Linq;
using System.Data;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.Serialization;
using MySql.Data.MySqlClient;

namespace _20241122212117_databasing_again_and_again
{
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public bool manager { get; set; }
    }

    public class Listing
    {
        public int id { get; set; }
        public string name { get; set; }
        public uint price { get; set; }
        public string kind { get; set; }
        public User owner { get; set; }
    }

    public class Meeting
    {
        public int id { get; set; }
        public int score { get; set; }
        public string status { get; set; }
        public Listing viewable { get; set; }
        public User viewer { get; set; }
    }

    public class Database
    {
        public MySqlConnection connection { get; set; }

        public Database(string connectionString)
        {
            connection = new MySqlConnection(connectionString);
        }
    }

    public class UserRepository
    {
        private readonly Database _db;

        public UserRepository(Database db) { _db = db; }

        public MySqlDataReader getUser(int id)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            MySqlCommand cmd = new MySqlCommand($"SELECT * FROM user WHERE id = @id", _db.connection);
            cmd.Parameters.AddWithValue("@id", id);
            return cmd.ExecuteReader();
        }

        public void createUser(User user)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "INSERT INTO user (name, manager) VALUES (@name, @manager);";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@name", user.name);
            cmd.Parameters.AddWithValue("@manager", user.manager);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }

        public void updateUser(User user)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "UPDATE user SET name = @name, manager = @manager WHERE id = @id;";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@name", user.name);
            cmd.Parameters.AddWithValue("@manager", user.manager);
            cmd.Parameters.AddWithValue("@id", user.id);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }

        public void deleteUser(User user)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "DELETE FROM user WHERE id = @id;";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@id", user.id);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }
    }

    public class ListingRepository
    {
        private readonly Database _db;

        public ListingRepository(Database db) { _db = db; }

        public MySqlDataReader getListing(int id)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            MySqlCommand cmd = new MySqlCommand($"SELECT * FROM listing WHERE id = @id", _db.connection);
            cmd.Parameters.AddWithValue("@id", id);
            return cmd.ExecuteReader();
        }

        public void createListing(Listing listing)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "INSERT INTO listing (name, price, kind, owner) VALUES (@name, @price, @kind, @owner);";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@name", listing.name);
            cmd.Parameters.AddWithValue("@price", listing.price);
            cmd.Parameters.AddWithValue("@kind", listing.kind);
            cmd.Parameters.AddWithValue("@owner", listing.owner.id);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }

        public void updateListing(Listing listing)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "UPDATE listing SET name = @name, price = @price, kind = @kind, owner = @owner WHERE id = @id;";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@name", listing.name);
            cmd.Parameters.AddWithValue("@price", listing.price);
            cmd.Parameters.AddWithValue("@kind", listing.kind);
            cmd.Parameters.AddWithValue("@owner", listing.owner.id);
            cmd.Parameters.AddWithValue("@id", listing.id);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }

        public void deleteListing(Listing listing)
        {
            if (_db.connection.State != ConnectionState.Open) { _db.connection.Open(); }
            string query = "DELETE FROM listing WHERE id = @id;";
            MySqlCommand cmd = new MySqlCommand(query, _db.connection);
            cmd.Parameters.AddWithValue("@id", listing.id);
            cmd.ExecuteNonQuery();
            cmd.Dispose();
            _db.connection.Close();
        }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            const string USER_NAME = "root";
            const string PASSWORD = "1313";
            const string HOST = "localhost";
            const string PORT = "3306";
            const string DATABASE_NAME = "fr_data";
            string connectionString = $"uid={USER_NAME};pwd={PASSWORD};host={HOST};port={PORT};database={DATABASE_NAME}";
            Console.WriteLine(connectionString);

            Database db = new Database(connectionString);
            UserRepository ur = new UserRepository(db);

            // add test admin user 
            User admin = new User
            {
                id = 1,
                name = "admin",
                manager = true
            };
            ur.createUser(admin);

            // get all users
            List<User> users = new List<User>();
            MySqlDataReader reader = ur.getUser(1);
            while (reader.Read())
            {
                User user = new User
                {
                    id = int.Parse(reader["id"].ToString()),
                    name = reader["name"].ToString(),
                    manager = reader["manager"].ToString() == "1"
                };
                users.Add(user);
            }
            reader.Close();

            // show the data for each user 
            foreach (User user in users)
            {
                Console.WriteLine($"id: {user.id}, name: {user.name}, manager: {user.manager}");
            }

            // create a new listing for admin 
            ListingRepository lr = new ListingRepository(db);
            Listing listing = new Listing
            {
                id = 1,
                name = "test listing",
                price = 120,
                kind = "Flat",
                owner = admin
            };
            lr.createListing(listing);

            // show listing data
            reader = lr.getListing(1);
            while (reader.Read())
            {
                Listing l = new Listing
                {
                    id = int.Parse(reader["id"].ToString()),
                    name = reader["name"].ToString(),
                    price = uint.Parse(reader["price"].ToString()),
                    kind = reader["kind"].ToString(),
                    owner = new User
                    {
                        id = int.Parse(reader["owner"].ToString()),
                        name = reader["name"].ToString(),
                        manager = reader["manager"].ToString() == "1"
                    }
                };
                Console.WriteLine($"id: {l.id}, name: {l.name}, price: {l.price}, kind: {l.kind}, owner: {l.owner.name}");
            }
            reader.Close();

            Console.ReadKey();
        }
    }
}
