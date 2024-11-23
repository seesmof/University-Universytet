﻿using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace three_source
{
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public bool manager { get; set; } = false;
    }
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
                    var user = new User();
                    user.id = int.Parse(reader[0].ToString());
                    user.name = reader[1].ToString();
                    user.manager = Convert.ToBoolean(Convert.ToInt16(reader[2].ToString()));
                    Console.WriteLine($"User {user.id} name {user.name} manager {user.manager}");
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
