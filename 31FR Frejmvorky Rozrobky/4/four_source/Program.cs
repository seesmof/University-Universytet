using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace four_source
{
    public class User
    {
        public int id { get; set; }
        public string name { get; set; }
        public int manager { get; set; } = 0;
    }
    public class Listing
    {
        public int id { get; set; }
        public string name { get; set; }
        public int price { get; set; }
        public string kind { get; set; }
        public User owner { get; set; }
    }
    public class Meeting
    {
        public int id { get; set; }
        public int score { get; set; } = 0;
        public string status { get; set; } = "Pending";
        public Listing viewable { get; set; }
        public User viewer { get; set; }
    }
    public class CurrentUser
    {
        public User user { get; set; }
        public bool entered { get; set; } = false;
    }
    public class Program
    {
        static void Main(string[] args)
        {
            var session = new CurrentUser();

            string menu = "";
            string WELCOME = @"1 Log in
2 Register";
            string DEFAULT = @"1 Profile
2 Market
3 
 Log out";
            string PROFILE = @"1 Info
2 Listings
3 Meetings
 Back";
            string PROFILE_INFO = @"1 View
2 Edit
3 Back";
            string PROFILE_INFO_VIEW = $@"User info for {session.user.name}:
- ID: {session.user.id}
- ";
            /* 
            login 
            if no user then register 
                keep track of current session with User class 
            implement all the functions
            */
            while (true)
            {
                if (!session.entered)
                {
                    menu = WELCOME;
                }
                else
                {
                    menu = DEFAULT;
                }
                Console.WriteLine(menu);
                Console.Write("> ");
                string response = Console.ReadLine();
                Console.WriteLine();

                int choice = Int32.Parse(response);
                if (!session.entered)
                {
                    if (choice == 1)
                    {
                        // login
                    }
                    else
                    {
                        // register
                    }
                }
                else
                {
                    if (choice)
                }
            }
        }
    }
}
