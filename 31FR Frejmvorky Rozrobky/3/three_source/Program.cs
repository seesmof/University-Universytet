using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace three_source
{
    public class Program
    {
        static void Main(string[] args)
        {
            const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(conStr);
            try
            {
                Console.WriteLine("Connecting to database...");
                connection.Open();

                var query = "select id,name,manager from user";
                var command = new MySqlCommand(query, connection);
                var reader = command.ExecuteReader();

                while (reader.Read())
                {
                    int id = int.Parse(reader[0].ToString());
                    string name = reader[1].ToString();
                    bool manager = Convert.ToBoolean(Convert.ToInt16(reader[2].ToString()));
                    Console.WriteLine($"User {id} name {name} manager {manager}");
                }
            } catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            connection.Close();
            Console.WriteLine("Disconnected");
        }
    }
}
