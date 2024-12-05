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
            viewModel.userName = "";
            DataContext = viewModel;
            InitializeComponent();
            UserNameInput.Focus();
            viewModel.userName = "admin";
        }
        private void Button_Click(object sender, RoutedEventArgs e){
            var userName = UserNameInput.Text;
            this.NavigationService.Navigate(new ProfileView(userName));
        }
    }
}
