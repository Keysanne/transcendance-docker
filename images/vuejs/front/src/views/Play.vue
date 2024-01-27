<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-4xl md:text-5xl lg:text-6xl text-center">{{ text.choose[lang] }}</h1>

        <div class="d-grid gap-3 col-6 col-md-3 mx-auto mt-20">
            <router-link to="/difficulty" class="btn btn-light btn-lg">{{ text.solo[lang] }}</router-link>
			<router-link to="/pong" class="btn btn-light btn-lg">{{ text.local[lang] }}</router-link>
            <router-link to="/pong4p" class="btn btn-light btn-lg">{{ text.local_4[lang] }}</router-link>
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
                choose: ["Choose your game mode", "Choisis ton mode de jeu", "ゲームモードを選択してください"],
                solo: ["Solo vs AI", "Solo vs IA", "ソロ vs IA"],
                local: ["Local 1 vs 1", "Local 1 vs 1", "ローカル 1 vs 1"],
                local_4: ["Local 1 vs 1 vs 1 vs 1", "Local 1 vs 1 vs 1 vs 1", "ローカル 1 vs 1 vs 1 vs 1"],
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
        var URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/"
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

        URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/status/1/"
		axios.get(URL, {
			headers: {
				'Authorization': 'Bearer ' + localStorage.getItem("access")
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