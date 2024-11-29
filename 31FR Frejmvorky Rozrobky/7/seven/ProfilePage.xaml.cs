using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Xml.Linq;

namespace seven
{
    /// <summary>
    /// Interaction logic for ProfilePage.xaml
    /// </summary>
    public partial class ProfilePage : Page
    {
        public User client;
        public MySqlConnection connection = new MySqlConnection(UtilityVariables.connectionString);
        public UtilityFunctions helper = new UtilityFunctions();
        Database db;
        public ProfilePage(string userName) {
            InitializeComponent();
            connection.Open();
            db = new Database(connection);

            // fetch user here
            User found=db.getUsers().Where(u => u.Name == userName).ToList().ElementAtOrDefault(0);
            if (found != null) {
                client = found;
            } else {
                client = db.createUser(userName);
            }

            // set client info to textboxes here
            showUserDetails();
        }
        public void showUserDetails() {
            UserNameBox.Text=client.Name;
            UserBalanceBox.Text= client.Balance.ToString();
            UserStatusToggle.IsChecked=Convert.ToBoolean(client.Admin);
        }
        private void ChangeNameButton_Click(object sender, RoutedEventArgs e) {
            var name = UserNameBox.Text;
            client.Name = name;
            db.updateUser(client);
            client = db.getUser(client.ID);
            UserNameBox.Text = client.Name;
        }
        private void ChangeBalanceButton_Click(object sender, RoutedEventArgs e) {
            int balance=client.Balance;
            try {
                balance = Convert.ToInt32(UserBalanceBox.Text);
            } catch { MessageBox.Show("Wrong balance. Please enter a number"); }
            client.Balance = balance;
            db.updateUser(client);
            client = db.getUser(client.ID);
            UserBalanceBox.Text = client.Balance.ToString();
        }
        private void UserStatusToggle_Click(object sender, RoutedEventArgs e) {
            var status = UserStatusToggle.IsChecked;
            client.Admin = Convert.ToInt32(status);
            db.updateUser(client);
            client = db.getUser(client.ID);
            UserStatusToggle.IsChecked = Convert.ToBoolean(client.Admin);
        }
    }
}
