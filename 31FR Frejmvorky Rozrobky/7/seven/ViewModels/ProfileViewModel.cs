using MySql.Data.MySqlClient;
using System;
using System.Collections.ObjectModel;
using System.Linq;
using System.Windows;
using System.Windows.Input;

namespace seven.ViewModels{
    public class ProfileViewModel : ViewModelBase{
        private string _userName;
        public string userName{
            get => _userName;
            set => SetProperty(ref _userName, value);
        }

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

        private ObservableCollection<Estate> _availableEstates;
        public ObservableCollection<Estate> availableEstates{
            get => _availableEstates;
            set => SetProperty(ref _availableEstates, value);
        }

        private Estate _selectedOwnedEstate;
        public Estate selectedOwnedEstate{
            get => _selectedOwnedEstate;
            set => SetProperty(ref _selectedOwnedEstate, value);
        }

        private Estate _newEstate;
        public Estate newEstate{
            get => _newEstate;
            set => SetProperty(ref _newEstate, value);
        }

        private Estate _selectedAvailableEstate;
        public Estate selectedAvailableEstate{
            get => _selectedAvailableEstate;
            set => SetProperty(ref _selectedAvailableEstate, value);
        }

        private MySqlConnection connection = new MySqlConnection(UtilityVariables.connectionString);
        private Database database;

        public void setClient(){
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
        private void _updateUser(){
            database.updateUser(client);
            client = database.getUser(client.ID);
        }

        private DelegateCommand _userStatusCommand;
        private void _updateUserStatus(object parameters){
            _updateUser();
        }
        public ICommand userStatusCommand => _userStatusCommand;

        private DelegateCommand _userNameCommand;
        private void _updateUserName(object p){
            _updateUser();
        }
        public ICommand userNameCommand => _userNameCommand;

        private DelegateCommand _userBalanceCommand;
        private void _updateUserBalance(object p){
            _updateUser();
        }
        public ICommand userBalanceCommand => _userBalanceCommand;

        private DelegateCommand _selectedOwnedEstateChange;
        private void _updateSelectedOwnedEstate(object p){
            database.updateEstate(selectedOwnedEstate);
        }
        public ICommand selectedOwnedEstateChange => _selectedOwnedEstateChange;

        private DelegateCommand _newEstateCommand;
        private void _addNewEstate(object p){
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

        public ProfileViewModel(){
            connection.Open();
            database = new Database(connection);
            _userStatusCommand = new DelegateCommand(_updateUserStatus);
            _userNameCommand = new DelegateCommand(_updateUserName);
            _userBalanceCommand = new DelegateCommand(_updateUserBalance);
            _selectedOwnedEstateChange = new DelegateCommand(_updateSelectedOwnedEstate);
            _newEstateCommand = new DelegateCommand(_addNewEstate);
            _buyEstateCommand = new DelegateCommand(_buyEstate);
        }
    }
}
