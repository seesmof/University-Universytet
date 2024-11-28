using MySql.Data.MySqlClient;
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
        public const string Home = "Home";
        public const string Flat = "Flat";
        public const string New = "New";
    }
    public static class MeetingStatus
    {
        public const string Wait = "Wait";
        public const string Done = "Done";
        public const string Skip = "Skip";
    }
    public static class MeetingScore
    {
        public const string Bad = "Bad";
        public const string Okay = "Okay";
        public const string Fine = "Fine";
    }
    public static class Query
    {
        public const string LastCreatedID = "SELECT LAST_INSERT_ID();";
    }
    public class Session
    {
        public bool Entered { get; set; } = false;
        public User Client { get; set; }
        public string getUserStatus()
        {
            string status = "Manager";
            if (this.Client.Admin == 0)
            {
                status = "Client";
            }
            return status;
        }
    }
    public class Helper 
    {
        public bool checkEstateKind(string kind){
            if (kind!=EstateKind.Home && kind!=EstateKind.Flat && kind!=EstateKind.New) {
                return false;
            }
            return true;
        }
    }
    public class Database
    {
        MySqlConnection connection;
        string query;
        MySqlCommand command;
        MySqlDataReader reader;
        public Database(MySqlConnection connection) { this.connection = connection; }
        public User getUserByName(string userName)
        {
            query = $"SELECT id,name,admin FROM user WHERE name='{userName}';";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                reader.Close();
                return user;
            }
            reader.Close();
            return null;
        }
        public User getUserById(int id)
        {
            query = $"SELECT id,name,admin FROM user WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            while (reader.Read())
            {
                var user = new User();
                user.ID = reader.GetInt32(0);
                user.Name = reader.GetString(1);
                user.Admin = reader.GetInt32(2);
                reader.Close();
                return user;
            }
            reader.Close();
            return null;
        }
        public User createUser(string userName, int admin = 0)
        {
            query = $"INSERT INTO user (name,admin) VALUES ('{userName}',{admin});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();

            query = Query.LastCreatedID;
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var user = new User();
            while (reader.Read())
            {
                user.ID = reader.GetInt32(0);
                user.Name = userName;
                user.Admin = admin;
            }
            reader.Close();
            return user;
        }
        public void updateUser(User user)
        {
            query = $"UPDATE user SET name='{user.Name}',admin={user.Admin} WHERE id={user.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public List<Estate> getAllEstate()
        {
            query=$"SELECT id,owner_id,title,kind FROM estate;";
            command=new MySqlCommand(query,connection);
            reader=command.ExecuteReader();
            List<Estate> estates=new List<Estate>();
            List<int> owners=new List<int>();
            while (reader.Read())
            {
                var estate=new Estate();
                estate.ID=reader.GetInt32(0);
                owners.Add(reader.GetInt32(1));
                estate.Title=reader.GetString(2);
                estate.Kind=reader.GetString(3);
                estates.Add(estate);
            }
            reader.Close();
            for (int i=0;i<estates.Count;i++){
                var owner = this.getUserById(owners[i]);
                estates[i].Owner = owner;
            }
            return estates;
        }
        public Estate getEstateById(int id)
        {
            query = $"SELECT id,owner_id,title,kind FROM estate WHERE id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var estate = new Estate();
            int ownerId = 0;
            while (reader.Read())
            {
                estate.ID=reader.GetInt32(0);
                ownerId=reader.GetInt32(1);
                estate.Title=reader.GetString(2);
                estate.Kind=reader.GetString(3);
            }
            reader.Close();
            estate.Owner=this.getUserById(ownerId);
            return estate;
        }
        public List<Estate> getEstatesByOwnerId(int id)
        {
            query = $"SELECT id,title,kind FROM estate WHERE owner_id={id};";
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var estates = new List<Estate>();
            while (reader.Read())
            {
                var estate=new Estate();
                estate.ID=reader.GetInt32(0);
                estate.Title=reader.GetString(1);
                estate.Kind=reader.GetString(2);
                estates.Add(estate);
            }
            reader.Close();
            foreach (var estate in estates){
                estate.Owner=this.getUserById(id);
            }
            return estates;
        }
        public void updateEstate(Estate estate)
        {
            query = $"UPDATE estate SET owner_id={estate.Owner.ID},title='{estate.Title}',kind='{estate.Kind}' WHERE id={estate.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
        public Estate createEstate(string title,string kind,User owner){
            query = $"INSERT INTO estate (title,kind,owner_id) VALUES ('{title}','{kind}',{owner.ID});";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();

            query = Query.LastCreatedID;
            command = new MySqlCommand(query, connection);
            reader = command.ExecuteReader();
            var estate = new Estate();
            while (reader.Read())
            {
                estate.ID = reader.GetInt32(0);
                estate.Title=title;
                estate.Kind=kind;
                estate.Owner=owner;
            }
            reader.Close();
            return estate;
        }
        public void deleteEstate(int id)
        {
            // TODO implement this
            query = $"UPDATE estate SET owner_id={estate.Owner.ID},title='{estate.Title}',kind='{estate.Kind}' WHERE id={estate.ID};";
            command = new MySqlCommand(query, connection);
            command.ExecuteNonQuery();
        }
    }
    public class Program
    {
        static void Main(string[] args)
        {
            const string connectionString = "uid=root;pwd=1313;host=localhost;port=3306;database=fr_data";
            var connection = new MySqlConnection(connectionString);
            var database = new Database(connection);
            var helper=new Helper();
            connection.Open();
            var session = new Session();
            while (true)
            {
                string choice;
                int point;
                if (!session.Entered)
                {
                    Console.WriteLine("User name:");
                    var userName = Console.ReadLine();
                    User foundUser = database.getUserByName(userName);
                    if (foundUser!=null)
                    {
                        session.Client = foundUser;
                    }
                    else
                    {
                        session.Client = database.createUser(userName);
                    }
                    session.Entered=true;
                }
                else
                {
                    const string menu = @"1 Edit profile
2 Buy estate
3 Sell estate
4 Edit estate
5 Remove estate
6 Set meeting
7 See scheduled meetings";
                    Console.WriteLine(menu);
                    choice = Console.ReadLine();
                    try
                    {
                        point = int.Parse(choice);
                    }
                    catch (Exception e)
                    {
                        break;
                    }
                    Console.WriteLine();

                    if (point == 1)
                    {
                        // EDIT PROFILE
                        // read use details 
                        // get input from user on what to change 
                        // Request manager status 
                        // update user object 

                        string userStatus = session.getUserStatus();
                        Console.WriteLine($"User name: {session.Client.Name}\nUser status: {userStatus}");

                        // show all owned property
                        var estates = database.getEstatesByOwnerId(session.Client.ID);
                        Console.WriteLine($"Owned property ({estates.Count})");
                        foreach (var estate in estates)
                        {
                            Console.WriteLine($"{estate.ID}. {estate.Title} of kind {estate.Kind} owned by {estate.Owner.Name}");
                        }

                        string options = "1 Change name\n2 Change status";
                        Console.WriteLine(options);
                        choice = Console.ReadLine();
                        try
                        {
                            point = int.Parse(choice);
                        }
                        catch (Exception e)
                        {
                            continue;
                        }
                        Console.WriteLine();

                        if (point == 1)
                        {
                            Console.WriteLine("Enter new user name:");
                            var newName = Console.ReadLine();
                            session.Client.Name = newName;
                            database.updateUser(session.Client);
                        } 
                        else if (point == 2)
                        {
                            if (session.Client.Admin == 1)
                            {
                                session.Client.Admin = 0;
                            } 
                            else
                            {
                                session.Client.Admin = 1;
                            }
                            database.updateUser(session.Client);
                        }
                    }
                    else if (point == 2)
                    {
                        // BUY ESTATE
                        // read all available estate 
                        // show all estate where owner is not user 
                        // get input from user on what to buy 

                        var foundEstates = database.getAllEstate();
                        List<Estate> estates = new List<Estate>();
                        foreach(var e in foundEstates)
                        {
                            if (e.Owner.Name != session.Client.Name)
                            {
                                estates.Add(e);
                            }
                        }
                        if (estates.Count < 1)
                        {
                            Console.WriteLine("No estates available");
                            continue;
                        }
                        Console.WriteLine($"Available estates ({estates.Count})");
                        foreach(var estate in estates)
                        {
                            if (estate.Owner.Name != session.Client.Name)
                            {
                                Console.WriteLine($"{estate.ID}. {estate.Title} of kind {estate.Kind} owned by {estate.Owner.Name}");
                            }
                        }
                        Console.WriteLine("Enter estate ID to buy:");
                        choice = Console.ReadLine();
                        int estateId;
                        try
                        {
                            estateId = int.Parse(choice);
                        }
                        catch (Exception e)
                        {
                            continue;
                        }
                        // buy estate here
                        var selectedEstate = database.getEstateById(estateId);
                        selectedEstate.Owner = session.Client;
                        database.updateEstate(selectedEstate);
                    }
                    else if (point == 3)
                    {
                        // SELL ESTATE
                        // get all the estate details 
                        // add new estate to database 

                        Console.WriteLine("Estate title:");
                        var title=Console.ReadLine();
                        if (session.Client.Admin==1){
                            Console.WriteLine($"Estate kind ({EstateKind.Home} or {EstateKind.Flat} or {EstateKind.New})");
                        }
                        else{
                            Console.WriteLine($"Estate kind ({EstateKind.Home} or {EstateKind.Flat})");
                        }
                        var kind=Console.ReadLine();
                        if (helper.checkEstateKind(kind)==false){
                            Console.WriteLine("Wrong estate kind, please select from a list");
                            continue;
                        }
                        else if (kind==EstateKind.New && session.Client.Admin==0){
                            Console.WriteLine($"Estate of kind {EstateKind.New} may be added only by managers");
                            continue;
                        }
                        var estate = database.createEstate(title, kind, session.Client);
                    }
                    else if (point == 4)
                    {
                        // EDIT ESTATE
                        // get all estate by owner 
                        // get estate id from user 
                        // get option to edit in estate 
                        // update estate in a database 

                        var estates = database.getEstatesByOwnerId(session.Client.ID);
                        foreach (var e in estates)
                        {
                            Console.WriteLine($"{e.ID}. {e.Title} of kind {e.Kind} owned by {e.Owner.Name}");
                        }

                        Console.WriteLine("Select estate ID to edit:");
                        var estateIdString = Console.ReadLine();
                        int estateId;
                        try{
                            estateId=int.Parse(estateIdString);
                        } catch (Exception e){
                            continue;
                        }
                        var estate=database.getEstateById(estateId);

                        Console.WriteLine("1 Title\n2 Kind");
                        choice=Console.ReadLine();
                        try{
                            point=int.Parse(choice);
                        } catch (Exception e){
                            continue;
                        }

                        if (point==1){
                            Console.Write("Enter new estate title please: ");
                            var newTitle=Console.ReadLine();
                            estate.Title=newTitle;
                        } 
                        else if (point==2){
                            if (session.Client.Admin==0){
                                Console.Write($"Enter new kind please ({EstateKind.Home} or {EstateKind.Flat} or {EstateKind.New}): ");
                            } else {
                                Console.Write($"Enter new kind please ({EstateKind.Home} or {EstateKind.Flat}): ");
                            }
                            var newKind = Console.ReadLine();
                            estate.Kind = newKind;
                        }
                        database.updateEstate(estate);
                    }
                    else if (point == 5)
                    {
                        // REMOVE ESTATE
                        // show all owned estates 
                        // get estate id to delete 

                        var estates = database.getEstatesByOwnerId(session.Client.ID);
                        foreach (var e in estates)
                        {
                            Console.WriteLine($"{e.ID}. {e.Title} of kind {e.Kind} owned by {e.Owner.Name}");
                        }

                        Console.WriteLine("Select estate ID to delete:");
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

                        database.deleteEstate(estateId);
                    }
                    else if (point == 6)
                    {
                        // SET MEETING
                    }
                    else if (point == 7)
                    {
                        // SEE SCHEDULED MEETINGS
                    }
                    else 
                    {
                        break;
                    }
                }
                Console.WriteLine();
            }
            connection.Close();
        }
    }
}
