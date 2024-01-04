<template>
	<div class="d-flex flex-column align-items-center justify-center min-h-screen">
		<Navbar />
		<div class="text-center flex items-center">
			<h1 class="display-1">Matchmaking</h1>
			<div class="spinner-border ml-5" style="width: 3rem; height: 3rem;" role="status">
				<span class="visually-hidden">Matchmaking</span>
			</div>	
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