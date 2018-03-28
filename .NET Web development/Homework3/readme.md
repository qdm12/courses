# .NET Web Development

## Homework 3: Persistent Tic Tac Toe

### Description

A persistent Tic Tac Toe game with login and registration.

It uses
- C# and Web forms
- EntityFramework with Code First
- SQL database

### Features

- 4 pages:
    - Public.aspx to show the rules of the game
    - Default.aspx to log in or log out if logged in
    - TicTacToe.aspx to play the game if allowed to
    - Register.aspx to register an account
- Register.aspx
    - Regular expressions and other validators are used to check the input is correct
    - Database errors or warning are displayed back to the client
    - The password is hidden
- TicTacToe.aspx
    - State of board is only stored in server memory, not on client side
    - The board is re-drawn on each postback
    - The board can be saved to the database or loaded from the database
    - The board can be cleared with the clear button
    - Reloading the page will simply load the board again
- User sessions are stored hashed in server memory
- User credentials and details are stored in database

### To dos

- Transparent background
- Fixed navban
- Disable viewstate