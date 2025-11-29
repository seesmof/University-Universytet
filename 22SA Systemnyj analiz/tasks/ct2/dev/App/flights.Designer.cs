namespace App
{
    partial class flights
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
            this.menuButton = new System.Windows.Forms.Button();
            this.selectedLabel = new System.Windows.Forms.Label();
            this.flightsList = new System.Windows.Forms.ListBox();
            this.priceLabel = new System.Windows.Forms.Label();
            this.dateLabel = new System.Windows.Forms.Label();
            this.seatsLabel = new System.Windows.Forms.Label();
            this.seatHeading = new System.Windows.Forms.Label();
            this.infoPanel = new System.Windows.Forms.Panel();
            this.optionsPanel = new System.Windows.Forms.Panel();
            this.windowRadio = new System.Windows.Forms.RadioButton();
            this.bookButton = new System.Windows.Forms.Button();
            this.totalPriceLabel = new System.Windows.Forms.Label();
            this.extrasLabel = new System.Windows.Forms.Label();
            this.privateBox = new System.Windows.Forms.CheckBox();
            this.luggageBox = new System.Windows.Forms.CheckBox();
            this.mealBox = new System.Windows.Forms.CheckBox();
            this.middleRadio = new System.Windows.Forms.RadioButton();
            this.randomRadio = new System.Windows.Forms.RadioButton();
            this.seatTypeLabel = new System.Windows.Forms.Label();
            this.rowSelect = new System.Windows.Forms.NumericUpDown();
            this.rowsLabel = new System.Windows.Forms.Label();
            this.infoPanel.SuspendLayout();
            this.optionsPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.rowSelect)).BeginInit();
            this.SuspendLayout();
            // 
            // menuButton
            // 
            this.menuButton.Location = new System.Drawing.Point(12, 12);
            this.menuButton.Name = "menuButton";
            this.menuButton.Size = new System.Drawing.Size(104, 34);
            this.menuButton.TabIndex = 0;
            this.menuButton.Text = "back";
            this.menuButton.UseVisualStyleBackColor = true;
            this.menuButton.Click += new System.EventHandler(this.menuButton_Click);
            // 
            // selectedLabel
            // 
            this.selectedLabel.AutoSize = true;
            this.selectedLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.selectedLabel.Location = new System.Drawing.Point(3, 0);
            this.selectedLabel.Name = "selectedLabel";
            this.selectedLabel.Size = new System.Drawing.Size(333, 29);
            this.selectedLabel.TabIndex = 2;
            this.selectedLabel.Text = "Selected flight name here...";
            // 
            // flightsList
            // 
            this.flightsList.FormattingEnabled = true;
            this.flightsList.ItemHeight = 20;
            this.flightsList.Items.AddRange(new object[] {
            "flight names here..."});
            this.flightsList.Location = new System.Drawing.Point(12, 66);
            this.flightsList.Name = "flightsList";
            this.flightsList.Size = new System.Drawing.Size(629, 144);
            this.flightsList.TabIndex = 3;
            this.flightsList.SelectedValueChanged += new System.EventHandler(this.flightsList_SelectedValueChanged);
            // 
            // priceLabel
            // 
            this.priceLabel.AutoSize = true;
            this.priceLabel.Location = new System.Drawing.Point(4, 39);
            this.priceLabel.Name = "priceLabel";
            this.priceLabel.Size = new System.Drawing.Size(137, 20);
            this.priceLabel.TabIndex = 4;
            this.priceLabel.Text = "Ticket price here...";
            // 
            // dateLabel
            // 
            this.dateLabel.AutoSize = true;
            this.dateLabel.Location = new System.Drawing.Point(4, 68);
            this.dateLabel.Name = "dateLabel";
            this.dateLabel.Size = new System.Drawing.Size(135, 20);
            this.dateLabel.TabIndex = 5;
            this.dateLabel.Text = "Ticket date here...";
            // 
            // seatsLabel
            // 
            this.seatsLabel.AutoSize = true;
            this.seatsLabel.Location = new System.Drawing.Point(4, 98);
            this.seatsLabel.Name = "seatsLabel";
            this.seatsLabel.Size = new System.Drawing.Size(142, 20);
            this.seatsLabel.TabIndex = 6;
            this.seatsLabel.Text = "Ticket seats here...";
            // 
            // seatHeading
            // 
            this.seatHeading.AutoSize = true;
            this.seatHeading.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.seatHeading.Location = new System.Drawing.Point(3, 0);
            this.seatHeading.Name = "seatHeading";
            this.seatHeading.Size = new System.Drawing.Size(120, 25);
            this.seatHeading.TabIndex = 7;
            this.seatHeading.Text = "Select seat";
            // 
            // infoPanel
            // 
            this.infoPanel.Controls.Add(this.selectedLabel);
            this.infoPanel.Controls.Add(this.priceLabel);
            this.infoPanel.Controls.Add(this.seatsLabel);
            this.infoPanel.Controls.Add(this.dateLabel);
            this.infoPanel.Location = new System.Drawing.Point(12, 229);
            this.infoPanel.Name = "infoPanel";
            this.infoPanel.Size = new System.Drawing.Size(629, 131);
            this.infoPanel.TabIndex = 8;
            // 
            // optionsPanel
            // 
            this.optionsPanel.Controls.Add(this.windowRadio);
            this.optionsPanel.Controls.Add(this.bookButton);
            this.optionsPanel.Controls.Add(this.totalPriceLabel);
            this.optionsPanel.Controls.Add(this.extrasLabel);
            this.optionsPanel.Controls.Add(this.privateBox);
            this.optionsPanel.Controls.Add(this.luggageBox);
            this.optionsPanel.Controls.Add(this.mealBox);
            this.optionsPanel.Controls.Add(this.middleRadio);
            this.optionsPanel.Controls.Add(this.randomRadio);
            this.optionsPanel.Controls.Add(this.seatTypeLabel);
            this.optionsPanel.Controls.Add(this.rowSelect);
            this.optionsPanel.Controls.Add(this.rowsLabel);
            this.optionsPanel.Controls.Add(this.seatHeading);
            this.optionsPanel.Location = new System.Drawing.Point(12, 366);
            this.optionsPanel.Name = "optionsPanel";
            this.optionsPanel.Size = new System.Drawing.Size(629, 428);
            this.optionsPanel.TabIndex = 9;
            // 
            // windowRadio
            // 
            this.windowRadio.AutoSize = true;
            this.windowRadio.Location = new System.Drawing.Point(8, 182);
            this.windowRadio.Name = "windowRadio";
            this.windowRadio.Size = new System.Drawing.Size(174, 24);
            this.windowRadio.TabIndex = 19;
            this.windowRadio.Text = "Window seat | +$30";
            this.windowRadio.UseVisualStyleBackColor = true;
            this.windowRadio.CheckedChanged += new System.EventHandler(this.windowRadio_CheckedChanged);
            // 
            // bookButton
            // 
            this.bookButton.Location = new System.Drawing.Point(8, 377);
            this.bookButton.Name = "bookButton";
            this.bookButton.Size = new System.Drawing.Size(618, 45);
            this.bookButton.TabIndex = 18;
            this.bookButton.Text = "Book Ticket";
            this.bookButton.UseVisualStyleBackColor = true;
            this.bookButton.Click += new System.EventHandler(this.bookButton_Click);
            // 
            // totalPriceLabel
            // 
            this.totalPriceLabel.AutoSize = true;
            this.totalPriceLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.totalPriceLabel.Location = new System.Drawing.Point(4, 345);
            this.totalPriceLabel.Name = "totalPriceLabel";
            this.totalPriceLabel.Size = new System.Drawing.Size(86, 20);
            this.totalPriceLabel.TabIndex = 17;
            this.totalPriceLabel.Text = "In total: $";
            // 
            // extrasLabel
            // 
            this.extrasLabel.AutoSize = true;
            this.extrasLabel.Location = new System.Drawing.Point(4, 222);
            this.extrasLabel.Name = "extrasLabel";
            this.extrasLabel.Size = new System.Drawing.Size(214, 20);
            this.extrasLabel.TabIndex = 16;
            this.extrasLabel.Text = "Select optional extra services";
            // 
            // privateBox
            // 
            this.privateBox.AutoSize = true;
            this.privateBox.Location = new System.Drawing.Point(8, 305);
            this.privateBox.Name = "privateBox";
            this.privateBox.Size = new System.Drawing.Size(230, 24);
            this.privateBox.TabIndex = 15;
            this.privateBox.Text = "Private compartment | +$77";
            this.privateBox.UseVisualStyleBackColor = true;
            this.privateBox.CheckedChanged += new System.EventHandler(this.privateBox_CheckedChanged);
            // 
            // luggageBox
            // 
            this.luggageBox.AutoSize = true;
            this.luggageBox.Location = new System.Drawing.Point(8, 275);
            this.luggageBox.Name = "luggageBox";
            this.luggageBox.Size = new System.Drawing.Size(229, 24);
            this.luggageBox.TabIndex = 14;
            this.luggageBox.Text = "Extra luggage space | +$30";
            this.luggageBox.UseVisualStyleBackColor = true;
            this.luggageBox.CheckedChanged += new System.EventHandler(this.luggageBox_CheckedChanged);
            // 
            // mealBox
            // 
            this.mealBox.AutoSize = true;
            this.mealBox.Location = new System.Drawing.Point(8, 245);
            this.mealBox.Name = "mealBox";
            this.mealBox.Size = new System.Drawing.Size(185, 24);
            this.mealBox.TabIndex = 13;
            this.mealBox.Text = "Meal on board | +$15";
            this.mealBox.UseVisualStyleBackColor = true;
            this.mealBox.CheckedChanged += new System.EventHandler(this.mealBox_CheckedChanged);
            // 
            // middleRadio
            // 
            this.middleRadio.AutoSize = true;
            this.middleRadio.Location = new System.Drawing.Point(8, 152);
            this.middleRadio.Name = "middleRadio";
            this.middleRadio.Size = new System.Drawing.Size(158, 24);
            this.middleRadio.TabIndex = 12;
            this.middleRadio.Text = "Middle row | +$10";
            this.middleRadio.UseVisualStyleBackColor = true;
            this.middleRadio.CheckedChanged += new System.EventHandler(this.middleRadio_CheckedChanged);
            // 
            // randomRadio
            // 
            this.randomRadio.AutoSize = true;
            this.randomRadio.Checked = true;
            this.randomRadio.Location = new System.Drawing.Point(8, 122);
            this.randomRadio.Name = "randomRadio";
            this.randomRadio.Size = new System.Drawing.Size(170, 24);
            this.randomRadio.TabIndex = 11;
            this.randomRadio.TabStop = true;
            this.randomRadio.Text = "Random seat | +$0";
            this.randomRadio.UseVisualStyleBackColor = true;
            this.randomRadio.CheckedChanged += new System.EventHandler(this.randomRadio_CheckedChanged);
            // 
            // seatTypeLabel
            // 
            this.seatTypeLabel.AutoSize = true;
            this.seatTypeLabel.Location = new System.Drawing.Point(4, 99);
            this.seatTypeLabel.Name = "seatTypeLabel";
            this.seatTypeLabel.Size = new System.Drawing.Size(123, 20);
            this.seatTypeLabel.TabIndex = 10;
            this.seatTypeLabel.Text = "Select seat type";
            // 
            // rowSelect
            // 
            this.rowSelect.Location = new System.Drawing.Point(8, 59);
            this.rowSelect.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.rowSelect.Name = "rowSelect";
            this.rowSelect.Size = new System.Drawing.Size(618, 26);
            this.rowSelect.TabIndex = 9;
            this.rowSelect.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // rowsLabel
            // 
            this.rowsLabel.AutoSize = true;
            this.rowsLabel.Location = new System.Drawing.Point(4, 36);
            this.rowsLabel.Name = "rowsLabel";
            this.rowsLabel.Size = new System.Drawing.Size(118, 20);
            this.rowsLabel.TabIndex = 8;
            this.rowsLabel.Text = "Select seat row";
            // 
            // flights
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(653, 804);
            this.Controls.Add(this.optionsPanel);
            this.Controls.Add(this.infoPanel);
            this.Controls.Add(this.flightsList);
            this.Controls.Add(this.menuButton);
            this.Name = "flights";
            this.Text = "flights";
            this.infoPanel.ResumeLayout(false);
            this.infoPanel.PerformLayout();
            this.optionsPanel.ResumeLayout(false);
            this.optionsPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.rowSelect)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button menuButton;
        private System.Windows.Forms.Label selectedLabel;
        private System.Windows.Forms.ListBox flightsList;
        private System.Windows.Forms.Label priceLabel;
        private System.Windows.Forms.Label dateLabel;
        private System.Windows.Forms.Label seatsLabel;
        private System.Windows.Forms.Label seatHeading;
        private System.Windows.Forms.Panel infoPanel;
        private System.Windows.Forms.Panel optionsPanel;
        private System.Windows.Forms.NumericUpDown rowSelect;
        private System.Windows.Forms.Label rowsLabel;
        private System.Windows.Forms.RadioButton middleRadio;
        private System.Windows.Forms.RadioButton randomRadio;
        private System.Windows.Forms.Label seatTypeLabel;
        private System.Windows.Forms.CheckBox luggageBox;
        private System.Windows.Forms.CheckBox mealBox;
        private System.Windows.Forms.Label extrasLabel;
        private System.Windows.Forms.CheckBox privateBox;
        private System.Windows.Forms.Button bookButton;
        private System.Windows.Forms.Label totalPriceLabel;
        private System.Windows.Forms.RadioButton windowRadio;
    }
}