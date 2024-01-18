<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-4xl md:text-5xl lg:text-6xl text-center">{{ text.choose[lang] }}</h1>

        <div class="d-grid gap-3 col-6 col-md-3 mx-auto mt-20">
            <router-link to="/pong" class="btn btn-light btn-lg">{{ text.easy[lang] }}</router-link>
            <router-link to="/pong" class="btn btn-light btn-lg">{{ text.medium[lang] }}</router-link>
			<router-link to="/pong" class="btn btn-light btn-lg">{{ text.hard[lang] }}</router-link>
        </div>

    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';

export default {
    data() {
        return {
            text: {
                choose: ["Select your difficulty", "Choisis une difficulte"],
                easy: ["Easy", "Facile"],
                medium: ["Medium", "Moyen"],
                hard: ["Hard", "Difficile"],
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