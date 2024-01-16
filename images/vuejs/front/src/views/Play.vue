<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-4xl md:text-5xl lg:text-6xl text-center">Choose your game mode</h1>

        <div class="d-grid gap-3 col-6 col-md-3 mx-auto mt-20">
            <router-link to="/difficulty" class="btn btn-light btn-lg">Solo vs AI</router-link>
			<router-link to="/pong" class="btn btn-light btn-lg">Local 1 vs 1</router-link>
            <router-link to="/pong4p" class="btn btn-light btn-lg">Local 1 vs 1 vs 1 vs 1</router-link>
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
    }
}
</script>