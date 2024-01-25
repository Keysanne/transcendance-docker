<template>
	<div class="d-flex flex-column align-items-center">
		<Navbar />

		<div class="d-flex flex-column mt-36 w-[90%] max-w-[722px]">
			<h2 class="text-light">{{ name }}</h2>
			<p class="mt-3 text-light">{{ description }}</p>
			<LaunchMatch v-if="max_players && players && check_end() == 0" :players="next_p" :tournament_id="this.$route.params.id"/>

			<TournamentTree v-if="max_players && players" class="mt-3" :size="max_players" :players="players" />
		</div>
	</div>
</template>

<style>

</style>

<script>
import LaunchMatch from '../components/LaunchMatch.vue';
import Navbar from '../components/Navbar.vue'
import TournamentTree from '../components/TournamentTree.vue';
import axios from 'axios';

export default {
	data() {
		return {
			name: "",
			description: "",
			players: [],
			max_players: 0,
			num: 0,
			next_p: [],
		}
	},
	methods: {
		check_next() {
			if (this.round_1() == 1) {
				return ;
			}
			if (this.round_2() == 1) {
				return ;
			}
			if (this.max_players >= 8)
			{
				if (this.round_3() == 1) {
					return ;
				}
			}
			if (this.max_players >= 16)
			{
				if (this.round_4() == 1) {
					return ;
				}
			}
		},
		round_1() {
			for (let i = 0; i < this.max_players; i += 2) {
				if (this.players[i].stage == this.players[i + 1].stage)
				{
					this.next_p[0] = this.players[i];
					this.next_p[1] = this.players[i + 1];
					return 1;
				}
			}
			return 0;
		},
		round_2() {
			let n = 0;
			for (let i = 0; i < this.max_players; i += 4) {
				for (let y = i; y < i + 4; y++) {
					if (this.players[y].stage == 1) {
						this.next_p[n] = this.players[y];
						n++;
					}
					if (n >= 2) {
						return 1;
					}
				}
				n = 0;
			}
			return 0;
		},
		round_3(){
			let n = 0;
			for (let i = 0; i < this.max_players; i += 8) {
				for (let y = i; y < i + 8; y++) {
					if (this.players[y].stage == 2) {
						this.next_p[n] = this.players[y];
						n++;
					}
					if (n >= 2) {
						return 1;
					}
				}
				n = 0;
			}
			return 0;
		},
		round_4(){
			let n = 0;
			for (let i = 0; i < this.max_players; i++) {
				if(this.players[i].stage == 3) {
					this.next_p[n] = this.players[i];
					n++;
				}
				if (n >= 2) {
					return 1;
				}
			}
			return 0;
		},
		check_end() {
			let save = 0;
			for(let i = 0; i < this.max_players; i++) {
				if (this.players[i].stage > save) {
					save = this.players[i].stage;
				}
			}
			if (this.max_players == 16 && save == 4) {
				return 1;
			}
			else if (this.max_players == 8 && save == 3) {
				return 1;
			}
			else if (this.max_players == 4 && save == 2) {
				return 1;
			}
			else {
				return 0;
			}
		}
	},
	mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        const URL = "http://127.0.0.1:8000/tournament/" + this.$route.params.id + "/contestant-list/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
		.then(response => {
			if (localStorage.getItem("pk") != response.data.organizer) {
				this.$router.push({path: '/'})
			}
			this.name = response.data.name
			this.description = response.data.description
			this.max_players = response.data.contestants.length
			this.players = []
			for (var i in response.data.contestants) {
				var player = {}
				player["id"] = response.data.contestants[i].pk
				player["username"] = response.data.contestants[i].username
				player["nickname"] = response.data.contestants[i].nickname
				player["image"] = response.data.contestants[i].pfp
				player["stage"] = response.data.contestants[i].stage
				this.players.push(player)
			}
			this.check_next();
		})
        .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })
	},
	components: {
		Navbar,
		TournamentTree,
		LaunchMatch
	}
}
</script>