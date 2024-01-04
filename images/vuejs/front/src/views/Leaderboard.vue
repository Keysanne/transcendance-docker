<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-20">
            <h1 class="text-4xl text-primary">Leaderboard</h1>
            <div class="flex flex-col mt-6 w-[90vw] max-w-[722px]">
                <LeaderboardPlayer v-for="player in players" :rank="player.rank" :username="player.username" :pic="player.pic" :elo="player.elo"/>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';
import LeaderboardPlayer from '../components/LeaderboardPlayer.vue';

export default {
    data() {
        return {
            players: [
                {
                    rank: 1,
                    username: "Player1",
                    pic: 2,
                    elo: 5603,
                },
                {
                    rank: 2,
                    username: "Player2",
                    pic: 4,
                    elo: 5403,
                },
                {
                    rank: 3,
                    username: "Player3",
                    pic: 3,
                    elo: 4932,
                },
                {
                    rank: 4,
                    username: "Player4",
                    pic: 6,
                    elo: 4567,
                },
                {
                    rank: 5,
                    username: "Player5",
                    pic: 0,
                    elo: 3877,
                },
                
            ]
        }
    },
    components: {
        LeaderboardPlayer,
        Navbar,
    }
}

</script>