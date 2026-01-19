using app.models;
using System;
using System.Collections.Generic;
using System.Text;

namespace app.controllers
{
    public class BuyerController
    {
        private List<Buyer> buyers = new List<Buyer>();
        private const string buyersFilePath = "D:\\University-Universytet\\42D Dyplom\\app\\data\\buyers.txt";

        public BuyerController()
        {
            LoadBuyers();
        }

        private void LoadBuyers() {
            List<Buyer> loadedBuyers = new List<Buyer>();

            var lines = File.ReadLines(buyersFilePath);
            foreach (string line in lines)
            {
                string[] data = line.Split(",");
                Buyer buyer = new Buyer(data[0], data[1], Convert.ToBoolean(data[2]));
                loadedBuyers.Add(buyer);
            }

            // Set 'buyers' to 'loadedBuyers'
            buyers.AddRange(loadedBuyers);
        }

        public List<Buyer> GetBuyers() { return buyers; }

        public Buyer GetBuyers(string buyername) {
            return buyers.FirstOrDefault(buyer => buyer.Name == buyername);
        }

        public Buyer GetBuyers(string buyername, string password)
        {
            return buyers.FirstOrDefault(buyer => buyer.Name == buyername && buyer.Password == password);
        }

        public bool DoesBuyersExist(string buyername) {
            return buyers.Any(buyer => buyer.Name == buyername);
        }

        public void CreateBuyers(string buyername, string password, bool isAdmin)
        {
            String line = $"{buyername},{password},{isAdmin}\n";
            File.AppendAllText(buyersFilePath, line);
        }
    }
}
