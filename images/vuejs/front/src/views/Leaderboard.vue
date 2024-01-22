<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-36">
            <h1 class="text-4xl text-light">Leaderboard</h1>
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
            players: [
                {
                    rank: 1,
                    username: "SkibidiPlayer1",
                    pic: "",
                    elo: 5603,
                    is_last: false
                },
                {
                    rank: 2,
                    username: "Player2",
                    pic: "",
                    elo: 5403,
                    is_last: false
                },
                {
                    rank: 3,
                    username: "Player3",
                    pic: "",
                    elo: 4932,
                    is_last: false
                },
                {
                    rank: 4,
                    username: "Player4",
                    pic: "",
                    elo: 4567,
                    is_last: false
                },
                {
                    rank: 5,
                    username: "Player5",
                    pic: "",
                    elo: 3877,
                    is_last: true
                },
                
            ]
        }
    },
    components: {
        LeaderboardPlayer,
        Navbar,
    },
    mounted() {
        const URL = "http://127.0.0.1:8000/user/leaderboard"
        axios.get(URL).then(response => {
            this.players = []
            var i = 1
            for (var elt in response.data) {
                var player = {}
                player["rank"] = i
                player["username"] = response.data[elt].username
                player["pic"] = response.data[elt].pfp
                player["elo"] = response.data[elt].elo
                player["is_last"] = false
                this.players.push(player)
                i += 1
            }
            this.players[this.players.length - 1]["is_last"] = true
        })
        .catch(error => {
            console.log(error)
        })
    }
}

</script>