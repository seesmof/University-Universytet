using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace dev
{
    public partial class login : Form
    {
        public login()
        {
            InitializeComponent();
        }

        public void loginButton_Click(object sender, EventArgs e)
        {
            string name = nameInput.Text;
            string password = passwordInput.Text;

            if (name == "" || password == "")
            {
                MessageBox.Show("Please enter username and password");
                nameInput.Text = "";
                passwordInput.Text = "";
                return;
            }

            if (userDataManager.validateCredentials(name, password))
            {
                currentUser.name = name;
                currentUser.password = password;
                currentUser.isAdmin = userDataManager.isAdmin(name);

                this.Hide();
                menu menu = new menu();
                menu.Show();
            }
            else
            {
                MessageBox.Show("Invalid username or password");
                nameInput.Text = "";
                passwordInput.Text = "";
            }
        }

        private void registerButton_Click(object sender, EventArgs e)
        {
            this.Hide();
            signup signup = new signup();
            signup.Show();
        }
    }
}
