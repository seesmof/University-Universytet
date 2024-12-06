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
        private string givenUserName = "";
        public ProfileView(string userName){
            DataContext = viewModel;
            InitializeComponent();
            givenUserName = userName;
            viewModel.setClient(givenUserName);
        }
        private void homeTabOpened(object sender, RoutedEventArgs e){
            viewModel.setClient(givenUserName);
        }
        private void ownedEstatesTabOpened(object sender, RoutedEventArgs e){
            viewModel.setOwnedEstates();
            viewModel.selectedOwnedEstate = new Estate();
        }
        private void availableEstatesTabOpened(object sender, RoutedEventArgs e){
            viewModel.setAvailableEstates();
            viewModel.newEstate = new Estate();
        }
        private void incomingMeetingsTabOpened(object sender, RoutedEventArgs e){
            viewModel.setIncomingMeetings();
            viewModel.selectedIncomingMeeting = new Meeting();
            viewModel.onlyPendingMeetings = false;
        }
        private void outgoingMeetingsTabOpened(object sender, RoutedEventArgs e){
            viewModel.setOutgoingMeetings();
            viewModel.selectedOutgoingMeeting = new Meeting();
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
        private void incomingMeetingsGrid_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (incomingMeetingsGrid.SelectedIndex < 0) { return; }
            try{
                viewModel.selectedIncomingMeeting = viewModel.incomingMeetings[incomingMeetingsGrid.SelectedIndex];
            } catch { return; }
        }
        private void outgoingMeetingsGrid_SelectionChanged(object sender, SelectionChangedEventArgs e){
            if (outgoingMeetingsGrid.SelectedIndex < 0) { return; }
            try{
                viewModel.selectedOutgoingMeeting = viewModel.outgoingMeetings[outgoingMeetingsGrid.SelectedIndex];
            } catch { return; }
        }
    }
}
