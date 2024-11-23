using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _20241123075052_source
{
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public bool manager { get; set; } = false;
    }

    public class UserRepository
    {
        private readonly MySqlConnection _connection;

        public UserRepository(MySqlConnection connection)
        {
            _connection = connection;
        }
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
        public Listing viewable { get; set; }
        public User viewer { get; set; }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            var userName = "root";
            var password = "1313";
            var host = "localhost";
            var port = "3306";
            var databaseName = "fr_data";

            MySqlConnection conn = new MySqlConnection($"Server={host};Port={port};Database={databaseName};Uid={userName};Pwd={password};");
            conn.Open();
            conn.Close();

            Console.ReadKey();
        }
    }
}
