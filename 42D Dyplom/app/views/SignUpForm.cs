using app.controllers;
using app.models;
using Microsoft.VisualBasic.ApplicationServices;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace app
{
    public partial class SignUpForm : Form
    {
        private string buyername;
        private string password;
        private string passwordConfirm;
        private bool isAdmin;

        public SignUpForm()
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

        private void passwordConfirmLabel_Click(object sender, EventArgs e)
        {
            passwordConfirmTextBox.Focus();
        }
        private void loginButton_Click(object sender, EventArgs e)
        {
            LoginForm loginForm = new LoginForm();
            loginForm.Show();
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

        private void passwordConfirmTextBox_TextChanged(object sender, EventArgs e)
        {
            passwordConfirm = passwordConfirmTextBox.Text;
        }

        private void signUpButton_Click(object sender, EventArgs e)
        {
            List<string> errors = new List<string>();
            if (buyername == String.Empty)
            {
                errors.Add("Please enter your buyer's name.");
            }
            if (password == String.Empty)
            {
                errors.Add("Please enter your password.");
            }
            if (passwordConfirm == String.Empty)
            {
                errors.Add("Please confirm your password.");
            }
            Utilities.ShowErrors(errors);

            BuyerController controller = new BuyerController();
            bool buyerExists = controller.DoesBuyersExist(buyername);
            if (!buyerExists)
            {
                controller.CreateBuyers(buyername, password, isAdmin);
            }
            
            Buyer buyer = controller.GetBuyers(buyername, password);
            MainWindow window = new MainWindow(buyer);
            window.Show();
            this.Hide();
        }

        private void adminCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            isAdmin = adminCheckBox.Checked ? true : false;
        }
    }
}
