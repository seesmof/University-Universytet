using app.models;

namespace app
{
    public partial class MainWindow : Form
    {
        private Buyer buyer;

        public MainWindow()
        {
            InitializeComponent();
        }

        public MainWindow(Buyer givenBuyer)
        {
            this.buyer = givenBuyer;
            InitializeComponent();
            setBuyersNameInGreeting();
            hideUsersButton();
        }

        private void hideUsersButton()
        {
            if (buyer != null && buyer.IsAdmin)
            {
                usersButton.Hide();
            }
        }

        private void setBuyersNameInGreeting()
        {
            if (buyer == null)
            {
                return;
            }

            const string buyerTemplatePlace = "buyer";
            buyerWelcomeLabel.Text = buyerWelcomeLabel.Text.Replace(buyerTemplatePlace, buyer.Name);
        }

        private void logOutButton_Click(object sender, EventArgs e)
        {
            if (buyer != null)
            {
                LoginForm loginForm = new LoginForm();
                loginForm.Show();
                this.Hide();
            }
        }

        private void usersButton_Click(object sender, EventArgs e)
        {

        }
    }
}
