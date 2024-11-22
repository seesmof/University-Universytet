using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _22112024153437_trying_database_again
{
    /*
    public class Listing
    {
        public Listing() { }
        public void createListing() { }
        public Listing readListing() { }
        public void updateListing() { }
        public void deleteListing() { }
    }

    public class Meeting
    {
        public Meeting() { }
        public void createMeeting() { }
        public Meeting readMeeting() { }
        public void updateMeeting() { }
        public void deleteMeeting() { }
    }

    public class User
    {
        public User() { }
        public void createUser() { }
        public User readUser() { }
        public void updateUser() { }
        public void deleteUser() { }
    }
    */

    public class Database
    {
        public MySqlConnection connection { get; set; }
        public string connectionString { get; set; }

        public Database(string connectionString)
        {
            this.connectionString = connectionString;
            this.connection = new MySqlConnection(this.connectionString);
        }

        public void create() { }
        public void read() { }
        public void update() { }
        public void delete() { }
    }

    public class Program
    {
        static void Main(string[] args)
        {
            const string USER_NAME = "root";
            const string PASSWORD = "1313";
            const string HOST = "localhost";
            const string PORT = "3306";
            const string DATABASE_NAME = "data";
            string connectionString = $"uid={USER_NAME};pwd={PASSWORD};host={HOST};port={PORT};database={DATABASE_NAME}";
            Console.WriteLine(connectionString);

            MySqlConnection conn = new MySqlConnection(connectionString);
            string query = "select id,name from finance_client";

            MySqlCommand cmd = new MySqlCommand(query, conn);
            MySqlDataAdapter adapter = new MySqlDataAdapter();
            adapter.SelectCommand = cmd;

            DataTable dt = new DataTable();
            adapter.Fill(dt);

            for (int i = 0; i < dt.Rows.Count; i++)
            {
                for (int j = 0; j < dt.Columns.Count; j++)
                {
                    Console.WriteLine(dt.Rows[i][j].ToString());
                }
            }

            Console.ReadKey();
        }
    }
}
