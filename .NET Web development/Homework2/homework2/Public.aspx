<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Public.aspx.cs" Inherits="homework2.Public" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>TicTacToe</title>
    <link href="Styles/TicTacToe.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">
        <asp:Menu ID="Menu1" runat="server" Orientation="Horizontal">
            <Items>
                <asp:MenuItem NavigateUrl="Default.aspx" Text="Login" Value="Login"></asp:MenuItem>
                <asp:MenuItem NavigateUrl="Public.aspx" Text="Rules" Value="Rules"></asp:MenuItem>
                <asp:MenuItem NavigateUrl="TicTacToe.aspx" Text="TicTacToe" Value="TicTacToe"></asp:MenuItem>
            </Items>
        </asp:Menu>
        <h1>Rules of Tic-Tac-Toe</h1>
        <ol>
            <li>The game is played on a grid that's 3 squares by 3 squares.</li>
            <li>One player is X, and the other is O. Players take turns putting their marks in empty squares.</li>
            <li>The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.</li>
            <li>When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.</li>
        </ol>
        <p>Click <a href="TicTacToe.aspx">here</a> to play the game.</p>
    </form>
</body>
</html>
