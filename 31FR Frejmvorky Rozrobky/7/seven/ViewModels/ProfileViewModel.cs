using MySql.Data.MySqlClient;
using System;
using System.Linq;
using System.Windows;
using System.Windows.Input;

namespace seven.ViewModels{
    public class ProfileViewModel : ViewModelBase{
        private string _userName;
        private User _client;
        private bool _clientStatus;

        public string userName{
            get => _userName;
            set => SetProperty(ref _userName, value);
        }
        public User client{
            get => _client;
            set => SetProperty(ref _client, value);
        }

        public MySqlConnection connection = new MySqlConnection(UtilityVariables.connectionString);
        public Database database;

        public ProfileViewModel(){
            connection.Open();
            database = new Database(connection);
        }
        public void setClient(){
            User found = database.getUsers().Where(u => u.Name == userName).ToList().ElementAtOrDefault(0);
            if (found != null){
                client = found;
            } else {
                client = database.createUser(userName);
            }
        }
    }
}
