using seven.ViewModels;
using System.Windows;
using System.Windows.Controls;

namespace seven {
    /// <summary>
    /// Interaction logic for LoginView.xaml
    /// </summary>
    public partial class LoginView : Page {
        public LoginViewModel viewModel = new LoginViewModel();
        public LoginView(){
            DataContext = viewModel;
            InitializeComponent();
            UserNameInput.Focus();
        }
        private void LoginButton_Click(object sender, RoutedEventArgs e){
            NavigationService.Navigate(new ProfileView(viewModel.userName));
        }
    }
}
