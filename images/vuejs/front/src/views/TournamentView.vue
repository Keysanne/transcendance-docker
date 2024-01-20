<template>
	<div class="d-flex flex-column align-items-center">
		<Navbar />

		<div class="d-flex flex-column mt-36 w-[90%] max-w-[722px]">
			<h2 class="text-light">{{ name }}</h2>
			<p class="mt-3 text-light">{{ description }}</p>
			<LaunchMatch :players="players"/>

			<TournamentTree class="mt-3" :size="max_players" :players="players" />
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
			name: "Tournament test",
			description: "Irure tempor amet mollit incididunt commodo consectetur aliqua. Ex ullamco enim labore laboris irure culpa incididunt. Nisi ipsum dolor laborum cupidatat ut elit dolore nulla. Mollit Lorem veniam reprehenderit occaecat excepteur veniam minim sunt proident cupidatat excepteur. Cillum ea reprehenderit adipisicing do aute non cupidatat. Enim ad laborum ad sunt cillum eiusmod eu.",
			players: [
				{
					username: "player1",
					nickname: "Player1nick",
					image: "",
					stage: 2,
				},
				{
					username: "player2",
					nickname: "Player2nick",
					image: "",
					stage: 0,
				},
				{
					username: "player3",
					nickname: "Player3nick",
					image: "",
					stage: 0,
				},
				{
					username: "player4",
					nickname: "Player4nick",
					image: "",
					stage: 1,
				},
				{
					username: "player5",
					nickname: "Player5nick",
					image: "",
					stage: 0,
				},
				{
					username: "player6",
					nickname: "Player6nick",
					image: "",
					stage: 0,
				},
				{
					username: "player7",
					nickname: "Player7nick",
					image: "",
					stage: 0,
				},
				{
					username: "player8",
					nickname: "Player8nick",
					image: "",
					stage: 0,
				},
				{
					username: "player9",
					nickname: "Player9nick",
					image: "",
					stage: 0,
				},
				{
					username: "player10",
					nickname: "Player10nick",
					image: "",
					stage: 0,
				},
				{
					username: "player11",
					nickname: "Player11nick",
					image: "",
					stage: 4,
				},
				{
					username: "player12",
					nickname: "Player12nick",
					image: "",
					stage: 0,
				},
				{
					username: "player13",
					nickname: "Player13nick",
					image: "",
					stage: 0,
				},
				{
					username: "player14",
					nickname: "Player14nick",
					image: "",
					stage: 0,
				},
				{
					username: "player15",
					nickname: "Player15nick",
					image: "",
					stage: 0,
				},
				{
					username: "player16",
					nickname: "Player16nick",
					image: "",
					stage: 0,
				},
			],
			max_players: 16,
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
	},
	components: {
    Navbar,
    TournamentTree,
    LaunchMatch
}
}
</script>

