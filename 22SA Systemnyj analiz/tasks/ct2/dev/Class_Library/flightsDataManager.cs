using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_Library{
    public interface IFlightsDataManager{
        List<flight> loadFlights();
        flight getFlight(string name);
    }
    public class flightsDataManager : IFlightsDataManager{
        public string flightsFilePath="E:\\all\\University\\y2t2\\SA\\tasks\\ct2\\dev\\App\\flights.txt";
        public List<flight> loadFlights(){
            List<flight> flights = new List<flight>();
            if (File.Exists(flightsFilePath)){
                string[] strings = File.ReadAllLines(flightsFilePath);
                foreach (string line in strings){
                    string[] parts = line.Split(',');
                    if (parts.Length == 4){
                        flight flight = new flight{
                            name = parts[0],
                            price = int.Parse(parts[1]),
                            date = parts[2],
                            seats = int.Parse(parts[3])
                        };
                        flights.Add(flight);
                    }
                }
            }
            return flights;
        }
        public flight getFlight(string name){
            List<flight> flights = loadFlights();
            foreach (flight flight in flights){
                if (flight.name == name){
                    return flight;
                }
            }
            return null;
        }
    }
}