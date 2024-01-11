<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        
        <h1 class="text-white text-6xl">Select your difficulty</h1>

        <div class="d-grid gap-3 col-3 mx-auto mt-20">
            <router-link to="/pong" class="btn btn-light btn-lg">Easy</router-link>
            <router-link to="/pong" class="btn btn-light btn-lg">Medium</router-link>
			<router-link to="/pong" class="btn btn-light btn-lg">Hard</router-link>
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