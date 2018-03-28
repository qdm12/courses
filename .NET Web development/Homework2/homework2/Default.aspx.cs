using System;
using System.Web.UI.WebControls;

namespace homework2
{
    public partial class Default : System.Web.UI.Page
    {
        private bool isSessionValid()
        {
            if (Request.Cookies["session"] != null)
            {
                string session = Request.Cookies["session"].Value;
                Application.Lock();
                Credentials c = null;
                foreach (string username in Application.Keys)
                {
                    c = (Credentials)Application[username];
                    if (c.isSessionValid(session))
                    {
                        Application.UnLock();
                        return true;
                    }
                }
            }
            return false;
        }

        protected void Page_Load(object sender, EventArgs e)
        {
            if (isSessionValid())
            {
                logindiv.Visible = false;
                logoutdiv.Visible = true;
            }
            else
            {
                logindiv.Visible = true;
                logoutdiv.Visible = false;
            }
        }

        protected void Login_Authenticate(object sender, AuthenticateEventArgs e)
        {
            bool UsernameValid = false, PasswordValid = false;
            Credentials c = null;
            Application.Lock();
            if (Application[Login.UserName] != null)
            {
                UsernameValid = true;
                c = (Credentials)Application[Login.UserName];
                PasswordValid = c.isPasswordValid(Login.Password);
            }
            Application.UnLock();
            if (UsernameValid && PasswordValid)
            {
                // Success log in
                string session = c.createSession();
                Response.Cookies["session"].Value = session;
                Response.Cookies["session"].Expires = DateTime.Now.AddMinutes(10);
                Application.Lock();
                Application[c.username] = c;
                Application.UnLock();
                Response.Redirect("TicTacToe.aspx");
            }
            else if (UsernameValid && ! PasswordValid)
            {
                // Failed log in TODO
                Response.Redirect("Default.aspx");
            }
            else
            {
                // Register
                c = new Credentials(Login.UserName, Login.Password);
                string session = c.createSession();
                Response.Cookies["session"].Value = session;
                Response.Cookies["session"].Expires = DateTime.Now.AddMinutes(10);
                Application.Lock();
                Application[c.username] = c;
                Application.UnLock();
                Response.Redirect("TicTacToe.aspx");
            }
        }

        protected void LogoutClick(object sender, EventArgs e)
        {
            // Delete cookie
            Response.Cookies.Remove("session");
            logindiv.Visible = true;
            logoutdiv.Visible = false;
        }
    }
}