using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Helpers;
using System.Web.SessionState;

namespace homework2
{
    public class Credentials
    {
        public Credentials(string username, string password)
        {
            this.username = username;
            this.hashedPasswordWithSalt = Crypto.HashPassword(password);
        
        }

        public string username;
        string hashedPasswordWithSalt;
        string sessionID;
        Int32 sessionExpiration;

        public string createSession()
        {
            SessionIDManager manager = new SessionIDManager();
            string newID = manager.CreateSessionID(HttpContext.Current);
            bool redirected = false, isAdded = false;
            manager.SaveSessionID(HttpContext.Current, newID, out redirected, out isAdded);
            if (isAdded)
            {
                this.sessionID = newID;
                this.sessionExpiration = (Int32)(DateTime.UtcNow.AddMinutes(10).Subtract(new DateTime(1970, 1, 1))).TotalSeconds;
            }
            return Crypto.HashPassword(this.sessionID);
        }

        public bool isSessionValid(string hashedSessionIDWithSalt)
        { // valid sessionID and not expired
            return Crypto.VerifyHashedPassword(hashedSessionIDWithSalt, sessionID) && (Int32)(DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1))).TotalSeconds < sessionExpiration;
        }

        public bool isPasswordValid(string password)
        {
            return Crypto.VerifyHashedPassword(this.hashedPasswordWithSalt, password);
        }
    }
}