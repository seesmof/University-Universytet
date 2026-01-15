using System;
using System.Collections.Generic;
using System.Text;

namespace app.models
{
    public class User
    {
        public string Name { get; set; } = "";
        public string Password { get; set; } = "";
        public string Admin { get; set; } = "no";

        public User(string name, string password, string admin)
        {
            Name = name;
            Password = password;
            Admin = admin;
        }
    }
}
