<template>
    <div class="d-flex flex-column align-items-center justify-center min-h-screen bg-[url(https://integraales.fr/wp-content/uploads/2019/12/source.gif)] bg-no-repeat bg-cover">
        <Navbar />
        <h1 class="text-white text-8xl">404 not found</h1>
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