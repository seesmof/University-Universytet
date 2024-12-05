using System;
using System.Linq;
using System.Windows;
using MySql.Data.MySqlClient;
using System.Windows.Controls;

namespace seven {
    /// <summary>
    /// Interaction logic for ProfileView.xaml
    /// </summary>
    public partial class ProfileView : Page
    {
        public User client;
        public MySqlConnection connection = new MySqlConnection(UtilityVariables.connectionString);
        public Database database;
        public ProfileView(string userName){
            InitializeComponent();
            connection.Open();
            database = new Database(connection);

            User found=database.getUsers().Where(u => u.Name == userName).ToList().ElementAtOrDefault(0);
            if (found != null){
                client = found;
            } else {
                client = database.createUser(userName);
            }
        }
        public void homeTabOpened(object sender, RoutedEventArgs e){
            showUserData();
        }
        public void ownedEstatesTabOpened(object sender, RoutedEventArgs e){
            showOwnedEstates();
        }
        public void availableEstatesTabOpened(object sender, RoutedEventArgs e){
            showAvailableEstates();
        }
        public void incomingMeetingsTabOpened(object sender, RoutedEventArgs e){
            showIncomingMeetings();
        }
        public void outgoingMeetingsTabOpened(object sender, RoutedEventArgs e){
            showOutgoingMeetings();
        }
        public void showUserData(){
            UserNameBox.Text=client.Name;
            UserBalanceBox.Text= client.Balance.ToString();
            UserStatusToggle.IsChecked=Convert.ToBoolean(client.Admin);
        }
        public void showOwnedEstates(){
            var data = database.getEstates().Where(e => e.Owner.ID == client.ID).ToList();
            OwnedEstatesContainer.Items.Clear();
            foreach (var e in data){
                OwnedEstatesContainer.Items.Add($"{e.ID}. {e.Title} of kind {e.Kind} price {e.Price} owned by {e.Owner.Name}");
            }
            EditTitleInput.Text = "";
            EditKindInput.Text = EstateKind.Home;
            EditPriceInput.Text = "0";
        }
        public void showAvailableEstates(){
            var data = database.getEstates().Where(e=>e.Owner.ID!=client.ID).ToList();
            AvailableEstatesContainer.Items.Clear();
            foreach (var e in data){
                AvailableEstatesContainer.Items.Add($"{e.ID}. {e.Title} of kind {e.Kind} price {e.Price} owned by {e.Owner.Name}");
            }
            SellTitleInput.Text = "";
            SellPriceInput.Text = "0";
            SellKindInput.Text = "Home";
        }
        public void showIncomingMeetings(bool onlyPending=false){
            var data = database.getMeetings().Where(m => m.Target.Owner.ID == client.ID).OrderBy(m=>m.ID).Reverse().ToList();
            if (onlyPending) { data = data.Where(m => m.Status == MeetingStatus.Wait && m.Score == "Unrated").ToList(); }
            IncomingMeetingsContainer.Items.Clear();
            foreach (var m in data){
                IncomingMeetingsContainer.Items.Add($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        public void showOutgoingMeetings(){
            var data = database.getMeetings().Where(m=>m.Sender.ID==client.ID).OrderBy(m => m.ID).Reverse().ToList();
            OutgoingMeetingsContainer.Items.Clear();
            foreach (var m in data){
                OutgoingMeetingsContainer.Items.Add($"{m.ID}. For {m.Target.Title} by {m.Sender.Name} to {m.Target.Owner.Name} rated {m.Score} status {m.Status}");
            }
        }
        private void ChangeNameButton_Click(object sender, RoutedEventArgs e){
            var name = UserNameBox.Text;
            client.Name = name;
            database.updateUser(client);

            client = database.getUser(client.ID);
            showUserData();
        }
        private void ChangeBalanceButton_Click(object sender, RoutedEventArgs e){
            int balance=client.Balance;
            try {
                balance = Convert.ToInt32(UserBalanceBox.Text);
            } catch { MessageBox.Show("Wrong balance. Please enter a number"); }

            client.Balance = balance;
            database.updateUser(client);

            client = database.getUser(client.ID);
            showUserData();
        }
        private void UserStatusToggle_Click(object sender, RoutedEventArgs e){
            var status = UserStatusToggle.IsChecked;
            client.Admin = Convert.ToInt32(status);
            database.updateUser(client);

            client = database.getUser(client.ID);
            showUserData();
        }
        private void BuyEstateButton_Click(object sender, RoutedEventArgs e){
            if (AvailableEstatesContainer.SelectedIndex<0){ return; }
            string id = AvailableEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            if (client.Balance < estate.Price){
                MessageBox.Show("Not enough money");
                return;
            }
            estate.Owner = client;
            client.Balance -= estate.Price;

            database.updateEstate(estate);
            showAvailableEstates();
        }
        private void SetMeetingButton_Click(object sender, RoutedEventArgs e){
            if (AvailableEstatesContainer.SelectedIndex < 0){ return; }
            string id = AvailableEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            database.createMeeting(client, estate);
            showOutgoingMeetings();
        }
        private void AeSellButton_Click(object sender, RoutedEventArgs e){
            var title = SellTitleInput.Text;
            var priceInput = SellPriceInput.Text;
            int price;
            var kind = SellKindInput.Text;
            try {
                price = int.Parse(priceInput);
            } catch {
                MessageBox.Show("Incorrect price, please enter a number");
                return;
            }
            if (kind==EstateKind.New && client.Admin == 0){
                MessageBox.Show($"Estate of kind {EstateKind.New} may be added only by managers");
                return;
            }

            database.createEstate(title, kind, client, price);
            showAvailableEstates();
        }
        private void OwnedEstatesContainer_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (OwnedEstatesContainer.SelectedIndex<0){ return; }
            string id = OwnedEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            EditTitleInput.Text = estate.Title;
            EditKindInput.Text = estate.Kind;
            EditPriceInput.Text = estate.Price.ToString();
        }
        private void OeEditButton_Click(object sender, RoutedEventArgs e){
            if (OwnedEstatesContainer.SelectedIndex < 0){ return; }
            string id = OwnedEstatesContainer.SelectedValue.ToString().Split('.')[0];
            var estate = database.getEstate(int.Parse(id));

            var title = EditTitleInput.Text;
            var kind = EditKindInput.Text;
            var priceInput = EditPriceInput.Text;
            int price;
            try {
                price = int.Parse(priceInput);
            } catch {
                MessageBox.Show("Incorrect price, please enter a number");
                return;
            }
            estate.Title = title;
            estate.Price = price;
            estate.Kind = kind;
            
            database.updateEstate(estate);
            showOwnedEstates();
        }
        private void ProcessButton_Click(object sender, RoutedEventArgs e){
            if (IncomingMeetingsContainer.SelectedIndex < 0){ return; }
            string id = IncomingMeetingsContainer.SelectedValue.ToString().Split('.')[0];
            var meeting = database.getMeeting(int.Parse(id));

            var status = ProcessInput.Text;
            meeting.Status = status;

            database.updateMeeting(meeting);
            showIncomingMeetings();
        }
        private void RateButton_Click(object sender, RoutedEventArgs e){
            if (OutgoingMeetingsContainer.SelectedIndex < 0){ return; }
            string id = OutgoingMeetingsContainer.SelectedValue.ToString().Split('.')[0];
            var meeting = database.getMeeting(int.Parse(id));

            var score = RateInput.Text;
            meeting.Score = score;

            database.updateMeeting(meeting);
            showOutgoingMeetings();
        }
        private void IncomingMeetingsContainer_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (IncomingMeetingsContainer.SelectedIndex < 0){ return; }
            string id = IncomingMeetingsContainer.SelectedValue.ToString().Split('.')[0];
            var meeting = database.getMeeting(int.Parse(id));

            ProcessInput.Text = meeting.Status;
        }
        private void OutgoingMeetingsContainer_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (OutgoingMeetingsContainer.SelectedIndex < 0){ return; }
            string id = OutgoingMeetingsContainer.SelectedValue.ToString().Split('.')[0];
            var meeting = database.getMeeting(int.Parse(id));

            RateInput.Text = meeting.Score;
        }
        private void CheckBox_Click(object sender, RoutedEventArgs e) {
            var status = Convert.ToBoolean(pendingMeetingsToggle.IsChecked);
            showIncomingMeetings(status);
        }
    }
}
