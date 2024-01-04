<template>
    <div class="card w-full sm:w-[47.5%] my-3">
        <div class="card-body flex flex-col justify-between">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <p class="card-text">{{ description }}</p>
            </div>
            <div class="flex justify-between items-center mt-3">
                <div>{{ nb_players }} / {{ max_players }}</div>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#' + modal_id">See details</button>
            </div>
        </div>
    </div>

    <div class="modal fade" :id="modal_id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">{{ name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div>
                        {{ description }}
                    </div>
                    <h5 class="mt-3">Players</h5>
                    <div class="flex flex-col">
                        <MyTournamentCardPlayer v-for="player in players" :username="player.username" :nickname="player.nickname" :image="player.image"/>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" :disabled="nb_players < max_players">Start tournament</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import MyTournamentCardPlayer from './MyTournamentCardPlayer.vue';

export default {
    props: {
        id: Number,
        name: String,
        description: String,
        max_players: Number,
        players: Array,
    },
    computed: {
        nb_players: function() {
            return this.players.length
        },
        
        modal_id: function() {
            return "modal" + this.id.toString()
        }
    },
    components: {
        MyTournamentCardPlayer,
    },
}
</script>