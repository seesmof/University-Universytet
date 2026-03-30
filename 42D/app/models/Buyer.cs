using System;
using System.Collections.Generic;
using System.Text;

namespace app.models
{
    public class Buyer
    {
        public string Name { get; set; } = "";
        public string Password { get; set; } = "";
        public bool IsAdmin { get; set; } = false;

        public Buyer() { }
        public Buyer(string name, string password, bool admin)
        {
            Name = name;
            Password = password;
            IsAdmin = admin;
        }
    }
}
