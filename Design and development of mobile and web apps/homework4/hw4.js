var TicTacToe = {
	winning_squares: [
						['0', '1', '2'],
						['3', '4', '5'],
						['6', '7', '8'],
						['0', '3', '6'],
						['0', '4', '8'],
						['1', '4', '7'],
						['2', '5', '8'],
						['2', '4', '6']
	],
	init: function() {
		$("#container").html('');
		for (i = 0; i < 9; i++) {
			$("#container").append("<div id=" + i + " onclick='TicTacToe.clicked(this.id)' class='square'></div>");
			if (((i + 1) % 3) == 0) {
				$("#container").append("<div style='clear:both;'>");
			}
		}
		this.player = 'X';
	},
	clicked: function(square_id) {
		var squares = [];
		for (i = 0; i < 9; i++) {
			squares.push($('#' + i));
		}
		if (squares[square_id].html() == "") {
			squares[square_id].text(this.player);
			if(this.player == 'O'){
				// Changes css of square clicked
				squares[square_id].css({
					"color" : "red",
					"background" : "rgba(255, 0, 0, 0.137)"
				});
				squares[square_id].hover(
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
				var border_size = 0.02 * 0.18 * Math.min($(window).width(), $(window).height());
				$(".square").css({
					"border" : border_size.toString() + "px solid #477bff",
				});
			} else { // X player just clicked
				// Changes css of square clicked
				squares[square_id].css({
					"color" : "blue",
					"background" : "rgba(3, 39, 138, 0.445)"
				});
				squares[square_id].hover(
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
				var border_size = 0.02 * 0.18 * Math.min($(window).width(), $(window).height());
				$(".square").css({
					"border" : border_size.toString() + "px solid #ff5f5f",
				});
			}
            if (this.player_won(square_id)) {
                /* use setTimeout to delay confirm message so that last move is recorded */
				/* this is needed for some browsers and mobile devices */
				if (this.player == 'X'){
					setTimeout(function(){TicTacToe.end_game('X');},500);
				} else {
					setTimeout(function(){TicTacToe.end_game('O');},500);
				}
            } else if (this.is_game_tied()){
                setTimeout(function(){TicTacToe.end_game();},500);
			} else {
                this.player = (this.player == 'X')? 'O': 'X'; // switch to other player
            }
		}
	},
	player_won: function(square_id) {
		for (var i in this.winning_squares) {
			if ($.inArray(square_id, this.winning_squares[i]) != -1) {
				var squares = this.winning_squares[i];
				var pattern = '';
				var pattern_objects = [];
				for (j in squares) {
					pattern += $('#' + squares[j]).html();
					pattern_objects.push($('#' + squares[j]));
				}
				if (pattern == this.player + this.player + this.player) {
					for (j in pattern_objects){
						if (this.player == 'X') {
							color = "blue";
						} else {
							color = "red";
						}
						pattern_objects[j].css({
							"color" : "white",
							"background" : "rgb(255,215,0)"							
						});
						pattern_objects[j].hover(
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
					return true;
				}
			}
		}
		return false;
	},

	is_game_tied: function() { // do better for ai eventually
		for (i = 0; i < 9; i++) {
			if ($('#' + i).html() == '') {
				return false;
            }
		}
		return true;
	},

	end_game: function(winner) {
		if (winner) {
			swal({
				title: winner + ' won!',
				text: "Play again?",
				icon: "success",
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
		} else {
			swal({
				title: 'The game ended in a tie',
				text: "Play again?",
				icon: "warning",
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
		}
	}
};

function resizeAll(){
	var square_size = 0.18 * Math.min($(window).width(), $(window).height());
	var border_size = 0.02 * square_size;
	var font_size = square_size / 2;
	$(".square").css({"width" : square_size.toString(),
					  "height" : square_size.toString(),
					  "border" : border_size.toString() + "px solid #ff2a2a70",
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