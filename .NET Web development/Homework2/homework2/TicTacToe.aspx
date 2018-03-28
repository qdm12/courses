<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="TicTacToe.aspx.cs" Inherits="homework2.TicTacToe" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>TicTacToe</title>
    <link href="Styles/TicTacToe.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">

        <asp:ScriptManager runat="server"></asp:ScriptManager>
        <asp:UpdatePanel runat="server">
        <ContentTemplate>

        <asp:Menu ID="Menu1" runat="server" Orientation="Horizontal">
            <Items>
                <asp:MenuItem NavigateUrl="Default.aspx" Text="Login" Value="Login"></asp:MenuItem>
                <asp:MenuItem NavigateUrl="Public.aspx" Text="Rules" Value="Rules"></asp:MenuItem>
                <asp:MenuItem NavigateUrl="TicTacToe.aspx" Text="TicTacToe" Value="TicTacToe"></asp:MenuItem>
            </Items>
        </asp:Menu>
        <div id="error" runat="server">
            You do not have access to this page. Please &nbsp<a href="Default.aspx">login</a>
        </div>
        <div id="game" runat="server">
            <div id="status" runat="server"></div>
            <div id="board">
                <asp:Button ID="b0" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b1" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b2" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <div style="clear:both;"></div>
                <asp:Button ID="b3" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b4" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b5" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <div style="clear:both;"></div>
                <asp:Button ID="b6" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b7" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
                <asp:Button ID="b8" class="square" runat="server" Text="" OnClick="ClickCell"></asp:Button>
            </div>
        </div>

       </ContentTemplate>
        </asp:UpdatePanel>
    </form>
</body>
</html>
