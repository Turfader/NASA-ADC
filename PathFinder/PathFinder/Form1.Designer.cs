namespace PathFinder
{
    partial class PathFinder
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
            this.submitButton = new System.Windows.Forms.Button();
            this.longButton = new System.Windows.Forms.Button();
            this.latButton = new System.Windows.Forms.Button();
            this.heightButton = new System.Windows.Forms.Button();
            this.slopeButton = new System.Windows.Forms.Button();
            this.longTextBox = new System.Windows.Forms.TextBox();
            this.latTextBox = new System.Windows.Forms.TextBox();
            this.heightTextBox = new System.Windows.Forms.TextBox();
            this.slopeTextBox = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // submitButton
            // 
            this.submitButton.Location = new System.Drawing.Point(684, 128);
            this.submitButton.Name = "submitButton";
            this.submitButton.Size = new System.Drawing.Size(104, 23);
            this.submitButton.TabIndex = 0;
            this.submitButton.Text = "Submit Pathing";
            this.submitButton.UseVisualStyleBackColor = true;
            this.submitButton.Click += new System.EventHandler(this.submitButton_Click);
            // 
            // longButton
            // 
            this.longButton.Location = new System.Drawing.Point(12, 12);
            this.longButton.Name = "longButton";
            this.longButton.Size = new System.Drawing.Size(140, 23);
            this.longButton.TabIndex = 1;
            this.longButton.Text = "Upload Longitude File";
            this.longButton.UseVisualStyleBackColor = true;
            this.longButton.Click += new System.EventHandler(this.longButton_Click);
            // 
            // latButton
            // 
            this.latButton.Location = new System.Drawing.Point(12, 41);
            this.latButton.Name = "latButton";
            this.latButton.Size = new System.Drawing.Size(140, 23);
            this.latButton.TabIndex = 2;
            this.latButton.Text = "Upload Latitude File";
            this.latButton.UseVisualStyleBackColor = true;
            this.latButton.Click += new System.EventHandler(this.LatButton_Click);
            // 
            // heightButton
            // 
            this.heightButton.Location = new System.Drawing.Point(12, 70);
            this.heightButton.Name = "heightButton";
            this.heightButton.Size = new System.Drawing.Size(140, 23);
            this.heightButton.TabIndex = 3;
            this.heightButton.Text = "Upload Height File";
            this.heightButton.UseVisualStyleBackColor = true;
            this.heightButton.Click += new System.EventHandler(this.heightButton_Click);
            // 
            // slopeButton
            // 
            this.slopeButton.Location = new System.Drawing.Point(12, 99);
            this.slopeButton.Name = "slopeButton";
            this.slopeButton.Size = new System.Drawing.Size(140, 23);
            this.slopeButton.TabIndex = 4;
            this.slopeButton.Text = "Upload Slope File";
            this.slopeButton.UseVisualStyleBackColor = true;
            this.slopeButton.Click += new System.EventHandler(this.slopeButton_Click);
            // 
            // longTextBox
            // 
            this.longTextBox.Location = new System.Drawing.Point(158, 12);
            this.longTextBox.Name = "longTextBox";
            this.longTextBox.ReadOnly = true;
            this.longTextBox.Size = new System.Drawing.Size(630, 23);
            this.longTextBox.TabIndex = 5;
            // 
            // latTextBox
            // 
            this.latTextBox.Location = new System.Drawing.Point(158, 41);
            this.latTextBox.Name = "latTextBox";
            this.latTextBox.ReadOnly = true;
            this.latTextBox.Size = new System.Drawing.Size(630, 23);
            this.latTextBox.TabIndex = 6;
            // 
            // heightTextBox
            // 
            this.heightTextBox.Location = new System.Drawing.Point(158, 70);
            this.heightTextBox.Name = "heightTextBox";
            this.heightTextBox.ReadOnly = true;
            this.heightTextBox.Size = new System.Drawing.Size(630, 23);
            this.heightTextBox.TabIndex = 7;
            // 
            // slopeTextBox
            // 
            this.slopeTextBox.Location = new System.Drawing.Point(158, 99);
            this.slopeTextBox.Name = "slopeTextBox";
            this.slopeTextBox.ReadOnly = true;
            this.slopeTextBox.Size = new System.Drawing.Size(630, 23);
            this.slopeTextBox.TabIndex = 8;
            // 
            // PathFinder
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.slopeTextBox);
            this.Controls.Add(this.heightTextBox);
            this.Controls.Add(this.latTextBox);
            this.Controls.Add(this.longTextBox);
            this.Controls.Add(this.slopeButton);
            this.Controls.Add(this.heightButton);
            this.Controls.Add(this.latButton);
            this.Controls.Add(this.longButton);
            this.Controls.Add(this.submitButton);
            this.Name = "PathFinder";
            this.Text = "PathFinder";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button submitButton;
        private Button longButton;
        private Button latButton;
        private Button heightButton;
        private Button slopeButton;
        private TextBox longTextBox;
        private TextBox latTextBox;
        private TextBox heightTextBox;
        private TextBox slopeTextBox;
    }
}