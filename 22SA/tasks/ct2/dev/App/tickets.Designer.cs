namespace App
{
    partial class tickets
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
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle5 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle6 = new System.Windows.Forms.DataGridViewCellStyle();
            this.ticketsGrid = new System.Windows.Forms.DataGridView();
            this.backButton = new System.Windows.Forms.Button();
            this.userName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.flightName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.price = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.date = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.seatRow = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.seatType = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.extrasList = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ticketBindingSource = new System.Windows.Forms.BindingSource(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.ticketsGrid)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ticketBindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // ticketsGrid
            // 
            this.ticketsGrid.AllowUserToAddRows = false;
            this.ticketsGrid.AllowUserToDeleteRows = false;
            this.ticketsGrid.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.ticketsGrid.BackgroundColor = System.Drawing.SystemColors.Control;
            this.ticketsGrid.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.ticketsGrid.ColumnHeadersBorderStyle = System.Windows.Forms.DataGridViewHeaderBorderStyle.None;
            dataGridViewCellStyle5.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle5.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle5.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            dataGridViewCellStyle5.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle5.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle5.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle5.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.ticketsGrid.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle5;
            this.ticketsGrid.ColumnHeadersHeight = 34;
            this.ticketsGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.DisableResizing;
            this.ticketsGrid.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.userName,
            this.flightName,
            this.price,
            this.date,
            this.seatRow,
            this.seatType,
            this.extrasList});
            this.ticketsGrid.GridColor = System.Drawing.SystemColors.ControlLightLight;
            this.ticketsGrid.Location = new System.Drawing.Point(12, 65);
            this.ticketsGrid.Name = "ticketsGrid";
            this.ticketsGrid.ReadOnly = true;
            this.ticketsGrid.RowHeadersVisible = false;
            this.ticketsGrid.RowHeadersWidth = 62;
            dataGridViewCellStyle6.Font = new System.Drawing.Font("Verdana", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ticketsGrid.RowsDefaultCellStyle = dataGridViewCellStyle6;
            this.ticketsGrid.RowTemplate.Height = 28;
            this.ticketsGrid.Size = new System.Drawing.Size(1169, 298);
            this.ticketsGrid.TabIndex = 0;
            // 
            // backButton
            // 
            this.backButton.Location = new System.Drawing.Point(12, 12);
            this.backButton.Name = "backButton";
            this.backButton.Size = new System.Drawing.Size(113, 30);
            this.backButton.TabIndex = 1;
            this.backButton.Text = "back";
            this.backButton.UseVisualStyleBackColor = true;
            this.backButton.Click += new System.EventHandler(this.backButton_Click);
            // 
            // userName
            // 
            this.userName.FillWeight = 80F;
            this.userName.HeaderText = "User Name";
            this.userName.MinimumWidth = 8;
            this.userName.Name = "userName";
            this.userName.ReadOnly = true;
            // 
            // flightName
            // 
            this.flightName.FillWeight = 160F;
            this.flightName.HeaderText = "Flight Name";
            this.flightName.MinimumWidth = 8;
            this.flightName.Name = "flightName";
            this.flightName.ReadOnly = true;
            // 
            // price
            // 
            this.price.FillWeight = 80F;
            this.price.HeaderText = "Total Price";
            this.price.MinimumWidth = 8;
            this.price.Name = "price";
            this.price.ReadOnly = true;
            // 
            // date
            // 
            this.date.FillWeight = 70F;
            this.date.HeaderText = "Flight Date";
            this.date.MinimumWidth = 8;
            this.date.Name = "date";
            this.date.ReadOnly = true;
            // 
            // seatRow
            // 
            this.seatRow.FillWeight = 67F;
            this.seatRow.HeaderText = "Seat Row";
            this.seatRow.MinimumWidth = 8;
            this.seatRow.Name = "seatRow";
            this.seatRow.ReadOnly = true;
            // 
            // seatType
            // 
            this.seatType.FillWeight = 70F;
            this.seatType.HeaderText = "Seat Type";
            this.seatType.MinimumWidth = 8;
            this.seatType.Name = "seatType";
            this.seatType.ReadOnly = true;
            // 
            // extrasList
            // 
            this.extrasList.FillWeight = 130F;
            this.extrasList.HeaderText = "Extra Services";
            this.extrasList.MinimumWidth = 8;
            this.extrasList.Name = "extrasList";
            this.extrasList.ReadOnly = true;
            // 
            // ticketBindingSource
            // 
            this.ticketBindingSource.DataSource = typeof(Class_Library.ticket);
            // 
            // tickets
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1193, 379);
            this.Controls.Add(this.backButton);
            this.Controls.Add(this.ticketsGrid);
            this.Name = "tickets";
            this.Text = "tickets";
            ((System.ComponentModel.ISupportInitialize)(this.ticketsGrid)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ticketBindingSource)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView ticketsGrid;
        private System.Windows.Forms.BindingSource ticketBindingSource;
        private System.Windows.Forms.Button backButton;
        private System.Windows.Forms.DataGridViewTextBoxColumn userName;
        private System.Windows.Forms.DataGridViewTextBoxColumn flightName;
        private System.Windows.Forms.DataGridViewTextBoxColumn price;
        private System.Windows.Forms.DataGridViewTextBoxColumn date;
        private System.Windows.Forms.DataGridViewTextBoxColumn seatRow;
        private System.Windows.Forms.DataGridViewTextBoxColumn seatType;
        private System.Windows.Forms.DataGridViewTextBoxColumn extrasList;
    }
}