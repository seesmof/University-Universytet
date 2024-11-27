using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace four_source
{
    public class User
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Admin { get; set; } = 0;
    }
    public class Estate
    {
        public int ID { get; set; }
        public User Owner { get; set; }
        public string Title { get; set; }
        public string Kind { get; set; }
    }
    public class Meeting
    {
        public int ID { get; set; }
        public string Score { get; set; }
        public string Status { get; set; } = "Wait";
        public User Sender { get; set; }
        public Estate Target { get; set; }
    }
    public static class EstateKind
    {
        public static string Home = "Home";
        public static string Flat = "Flat";
        public static string New = "New";
    }
    public static class MeetingStatus
    {
        public static string Wait = "Wait";
        public static string Done = "Done";
        public static string Skip = "Skip";
    }
    public static class MeetingScore
    {
        public static string Bad = "Bad";
        public static string Okay = "Okay";
        public static string Fine = "Fine";
    }
    public class Program
    {
        static void Main(string[] args)
        {
            /* 
            enter user name 
                if not found in users, create new 
            load 
            */
            /* 
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
            */
        }
    }
}
