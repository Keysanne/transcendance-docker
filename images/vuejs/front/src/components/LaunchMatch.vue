<template>
    <div>
		<!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  			Launch the next match
		</button>

		<div class="modal fade modal-dialog modal-xl" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title fs-5 text-light" id="exampleModalLabel">Next match</h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" id="close_button"></button>
					</div>
					<div class="modal-body flex items-center justify-between">
						<div class="flex items-center">
							<img v-if="players[0].image == null || players[0].image == ''" class="w-16 h-16 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
                			<img v-else class="w-16 h-16 rounded-full" :src="players[0].image" alt="profile_pic">
							<div class="flex flex-col ml-3">
                       	    	<h5 class="text-lg font-semibold text-light my-0">{{players[0].nickname}}</h5>
                      	    	<h5 class="text-lg text-secondary my-0">{{players[0].username}}</h5>
                        	</div>
						</div>
						<div>
							<h1 class="text-light ml-3">VS</h1>
						</div>
						<div class="flex items-center">
							<div class="flex flex-col items-center mr-3">
								<h5 class="text-lg font-semibold text-light my-0">{{players[1].nickname}}</h5>
                            	<h5 class="text-lg text-secondary my-0">{{players[1].username}}</h5>
                        	</div>
							<img v-if="players[1].image == null || players[1].image == ''" class="w-16 h-16 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
                			<img v-else class="w-16 h-16 rounded-full" :src="players[1].image" alt="profile_pic">
						</div>
                    </div>
				<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
				<button type="button" class="btn btn-primary" @click="startMatch">Start the match</button>
				</div>
				</div>
			</div>
		</div> -->

		<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#match_modal">{{ text.launch[lang] }}</button>
		<div class="modal modal-lg fade" id="match_modal" tabindex="-1" aria-labelledby="match_modal_label" aria-hidden="true">
			<div class="modal-dialog modal-dialog-centered">
				<div class="modal-content">
					<div class="modal-header">
						<h1 class="modal-title fs-5 text-light" id="match_modal_label">{{ text.next[lang] }}</h1>
						<button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="text.close[lang]"></button>
					</div>
					<div class="modal-body flex items-center justify-between">
						<div class="flex items-center">
							<img v-if="players[0].image == null || players[0].image == ''" class="w-16 h-16 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
                			<img v-else class="w-16 h-16 rounded-full" :src="players[0].image" alt="profile_pic">
							<div class="flex flex-col ml-3">
                       	    	<h5 class="text-lg font-semibold text-light my-0">{{players[0].nickname}}</h5>
                      	    	<h5 class="text-lg text-secondary my-0">{{players[0].username}}</h5>
                        	</div>
						</div>
						<div>
							<h1 class="text-light ml-3">VS</h1>
						</div>
						<div class="flex items-center">
							<div class="flex flex-col items-center mr-3">
								<h5 class="text-lg font-semibold text-light my-0">{{players[1].nickname}}</h5>
                            	<h5 class="text-lg text-secondary my-0">{{players[1].username}}</h5>
                        	</div>
							<img v-if="players[1].image == null || players[1].image == ''" class="w-16 h-16 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
                			<img v-else class="w-16 h-16 rounded-full" :src="players[1].image" alt="profile_pic">
						</div>
                    </div>
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close_button">{{ text.close[lang] }}</button>
						<button type="button" class="btn btn-primary" @click="startMatch">{{ text.start[lang] }}</button>
					</div>
				</div>
			</div>
		</div>
    </div>
</template>

<style>

</style>

<script>
export default {
	data() {
		return {
			text: {
				next: ["Next match", "Prochain match"],
				close: ["Close", "Fermer"],
				start: ["Start the match", "Commencer le match"],
				launch: ["Launch the next match", "Lancer le prochain match"]
			}
		}
	},
    props: {
        players: Array,
		tournament_id: String,
    },
	methods: {
		startMatch() {
			document.getElementById("close_button").click()
			this.$router.push({path: "/pong/" + this.tournament_id + "/" + this.players[0].id + "/" + this.players[1].id})
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