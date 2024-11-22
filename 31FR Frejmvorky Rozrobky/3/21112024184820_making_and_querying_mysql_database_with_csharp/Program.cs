using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

public class Program
{
  static void Main(string[] args)
  {
    var USER = "root";
    var PASSWORD = "1313";
    var HOST = "localhost";
    var PORT = "3306";
    var NAME = "data";
    var connectionString = $"server={HOST};port={PORT};UID={USER};password={PASSWORD};database={NAME};";
    var data = new DataTable();

    var query = "SELECT * FROM data.finance_client;";
    using (var connection = new MySqlConnection(connectionString))
    using (var command = new MySqlCommand(query, connection))
    {
      connection.Open();
      using (var reader = command.ExecuteReader())
      {
        data.Load(reader);
      }
    }

    using (var c = new MySqlConnection(connectionString))
    using (var a = new MySqlDataAdapter(query, c))
    {
      a.Fill(data);
    }

    foreach (DataRow row in data.Rows)
    {
      foreach (var item in row.ItemArray)
      {
        Console.WriteLine(item.ToString());
      }
    }
    Console.ReadKey();

    var TABLE_PREFIX = "fr_";
  }
}

var query = "SELECT * FROM finance_client;";
using (var c = new MySqlConnection(connectionString))
using (var a = new MySqlDataAdapter(query, c))
{
  a.Fill(data);
}

foreach (DataRow row in data.Rows)
{
  foreach (var item in row.ItemArray)
  {
    Console.WriteLine(item.ToString());
  }
  Console.WriteLine();
}
Console.ReadKey();
  }
}