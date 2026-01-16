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
            buyerNameLabel = new Label();
            buyerNameTextBox = new TextBox();
            passwordLabel = new Label();
            passwordTextBox = new TextBox();
            loginButton = new Button();
            signUpButton = new Button();
            passwordConfirmLabel = new Label();
            passwordConfirmTextBox = new TextBox();
            adminCheckBox = new CheckBox();
            SuspendLayout();
            // 
            // buyerNameLabel
            // 
            buyerNameLabel.AutoSize = true;
            buyerNameLabel.Location = new Point(12, 9);
            buyerNameLabel.Name = "buyerNameLabel";
            buyerNameLabel.Size = new Size(91, 25);
            buyerNameLabel.TabIndex = 0;
            buyerNameLabel.Text = "Username";
            buyerNameLabel.Click += buyerNameLabel_Click;
            // 
            // buyerNameTextBox
            // 
            buyerNameTextBox.Location = new Point(12, 37);
            buyerNameTextBox.Name = "buyerNameTextBox";
            buyerNameTextBox.PlaceholderText = "Your buyername here...";
            buyerNameTextBox.Size = new Size(289, 31);
            buyerNameTextBox.TabIndex = 0;
            buyerNameTextBox.TextChanged += buyerNameTextBox_TextChanged;
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
            passwordTextBox.TabIndex = 1;
            passwordTextBox.TextChanged += passwordTextBox_TextChanged;
            // 
            // loginButton
            // 
            loginButton.Location = new Point(12, 285);
            loginButton.Name = "loginButton";
            loginButton.Size = new Size(105, 34);
            loginButton.TabIndex = 5;
            loginButton.Text = "Login";
            loginButton.UseVisualStyleBackColor = true;
            loginButton.Click += loginButton_Click;
            // 
            // signUpButton
            // 
            signUpButton.Location = new Point(123, 285);
            signUpButton.Name = "signUpButton";
            signUpButton.Size = new Size(178, 34);
            signUpButton.TabIndex = 4;
            signUpButton.Text = "Sign Up";
            signUpButton.UseVisualStyleBackColor = true;
            signUpButton.Click += signUpButton_Click;
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
            passwordConfirmTextBox.TabIndex = 2;
            passwordConfirmTextBox.TextChanged += passwordConfirmTextBox_TextChanged;
            // 
            // adminCheckBox
            // 
            adminCheckBox.AutoSize = true;
            adminCheckBox.Location = new Point(12, 239);
            adminCheckBox.Name = "adminCheckBox";
            adminCheckBox.Size = new Size(114, 29);
            adminCheckBox.TabIndex = 3;
            adminCheckBox.Text = "Is admin?";
            adminCheckBox.UseVisualStyleBackColor = true;
            adminCheckBox.CheckedChanged += adminCheckBox_CheckedChanged;
            // 
            // SignUpForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(316, 341);
            Controls.Add(adminCheckBox);
            Controls.Add(passwordConfirmTextBox);
            Controls.Add(passwordConfirmLabel);
            Controls.Add(signUpButton);
            Controls.Add(loginButton);
            Controls.Add(passwordTextBox);
            Controls.Add(passwordLabel);
            Controls.Add(buyerNameTextBox);
            Controls.Add(buyerNameLabel);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Name = "SignUpForm";
            Text = "Sign Up";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label buyerNameLabel;
        private TextBox buyerNameTextBox;
        private Label passwordLabel;
        private TextBox passwordTextBox;
        private Button loginButton;
        private Button signUpButton;
        private Label passwordConfirmLabel;
        private TextBox passwordConfirmTextBox;
        private CheckBox adminCheckBox;
    }
}