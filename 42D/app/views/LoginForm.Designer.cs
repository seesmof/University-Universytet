namespace app
{
    partial class LoginForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            signUpLinkButton = new Button();
            buyerNameLabel = new Label();
            buyerNameTextBox = new TextBox();
            passwordLabel = new Label();
            passwordTextBox = new TextBox();
            loginButton = new Button();
            SuspendLayout();
            // 
            // signUpLinkButton
            // 
            signUpLinkButton.Location = new Point(12, 164);
            signUpLinkButton.Name = "signUpLinkButton";
            signUpLinkButton.Size = new Size(124, 34);
            signUpLinkButton.TabIndex = 3;
            signUpLinkButton.Text = "Sign Up";
            signUpLinkButton.UseVisualStyleBackColor = true;
            signUpLinkButton.Click += signUpLinkButton_Click;
            // 
            // buyerNameLabel
            // 
            buyerNameLabel.AutoSize = true;
            buyerNameLabel.Location = new Point(12, 9);
            buyerNameLabel.Name = "buyerNameLabel";
            buyerNameLabel.Size = new Size(91, 25);
            buyerNameLabel.TabIndex = 1;
            buyerNameLabel.Text = "Buyersname";
            buyerNameLabel.Click += buyerNameLabel_Click;
            // 
            // buyerNameTextBox
            // 
            buyerNameTextBox.Location = new Point(12, 37);
            buyerNameTextBox.Name = "buyerNameTextBox";
            buyerNameTextBox.PlaceholderText = "Your buyername here...";
            buyerNameTextBox.Size = new Size(297, 31);
            buyerNameTextBox.TabIndex = 0;
            buyerNameTextBox.TextChanged += buyerNameTextBox_TextChanged;
            // 
            // passwordLabel
            // 
            passwordLabel.AutoSize = true;
            passwordLabel.Location = new Point(12, 85);
            passwordLabel.Name = "passwordLabel";
            passwordLabel.Size = new Size(87, 25);
            passwordLabel.TabIndex = 3;
            passwordLabel.Text = "Password";
            passwordLabel.Click += passwordLabel_Click;
            // 
            // passwordTextBox
            // 
            passwordTextBox.Location = new Point(12, 113);
            passwordTextBox.Name = "passwordTextBox";
            passwordTextBox.PasswordChar = '*';
            passwordTextBox.PlaceholderText = "Your password here...";
            passwordTextBox.Size = new Size(297, 31);
            passwordTextBox.TabIndex = 1;
            passwordTextBox.TextChanged += passwordTextBox_TextChanged;
            // 
            // loginButton
            // 
            loginButton.Location = new Point(142, 164);
            loginButton.Name = "loginButton";
            loginButton.Size = new Size(167, 34);
            loginButton.TabIndex = 2;
            loginButton.Text = "Log In";
            loginButton.UseVisualStyleBackColor = true;
            loginButton.Click += loginButton_Click;
            // 
            // LoginForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(321, 220);
            Controls.Add(loginButton);
            Controls.Add(passwordTextBox);
            Controls.Add(passwordLabel);
            Controls.Add(buyerNameTextBox);
            Controls.Add(buyerNameLabel);
            Controls.Add(signUpLinkButton);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Name = "LoginForm";
            Text = "Login";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button signUpLinkButton;
        private Label buyerNameLabel;
        private TextBox buyerNameTextBox;
        private Label passwordLabel;
        private TextBox passwordTextBox;
        private Button loginButton;
    }
}