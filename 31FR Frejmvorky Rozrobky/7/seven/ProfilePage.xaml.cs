using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
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

            showIncomingMeetings();
            showOutgoingMeetings();
        }
        public void homeTabOpened(object sender, RoutedEventArgs e) {
            showUserData();
        }
        public void ownedEstatesTabOpened(object sender, RoutedEventArgs e) {
            showOwnedEstates();
        }
        public void availableEstatesTabOpened(object sender, RoutedEventArgs e) {
            showAvailableEstates();
        }
        public void showUserData() {
            UserNameBox.Text=client.Name;
            UserBalanceBox.Text= client.Balance.ToString();
            UserStatusToggle.IsChecked=Convert.ToBoolean(client.Admin);
        }
        public void showOwnedEstates() {
            var data = database.getEstates().Where(e => e.Owner.ID == client.ID).ToList();
            OwnedEstatesContainer.Items.Clear();
            foreach (var e in data) {
                OwnedEstatesContainer.Items.Add($"{e.ID}. {e.Title} of kind {e.Kind} price {e.Price} owned by {e.Owner.Name}");
            }
            OeTitleInput.Text = "";
            OeKindInput.Text = EstateKind.Home;
            OePriceInput.Text = "0";
        }
        public void showIncomingMeetings() {
            var data = database.getMeetings().Where(m => m.Target.Owner.ID == client.ID).ToList();
            IncomingMeetingsContainer.Items.Clear();
            foreach (var m in data) {
                IncomingMeetingsContainer.Items.Add($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        public void showOutgoingMeetings() {
            var data = database.getMeetings().Where(m=>m.Sender.ID==client.ID).ToList();
            OutgoingMeetingsContainer.Items.Clear();
            foreach (var m in data) {
                OutgoingMeetingsContainer.Items.Add($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        public void showAvailableEstates() {
            var data = database.getEstates().Where(e=>e.Owner.ID!=client.ID).ToList();
            AvailableEstatesContainer.Items.Clear();
            foreach (var e in data) {
                AvailableEstatesContainer.Items.Add($"{e.ID}. {e.Title} of kind {e.Kind} price {e.Price} owned by {e.Owner.Name}");
            }
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
        private void BuyEstateButton_Click(object sender, RoutedEventArgs e) {
            if (AvailableEstatesContainer.SelectedIndex<0) { return; }
            string id = AvailableEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));
            if (client.Balance < estate.Price) {
                MessageBox.Show("Not enough money");
                return;
            }
            estate.Owner = client;
            client.Balance -= estate.Price;
            database.updateEstate(estate);
            showAvailableEstates();
        }
        private void AeSellButton_Click(object sender, RoutedEventArgs e) {
            var title = AeTitleInput.Text;
            var priceInput = AePriceInput.Text;
            int price;
            var kind = AeKindInput.Text;

            try {
                price = int.Parse(priceInput);
            } catch {
                MessageBox.Show("Incorrect price, please enter a number");
                return;
            }
            if (kind==EstateKind.New && client.Admin == 0) {
                MessageBox.Show($"Estate of kind {EstateKind.New} may be added only by managers");
                return;
            }
            MessageBox.Show($"title {title} price {price} kind {kind}");
            database.createEstate(title, kind, client, price);
            showAvailableEstates();
        }
        private void OwnedEstatesContainer_SelectionChanged(object sender, SelectionChangedEventArgs e) {
            if (OwnedEstatesContainer.SelectedIndex<0) { return; }
            string id = OwnedEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            OeTitleInput.Text = estate.Title;
            OeKindInput.Text = estate.Kind;
            OePriceInput.Text = estate.Price.ToString();
        }
        private void OeEditButton_Click(object sender, RoutedEventArgs e) {
            var title = OeTitleInput.Text;
            var kind = OeKindInput.Text;
            var priceInput = OePriceInput.Text;
            int price;
            try {
                price = int.Parse(priceInput);
            } catch {
                MessageBox.Show("Incorrect price, please enter a number");
                return;
            }
            if (OwnedEstatesContainer.SelectedIndex < 0) { return; }
            string id = OwnedEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            estate.Title = title;
            estate.Price = price;
            estate.Kind = kind;
            database.updateEstate(estate);
            showOwnedEstates();
        }
    }
}
