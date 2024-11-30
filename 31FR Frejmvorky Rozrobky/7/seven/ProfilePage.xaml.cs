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
        public Database database;
        public ProfilePage(string userName) {
            InitializeComponent();
            connection.Open();
            database = new Database(connection);

            // fetch user here
            User found=database.getUsers().Where(u => u.Name == userName).ToList().ElementAtOrDefault(0);
            if (found != null) {
                client = found;
            } else {
                client = database.createUser(userName);
            }
        }
        public void showUserData() {
            UserNameBox.Text=client.Name;
            UserBalanceBox.Text= client.Balance.ToString();
            UserStatusToggle.IsChecked=Convert.ToBoolean(client.Admin);
        }
        private void UserDataTabOpened(object sender, RoutedEventArgs e){
            showUserData();
        }
        public void showUserEstates(){
            
        }
        private void UserPropertyTabOpened(object sender, RoutedEventArgs e){
            showUserEstates();
        }
        private void ChangeNameButton_Click(object sender, RoutedEventArgs e) {
            var name = UserNameBox.Text;
            client.Name = name;
            database.updateUser(client);
            client = database.getUser(client.ID);
            UserNameBox.Text = client.Name;
        }
        private void ChangeBalanceButton_Click(object sender, RoutedEventArgs e) {
            int balance=client.Balance;
            try {
                balance = Convert.ToInt32(UserBalanceBox.Text);
            } catch { MessageBox.Show("Wrong balance. Please enter a number"); }
            client.Balance = balance;
            database.updateUser(client);
            client = database.getUser(client.ID);
            UserBalanceBox.Text = client.Balance.ToString();
        }
        private void UserStatusToggle_Click(object sender, RoutedEventArgs e) {
            var status = UserStatusToggle.IsChecked;
            client.Admin = Convert.ToInt32(status);
            database.updateUser(client);
            client = database.getUser(client.ID);
            UserStatusToggle.IsChecked = Convert.ToBoolean(client.Admin);
        }
    }
}
