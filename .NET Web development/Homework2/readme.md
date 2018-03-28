# .NET Web Development

## Homework 2: Authentication and security questions

### Tic-Tac-Toe authentication

- Create 3 pages
    - [Public](homework2/Public.aspx) to show the Tic-Tac-Toe rules
    - [Default](homework2/Default.aspx) to Log in or Log out
    - [TicTacToe](homework2/TicTacToe.aspx.cs) to play the game if logged in
- The login should also register a new user
- The user obtains a session ID in a cookie that he uses for subsequent requests
- User credentials are stored in the Application State in memory for simplicity

### Security questions

1. *Explain one type of possible security breach scenario if the user session ID is stored in plain text in the browser cookie.*

An attacker could understand the pattern of the session ID generation and gain access.

2. *What happens if a user tampers with the encrypted user session ID value in the cookie?*

Because the value is encrypted, the decryption process of the modified session ID cookie will fail (due to checksum error, padding issues etc.).

3. *If the username is stored in plain text in the browser cookie and the user tampers with this value, why should the system still disallow unauthorized access?*

All access is controlled through the encrypted session ID in the cookie. If the username is changed, the session stays the same and won't allow the user for unauthorized access.

4. *Which of the pages should have a secured HTTPS connection and why?*
    - [Default](homework2/Default.aspx) receives the username and password and exchange the session ID cookie with the user. It must have HTTPS as a consequence.
    - [TicTacToe](homework2/TicTacToe.aspx) checks for the session ID cookie which should be kept safe with HTTPS as well.
    - [Public](homework2/Public.aspx) needs HTTPS as well in our case because the session ID cookie is also sent (seen with Fiddler). 
      This can be avoided once HTTPS is setup by setting the `secure` property of the session ID cookie to true.
      The Public page would then no require HTTPS anymore.

5. *Why should the user session ID be encrypted in server memory?*

An attacker gaining access to the server could not find information about the session ID generation. 

6. *Why does the session expiration have to be not implemented as a cookie expiration?*

The cookie goes in the browser of the user and can be tampered with.
Setting the session expiration on the client side is thus dangerous because it can be changed by the user.
The system should only rely on the server with the session expiration stored in server memory or disk.

### Tic-Tac-Toe Game

The logic is implemented in [TicTacToe.aspx.cs](homework2/TicTacToe.aspx.cs).

It uses the Session to keep track of the board and the player.