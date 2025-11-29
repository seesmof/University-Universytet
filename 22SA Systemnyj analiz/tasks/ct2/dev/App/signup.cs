using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Class_Library;

namespace App{
    public partial class signup : Form{
        public signup(){
            InitializeComponent();
        }
        private void loginButton_Click(object sender, EventArgs e){
            this.Hide();
            login login = new login();
            login.Show();
        }
        private void signupButton_Click(object sender, EventArgs e){
            string name = nameInput.Text;
            string password = passwordInput.Text;
            bool isAdmin = adminCheck.Checked;

            userDataManager Manager = new userDataManager();
            user user = Manager.getUser(name);
            if (user != null){
                MessageBox.Show("Username already exists");
                nameInput.Text = "";
                passwordInput.Text = "";
                return;
            }

            Manager.addUser(name, password, isAdmin);
            this.Hide();
            login login = new login();
            login.Show();
        }
    }
}