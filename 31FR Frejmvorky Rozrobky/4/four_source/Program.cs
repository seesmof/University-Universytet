using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace four_source
{
    public class User { }
    public class Estate { }
    public class Meeting { }
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
            login 
            if no user then register 
                keep track of current session with User class 
            implement all the functions
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
