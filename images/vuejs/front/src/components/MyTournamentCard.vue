<template>
    <div class="card bg-dark border-secondary border-opacity-50 text-light w-full sm:w-[47.5%] my-3">
        <div class="card-body flex flex-col justify-between">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <p class="card-text">{{ description }}</p>
            </div>
            <div class="flex justify-between items-center mt-3">
                <div>{{ nb_players }} / {{ max_players }}</div>
                <button type="button" class="btn btn-secondary" data-bs-toggle="modal" :data-bs-target="'#' + modal_id" :id="'close' + modal_id">{{ text.details[lang] }}</button>
            </div>
        </div>
    </div>

    <div class="modal fade" :id="modal_id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-light" id="exampleModalLabel">{{ name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="text-light">
                        {{ description }}
                    </div>
                    <h5 class="mt-3 text-light">{{ text.players[lang] }}</h5>
                    <div v-if="players == null || players.length == 0" class="text-light">
                        {{ text.no_players[lang] }}
                    </div>
                    <div v-else class="flex flex-col">
                        <MyTournamentCardPlayer v-for="player in players" :username="player.username" :nickname="player.nickname" :image="player.image"/>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ text.close[lang] }}</button>
                    <button v-if="status == 0" type="button" class="btn btn-primary" :disabled="nb_players < max_players" @click="startTournament">{{ text.start[lang] }}</button>
                    <button v-else type="button" class="btn btn-primary" @click="pushTournamentTree">{{ text.tree[lang] }}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import MyTournamentCardPlayer from './MyTournamentCardPlayer.vue';
import axios from 'axios';

export default {

    data() {
        return {
            text: {
                details: ["Details", "Détails", "詳細"],
                players: ["Players", "Joueurs", "プレイヤー"],
                close: ["Close", "Fermer", "閉じる"],
                start: ["Start tournament", "Commencer le tournois", "トーナメント開始"],
                no_players: ["No players yet...", "Pas encore de joueurs ...", "まだプレイヤーはいません..."],
                tree: ["Tournament page", "Page du tournois", "トーナメントページ"],
            },
        }
    },
    props: {
        id: Number,
        name: String,
        description: String,
        max_players: Number,
        players: Array,
        status: Number,
    },
    computed: {
        nb_players: function() {
            return this.players.length
        },
        
        modal_id: function() {
            return "modal" + this.id.toString()
        },

        lang: function() {
            if (localStorage.getItem("lang") === null) {
                localStorage.setItem("lang", 0)
            }
            return localStorage.getItem("lang")
        }
    },
    components: {
        MyTournamentCardPlayer,
    },
    methods: {
        startTournament() {
            const URL = import.meta.env.VITE_URL_BASE + "tournament/" + this.id + "/start/"
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                this.pushTournamentTree()
            })
        },
        pushTournamentTree() {
            document.getElementById("close" + this.modal_id).click()
            this.$router.push({path: '/tournament/' + this.id})
        }
    }
}
</script>