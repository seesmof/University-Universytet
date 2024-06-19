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
    public partial class menu : Form{
        public menu(){
            InitializeComponent();

            if (currentUser.isAdmin){
                ticketsButton.Text = "All Tickets";
            }
        }
        private void signoutButton_Click(object sender, EventArgs e){
            this.Hide();
            login login = new login();
            login.Show();
        }
        private void flightsButton_Click(object sender, EventArgs e){
            this.Hide();
            flights flights = new flights();
            flights.Show();
        }
        private void ticketsButton_Click(object sender, EventArgs e){
            this.Hide();
            tickets tickets = new tickets();
            tickets.Show();
        }
    }
}