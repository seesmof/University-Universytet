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
        string userName;
        string password;

        public LoginForm()
        {
            InitializeComponent();
        }

        private void userNameLabel_Click(object sender, EventArgs e)
        {
            userNameTextBox.Focus();
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

        private void userNameTextBox_TextChanged(object sender, EventArgs e)
        {
            userName = userNameTextBox.Text;
        }

        private void passwordTextBox_TextChanged(object sender, EventArgs e)
        {
            password = passwordTextBox.Text;
        }

        private void loginButton_Click(object sender, EventArgs e)
        {
            if (userNameTextBox.Text == String.Empty)
            {
                MessageBox.Show("Please enter your user's name","Empty username",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }
            if (passwordTextBox.Text == String.Empty)
            {
                MessageBox.Show("Please enter your password","Empty password",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }

            string filePath = "D:\\University-Universytet\\42D Dyplom\\app\\data\\users.txt";
            var lines = File.ReadLines(filePath);
            foreach (string line in lines)
            {
                var data = line.Split(",");
                User user = new User(data[0], data[1], data[2]);
                Console.WriteLine(user.Name);
            }
        }
    }
}
