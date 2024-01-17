<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-4xl md:text-5xl lg:text-6xl text-center">Welcome to transcendance!</h1>
        <h3 class="text-gray-300">The best pong game in the world</h3>
        <h4 class="text-white opacity-25 text-sm">(GOTY 2024)</h4>

        <div class="d-grid gap-3 col-6 col-md-3 mx-auto mt-20">
            <router-link to="/play" class="btn btn-light btn-lg" type="button">Play</router-link>
            <router-link to="/leaderboard" class="btn btn-light btn-lg" type="button">Leaderboard</router-link>
            <router-link to="/tournaments" class="btn btn-light btn-lg" type="button">Tournaments</router-link>
        </div>

    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';

export default {
    components: {
        Navbar,
    },
    mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
    }
}
</script>