<template>
	<div class="d-flex flex-column align-items-center justify-center min-h-screen">
		<Navbar />
		<canvas class="font-pixel" id = board></canvas>
	</div>
</template>

<style>
	body{
		text-align: center;
	}
	#board{
		background-color: black;
		border-top: 5px solid white;
		border-bottom: 5px solid white;
		border-left: 5px solid white;
		border-right: 5px solid white;
	}
</style>

<script>
import Navbar from '../components/Navbar.vue';

export default {
	data() {
		return {
			board: undefined,
			boardWidth: 900,
			boardHeight: 600,
			context: undefined,

			playerWidth: 10,
			playerHeight: 80,
			player1Score: 0,
			player2Score: 0,
			player1: undefined,
			player2: undefined,
			playerVelocityY: 0,

			ballWidth: 10,
			ballHeight: 10,
			ball:undefined,
			isstart: 0,
		}
	},
	components: {
		Navbar,
	},
	methods: {
		initializeBoard() {
			this.board = document.getElementById("board");
			this.board.height = this.boardHeight;
			this.board.width = this.boardWidth;
			this.context = this.board.getContext("2d");
		
			this.context.fillStyle = "white";
			this.context.fillRect(this.player1.x, this.player1.y, this.player1.width, this.player1.height);
			this.context.fillRect(this.player2.x, this.player2.y, this.player2.width, this.player2.height);

			requestAnimationFrame(this.update);
			document.addEventListener("keydown", this.movePlayer);
			document.addEventListener("keyup", this.stopMovePlayer);
		},
		update() {
			requestAnimationFrame(this.update);
			this.context.clearRect(0, 0, this.board.width, this.board.height);

			this.context.fillStyle = "white";

			let nextPlayer1Y = this.player1.y + this.player1.velocityY;
			if (!this.outOfBound(nextPlayer1Y)) {
				this.player1.y += this.player1.velocityY;
			}
			this.context.fillRect(this.player1.x, this.player1.y, this.player1.width, this.player1.height);
			
			let nextPlayer2Y = this.player2.y + this.player2.velocityY;
			if (!this.outOfBound(nextPlayer2Y)) {
				this.player2.y += this.player2.velocityY;
			}
			this.context.fillRect(this.player2.x, this.player2.y, this.player2.width, this.player2.height);
		
			this.ball.x += this.ball.velocityX;
			this.ball.y += this.ball.velocityY;
			this.ball.velocityX *= 1.001;
			this.ball.velocityY *= 1.001;
			this.context.fillRect(this.ball.x, this.ball.y, this.ball.width, this.ball.height);
			if (this.ball.y <= 0 || (this.ball.y + this.ball.height >= this.boardHeight)) {
				this.ball.velocityY *= -1;
			}
			this.detectCollision();
			// if (this.detectCollision(this.ball, this.player1)) {
			// 	if (this.ball.x <= this.player1.x + this.player1.width) {
			// 		this.ball.velocityX *= -1;
			// 	}
			// }
			// else if (this.detectCollision(this.ball, this.player2)) {
			// 	if (this.ball.x + this.ballWidth >= this.player2.x) {
			// 		this.ball.velocityX *= -1;
			// 	}
			// }

			if (this.ball.x < 0) {
				this.player2Score += 1;
				this.resetGame(1);
			}
			else if (this.ball.x + this.ballWidth > this.boardWidth) {
				this.player1Score += 1;
				this.resetGame(-1);
			}

			this.context.font = "40px 'Press Start 2P'";
			if (this.player1Score >= 5) {
				this.endgame(1);
			}
			else if (this.player2Score >= 5) {
				this.endgame(0);
			}
			if (this.isstart == 0) {
				this.context.fillText("Press a key to start", 50, 160);
				this.context.fillText("W / S", 120, 320);
				this.context.fillText("UP / DOWN", 490, 320);
			}
			this.context.fillText(this.player1Score, 200, 60);
			this.context.fillText(this.player2Score, 655, 60);
		
			for (let d = 10; d < this.board.height; d += 25) {
				this.context.fillRect(this.board.width / 2 - 10, d, 5, 5);
			}
		},
		endgame(e) {
			if(e == 1){
				this.context.fillText("WINNER", 95, 320);
				this.context.fillText("LOSER", 570, 320);
			}
			else {
				this.context.fillText("LOSER", 120, 320);
				this.context.fillText("WINNER", 550, 320);
			}
			this.resetGame(0);
			this.ball.velocityY = 0;
		},
		movePlayer(e) {
			if (this.isstart == 0 && (e.code == "KeyW" || e.code == "KeyS" || e.code == "ArrowUp" || e.code == "ArrowDown")) {
				this.isstart = 1;
				this.gostart();
			}

			if (e.code == "KeyW") {
				this.player1.velocityY = -5;
			}
			else if (e.code == "KeyS") {
				this.player1.velocityY = 5;
			}

			if (e.code == "ArrowUp") {
				this.player2.velocityY = -5;
			}
			else if (e.code == "ArrowDown") {
				this.player2.velocityY = 5;
			}
		},
		gostart() {
			this.ball = {
				x: (this.boardWidth / 2) - (this.ballWidth / 2) - 7,
				y: (this.boardHeight / 2) - (this.ballHeight / 2),
				width: this.ballWidth,
				height: this.ballHeight,
				velocityX: 1,
				velocityY: 2
			};
		},
		stopMovePlayer(e) {
			if (e.code == "KeyW") {
				this.player1.velocityY = 0;
			}
			else if (e.code == "KeyS") {
				this.player1.velocityY = 0;
			}

			if (e.code == "ArrowUp") {
				this.player2.velocityY = 0;
			}
			else if (e.code == "ArrowDown") {
				this.player2.velocityY = 0;
			}
		},
		outOfBound(yPosition) {
			return (yPosition < 0 || yPosition + this.playerHeight > this.boardHeight);
		},
		detectCollision() {
			if ((this.ball.y >= this.player1.y && this.ball.y <= this.player1.y + 80) && (this.ball.x <= this.player1.x + 10)) {
				this.ball.velocityX *= -1;
				this.ball.velocityY *= -1;
				this.ball.x = this.player1.x + 11;
			}
			if ((this.ball.y >= this.player2.y && this.ball.y <= this.player2.y + 80) && (this.ball.x <= this.player1.x)) {
				this.ball.velocityX *= -1;
				this.ball.velocityY *= -1;
			}
		},
		resetGame(direction) {
				this.player1 = {
				x: 10,
				y: (this.boardHeight / 2) - (this.playerHeight / 2),
				width: this.playerWidth,
				height: this.playerHeight,
				velocityY: this.playerVelocityY
			};
			this.player2 = {
				x: this.boardWidth - this.playerWidth - 10,
				y: (this.boardHeight / 2) - (this.playerHeight / 2),
				width: this.playerWidth,
				height: this.playerHeight,
				velocityY: this.playerVelocityY
			};
			this.ball = {
				x: (this.boardWidth / 2) - (this.ballWidth / 2) - 7,
				y: (this.boardHeight / 2) - (this.ballHeight / 2),
				width: this.ballWidth,
				height: this.ballHeight,
				velocityX: direction,
				velocityY: 2
			};
		}
	},
	mounted() {
		this.player1 = {
			x: 10,
			y: (this.boardHeight / 2) - (this.playerHeight / 2),
			width: this.playerWidth,
			height: this.playerHeight,
			velocityY: this.playerVelocityY,
		};
		this.player2 = {
			x: this.boardWidth - this.playerWidth - 10,
			y: (this.boardHeight / 2) - (this.playerHeight / 2),
			width: this.playerWidth,
			height: this.playerHeight,
			velocityY: this.playerVelocityY,
		};
		this.ball = {
			x: (this.boardWidth / 2) - (this.ballWidth / 2) - 7,
			y: (this.boardHeight / 2) - (this.ballHeight / 2),
			width: this.ballWidth,
			height: this.ballHeight,
			velocityX: 0,
			velocityY: 0
		};
		this.initializeBoard();
 	},
}
</script>