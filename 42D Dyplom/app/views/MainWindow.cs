using app.models;

namespace app
{
    public partial class MainWindow : Form
    {
        Buyer buyer;
        public MainWindow()
        {
            InitializeComponent();
        }

        public MainWindow(Buyer buyer)
        {
            this.buyer = buyer;
            InitializeComponent();
            setUserNameInGreeting();
        }

        private void setUserNameInGreeting()
        {
            if (buyer == null)
            {
                return;
            }

            const string buyerTemplatePlace = "{buyer}";
            buyerWelcomeLabel.Text = buyerWelcomeLabel.Text.Replace(buyerTemplatePlace, buyer.Name);
        }

        private void logOutButton_Click(object sender, EventArgs e)
        {
            if (buyer != null)
            {
                Application.Exit();
            }
        }
    }
}
