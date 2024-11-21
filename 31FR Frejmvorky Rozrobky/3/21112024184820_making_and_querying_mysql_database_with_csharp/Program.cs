using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace _21112024184820_making_and_querying_mysql_database_with_csharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var USER = "root";
            var PASSWORD = "1313";
            var HOST = "localhost";
            var PORT = "3306";
            var NAME = "data";
            var conn = new MySqlConnection($"server={HOST};port={PORT};UID={USER};password={PASSWORD};database={NAME};");
            conn.Open();
            Console.WriteLine("ALLEUJAH JESUS THANK YOU LORD GOD ALMIGHTY AMEN");
            conn.Close();
        }
    }
}
