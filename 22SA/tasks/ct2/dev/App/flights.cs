using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Class_Library;

namespace App{
    public partial class flights : Form{
        public flight selectedFlight;
        public const int collapsedHeight = 190;
        public const int expandedHeight = 560;

        public int totalPrice;
        public int seatTypePrice = 0;
        public int mealPrice = 0;
        public int luggagePrice = 0;
        public int privatePrice = 0;
        public flights(){
            InitializeComponent();
            infoPanel.Visible = false;
            optionsPanel.Visible = false;
            this.Height = collapsedHeight;

            flightsDataManager Manager = new flightsDataManager();
            List<flight> flights = Manager.loadFlights();
            renderFlightNames(flights);
        }
        public void updateTotal(){
            totalPrice = selectedFlight.price + seatTypePrice + mealPrice + luggagePrice + privatePrice;
            totalPriceLabel.Text = $"In total: ${totalPrice}";
        }
        public void renderFlightNames(List<flight> flights){
            flightsList.Items.Clear();
            foreach (flight flight in flights){
                flightsList.Items.Add(flight.name);
            }
        }
        private void menuButton_Click(object sender, EventArgs e){
            this.Hide();
            menu menu = new menu();
            menu.Show();
        }
        private void flightsList_SelectedValueChanged(object sender, EventArgs e){
            flightsDataManager Manager = new flightsDataManager();
            selectedFlight = Manager.getFlight(flightsList.SelectedItem.ToString());
            infoPanel.Visible = true;
            optionsPanel.Visible = true;
            this.Height = expandedHeight;

            selectedLabel.Text = selectedFlight.name;
            priceLabel.Text = $"Ticket price: ${selectedFlight.price}";
            dateLabel.Text = $"Flight date: {selectedFlight.date.Replace("-", "/")}";
            seatsLabel.Text = $"Available seats: {selectedFlight.seats}";

            int seatRows = (int)Math.Floor((double)selectedFlight.seats / 10);
            rowSelect.Maximum = seatRows;

            totalPrice = selectedFlight.price;
            updateTotal();
        }
        private void middleRadio_CheckedChanged(object sender, EventArgs e){
            if (middleRadio.Checked){
                randomRadio.Checked = false;
                windowRadio.Checked = false;
                seatTypePrice = 10;
                updateTotal();
            }
        }
        private void randomRadio_CheckedChanged(object sender, EventArgs e){
            if (randomRadio.Checked){
                windowRadio.Checked = false;
                middleRadio.Checked = false;
                seatTypePrice = 0;
                updateTotal();
            }
        }
        private void windowRadio_CheckedChanged(object sender, EventArgs e){
            if (windowRadio.Checked){
                randomRadio.Checked = false;
                middleRadio.Checked = false;
                seatTypePrice = 30;
                updateTotal();
            }
        }
        private void mealBox_CheckedChanged(object sender, EventArgs e){
            mealPrice = mealBox.Checked ? 15 : 0;
            updateTotal();
        }
        private void luggageBox_CheckedChanged(object sender, EventArgs e){
            luggagePrice = luggageBox.Checked ? 30 : 0;
            updateTotal();
        }
        private void privateBox_CheckedChanged(object sender, EventArgs e){
            privatePrice = privateBox.Checked ? 77 : 0;
            updateTotal();
        }
        private void bookButton_Click(object sender, EventArgs e){
            ticketsDataManager Manager = new ticketsDataManager();
            Manager.AddTicket(currentUser.name, selectedFlight.name, totalPrice, selectedFlight.date, (int)rowSelect.Value, middleRadio.Checked, windowRadio.Checked, privateBox.Checked, luggageBox.Checked, mealBox.Checked);
            MessageBox.Show("Ticket booked successfully");
            this.Hide();
            menu menu = new menu();
            menu.Show();
        }
    }
}