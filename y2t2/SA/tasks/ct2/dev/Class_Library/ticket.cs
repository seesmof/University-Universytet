using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_Library{
    public class ticket{
        public string userName { get; set; }
        public string flightName { get; set; }
        public int price { get; set; }
        public string date { get; set; }
        public int seatRow { get; set; }
        public bool isMiddle { get; set; }
        public bool isWindow { get; set; }
        public bool isPrivate { get; set; }
        public bool isBaggage { get; set; }
        public bool isMeal { get; set; }
    }
}