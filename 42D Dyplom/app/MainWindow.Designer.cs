namespace app
{
    partial class MainWindow
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindow));
            splitContainer1 = new SplitContainer();
            storeButton = new Button();
            ownedButton = new Button();
            logOutButton = new Button();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.SuspendLayout();
            SuspendLayout();
            // 
            // splitContainer1
            // 
            splitContainer1.Dock = DockStyle.Fill;
            splitContainer1.Location = new Point(0, 0);
            splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.Controls.Add(logOutButton);
            splitContainer1.Panel1.Controls.Add(ownedButton);
            splitContainer1.Panel1.Controls.Add(storeButton);
            splitContainer1.Size = new Size(778, 544);
            splitContainer1.SplitterDistance = 214;
            splitContainer1.TabIndex = 0;
            // 
            // storeButton
            // 
            storeButton.Location = new Point(12, 12);
            storeButton.Name = "storeButton";
            storeButton.Size = new Size(199, 70);
            storeButton.TabIndex = 0;
            storeButton.Text = "Store";
            storeButton.UseVisualStyleBackColor = true;
            // 
            // ownedButton
            // 
            ownedButton.Location = new Point(12, 88);
            ownedButton.Name = "ownedButton";
            ownedButton.Size = new Size(199, 70);
            ownedButton.TabIndex = 1;
            ownedButton.Text = "Owned";
            ownedButton.UseVisualStyleBackColor = true;
            // 
            // logOutButton
            // 
            logOutButton.Location = new Point(12, 462);
            logOutButton.Name = "logOutButton";
            logOutButton.Size = new Size(199, 70);
            logOutButton.TabIndex = 2;
            logOutButton.Text = "Log Out";
            logOutButton.UseVisualStyleBackColor = true;
            // 
            // MainWindow
            // 
            AutoScaleDimensions = new SizeF(144F, 144F);
            AutoScaleMode = AutoScaleMode.Dpi;
            ClientSize = new Size(778, 544);
            Controls.Add(splitContainer1);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Icon = (Icon)resources.GetObject("$this.Icon");
            Name = "MainWindow";
            Text = "Trucks Store";
            splitContainer1.Panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer splitContainer1;
        private Button storeButton;
        private Button ownedButton;
        private Button logOutButton;
    }
}
