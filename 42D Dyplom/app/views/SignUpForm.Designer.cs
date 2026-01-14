namespace app
{
    partial class SignUpForm
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
            userNameLabel = new Label();
            userNameTextBox = new TextBox();
            passwordLabel = new Label();
            passwordTextBox = new TextBox();
            loginButton = new Button();
            signUpButton = new Button();
            passwordConfirmLabel = new Label();
            passwordConfirmTextBox = new TextBox();
            SuspendLayout();
            // 
            // userNameLabel
            // 
            userNameLabel.AutoSize = true;
            userNameLabel.Location = new Point(12, 9);
            userNameLabel.Name = "userNameLabel";
            userNameLabel.Size = new Size(91, 25);
            userNameLabel.TabIndex = 0;
            userNameLabel.Text = "Username";
            userNameLabel.Click += userNameLabel_Click;
            // 
            // userNameTextBox
            // 
            userNameTextBox.Location = new Point(12, 37);
            userNameTextBox.Name = "userNameTextBox";
            userNameTextBox.PlaceholderText = "Your username here...";
            userNameTextBox.Size = new Size(289, 31);
            userNameTextBox.TabIndex = 1;
            // 
            // passwordLabel
            // 
            passwordLabel.AutoSize = true;
            passwordLabel.Location = new Point(12, 84);
            passwordLabel.Name = "passwordLabel";
            passwordLabel.Size = new Size(87, 25);
            passwordLabel.TabIndex = 2;
            passwordLabel.Text = "Password";
            passwordLabel.Click += passwordLabel_Click;
            // 
            // passwordTextBox
            // 
            passwordTextBox.Location = new Point(12, 112);
            passwordTextBox.Name = "passwordTextBox";
            passwordTextBox.PasswordChar = '*';
            passwordTextBox.PlaceholderText = "Your password here...";
            passwordTextBox.Size = new Size(289, 31);
            passwordTextBox.TabIndex = 3;
            // 
            // loginButton
            // 
            loginButton.Location = new Point(12, 245);
            loginButton.Name = "loginButton";
            loginButton.Size = new Size(105, 34);
            loginButton.TabIndex = 4;
            loginButton.Text = "Login";
            loginButton.UseVisualStyleBackColor = true;
            loginButton.Click += loginButton_Click;
            // 
            // signUpButton
            // 
            signUpButton.Location = new Point(123, 245);
            signUpButton.Name = "signUpButton";
            signUpButton.Size = new Size(178, 34);
            signUpButton.TabIndex = 5;
            signUpButton.Text = "Sign Up";
            signUpButton.UseVisualStyleBackColor = true;
            // 
            // passwordConfirmLabel
            // 
            passwordConfirmLabel.AutoSize = true;
            passwordConfirmLabel.Location = new Point(12, 163);
            passwordConfirmLabel.Name = "passwordConfirmLabel";
            passwordConfirmLabel.Size = new Size(184, 25);
            passwordConfirmLabel.TabIndex = 6;
            passwordConfirmLabel.Text = "Password Once Again";
            passwordConfirmLabel.Click += passwordConfirmLabel_Click;
            // 
            // passwordConfirmTextBox
            // 
            passwordConfirmTextBox.Location = new Point(12, 191);
            passwordConfirmTextBox.Name = "passwordConfirmTextBox";
            passwordConfirmTextBox.PasswordChar = '*';
            passwordConfirmTextBox.PlaceholderText = "Your password once again...";
            passwordConfirmTextBox.Size = new Size(289, 31);
            passwordConfirmTextBox.TabIndex = 7;
            // 
            // SignUpForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(316, 308);
            Controls.Add(passwordConfirmTextBox);
            Controls.Add(passwordConfirmLabel);
            Controls.Add(signUpButton);
            Controls.Add(loginButton);
            Controls.Add(passwordTextBox);
            Controls.Add(passwordLabel);
            Controls.Add(userNameTextBox);
            Controls.Add(userNameLabel);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Name = "SignUpForm";
            Text = "Sign Up";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label userNameLabel;
        private TextBox userNameTextBox;
        private Label passwordLabel;
        private TextBox passwordTextBox;
        private Button loginButton;
        private Button signUpButton;
        private Label passwordConfirmLabel;
        private TextBox passwordConfirmTextBox;
    }
}