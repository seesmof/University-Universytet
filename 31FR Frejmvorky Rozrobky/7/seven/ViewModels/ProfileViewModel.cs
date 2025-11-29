using MySql.Data.MySqlClient;
using System.Collections.ObjectModel;
using System.Linq;
using System.Windows;
using System.Windows.Input;

namespace seven.ViewModels{
    public class ProfileViewModel : ViewModelBase{
        // SYSTEM
        private MySqlConnection connection = new MySqlConnection(UtilityVariables.connectionString);
        private Database database;

        public void setClient(string userName){
            User found = database.getUsers().Where(u => u.Name == userName).ToList().ElementAtOrDefault(0);
            if (found != null){
                client = found;
            } else {
                client = database.createUser(userName);
            }
        }
        public void setOwnedEstates(){
            ownedEstates = new ObservableCollection<Estate>(database.getEstates().Where(e => e.Owner.ID == client.ID));
        }
        public void setAvailableEstates(){
            availableEstates = new ObservableCollection<Estate>(database.getEstates().Where(e => e.Owner.ID != client.ID));
        }
        public void setIncomingMeetings(){
            incomingMeetings = new ObservableCollection<Meeting>(database.getMeetings().Where(m => m.Target.Owner.ID == client.ID).OrderBy(m => m.ID).Reverse());
        }
        public void setOutgoingMeetings(){
            outgoingMeetings = new ObservableCollection<Meeting>(database.getMeetings().Where(m=>m.Sender.ID==client.ID).OrderBy(m => m.ID).Reverse());
        }

        // VARIABLES
        private User _client;
        public User client{
            get => _client;
            set => SetProperty(ref _client, value);
        }

        private ObservableCollection<Estate> _ownedEstates;
        public ObservableCollection<Estate> ownedEstates{
            get => _ownedEstates;
            set => SetProperty(ref _ownedEstates, value);
        }

        private Estate _selectedOwnedEstate;
        public Estate selectedOwnedEstate{
            get => _selectedOwnedEstate;
            set => SetProperty(ref _selectedOwnedEstate, value);
        }

        private ObservableCollection<Estate> _availableEstates;
        public ObservableCollection<Estate> availableEstates{
            get => _availableEstates;
            set => SetProperty(ref _availableEstates, value);
        }

        private Estate _selectedAvailableEstate;
        public Estate selectedAvailableEstate{
            get => _selectedAvailableEstate;
            set => SetProperty(ref _selectedAvailableEstate, value);
        }

        private Estate _newEstate;
        public Estate newEstate{
            get => _newEstate;
            set => SetProperty(ref _newEstate, value);
        }

        private ObservableCollection<Meeting> _incomingMeetings;
        public ObservableCollection<Meeting> incomingMeetings{
            get => _incomingMeetings;
            set => SetProperty(ref _incomingMeetings, value);
        }

        private Meeting _selectedIncomingMeeting;
        public Meeting selectedIncomingMeeting{
            get => _selectedIncomingMeeting;
            set => SetProperty(ref _selectedIncomingMeeting, value);
        }

        private bool _onlyPendingMeetings;
        public bool onlyPendingMeetings{
            get => _onlyPendingMeetings;
            set => SetProperty(ref _onlyPendingMeetings, value);
        }

        private ObservableCollection<Meeting> _outgoingMeetings;
        public ObservableCollection<Meeting> outgoingMeetings{
            get => _outgoingMeetings;
            set => SetProperty(ref _outgoingMeetings, value);
        }

        private Meeting _selectedOutgoingMeeting;
        public Meeting selectedOutgoingMeeting{
            get => _selectedOutgoingMeeting;
            set => SetProperty(ref _selectedOutgoingMeeting, value);
        }

        // FUNCTIONS (COMMANDS)
        private void _updateUser(object p){
            database.updateUser(client);
            client = database.getUser(client.ID);
        }

        private DelegateCommand _userStatusCommand;
        public ICommand userStatusCommand => _userStatusCommand;

        private DelegateCommand _userNameCommand;
        public ICommand userNameCommand => _userNameCommand;

        private DelegateCommand _userBalanceCommand;
        public ICommand userBalanceCommand => _userBalanceCommand;

        private DelegateCommand _updateEstateCommand;
        private void _updateEstate(object p){
            database.updateEstate(selectedOwnedEstate);
        }
        public ICommand updateEstateCommand => _updateEstateCommand;

        private DelegateCommand _newEstateCommand;
        private void _addEstate(object p){
            if (newEstate.Kind==EstateKind.New && client.Admin==0){
                MessageBox.Show("Can only add new buildings by managers");
                return;
            }
            database.createEstate(newEstate.Title, newEstate.Kind,client, newEstate.Price);
            newEstate = new Estate();
        }
        public ICommand newEstateCommand => _newEstateCommand;

        private DelegateCommand _buyEstateCommand;
        private void _buyEstate(object p){
            if (client.Balance < selectedAvailableEstate.Price){
                MessageBox.Show("Not enough money");
                return;
            }
            selectedAvailableEstate.Owner = client;
            client.Balance -= selectedAvailableEstate.Price;
            database.updateEstate(selectedAvailableEstate);
            setAvailableEstates();
        }
        public ICommand buyEstateCommand => _buyEstateCommand;

        private DelegateCommand _viewEstateCommand;
        private void _viewEstate(object p){
            database.createMeeting(client, selectedAvailableEstate);
            MessageBox.Show("Meeting scheduled");
        }
        public ICommand viewEstateCommand => _viewEstateCommand;

        private DelegateCommand _processMeetingCommand;
        private void _processMeeting(object p){
            database.updateMeeting(selectedIncomingMeeting);
            setIncomingMeetings();
        }
        public ICommand processMeetingCommand => _processMeetingCommand;

        private DelegateCommand _pendingMeetingsCommand;
        private void _showOnlyPendingMeetings(object p){
            if (onlyPendingMeetings) { 
                incomingMeetings = new ObservableCollection<Meeting>(database.getMeetings().Where(m => m.Status == MeetingStatus.Wait && m.Score == "Unrated" && m.Target.Owner.ID == client.ID)); 
            } else {
                setIncomingMeetings();
            }
        }
        public ICommand pendingMeetingsCommand => _pendingMeetingsCommand;

        private DelegateCommand _rateMeetingCommand;
        private void _rateMeeting(object p){
            database.updateMeeting(selectedOutgoingMeeting);
            setOutgoingMeetings();
        }
        public ICommand rateMeetingCommand => _rateMeetingCommand;

        public ProfileViewModel(){
            connection.Open();
            database = new Database(connection);
            _userStatusCommand = new DelegateCommand(_updateUser);
            _userNameCommand = new DelegateCommand(_updateUser);
            _userBalanceCommand = new DelegateCommand(_updateUser);
            _updateEstateCommand = new DelegateCommand(_updateEstate);
            _newEstateCommand = new DelegateCommand(_addEstate);
            _buyEstateCommand = new DelegateCommand(_buyEstate);
            _processMeetingCommand = new DelegateCommand(_processMeeting);
            _pendingMeetingsCommand = new DelegateCommand(_showOnlyPendingMeetings);
            _rateMeetingCommand = new DelegateCommand(_rateMeeting);
            _viewEstateCommand = new DelegateCommand(_viewEstate);
        }
    }
}
