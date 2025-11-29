namespace seven.ViewModels {
    public class LoginViewModel : ViewModelBase {
        private string _userName;
        public string userName{
            get => _userName;
            set => SetProperty(ref _userName, value);
        }
    }
}
