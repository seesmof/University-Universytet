using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dev
{
    public class ticketsDataManager
    {
        public static string ticketsFilePath = "E:\\all\\University\\y2t2\\SA\\tasks\\lb4\\dev\\tickets.txt";

        public static List<ticket> loadTickets(){
            List<ticket> tickets = new List<ticket>();
            if (File.Exists(ticketsFilePath))
            {
                string[] strings = File.ReadAllLines(ticketsFilePath);
                foreach (string line in strings)
                {
                    string[] parts = line.Split(',');
                    if (parts.Length == 10)
                    {
                        ticket ticket = new ticket
                        {
                            userName = parts[0],
                            flightName = parts[1],
                            price = int.Parse(parts[2]),
                            date = parts[3],
                            seatRow = int.Parse(parts[4]),
                            isMiddle = bool.Parse(parts[5]),
                            isWindow = bool.Parse(parts[6]),
                            isPrivate = bool.Parse(parts[7]),
                            isBaggage = bool.Parse(parts[8]),
                            isMeal = bool.Parse(parts[9]),
                        };
                        tickets.Add(ticket);
                    }
                }
            }
            return tickets;
        }

        public static ticket GetTicket(string flightName)
        {
            List<ticket> tickets = loadTickets();
            foreach (ticket ticket in tickets)
            {
                if (ticket.flightName == flightName)
                {
                    return ticket;
                }
            }
            return null;
        }

        public static List<ticket> GetOwnTickets(string userName)
        {
            List<ticket> tickets = loadTickets();
            List<ticket> ownTickets = new List<ticket>();
            foreach (ticket ticket in tickets)
            {
                if (ticket.userName == userName)
                {
                    ownTickets.Add(ticket);
                }
            }
            return ownTickets;
        }

        public static void AddTicket(string userName, string flightName, int price, string date, int seatRow, bool isMiddle, bool isWindow, bool isPrivate, bool isBaggage, bool isMeal)
        {
            File.AppendAllText(ticketsFilePath, $"\n{userName},{flightName},{price},{date},{seatRow},{isMiddle.ToString().ToLower()},{isWindow.ToString().ToLower()},{isPrivate.ToString().ToLower()},{isBaggage.ToString().ToLower()},{isMeal.ToString().ToLower()}");
            Console.WriteLine("Ticket added successfully");
        }
    }
}
