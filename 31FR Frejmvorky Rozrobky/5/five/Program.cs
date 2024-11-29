using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace five
{
    public class User {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Admin { get; set; } = 0;
    }
    public class Estate {
        public int ID { get; set; }
        public User Owner { get; set; }
        public string Title { get; set; }
        public string Kind { get; set; }
    }
    public class Meeting {
        public int ID { get; set; }
        public User Sender { get; set; }
        public Estate Target { get; set; }
        public string Score { get; set; } = "Unrated";
        public string Status { get; set; } = MeetingStatus.Wait;
    }
    public static class EstateKind {
        public const string Home = "Home";
        public const string Flat = "Flat";
        public const string New = "New";
    }
    public static class MeetingStatus {
        public const string Wait = "Wait";
        public const string Done = "Done";
        public const string Skip = "Skip";
    }
    public static class MeetingScore {
        public const string Bad = "Bad";
        public const string Okay = "Okay";
        public const string Fine = "Fine";
    }
    public class Session {
        public bool Entered { get; set; } = false;
        public User Client { get; set; }
    }
    public class Database
    {
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        MySqlConnection connection;
        public const string LastCreatedID="SELECT LAST_INSERT_ID();";

        // SYSTEM
        public Database(MySqlConnection connection) { this.connection = connection; }
        public MySqlDataReader read(string query){
            command=new MySqlCommand(query,connection);
            return command.ExecuteReader();
        }
        public void write(string query){
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }

        // CREATE
        public User createUser(string name, int admin = 0) {
            write($"INSERT INTO user (name,admin) VALUES ('{name}',{admin});");
            reader=read(LastCreatedID);
            var user = new User();
            while (reader.Read()) {
                user.ID = reader.GetInt32(0);
                user.Name = name;
                user.Admin = admin;
            }
            reader.Close();
            return user;
        }
        public Estate createEstate(string title, string kind, User owner) {
            write($"INSERT INTO estate (title,kind,owner_id) VALUES ('{title}','{kind}',{owner.ID});");
            reader=read(LastCreatedID);
            var estate = new Estate();
            while (reader.Read()) {
                estate.ID = reader.GetInt32(0);
                estate.Title = title;
                estate.Kind = kind;
                estate.Owner = owner;
            }
            reader.Close();
            return estate;
        }
        public Meeting createMeeting(User sender,Estate target){
            write($"INSERT INTO meeting (sender_id,target_id) VALUES ({sender.ID},{target.ID});");
            reader=read(LastCreatedID);
            var meeting = new Meeting();
            while (reader.Read()) {
                meeting.ID = reader.GetInt32(0);
                meeting.Sender=sender;
                meeting.Target=target;
            }
            reader.Close();
            return meeting;
        }

        // READ
        public List<User> getUsers(){
            reader=read("SELECT id,name,admin FROM user;");
            var users=new List<User>();
            while (reader.Read()) {
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                users.Add(user);
            }
            reader.Close();
            return users;
        }
        public User getUser(int id){
            return getUsers().Where(u=>u.ID==id).ToList().ElementAtOrDefault(0);
        }
        public List<Estate> getEstates(){
            reader=read("SELECT id,owner_id,title,kind FROM estate;");
            var estates=new List<Estate>();
            var owners=new List<int>();
            while (reader.Read()){
                var estate=new Estate();
                estate.ID=reader.GetInt32(0);
                owners.Add(reader.GetInt32(1));
                estate.Title=reader.GetString(2);
                estate.Kind=reader.GetString(3);
                estates.Add(estate);
            }
            reader.Close();
            for (int i=0;i<estates.Count;i++){
                estates[i].Owner=getUser(owners[i]);
            }
            return estates;
        }
        public Estate getEstate(int id){
            return getEstates().Where(e=>e.ID==id).ToList().ElementAtOrDefault(0);
        }
        public List<Meeting> getMeetings(){
            reader=read("SELECT id,sender_id,target_id,score,status FROM meeting;");
            var meetings=new List<Meeting>();
            var senders = new List<int>();
            var targets = new List<int>();
            while (reader.Read()) {
                var meeting = new Meeting();
                meeting.ID = reader.GetInt32(0);
                senders.Add(reader.GetInt32(1));
                targets.Add(reader.GetInt32(2));
                meeting.Score = reader.GetString(3);
                meeting.Status = reader.GetString(4);
                meetings.Add(meeting);
            }
            reader.Close();
            for (int i = 0; i < meetings.Count; i++) {
                meetings[i].Sender = getUser(senders[i]);
                meetings[i].Target = getEstate(targets[i]);
            }
            return meetings;
        }
        public Meeting getMeeting(int id){
            return getMeetings().Where(m=>m.ID==id).ToList().ElementAtOrDefault(0);
        }

        // UPDATE
        public void updateUser(User user) {
            write($"UPDATE user SET name='{user.Name}',admin={user.Admin} WHERE id={user.ID};");
        }
        public void updateEstate(Estate estate) {
            write($"UPDATE estate SET owner_id={estate.Owner.ID},title='{estate.Title}',kind='{estate.Kind}' WHERE id={estate.ID};");
        }
        public void updateMeeting(Meeting meeting) {
            write($"UPDATE meeting SET sender_id={meeting.Sender.ID},target_id={meeting.Target.ID},score='{meeting.Score}',status='{meeting.Status}' WHERE id={meeting.ID};");
        }

        // DELETE
        public void deleteEstate(int id) {
            write($"DELETE FROM estate WHERE id={id};");
        }
    }
    public class Helper {
        // CHECKERS
        public bool checkEstateKind(string kind) {
            return kind != EstateKind.Home && kind != EstateKind.Flat && kind != EstateKind.New ? false : true;
        }
        public bool checkMeetingStatus(string status) {
            return status != MeetingStatus.Wait && status != MeetingStatus.Done && status != MeetingStatus.Skip ? false : true;
        }
        public bool checkMeetingScore(string score) {
            return score != MeetingScore.Bad && score != MeetingScore.Okay && score != MeetingScore.Fine ? false : true;
        }

        // INPUT
        public string getInputString(string hint){
            Console.Write($"{hint}: ");
            return Console.ReadLine();
        }
        public int getInputNumber(string hint){
            var userInput=getInputString(hint);
            try {
                return int.Parse(userInput);
            } catch { return -1; }
        }

        // FORMATTERS
        public string getUserStatusString(User client) {
            return client.Admin==0 ? "Client" : "Manager";
        }

        // DISPLAYS
        // Estate
        public void showEstates(List<Estate> estates,string header=""){
            if (header!=""){
                Console.WriteLine($"{header} estates ({estates.Count})");
            }
            foreach (var e in estates) {
                Console.WriteLine($"{e.ID}. {e.Title} of kind {e.Kind} owned by {e.Owner.Name}");
            }
        }
        public bool showOwnedEstates(Database db,User user){
            var ownedEstates=db.getEstates().Where(e=>e.Owner.ID==user.ID).ToList();
            if (ownedEstates.Count<1){
                Console.WriteLine("No owned estates");
                return false;
            } else {
                showEstates(ownedEstates,"Owned");
                return true;
            }
        }
        public bool showAvailableEstates(Database db,User user){
            var availableEstates=db.getEstates().Where(e=>e.Owner.ID!=user.ID).ToList();
            if (availableEstates.Count<1){
                Console.WriteLine("No available estates");
                return false;
            } else {
                showEstates(availableEstates,"Available");
                return true;
            }
        }
        // Meeting
        public void showMeetings(List<Meeting> meetings,string header=""){
            if (header!=""){
                Console.WriteLine($"{header} meetings ({meetings.Count})");
            }
            foreach (var m in meetings) {
                Console.WriteLine($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        public bool showIncomingMeetings(Database db,User user){
            var incomingMeetings=db.getMeetings().Where(m=>m.Target.Owner.ID==user.ID).ToList();
            if (incomingMeetings.Count<1){
                Console.WriteLine("No incoming meetings");
                return false;
            } else {
                showMeetings(incomingMeetings,"Incoming");
                return true;
            }
        }
        public bool showOutgoingMeetings(Database db,User user){
            var incomingMeetings=db.getMeetings().Where(m=>m.Sender.ID==user.ID).ToList();
            if (incomingMeetings.Count<1){
                Console.WriteLine("No outgoing meetings");
                return false;
            } else {
                showMeetings(incomingMeetings,"Outgoing");
                return true;
            }
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(connectionString);
            connection.Open();

            var database = new Database(connection);
            var session = new Session();
            var helper = new Helper();
            
            while (true) {
                if (!session.Entered) {
                    var name=helper.getInputString("User name");
                    User foundUser = database.getUsers().Where(u=>u.Name==name).ToList().ElementAtOrDefault(0);
                    session.Entered = true;

                    if (foundUser != null) {
                        session.Client = foundUser;
                    } else {
                        session.Client = database.createUser(name);
                    }
                    continue;
                }
            
                int point=helper.getInputNumber("1 Edit profile\n2 Buy estate\n3 Sell estate\n4 Edit estate\n5 Remove estate\n6 Schedule meeting\n7 Rate meeting (Viewer)\n8 Process meeting (Owner)\n");
                if (point==-1){
                    break;
                }

                // EDIT PROFILE
                if (point == 1) {
                    string status = helper.getUserStatusString(session.Client);
                    Console.WriteLine($"User name: {session.Client.Name}\nUser status: {status}");

                    helper.showOwnedEstates(database,session.Client);
                    helper.showIncomingMeetings(database,session.Client);
                    helper.showOutgoingMeetings(database,session.Client);

                    point=helper.getInputNumber("1 Change name\n2 Change status\n");
                    if (point==-1){
                        continue;
                    }
                    if (point == 1) {
                        var newName=helper.getInputString("New user name");
                        session.Client.Name = newName;
                    } else if (point == 2) {
                        if (session.Client.Admin == 1) {
                            session.Client.Admin = 0;
                        } else { 
                            session.Client.Admin = 1;
                        }
                    }
                    database.updateUser(session.Client);
                }
                // BUY ESTATE
                else if (point == 2) {
                    if (helper.showAvailableEstates(database,session.Client)==false){
                        continue;
                    }
                    point=helper.getInputNumber("Estate ID to buy");
                    if (point==-1){
                        continue;
                    }
                    var estate = database.getEstate(point);
                    estate.Owner = session.Client;
                    database.updateEstate(estate);
                }
                // SELL ESTATE
                else if (point == 3) {
                    string kindPrompt=session.Client.Admin==0 ? $"Estate kind ({EstateKind.Home} or {EstateKind.Flat})" : $"Estate kind ({EstateKind.Home} or {EstateKind.Flat} or {EstateKind.New})";

                    var title=helper.getInputString("Title");
                    var kind=helper.getInputString(kindPrompt);

                    if (helper.checkEstateKind(kind) == false) {
                        Console.WriteLine("Wrong estate kind, please select from a list");
                        continue;
                    } else if (kind == EstateKind.New && session.Client.Admin == 0) {
                        Console.WriteLine($"Estate of kind {EstateKind.New} may be added only by managers");
                        continue;
                    }
                    database.createEstate(title, kind, session.Client);
                }
                // EDIT ESTATE
                else if (point == 4) {
                    if (helper.showOwnedEstates(database,session.Client)==false){
                        continue;
                    }
                    point=helper.getInputNumber("Estate ID to edit");
                    if (point==-1){
                        continue;
                    }
                    var estate = database.getEstate(point);

                    point = helper.getInputNumber("1 Title\n2 Kind\n");
                    if (point==-1){
                        continue;
                    }
                    if (point == 1) {
                        var newTitle=helper.getInputString("New estate title");
                        estate.Title = newTitle;
                    } else if (point == 2) {
                        var kindPrompt=session.Client.Admin==0 ? $"New kind ({EstateKind.Home} or {EstateKind.Flat})" : $"New kind ({EstateKind.Home} or {EstateKind.Flat} or {EstateKind.New})";

                        var kind=helper.getInputString(kindPrompt);
                        estate.Kind = kind;
                    }
                    database.updateEstate(estate);
                }
                // REMOVE ESTATE
                else if (point == 5) {
                    if (helper.showOwnedEstates(database,session.Client)==false){
                        continue;
                    }
                    point=helper.getInputNumber("Estate ID to remove");
                    if (point==-1){
                        continue;
                    }
                    database.deleteEstate(point);
                }
                // SET MEETING
                else if (point == 6) {
                    if (helper.showAvailableEstates(database,session.Client)==false){
                        continue;
                    }
                    point=helper.getInputNumber("Estate ID to schedule a meeting for");
                    if (point==-1){
                        continue;
                    }
                    var estate = database.getEstate(point);
                    database.createMeeting(session.Client, estate);
                }
                /*
                // RATE MEETING FOR VIEWER
                else if (point == 7) {
                    if (helper.showOutgoingMeetings(database,session.Client)==false){
                        continue;
                    }

                    var foundMeetings = database.getOutgoingMeetings(session.Client);
                    var meetings = new List<Meeting>();
                    foreach (var m in foundMeetings)
                    {
                        if (m.Status == MeetingStatus.Done)
                        {
                            meetings.Add(m);
                        }
                    }
                    if (meetings.Count < 1)
                    {
                        Console.WriteLine("No meetings to rate");
                        continue;
                    }
                    foreach (var m in meetings)
                    {
                        Console.WriteLine($"{m.ID}. For {m.Target.Title} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
                    }

                    Console.Write("Enter meeting ID to rate please: ");
                    var response = Console.ReadLine();
                    int meetingId;
                    try
                    {
                        meetingId = int.Parse(response);
                    }
                    catch (Exception e)
                    {
                        continue;
                    }

                    Console.Write($"Enter meeting rating ({MeetingScore.Bad} or {MeetingScore.Okay} or {MeetingScore.Fine}): ");
                    var meetingScore = Console.ReadLine();
                    if (helper.checkMeetingScore(meetingScore) == false)
                    {
                        Console.WriteLine("Incorrect score, please select from the list");
                        continue;
                    }
                    var meeting = database.getMeetingById(meetingId);
                    meeting.Score = meetingScore;
                    database.updateMeeting(meeting.ID, meeting.Score, meeting.Status, meeting.Sender, meeting.Target);
                }
                else if (point == 8)
                {
                    // PROCESS MEETING FOR OWNER
                    // see for all estate or only for selected 

                    Console.WriteLine("Would you like to see incoming meetings for all estate or only for selected?");
                    Console.WriteLine("1 All\n2 Selected");
                    choice = Console.ReadLine();
                    try
                    {
                        point = int.Parse(choice);
                    }
                    catch (Exception e)
                    {
                        continue;
                    }

                    if (point == 1)
                    {
                        var incomingMeetings = database.getIncomingMeetings(session.Client);
                        if (incomingMeetings.Count > 0)
                        {
                            Console.WriteLine($"Incoming meetings ({incomingMeetings.Count})");
                            foreach (var m in incomingMeetings)
                            {
                                Console.WriteLine($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} rated {m.Score} status {m.Status}");
                            }
                        }
                        else
                        {
                            Console.WriteLine("No meetings found");
                        }
                    }
                    else
                    {
                        var estates = database.getEstatesByOwnerId(session.Client.ID);
                        foreach (var e in estates)
                        {
                            Console.WriteLine($"{e.ID}. {e.Title} of kind {e.Kind} owned by {e.Owner.Name}");
                        }
                        Console.Write("Please enter estate ID to see meetings for: ");
                        var estateIdString = Console.ReadLine();
                        int estateId;
                        try
                        {
                            estateId = int.Parse(estateIdString);
                        }
                        catch (Exception e)
                        {
                            continue;
                        }

                        var incomingMeetings = database.getMeetingsByTargetId(estateId);
                        var estate = database.getEstateById(estateId);
                        if (incomingMeetings.Count > 0)
                        {
                            Console.WriteLine($"Incoming meetings for {estate.Title} ({incomingMeetings.Count})");
                            foreach (var m in incomingMeetings)
                            {
                                Console.WriteLine($"{m.ID}. By {m.Sender.Name} rated {m.Score} status {m.Status}");
                            }
                        }
                        else
                        {
                            Console.WriteLine("No meetings found");
                        }
                    }

                    Console.Write("Enter meeting ID to change status for please: ");
                    choice = Console.ReadLine();
                    int meetingId;
                    try
                    {
                        meetingId = int.Parse(choice);
                    }
                    catch (Exception e)
                    {
                        continue;
                    }
                    var meeting = database.getMeetingById(meetingId);

                    Console.Write($"Please enter new meeting status ({MeetingStatus.Done} or {MeetingStatus.Skip} or {MeetingStatus.Wait}): ");
                    var status = Console.ReadLine();
                    if (helper.checkMeetingStatus(status) == false)
                    {
                        Console.WriteLine("Incorrect meeting status, please select from a list");
                        continue;
                    }
                    meeting.Status = status;
                    database.updateMeeting(meeting.ID, meeting.Score, meeting.Status, meeting.Sender, meeting.Target);
                }
                */
            }
            connection.Close();
        }
    }
}