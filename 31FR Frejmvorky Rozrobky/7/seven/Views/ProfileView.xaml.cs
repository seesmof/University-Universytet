using System;
using System.Linq;
using System.Windows;
using MySql.Data.MySqlClient;
using System.Windows.Controls;
using seven.ViewModels;

namespace seven {
    /// <summary>
    /// Interaction logic for ProfileView.xaml
    /// </summary>
    public partial class ProfileView : Page
    {
        ProfileViewModel viewModel = new ProfileViewModel();
        public ProfileView(string userName){
            DataContext = viewModel;
            InitializeComponent();
            viewModel.userName = userName;
            viewModel.setClient();
        }
        public void homeTabOpened(object sender, RoutedEventArgs e){
            viewModel.setClient();
        }
        public void ownedEstatesTabOpened(object sender, RoutedEventArgs e){
            viewModel.setOwnedEstates();
            viewModel.selectedOwnedEstate = null;
        }
        public void availableEstatesTabOpened(object sender, RoutedEventArgs e){
            viewModel.setAvailableEstates();
            viewModel.newEstate = new Estate();
        }
        public void incomingMeetingsTabOpened(object sender, RoutedEventArgs e){
            //showIncomingMeetings();
        }
        public void outgoingMeetingsTabOpened(object sender, RoutedEventArgs e){
            //showOutgoingMeetings();
        }
        private void ownedEstatesGrid_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (ownedEstatesGrid.SelectedIndex < 0) { return; }
            try{
                viewModel.selectedOwnedEstate = viewModel.ownedEstates[ownedEstatesGrid.SelectedIndex];
            } catch { return; }
        }
        private void availableEstatesGrid_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (availableEstatesGrid.SelectedIndex < 0) { return; }
            try{
                viewModel.selectedAvailableEstate = viewModel.availableEstates[availableEstatesGrid.SelectedIndex];
            } catch { return; }
        }
    }
}
