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
        var data=new DataTable();

        var query = "SELECT * FROM data.finance_client;";
        using (var c=new MySqlConnection(connectionString))
        using (var a=new MySqlDataAdapter(query, c))
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