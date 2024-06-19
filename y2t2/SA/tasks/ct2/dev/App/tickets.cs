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
    public partial class tickets : Form{
        public tickets(){
            InitializeComponent();
            if (!currentUser.isAdmin){
                ticketsGrid.Columns[0].Visible = false;
            }
            loadTickets();
        }
        public void loadTickets(){
            ticketsDataManager Manager = new ticketsDataManager();
            ticketsGrid.Rows.Clear();
            List<ticket> tickets;
            if (currentUser.isAdmin){
                tickets = Manager.loadTickets();
            }
            else{
                tickets = Manager.GetOwnTickets(currentUser.name);
            }
            for (int i = 0; i < tickets.Count; i++){
                ticket ticket = tickets[i];
                string seatType = ticket.isMiddle ? "Middle" : (ticket.isWindow ? "Window" : "Normal");
                string extraServices = "";
                extraServices += ticket.isBaggage ? "Baggage " : "";
                extraServices += ticket.isMeal ? "Meal " : "";
                extraServices += ticket.isPrivate ? "Private " : "";
                ticketsGrid.Rows.Add(ticket.userName, ticket.flightName, ticket.price, ticket.date, ticket.seatRow, seatType, extraServices);
            }
        }
        private void backButton_Click(object sender, EventArgs e){
            this.Hide();
            menu menu = new menu();
            menu.Show();
        }
    }
}