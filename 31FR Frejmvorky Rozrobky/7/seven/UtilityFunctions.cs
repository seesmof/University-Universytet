using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace seven
{
    public class UtilityFunctions {
        // CHECKERS
        public bool checkEstateKind(string kind)
        {
            return kind != EstateKind.Home && kind != EstateKind.Flat && kind != EstateKind.New ? false : true;
        }
        public bool checkMeetingStatus(string status)
        {
            return status != MeetingStatus.Wait && status != MeetingStatus.Done && status != MeetingStatus.Skip ? false : true;
        }
        public bool checkMeetingScore(string score)
        {
            return score != MeetingScore.Bad && score != MeetingScore.Okay && score != MeetingScore.Fine ? false : true;
        }

        // INPUT
        public string getInputString(string hint)
        {
            Console.Write($"{hint}: ");
            return Console.ReadLine();
        }
        public int getInputNumber(string hint)
        {
            var userInput = getInputString(hint);
            try
            {
                return int.Parse(userInput);
            }
            catch { return -1; }
        }

        // FORMATTERS
        public string getUserStatusString(User client)
        {
            return client.Admin == 0 ? "Client" : "Manager";
        }
        public string getEstateKindString(User client)
        {
            return client.Admin == 0 ? $"Estate kind ({EstateKind.Home} or {EstateKind.Flat})" : $"Estate kind ({EstateKind.Home} or {EstateKind.Flat} or {EstateKind.New})";
        }

        // DISPLAYS
        // Estate
        public void showEstates(List<Estate> estates, string header = "")
        {
            if (header != "")
            {
                Console.WriteLine($"{header} estates ({estates.Count})");
            }
            foreach (var e in estates)
            {
                Console.WriteLine($"{e.ID}. {e.Title} of kind {e.Kind} price {e.Price} owned by {e.Owner.Name}");
            }
        }
        public bool showOwnedEstates(Database db, User user)
        {
            var ownedEstates = db.getEstates().Where(e => e.Owner.ID == user.ID).ToList();
            if (ownedEstates.Count < 1)
            {
                Console.WriteLine("No owned estates");
                return false;
            }
            else
            {
                showEstates(ownedEstates, "Owned");
                return true;
            }
        }
        public bool showAvailableEstates(Database db, User user)
        {
            var availableEstates = db.getEstates().Where(e => e.Owner.ID != user.ID).ToList();
            if (availableEstates.Count < 1)
            {
                Console.WriteLine("No available estates");
                return false;
            }
            else
            {
                showEstates(availableEstates, "Available");
                return true;
            }
        }
        // Meeting
        public void showMeetings(List<Meeting> meetings, string header = "")
        {
            if (header != "")
            {
                Console.WriteLine($"{header} meetings ({meetings.Count})");
            }
            foreach (var m in meetings)
            {
                Console.WriteLine($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        public bool showIncomingMeetings(Database db, User user)
        {
            var incomingMeetings = db.getMeetings().Where(m => m.Target.Owner.ID == user.ID).ToList();
            if (incomingMeetings.Count < 1)
            {
                Console.WriteLine("No incoming meetings");
                return false;
            }
            else
            {
                showMeetings(incomingMeetings, "Incoming");
                return true;
            }
        }
        public bool showOutgoingMeetings(Database db, User user)
        {
            var incomingMeetings = db.getMeetings().Where(m => m.Sender.ID == user.ID).ToList();
            if (incomingMeetings.Count < 1)
            {
                Console.WriteLine("No outgoing meetings");
                return false;
            }
            else
            {
                showMeetings(incomingMeetings, "Outgoing");
                return true;
            }
        }
    }
}
