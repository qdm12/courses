var TicTacToe = {
	board_logic:[
		[null,null,null],
		[null,null,null],
		[null,null,null],
	],
	board_html:[
		[null,null,null],
		[null,null,null],
		[null,null,null],
	],
	nodes:0,
	x:0,
	ai:true,
	init: function() {
		$("#container").html('');
		for (i = 0; i < 9; i++) {
			$("#container").append("<div id=" + i + " onclick='TicTacToe.clicked(this.id)' class='square'></div>");
			if (((i + 1) % 3) == 0) {
				$("#container").append("<div style='clear:both;'>");
			}
			this.board_html[Math.floor(i / 3)][i % 3] = $('#' + i);
		}
		this.player = 'X'; // TODO give choice
	},
	clicked: function(square_id) {
		var row = Math.floor(square_id / 3);
		var col = square_id % 3;
		if (this.board_logic[row][col] == null) {
			this.board_logic[row][col] = this.player;
			this.board_html[row][col].text(this.player);
			// Style effects
			var border_size = 0.02 * 0.18 * Math.min($(window).width(), $(window).height());
			if(this.player == 'O'){
				// Changes css of square clicked
				this.board_html[row][col].css({
											"color" : "red",
											"background" : "rgba(255, 0, 0, 0.137)"
										});
				this.board_html[row][col].hover(
					function(){
						$(this).css({
										"color" : "white",
										"background" : "rgba(138, 3, 3, 0.822)"
									});
					}, function(){
						$(this).css({
										"color" : "red",
										"background" : "rgba(255, 0, 0, 0.137)"
									});
					}
				);
				// Changes UI for X player
				$(".square").css({
					"border" : border_size.toString() + "px solid #477bff",
				});
			} else { // X player just clicked
				// Changes css of square clicked
				this.board_html[row][col].css({
											"color" : "blue",
											"background" : "rgba(3, 39, 138, 0.445)"
										});
				this.board_html[row][col].hover(
					function(){
						$(this).css({
										"color" : "white",
										"background" : "rgba(2, 38, 138, 0.986)"
									});
					}, function(){
						$(this).css({
										"color" : "blue",
										"background" : "rgba(3, 39, 138, 0.445)"
									});
					}
				);
				// Changes UI for O player
				$(".square").css({
					"border" : border_size.toString() + "px solid #ff5f5f",
				});
			}
			winner = this.get_winner(this.board_logic, this.player, false);
            if (winner) {
                /* use setTimeout to delay confirm message so that last move is recorded */
				/* this is needed for some browsers and mobile devices */
				setTimeout(function(){TicTacToe.end_game(winner);},500);
			} else {
				this.player = (this.player == 'X')? 'O': 'X'; // switch to other player
				if (this.player == 'O' && this.ai) {
					this.aiMove(this.board_logic);
				}
            }
		}
	},
	get_winner: function(board_logic, last_player, simulation) {
		var full = true;
		var i, j;
		var diag1_squares = [];
		var diag2_squares = [];
		var row_squares = [];
		var col_squares = [];

		for (i = 0; i < 3; i++) {
			diag1_squares.push(this.board_html[i][i]);
			diag2_squares.push(this.board_html[2 - i][i]);
			if (board_logic[i][i] != last_player) {
				diag1_squares = [];
			}
			if (board_logic[2 - i][i] != last_player) {
				diag2_squares = [];
			}
			for (j = 0; j < 3; j++) {
				row_squares.push(this.board_html[i][j]);
				col_squares.push(this.board_html[j][i]);
				if (board_logic[i][j] != last_player) {
					row_squares = [];
				}
				if (board_logic[j][i] != last_player) {
					col_squares = [];
				}
				if (board_logic[i][j] == null) {
					full = false;
				}
			}
			if (row_squares.length == 3) {
				TicTacToe.highlight_success(row_squares, last_player, simulation);
				return last_player;
			}
			if (col_squares.length == 3) {
				TicTacToe.highlight_success(col_squares, last_player, simulation);
				return last_player;
			}
		}
		if (diag1_squares.length == 3) {
			TicTacToe.highlight_success(diag1_squares, last_player, simulation);
			return last_player;
		}
		if (diag2_squares.length == 3) {
			TicTacToe.highlight_success(diag2_squares, last_player, simulation);
			return last_player;
		}
		// Board is filled
		if (full) {
			return "TIE";
		}
		// No winner yet
		return null;
	},
	highlight_success: function(squares, winner, simulation) {
		if (!simulation) {
			for (var i = 0; i < 3; i++){
				if (winner == 'X') {
					color = "blue";
				} else {
					color = "red";
				}
				squares[i].css({
					"color" : "white",
					"background" : "rgb(255,215,0)"							
				});
				squares[i].hover(
					function(){
						$(this).css({
							"color" : color,
							"background" : "rgb(255,215,0)"
						});
					}, function(){
						$(this).css({
							"color" : "white",
							"background" : "rgb(255,215,0)"
						});
					}
				);
			}
		}
	},
	end_game: function(winner) {
		var icon = "success";
		var title  = winner + ' won!';
		if (winner == "TIE") {
			icon = "warning";
			title  = "The game ended in a tie";
		}
		swal({
			title: title,
			text: "Play again?",
			icon: icon,
			closeOnClickOutside: false,
			closeOnEsc: false,
			timer: 10000,
			buttons: {
				cancel: "Nah",
				confirm: "Yes"
			}
		}).then((replay) => {
			if (replay) {
				this.init();
				resizeAll();
			}
		});
	},
	recurseMinimax: function(board_logic, player) {
		this.nodes++;
		var winner = this.get_winner(board_logic, player, true);
		if (winner == 'O') {
			return [1, board_logic]
		} else if (winner == 'X') {
			return [-1, board_logic]
		} else if (winner == 'TIE') {
			this.x++;
			return [0, board_logic];
		} else {
			// Next states
			var nextVal = null;
			var nextBoard = null;
			var nextPlayer = (player == 'X') ? 'O' : 'X';
			for (var i = 0; i < 3; i++) {
				for (var j = 0; j < 3; j++) {
					if (board_logic[i][j] == null) {
						board_logic[i][j] = player;
						var value = this.recurseMinimax(board_logic, nextPlayer)[0];
						if ((player && (nextVal == null || value > nextVal)) || 
						    (nextPlayer && (nextVal == null || value < nextVal))) {
							nextBoard = board_logic.map(function(arr) {
								return arr.slice();
							});
							nextVal = value;
						}
						board_logic[i][j] = null;
					}
				}
			}
			return [nextVal, nextBoard];
		}
	},
	findSquarePlayed: function(board, new_board) {
		for (var i = 0; i < 3; i++) {
			for (var j = 0; j < 3; j++) {
				if (board[i][j] != new_board[i][j]) {
					return i * 3 + j;
				}
			}
		}
	},
	aiMove: function(board_logic) {
		this.nodes = 0;
		next_board_logic = this.recurseMinimax(board_logic, 'O')[1];
		console.log(this.x);
		square_id = this.findSquarePlayed(board_logic, next_board_logic);
		this.clicked(square_id);
	}
};

function resizeAll(){
	var square_size = 0.18 * Math.min($(window).width(), $(window).height());
	var border_size = 0.02 * square_size;
	var font_size = square_size / 2;
	$(".square").css({"width" : square_size.toString(),
					  "height" : square_size.toString(),
					  "border" : border_size.toString() + "px solid #5479FD",
					  "font-size" : font_size.toString()});
	var left = ( $(window).width() - 3*square_size ) / 2;
	var top = ( $(window).height() - 3*square_size ) / 2;
	$("#container").css({"left" : left.toString(),
						 "top" : top.toString()});
}

$(document).ready(function(){
	TicTacToe.init();
});

$(window).bind("load", function() {
	resizeAll();
});

$(window).resize(function() {
	resizeAll();
});



// TODO on resize