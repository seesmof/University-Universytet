using MySql.Data;
using MySql.Data.MySqlClient;

const string conStr = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
using var connection = new MySqlConnection(conStr);
connection.Open();
string query = "select id, name, manager from user";
using var command = new MySqlCommand(query, connection);
using var reader = command.ExecuteReader();

while (reader.Read())
{
    Console.WriteLine(reader);
}
connection.Close();