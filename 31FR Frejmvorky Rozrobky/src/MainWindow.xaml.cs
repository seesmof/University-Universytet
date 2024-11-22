using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace src
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public Database databaseConnection;
        public string userName;
        public string password;
        public string host;
        public string port;
        public string databaseName;

        public MainWindow()
        {
            InitializeComponent();

            userName = "root";
            password = "1313";
            host = "localhost";
            port = "3306";
            databaseName = "fr_data";

            User_Name.Text = userName;
            Password.Text = password;
            Host.Text = host;
            Port.Text = port;
            Database_Name.Text = databaseName;
        }

        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            databaseConnection=new Database(userName,password,host,port,databaseName);
            Result.Text = databaseConnection.connection.ToString();
        }
    }
}
