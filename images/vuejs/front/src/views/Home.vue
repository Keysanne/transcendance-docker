<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-4xl md:text-5xl lg:text-6xl text-center">{{ text.welcome[lang] }}</h1>
        <h3 class="text-gray-300">{{ text.best[lang] }}</h3>
        <h4 class="text-white opacity-25 text-sm">{{ text.goty[lang] }}</h4>

        <div class="d-grid gap-3 col-6 col-md-3 mx-auto mt-20">
            <router-link to="/play" class="btn btn-light btn-lg" type="button">{{ text.play[lang] }}</router-link>
            <router-link to="/leaderboard" class="btn btn-light btn-lg" type="button">{{ text.leaderboard[lang] }}</router-link>
            <router-link to="/tournaments" class="btn btn-light btn-lg" type="button">{{ text.tournaments[lang] }}</router-link>
        </div>

    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';

export default {
    data() {
        return {
            text: {
                welcome: ["Welcome to transcendance!", "Bienvenue sur transcendance !", "「Transcendance」へようこそ !"],
                best: ["The best pong game in the world", "Le meilleur pong du monde", "世界最高のポンゲーム"],
                goty: ["(GOTY 2024)", "(GOTY 2024)", "「GOTY 2024」"],
                play: ["Play", "Jouer", "プレイ"],
                leaderboard: ["Leaderboard", "Classement", "ランキング"],
                tournaments: ["Tournaments", "Tournois", "トーナメント"],
            },
        }
    },
    components: {
        Navbar,
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