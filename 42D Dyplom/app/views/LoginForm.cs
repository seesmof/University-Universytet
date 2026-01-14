using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace app
{
    public partial class LoginForm : Form
    {
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
    }
}
