<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-36">
            <h1 class="text-4xl text-light">{{ text.leaderboard[lang] }}</h1>
            <div class="flex flex-col mt-6 w-[90vw] max-w-[722px] rounded-lg border-1 border-gray-700/50">
                <LeaderboardPlayer v-for="player in players" :rank="player.rank" :username="player.username" :pic="player.pic" :elo="player.elo" :is_last="player.is_last"/>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';
import LeaderboardPlayer from '../components/LeaderboardPlayer.vue';
import axios from 'axios';

export default {
    data() {
        return {
            text: {
                leaderboard: ["Leaderboard", "Classement", "ランキング"],
            },

            players: [],
        }
    },
    components: {
        LeaderboardPlayer,
        Navbar,
    },
    mounted() {
    	if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
    	const URL = "http://127.0.0.1:8000/user/leaderboard/"
	    axios.get(URL, {
	    	headers: {
	    		'Authorization': 'Bearer ' + localStorage.getItem("access")
	    	}
        }).then(response => {
            this.players = []
            var j = 1
            for (var i in response.data){
                var player = {}
                player["rank"] = j
                player["username"] = response.data[i].username
                player["pic"] = response.data[i].pfp
                player["elo"] = response.data[i].elo
                player["is_last"] = false
                this.players.push(player)
                j += 1
            }
            this.players[this.players.length - 1]["is_last"] = true
	    })
	    .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })
    },
    computed: {
        lang: function() {
            if (localStorage.getItem("lang") === null) {
                localStorage.setItem("lang", 0)
            }
            return localStorage.getItem("lang")
        }
    }
}

</script>
