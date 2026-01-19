using System;
using System.Collections.Generic;
using System.Text;

namespace app.models
{
    public class Truck
    {
        public string Name { get; set; } = "";
        public string Category { get; set; } = "";
        public int Price { get; set; } = 0;
        public string PictureName { get; set; } = string.Empty;

        public Truck(string name, string category, int price, string pictureName)
        {
            Name = name;
            Category = category;
            Price = price;
            PictureName = pictureName;
        }
    }
}
