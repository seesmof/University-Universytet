using app.controllers;
using app.models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Windows.Forms;

namespace app
{
    public partial class LoginForm : Form
    {
        string buyername;
        string password;

        public LoginForm()
        {
            InitializeComponent();
        }

        private void buyerNameLabel_Click(object sender, EventArgs e)
        {
            buyerNameTextBox.Focus();
        }

        private void passwordLabel_Click(object sender, EventArgs e)
        {
            passwordTextBox.Focus();
        }

        private void signUpLinkButton_Click(object sender, EventArgs e)
        {
            SignUpForm signUpForm = new SignUpForm();
            signUpForm.Show();
            this.Hide();
        }

        private void buyerNameTextBox_TextChanged(object sender, EventArgs e)
        {
            buyername = buyerNameTextBox.Text;
        }

        private void passwordTextBox_TextChanged(object sender, EventArgs e)
        {
            password = passwordTextBox.Text;
        }

        private void loginButton_Click(object sender, EventArgs e)
        {
            List<string> errors = new List<string>();
            if (buyerNameTextBox.Text == String.Empty)
            {
                errors.Add("Please enter your buyer's name");
            }
            if (passwordTextBox.Text == String.Empty)
            {
                errors.Add("Please enter your password");
            }
            Utilities.ShowErrors(errors);

            BuyerController buyerController = new BuyerController();
            List<Buyer> buyers = buyerController.GetBuyers();

            var buyer = buyers.FirstOrDefault(buyer => buyer.Name == buyername && buyer.Password == password);
            if (buyer != null)
            {
                MainWindow window = new MainWindow(buyer);
                window.Show();
                this.Hide();
            }
        }
    }
}
