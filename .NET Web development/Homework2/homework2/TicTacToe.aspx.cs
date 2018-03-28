using System;
using System.Collections.Generic;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace homework2
{
    public partial class TicTacToe : System.Web.UI.Page
    {
        private enum Player { X, O };
        private enum Cell { X, O, None }
        private enum Winner { X, O, None, Tie };

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
            if (this.isSessionValid())
            {
                error.Visible = false;
                game.Visible = true;
            }
            else
            {
                error.Visible = true;
                game.Visible = false;
            }
            if (!IsPostBack)
            {
                ViewState["ViewStateId"] = System.Guid.NewGuid().ToString();
                Session["SessionId"] = ViewState["ViewStateId"];
                Session.Remove("board");
                Session.Remove("player");
                Session.Remove("winner");
                b0.Text = b1.Text = b2.Text = b3.Text = b4.Text = b5.Text = b6.Text = b7.Text = b8.Text = "";
                status.InnerText = "This is the turn of X";
            }
            else
            {
                if (ViewState["ViewStateId"].ToString() != Session["SessionId"].ToString())
                {
                    Response.Redirect(Page.Request.Url.ToString(), true);
                }
                ViewState["ViewStateId"] = System.Guid.NewGuid().ToString();
                Session["SessionId"] = ViewState["ViewStateId"];
            }
        }

        private Winner GetWinner(Cell[,] board, Player lastPlayer)
        {
            bool full = true;
            List<Cell> diag1Cells = new List<Cell>();
            List<Cell> diag2Cells = new List<Cell>();
            List<Cell> rowCells = new List<Cell>();
            List<Cell> colCells = new List<Cell>();
            for (int i = 0; i < 3; i++)
            {
                diag1Cells.Add(board[i, i]); // TODO board html
                diag2Cells.Add(board[2 - i, i]);
                if (board[i, i] != ((lastPlayer == Player.X) ? Cell.X : Cell.O))
                {
                    diag1Cells.Clear();
                }
                if (board[2 - i, i] != ((lastPlayer == Player.X) ? Cell.X : Cell.O))
                {
                    diag2Cells.Clear();
                }
                for (int j = 0; j < 3; j++)
                {
                    rowCells.Add(board[i, j]); // TODO board html
                    colCells.Add(board[j, i]);
                    if (board[i, j] != ((lastPlayer == Player.X) ? Cell.X : Cell.O))
                    {
                        rowCells.Clear();
                    }
                    if (board[j, i] != ((lastPlayer == Player.X) ? Cell.X : Cell.O))
                    {
                        colCells.Clear();
                    }
                    if (board[i, j] == Cell.None)
                    {
                        full = false;
                    }
                }
                if (rowCells.Count == 3)
                {
                    return ((lastPlayer == Player.X) ? Winner.X : Winner.O);
                }
                if (colCells.Count == 3)
                {
                    return ((lastPlayer == Player.X) ? Winner.X : Winner.O);
                }
            }
            if (diag1Cells.Count == 3)
            {
                return ((lastPlayer == Player.X) ? Winner.X : Winner.O);
            }
            if (diag2Cells.Count == 3)
            {
                return ((lastPlayer == Player.X) ? Winner.X : Winner.O);

            }
            if (full)
            {
                return Winner.Tie;
            }
            return Winner.None;
        }

        public void ClickCell(Object sender, EventArgs e)
        {
            Button b = (Button)sender;
            int cellID = (int)Char.GetNumericValue(b.ID[1]);
            int row = cellID / 3;
            int col = cellID % 3;
            Cell[,] board;
            if (Session["board"] == null)
            {
                board = new Cell[,]
                {
                {Cell.None, Cell.None, Cell.None},
                {Cell.None, Cell.None, Cell.None},
                {Cell.None, Cell.None, Cell.None},
                };
            }
            else
            {
                board = (Cell[,])Session["board"];
            }
            Player player;
            if (Session["player"] == null)
            {
                player = Player.X;
            }
            else
            {
                player = (Player)Session["player"];
            }
            Winner winner;
            if (Session["winner"] == null)
            {
                winner = Winner.None;
            }
            else
            {
                winner = (Winner)Session["winner"];
            }
            if (winner != Winner.None)
            {
                status.InnerText = "The game is over now. Please restart.";
            }
            else if (board[row, col] == Cell.None)
            {
                board[row, col] = ((player == Player.X) ? Cell.X : Cell.O);
                b.Text = ((player == Player.X) ? "X" : "O");
                b.ForeColor = ((player == Player.X) ? System.Drawing.Color.Red : System.Drawing.Color.Blue);
                winner = this.GetWinner(board, player);
                player = ((player == Player.X) ? Player.O : Player.X);
                Session["player"] = player;
                Session["board"] = board;
                Session["winner"] = winner;
                status.InnerText = "This is the turn of " + ((player == Player.X) ? "X" : "O");
                if (winner != Winner.None)
                {
                    status.InnerText = winner + " won !";
                }
            }
        }
    }
}