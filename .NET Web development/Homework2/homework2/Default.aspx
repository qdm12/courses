<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="homework2.Default" %>

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
        <h2>Welcome to the Tic Tac Toe game!</h2>
        <div id="logindiv" runat="server">
            <asp:Login ID="Login" runat="server" OnAuthenticate="Login_Authenticate"></asp:Login>
        </div>
        <div id="logoutdiv" runat="server">
            <input id="Logout" type="button" value="Log out" runat="server" onServerClick="LogoutClick" />
        </div>
         <span id="infomessage">Click <a href="Public.aspx">here</a> for general information</span>
    </form>
</body>
</html>
