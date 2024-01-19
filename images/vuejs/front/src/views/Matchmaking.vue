<template>
	<div class="d-flex flex-column align-items-center justify-center min-h-screen">
		<Navbar />
		<LaunchMatch :players="players"/>
	</div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';
import LaunchMatch from '../components/LaunchMatch.vue';

export default {
	data() {
		return {
			players: [
				{
					username: "User1",
					nickname: "Nick",
					image: ""
				},
				{
					username: "User2",
					nickname: "Nick",
					image: ""
				}
			]
		}
	},
	components: {
		Navbar,
		LaunchMatch,
	}
}
</script>