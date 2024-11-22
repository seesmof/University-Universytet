using MySql.Data.MySqlClient;
using System.Data;

const string USER_NAME = "root";
const string PASSWORD = "1313";
const string HOST = "localhost";
const string PORT = "3306";
const string DATABASE_NAME = "data";
string connectionString = $"uid={USER_NAME};pwd={PASSWORD};host={HOST};port={PORT};database={DATABASE_NAME}";
Console.WriteLine(connectionString);

using var connection = new MySqlConnection(connectionString);
await connection.OpenAsync();

var query = "select id,name from finance_client";
using var command = new MySqlCommand(query, connection);
using var reader = await command.ExecuteReaderAsync();

while (await reader.ReadAsync())
{
    var value = reader.GetValue(0);
    Console.WriteLine(value);
}