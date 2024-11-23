using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace three_source
{
    internal class Program
    {
        static void Main(string[] args)
        {
            const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            using MySqlConnection conn = new MySqlConnection(conStr);
            Console.WriteLine("Connected and disconnected praise JESUS CHRIST my LODR GOD MOST HIGH!");
            Console.ReadKey();
        }
    }
}
