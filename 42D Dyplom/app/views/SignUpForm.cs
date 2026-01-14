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
        public SignUpForm()
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
    }
}
