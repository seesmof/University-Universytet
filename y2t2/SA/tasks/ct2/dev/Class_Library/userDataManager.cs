using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_Library{
    public interface IuserDataManager{
        List<user> loadUsers();
        void addUser(string name, string password, bool isAdmin);
        user getUser(string name);
        bool isAdmin(string name);
        bool validateCredentials(string name, string password);
    }
    public class userDataManager : IuserDataManager{
        public string usersFilePath = "E:\\all\\University\\y2t2\\SA\\tasks\\ct2\\dev\\App\\users.txt";
        public List<user> loadUsers(){
            List<user> users = new List<user>();
            if (File.Exists(usersFilePath)){
                string[] lines = File.ReadAllLines(usersFilePath);
                foreach (string line in lines){
                    string[] parts = line.Split(',');
                    if (parts.Length == 3){
                        user user = new user{
                            name = parts[0],
                            password = parts[1],
                            isAdmin = bool.Parse(parts[2]),
                        };
                        users.Add(user);
                    }
                }
            }
            return users;
        }
        public void addUser(string name, string password, bool isAdmin){
            File.AppendAllText(usersFilePath, $"\n{name},{password},{isAdmin.ToString().ToLower()}\n");
            Console.WriteLine("User added successfully");
        }
        public user getUser(string name){
            List<user> users = loadUsers();
            foreach (user user in users){
                if (user.name == name){
                    return user;
                }
            }
            return null;
        }
        public bool isAdmin(string name){
            user user = getUser(name);
            if (user != null) { return user.isAdmin; }
            return false;
        }
        public bool validateCredentials(string name, string password){
            user user = getUser(name);
            if (user != null && user.password == password) { return true; }
            return false;
        }
    }
}