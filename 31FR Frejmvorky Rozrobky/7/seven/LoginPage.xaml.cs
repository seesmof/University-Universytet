using System.Windows;
using System.Windows.Controls;

namespace seven {
    /// <summary>
    /// Interaction logic for LoginPage.xaml
    /// </summary>
    public partial class LoginPage : Page {
        public LoginPage() {
            InitializeComponent();
            UserNameInput.Focus();
        }
        private void Button_Click(object sender, RoutedEventArgs e) {
            var userName = UserNameInput.Text;
            this.NavigationService.Navigate(new ProfilePage(userName));
        }
    }
}
