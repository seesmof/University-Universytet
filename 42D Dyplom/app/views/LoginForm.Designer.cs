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
            userNameLabel = new Label();
            userNameTextBox = new TextBox();
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
            signUpLinkButton.TabIndex = 0;
            signUpLinkButton.Text = "Sign Up";
            signUpLinkButton.UseVisualStyleBackColor = true;
            signUpLinkButton.Click += signUpLinkButton_Click;
            // 
            // userNameLabel
            // 
            userNameLabel.AutoSize = true;
            userNameLabel.Location = new Point(12, 9);
            userNameLabel.Name = "userNameLabel";
            userNameLabel.Size = new Size(91, 25);
            userNameLabel.TabIndex = 1;
            userNameLabel.Text = "Username";
            userNameLabel.Click += userNameLabel_Click;
            // 
            // userNameTextBox
            // 
            userNameTextBox.Location = new Point(12, 37);
            userNameTextBox.Name = "userNameTextBox";
            userNameTextBox.PlaceholderText = "Your username here...";
            userNameTextBox.Size = new Size(297, 31);
            userNameTextBox.TabIndex = 2;
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
            passwordTextBox.TabIndex = 4;
            // 
            // loginButton
            // 
            loginButton.Location = new Point(142, 164);
            loginButton.Name = "loginButton";
            loginButton.Size = new Size(167, 34);
            loginButton.TabIndex = 5;
            loginButton.Text = "Log In";
            loginButton.UseVisualStyleBackColor = true;
            // 
            // LoginForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(321, 220);
            Controls.Add(loginButton);
            Controls.Add(passwordTextBox);
            Controls.Add(passwordLabel);
            Controls.Add(userNameTextBox);
            Controls.Add(userNameLabel);
            Controls.Add(signUpLinkButton);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Name = "LoginForm";
            Text = "Login";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button signUpLinkButton;
        private Label userNameLabel;
        private TextBox userNameTextBox;
        private Label passwordLabel;
        private TextBox passwordTextBox;
        private Button loginButton;
    }
}