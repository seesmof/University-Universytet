using MySql.Data.MySqlClient;

namespace src
{
    public class Database
    {
        // IDEA: connect to database, provided all the data 
        public MySqlConnection connection { get; set; }
        public string user { get; set; }
        public string password { get; set; }
        public string host { get; set; }
        public string port { get; set; }
        public string databaseName { get; set; }
        public string connectionString { get; set; }

        // make a constructor that accepts database connection parameters
        public Database(string userName, string password, string host, string port, string databaseName)
        {
            this.user = userName;
            this.password = password;
            this.host = host;
            this.port = port;
            this.databaseName = databaseName;
            this.connectionString = formConnectionString();
            this.connection=new MySqlConnection(this.connectionString);
        }

        public string formConnectionString()
        {
            return $"uid={user};pwd={password};server={host};port={port};database={databaseName}";
        }
        // store database connection object
    }
}
