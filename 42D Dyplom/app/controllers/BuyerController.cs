using app.models;
using System;
using System.Collections.Generic;
using System.Text;

namespace app.controllers
{
    public class UserController
    {
        private List<Buyer> buyers = new List<Buyer>();
        private const string buyersFilePath = "D:\\University-Universytet\\42D Dyplom\\app\\data\\buyers.txt";

        public UserController()
        {
            LoadUsers();
        }

        private void LoadUsers() {
            List<Buyer> loadedUsers = new List<Buyer>();

            var lines = File.ReadLines(buyersFilePath);
            foreach (string line in lines)
            {
                string[] data = line.Split(",");
                Buyer buyer = new Buyer(data[0], data[1], Convert.ToBoolean(data[2]));
                loadedUsers.Add(buyer);
            }

            // Set 'buyers' to 'loadedUsers'
            buyers.AddRange(loadedUsers);
        }

        public List<Buyer> GetUsers() { return buyers; }

        public Buyer GetUser(string buyername) {
            return buyers.FirstOrDefault(buyer => buyer.Name == buyername);
        }

        public Buyer GetUser(string buyername, string password)
        {
            return buyers.FirstOrDefault(buyer => buyer.Name == buyername && buyer.Password == password);
        }

        public bool DoesUserExist(string buyername) {
            return buyers.Any(buyer => buyer.Name == buyername);
        }

        public void CreateUser(string buyername, string password, bool isAdmin)
        {
            String line = $"{buyername},{password},{isAdmin}\n";
            File.AppendAllText(buyersFilePath, line);
        }
    }
}
