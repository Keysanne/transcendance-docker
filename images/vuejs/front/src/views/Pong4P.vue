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
import axios from 'axios';

export default {
	data() {
		return {
			board: undefined,
			boardWidth: 700,
			boardHeight: 700,
			context: undefined,

			playerVWidth: 10,
			playerVHeight: 80,
			playerHWidth: 80,
			playerHHeight: 10,
			player1Score: 0,
			player2Score: 0,
			player3Score: 0,
			player4Score: 0,
			player1: undefined,
			player2: undefined,
			player3: undefined,
			player4: undefined,
			playerVelocityY: 0,
			playerVelocityX: 0,
			
			ballWidth: 10,
			ballHeight: 10,
			ball:undefined,
			acceleration: 2,
			isstart: 0,
			gameover: 0,
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
			this.context.fillRect(this.player3.x, this.player3.y, this.player3.width, this.player3.height);
			this.context.fillRect(this.player4.x, this.player4.y, this.player4.width, this.player4.height);

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
			
			let nextPlayer3X = this.player3.x + this.player3.velocityX;
			if (!this.outOfBoundX(nextPlayer3X)) {
				this.player3.x += this.player3.velocityX;
			}
			this.context.fillRect(this.player3.x, this.player3.y, this.player3.width, this.player3.height);

			let nextPlayer4X = this.player4.x + this.player4.velocityX;
			if (!this.outOfBoundX(nextPlayer4X)) {
				this.player4.x += this.player4.velocityX;
			}
			this.context.fillRect(this.player4.x, this.player4.y, this.player4.width, this.player4.height);
			
			this.detectCollision()
			this.ball.x += this.ball.velocityX * this.acceleration;
			this.ball.y += this.ball.velocityY * this.acceleration;
			this.detectCollision();
			if (this.ball.y <= 0) {
				this.givepuntos();
				this.resetGame(-1);
			}
			else if (this.ball.y + this.ball.height >= this.boardHeight) {
				this.givepuntos();
				this.resetGame(1);
			}
			else if (this.ball.x < 0) {
				this.givepuntos();
				this.resetGame(1);
			}
			else if (this.ball.x + this.ballWidth > this.boardWidth) {
				this.givepuntos();
				this.resetGame(-1);                                                                                                                                                 
			}
			this.context.fillRect(this.ball.x, this.ball.y, this.ball.width, this.ball.height);

			this.context.font = "25px 'Press Start 2P'";
			if (this.player1Score >= 5) {
				this.endgame(1);
			}
			else if (this.player2Score >= 5) {
				this.endgame(0);
			}
			else if (this.player3Score >= 5) {
				this.endgame(2);
			}
			else if (this.player4Score >= 5) {
				this.endgame(3);
			}
			if (this.isstart == 0) {
				// this.context.fillText("Press a key to start", 5, 160);
				this.context.fillText("W / S", 140, 365);
				this.context.fillText("UP / DOWN", 400, 365);
				this.context.fillText("B / N", 290, 170);
				this.context.fillText("X / C", 290, 555);
			}
			this.context.fillText(this.player1Score, 40, 365);
			this.context.fillText(this.player2Score, 640, 365);
			this.context.fillText(this.player3Score, 340, 65);
			this.context.fillText(this.player4Score, 340, 660);
		
			for (let d = 10; d < this.board.height; d += 25) {
				this.context.fillRect(d, d, 5, 5);
			}
			for (let d = this.board.height - 10; d > 0; d -= 25) {
				this.context.fillRect(d, this.board.height - d, -5, 5);
			}
		},
		givepuntos() {
			if (this.player1.puntos == 1) {
				this.player1Score += 1;
			}
			if (this.player2.puntos == 1) {
				this.player2Score += 1;
			}
			if (this.player3.puntos == 1) {
				this.player3Score += 1;
			}
			if (this.player4.puntos == 1) {
				this.player4Score += 1;
			}
		},
		endgame(e) {
			if(e == 1){
				this.context.fillText("WINNER", 115, 365);
				this.context.fillText("LOSER", 450, 365);
				this.context.fillText("LOSER", 290, 200);
				this.context.fillText("LOSER", 290, 525);
			}
			else if (e == 0){
				this.context.fillText("WINNER", 440, 365);
				this.context.fillText("LOSER", 125, 365);
				this.context.fillText("LOSER", 290, 200);
				this.context.fillText("LOSER", 290, 525);
			}
			else if (e == 2){
				this.context.fillText("WINNER", 275, 200);
				this.context.fillText("LOSER", 125, 365);
				this.context.fillText("LOSER", 290, 525);
				this.context.fillText("LOSER", 450, 365);
			}
			else if (e == 3){
				this.context.fillText("WINNER", 275, 525);
				this.context.fillText("LOSER", 125, 365);
				this.context.fillText("LOSER", 450, 365);
				this.context.fillText("LOSER", 290, 200);
			}
			this.context.fillText("Press any key", 190, 260);
			this.context.fillText("to restart", 230, 300);
			this.resetGame(0);
			this.gameover = 1;
			this.ball.velocityY = 0;
			this.acceleration = 0;
		},
		movePlayer(e) {
			if (this.isstart == 0 && (e.code == "KeyW" || e.code == "KeyS" || e.code == "ArrowUp" || e.code == "ArrowDown" || e.code == "KeyB" || e.code == "KeyN" || e.code == "KeyX" || e.code == "KeyC")) {
				this.isstart = 1;
				this.gostart();
			}
			else if (this.gameover == 1) {
				this.gostart();
			}
			if (this.player1Score >= 5 || this.player2Score >= 5 || this.player3Score >= 5 || this.player4Score >= 5){
				return;
			}
			if (e.code == "KeyW") {
				this.player1.velocityY = -7;
			}
			else if (e.code == "KeyS") {
				this.player1.velocityY = 7;
			}

			if (e.code == "ArrowUp") {
				this.player2.velocityY = -7;
			}
			else if (e.code == "ArrowDown") {
				this.player2.velocityY = 7;
			}

			if (e.code == "KeyB") {
				this.player3.velocityX = -7;
			}
			else if (e.code == "KeyN") {
				this.player3.velocityX = 7;
			}

			if (e.code == "KeyX") {
				this.player4.velocityX = -7;
			}
			else if (e.code == "KeyC") {
				this.player4.velocityX = 7;
			}
		},
		gostart() {
			this.gameover = 0;
			this.player1Score = 0;
			this.player2Score = 0;
			this.player3Score = 0;
			this.player4Score = 0;
			this.acceleration = 2,
			this.ball = {
				x: (this.boardWidth / 2) - (this.ballWidth / 2) - 7,
				y: (this.boardHeight / 2) - (this.ballHeight / 2),
				width: this.ballWidth,
				height: this.ballHeight,
				velocityX: 1,
				velocityY: 0
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

			if (e.code == "KeyB") {
				this.player3.velocityX = 0;
			}
			else if (e.code == "KeyN") {
				this.player3.velocityX = 0;
			}

			if (e.code == "KeyX") {
				this.player4.velocityX = 0;
			}
			else if (e.code == "KeyC") {
				this.player4.velocityX = 0;
			}
		},
		outOfBound(yPosition) {
			return (yPosition < 0 || yPosition + this.playerVHeight > this.boardHeight);
		},
		outOfBoundX(xPosition) {
			return (xPosition < 0 || xPosition + this.playerHWidth > this.boardHeight);
		},
		resetpuntos() {
			this.player1.puntos = 0;
			this.player2.puntos = 0;
			this.player3.puntos = 0;
			this.player4.puntos = 0;
		},
		detectCollision() {
			let cal = 0; 
			let last = 1;
			if ((this.ball.y >= this.player1.y && this.ball.y <= this.player1.y + 80) && (this.ball.x <= this.player1.x + 10)) {
				cal = (this.ball.y - this.player1.y) / 40 - 1;
				if (cal < -0.45){
					this.ball.velocityX = 0.5;
					this.ball.velocityY = -0.5;
				}
				else if (cal < -0.05){
					this.ball.velocityX = 0.75;
					this.ball.velocityY = -0.25;
				}
				else if (cal < 0.05){
					this.ball.velocityX = 1;
					this.ball.velocityY = 0;
				}
				else if (cal < 0.55){
					this.ball.velocityX = 0.75;
					this.ball.velocityY = 0.25;
				}
				else if (cal <= 1){
					this.ball.velocityX = 0.5;
					this.ball.velocityY = 0.5;
				}
				if (this.acceleration <= 28) {
					this.acceleration += 0.25;
				}
				this.ball.x = this.player1.x + 11;
				this.resetpuntos();
				this.player1.puntos = 1;
			}
			if ((this.ball.y >= this.player2.y && this.ball.y <= this.player2.y + 80) && (this.ball.x >= this.player2.x - 10)) {
				cal = (this.ball.y - this.player2.y) / 40 - 1;

				if (cal < -0.45){
					this.ball.velocityX = -0.5;
					this.ball.velocityY = -0.5;
				}
				else if (cal < -0.05){
					this.ball.velocityX = -0.75;
					this.ball.velocityY = -0.25;
				}
				else if (cal < 0.05){
					this.ball.velocityX = -1;
					this.ball.velocityY = 0;
				}
				else if (cal < 0.55){
					this.ball.velocityX = -0.75;
					this.ball.velocityY = 0.25;
				}
				else if (cal <= 1){
					this.ball.velocityX = -0.5;
					this.ball.velocityY = 0.5;
				}
				if (this.acceleration <= 28) {
					this.acceleration += 0.25;
				}
				this.ball.x = this.player2.x - 11;
				this.resetpuntos();
				this.player2.puntos = 1;
			}
			if ((this.ball.y <= this.player3.y + 10) && (this.ball.x >= this.player3.x && this.ball.x <= this.player3.x + 80)) {
				cal = (this.ball.x - this.player3.x) / 40 - 1;

				if (cal < -0.45){
					this.ball.velocityX = -0.5;
					this.ball.velocityY = 0.5;
				}
				else if (cal < -0.05){
					this.ball.velocityX = -0.25;
					this.ball.velocityY = 0.75;
				}
				else if (cal < 0.05){
					this.ball.velocityX = 0;
					this.ball.velocityY = 1;
				}
				else if (cal < 0.55){
					this.ball.velocityX = 0.25;
					this.ball.velocityY = 0.75;
				}
				else if (cal <= 1){
					this.ball.velocityX = 0.5;
					this.ball.velocityY = 0.5;
				}
				if (this.acceleration <= 28) {
					this.acceleration += 0.25;
				}
				this.ball.y = this.player3.y + 11;
				this.resetpuntos();
				this.player3.puntos = 1;
			}
			if ((this.ball.y + 10 >= this.player4.y) && (this.ball.x >= this.player4.x && this.ball.x <= this.player4.x + 80)) {
				cal = (this.ball.x - this.player4.x) / 40 - 1;

				if (cal < -0.45){
					this.ball.velocityX = -0.5;
					this.ball.velocityY = -0.5;
				}
				else if (cal < -0.05){
					this.ball.velocityX = -0.25;
					this.ball.velocityY = -0.75;
				}
				else if (cal < 0.05){
					this.ball.velocityX = 0;
					this.ball.velocityY = -1;
				}
				else if (cal < 0.55){
					this.ball.velocityX = 0.25;
					this.ball.velocityY = -0.75;
				}
				else if (cal <= 1){
					this.ball.velocityX = 0.5;
					this.ball.velocityY = -0.5;
				}
				if (this.acceleration <= 28) {
					this.acceleration += 0.25;
				}
				this.ball.y = this.player4.y - 11;
				this.resetpuntos();
				this.player4.puntos = 1;
			}
		},
		resetGame(direction) {
			this.acceleration = 2;
				this.player1 = {
				x: 10,
				y: (this.boardHeight / 2) - (this.playerVHeight / 2),
				width: this.playerVWidth,
				height: this.playerVHeight,
				velocityY: this.playerVelocityY,
				puntos: 0
			};
			this.player2 = {
				x: this.boardWidth - this.playerVWidth - 10,
				y: (this.boardHeight / 2) - (this.playerVHeight / 2),
				width: this.playerVWidth,
				height: this.playerVHeight,
				velocityY: this.playerVelocityY,
				puntos: 0
			};
			this.player3 = {
				x: (this.boardHeight / 2) - (this.playerVHeight / 2),
				y: 10,
				width: this.playerHWidth,
				height: this.playerHHeight,
				velocityX: this.playerVelocityX,
				puntos: 0
			};
			this.player4 = {
				x: (this.boardHeight / 2) - (this.playerVHeight / 2),
				y: this.boardWidth - this.playerVWidth - 10,
				width: this.playerHWidth,
				height: this.playerHHeight,
				velocityX: this.playerVelocityX,
				puntos: 0
			};
			this.ball = {
				x: (this.boardWidth / 2) - (this.ballWidth / 2),
				y: (this.boardHeight / 2) - (this.ballHeight / 2),
				width: this.ballWidth,
				height: this.ballHeight,
				velocityX: direction,
				velocityY: 0
			};
		}
	},
	mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })
		this.player1 = {
			x: 10,
			y: (this.boardHeight / 2) - (this.playerVHeight / 2),
			width: this.playerVWidth,
			height: this.playerVHeight,
			velocityY: this.playerVelocityY,
			puntos: 0,
		};
		this.player2 = {
			x: this.boardWidth - this.playerVWidth - 10,
			y: (this.boardHeight / 2) - (this.playerVHeight / 2),
			width: this.playerVWidth,
			height: this.playerVHeight,
			velocityY: this.playerVelocityY,
			puntos: 0,
		};
		this.player3 = {
			x: (this.boardHeight / 2) - (this.playerVHeight / 2),
			y: 10,
			width: this.playerHWidth,
			height: this.playerHHeight,
			velocityX: this.playerVelocityX,
			puntos: 0,
		};
		this.player4 = {
			x: (this.boardHeight / 2) - (this.playerVHeight / 2),
			y: this.boardWidth - this.playerVWidth - 10,
			width: this.playerHWidth,
			height: this.playerHHeight,
			velocityX: this.playerVelocityX,
			puntos: 0,
		};
		this.ball = {
			x: (this.boardWidth / 2) - (this.ballWidth / 2),
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