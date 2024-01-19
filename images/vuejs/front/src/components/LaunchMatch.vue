<template>
    <div>
		<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  			Launch the next match
		</button>

		<div class="modal fade modal-dialog modal-xl" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title fs-5 text-light" id="exampleModalLabel">Next match</h5>
						<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<div class="modal-body flex items-center">
						<img class="w-16 h-16 rounded-full" src="../assets/avatars/todo.jpg" alt="profile_pic">
						<div class="flex flex-col">
                            <h5 class="text-lg font-semibold text-light ml-3 my-0">{{players[0].nickname}}</h5>
                            <h5 class="text-lg text-secondary ml-3 my-0">{{players[0].username}}</h5>
                        </div>
						<div>
							<h1 class="text-light ml-3">VS</h1>
						</div>
						<div class="flex flex-col items-end">
							<h5 class="text-lg font-semibold text-light ml-3 my-0">{{players[1].nickname}}</h5>
                            <h5 class="text-lg text-secondary ml-3 my-0">{{players[1].username}}</h5>
                        </div>
						<img class="w-16 h-16 rounded-full ml-3" src="../assets/avatars/todo.jpg" alt="profile_pic">
                    </div>
				<div class="modal-footer">
				<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
				<button type="button" class="btn btn-primary">Start the match</button>
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
    props: {
        players: Array
    }
}
</script>