namespace dev
{
    partial class menu
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
            this.signoutButton = new System.Windows.Forms.Button();
            this.flightsButton = new System.Windows.Forms.Button();
            this.ticketsButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // signoutButton
            // 
            this.signoutButton.Location = new System.Drawing.Point(12, 128);
            this.signoutButton.Name = "signoutButton";
            this.signoutButton.Size = new System.Drawing.Size(370, 49);
            this.signoutButton.TabIndex = 0;
            this.signoutButton.Text = "Sign Out";
            this.signoutButton.UseVisualStyleBackColor = true;
            this.signoutButton.Click += new System.EventHandler(this.signoutButton_Click);
            // 
            // flightsButton
            // 
            this.flightsButton.Location = new System.Drawing.Point(12, 12);
            this.flightsButton.Name = "flightsButton";
            this.flightsButton.Size = new System.Drawing.Size(370, 53);
            this.flightsButton.TabIndex = 1;
            this.flightsButton.Text = "Available Flights";
            this.flightsButton.UseVisualStyleBackColor = true;
            this.flightsButton.Click += new System.EventHandler(this.flightsButton_Click);
            // 
            // ticketsButton
            // 
            this.ticketsButton.Location = new System.Drawing.Point(12, 71);
            this.ticketsButton.Name = "ticketsButton";
            this.ticketsButton.Size = new System.Drawing.Size(370, 51);
            this.ticketsButton.TabIndex = 2;
            this.ticketsButton.Text = "Tickets";
            this.ticketsButton.UseVisualStyleBackColor = true;
            this.ticketsButton.Click += new System.EventHandler(this.ticketsButton_Click);
            // 
            // menu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(394, 193);
            this.Controls.Add(this.ticketsButton);
            this.Controls.Add(this.flightsButton);
            this.Controls.Add(this.signoutButton);
            this.Name = "menu";
            this.Text = "menu";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button signoutButton;
        private System.Windows.Forms.Button flightsButton;
        private System.Windows.Forms.Button ticketsButton;
    }
}