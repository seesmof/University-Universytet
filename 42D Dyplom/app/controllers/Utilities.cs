using System;
using System.Collections.Generic;
using System.Text;

namespace app.controllers
{
    public static class Utilities
    {
        public static void ShowErrors(List<string> errors)
        {
            if (errors.Count > 0)
            {
                string message = string.Join(Environment.NewLine, errors.Select(e => $"• {e}"));
                MessageBox.Show(message, "Something is wrong", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
