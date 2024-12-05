using System.ComponentModel;
using System.Windows.Input;
using System.Windows.Navigation;

namespace seven.ViewModels {
    public class LoginViewModel : ViewModelBase {
        private string _userName;
        public string userName{
            get => _userName;
            set => SetProperty(ref _userName, value);
        }
    }
}
