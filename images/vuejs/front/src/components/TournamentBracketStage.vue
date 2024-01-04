<template>
	<div class="flex flex-col justify-evenly">
		<TournamentBracketElt v-for="item in stage" :players="item" class="mb-4"/>
	</div>
</template>

<style>

</style>

<script>
import TournamentBracketElt from './TournamentBracketElt.vue';

export default {
	props: {
		stage: {
			type: Array,
			required: false,
		}
	},
	components: {
		TournamentBracketElt,
	}
}
</script>