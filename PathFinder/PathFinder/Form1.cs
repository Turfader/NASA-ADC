namespace PathFinder
{
    public partial class PathFinder : Form
    {
        public PathFinder()
        {
            InitializeComponent();
        }

        public String getSelectCSVPath()
        {
            OpenFileDialog dialog = new OpenFileDialog();
            dialog.Filter = "CSV files | *.csv"; // file types, that will be allowed to upload
            dialog.Multiselect = false; // allow/deny user to upload more than one file at a time
            if (dialog.ShowDialog() == DialogResult.OK) // if user clicked OK
            {
                String path = dialog.FileName; // get name of file
                return path;
                //using (StreamReader reader = new StreamReader(new FileStream(path, FileMode.Open), new UTF8Encoding())) // do anything you want, e.g. read it
                {
                    // ...
                }
            }
            else
            {
                return null;
            }
        }

        private void longButton_Click(object sender, EventArgs e)
        {
            String longPath = getSelectCSVPath();
            longTextBox.Text = longPath;

        }

        private void LatButton_Click(object sender, EventArgs e)
        {
            String latPath = getSelectCSVPath();
            latTextBox.Text = latPath;
        }

        private void heightButton_Click(object sender, EventArgs e)
        {
            String heightPath = getSelectCSVPath();
            heightTextBox.Text = heightPath;
        }

        private void slopeButton_Click(object sender, EventArgs e)
        {
            String slopePath = getSelectCSVPath();
            slopeTextBox.Text = slopePath;

        }

        private void submitButton_Click(object sender, EventArgs e)
        {
            async Task ExampleAsync()
            {
                string[] lines =
                {
            longTextBox.Text, latTextBox.Text, heightTextBox.Text, slopeTextBox.Text
                };

                await File.WriteAllLinesAsync("C:/Users/Owner/Documents/TestWrite.txt", lines);
            }

            ExampleAsync();
        }
    }
}