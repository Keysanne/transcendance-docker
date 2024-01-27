<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-36 max-w-[722px]">
            <h1 class="text-4xl text-light">{{ text.tournaments[lang] }}</h1>

            <div class="flex justify-between items-center w-full mt-16">
                <h3 class="text-light">{{ text.my_tournaments[lang] }}</h3>
                <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#new_tournament_modal">{{ text.new[lang] }}</button>

                <div class="modal fade" id="new_tournament_modal" tabindex="-1" aria-labelledby="new_tournament_modal_label" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5 text-light" id="new_tournament_modal_label">{{ text.new_tournament[lang] }}</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating">
                                    <input v-model="new_tournament_name" type="text" class="form-control" id="new_tournament_name" placeholder="name">
                                    <label for="new_tournament_name">{{ text.name[lang] }}</label>
                                </div>
                                <div class="form-floating mt-3">
                                    <textarea v-model="new_tournament_description" class="form-control" style="height: 128px;" id="new_tournament_description" placeholder="description"></textarea>
                                    <label for="new_tournament_description">{{ text.description[lang] }}</label>
                                </div>
                                <div class="form-floating">
                                    <select v-model="new_tournament_size" class="form-select mt-3" id="new_tournament_size">
                                        <option>4</option>
                                        <option>8</option>
                                        <option>16</option>
                                    </select>
                                    <label for="new_tournament_size">{{ text.size[lang] }}</label>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ text.close[lang] }}</button>
                                <button type="button" class="btn btn-primary" :disabled="new_tournament_name == '' || new_tournament_description == '' || new_tournament_size == ''" @click="createTournament">{{ text.create[lang] }}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="my_tournaments == null || my_tournaments.length == 0" class="w-[90vw] max-w-[722px]">
                <div class="card bg-dark border-secondary border-opacity-50 text-light w-full my-3">
                    <div class="card-body">
                        <div class="card-text text-center">{{ text.no_tournaments[lang] }}</div>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-between flex-wrap w-full">
                <MyTournamentCard v-for="tournament in my_tournaments" :id="tournament.id" :name="tournament.name" :description="tournament.description" :max_players="tournament.max_players" :players="tournament.players" :status="tournament.status" />
            </div>

            <div class="w-[90%] xl:w-full bg-gray-700/50 h-[2px] mt-16 mb-16"></div>
 
            <div class="flex justify-start w-full">
                <h2 class="text-light">{{ text.join[lang] }}</h2>
            </div>
            <div v-if="tournaments == null || tournaments.length == 0" class="w-[90vw] max-w-[722px]">
                <div class="card bg-dark border-secondary border-opacity-50 text-light w-full my-3">
                    <div class="card-body">
                        <div class="card-text text-center">{{ text.no_tournaments[lang] }}</div>
                    </div>
                </div>
            </div>
            <div v-else class="flex justify-between flex-wrap w-full">
                <TournamentCard v-for="tournament in tournaments" :id_t="tournament.id" :name="tournament.name" :description="tournament.description" :nb_players="tournament.nb_players" :max_players="tournament.max_players" :registered="tournament.registered" />
            </div>
        </div>
    </div>
</template>

<style>
label {
    color:#6c757d
}
</style>

<script>
import Navbar from '../components/Navbar.vue';
import TournamentCard from '../components/TournamentCard.vue';
import MyTournamentCard from '../components/MyTournamentCard.vue';
import axios from 'axios';

export default {
    data() {
        return {
            text: {
                tournaments: ["Tournaments", "Tournois", "トーナメント"],
                my_tournaments: ["My Tournaments", "Mes tournois", "私のトーナメント"],
                new: ["New", "Nouveau", "新しい"],
                new_tournament: ["New tournament", "Nouveau tournois", "新たなイベント"],
                name: ["Name", "Nom", "名前"],
                description: ["Description", "Description", "記述"],
                size: ["Select a size", "Choisis une taille", "サイズを選択する"],
                close: ["Close", "Fermer", "閉じる"],
                create: ["Create tournament", "Créer le tournois", "トーナメントを作成"],
                join: ["Join a tournament", "Rejoindre un tournois", "トーナメントに参加する"],
                no_tournaments: ["No tournaments yet...", "Pas encore de tournois ...", "まだトーナメントはありません..."]
            },

            new_tournament_name: "",
            new_tournament_description: "",
            new_tournament_size: "",
            tournaments: [],
            my_tournaments: []
        }
    },
    components:{
        Navbar,
        TournamentCard,
        MyTournamentCard,
    },
    mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        var URL = import.meta.env.VITE_URL_BASE + "tournament/list/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            for (var i in response.data.tournaments) {
                var tournament = {}
                tournament["id"] = response.data.tournaments[i].pk
                tournament["name"] = response.data.tournaments[i].name
                tournament["description"] = response.data.tournaments[i].description
                tournament["max_players"] = response.data.tournaments[i].capacity
                tournament["status"] = response.data.tournaments[i].status

                var id_list = []
                for (var j in response.data.tournaments[i].contestants) {
                    id_list.push(response.data.tournaments[i].contestants[j].user.toString())
                }

                if (localStorage.getItem("pk") == response.data.tournaments[i].organizer) {
                    var players = []
                    for (j in response.data.tournaments[i].contestants) {
                        var player = {}
                        player["username"] = response.data.tournaments[i].contestants[j].username
                        player["nickname"] = response.data.tournaments[i].contestants[j].nickname
                        player["image"] = response.data.tournaments[i].contestants[j].pfp
                        players.push(player)
                    }
                    tournament["players"] = players
                    this.my_tournaments.push(tournament)
                }
                else if (tournament["status"] == 0 && id_list.includes(localStorage.getItem("pk"))) {
                    tournament["registered"] = true
                    tournament["nb_players"] = response.data.tournaments[i].contestants.length
                    this.tournaments.push(tournament)
                }
                else if (tournament["status"] == 0) {
                    tournament["registered"] = false
                    tournament["nb_players"] = response.data.tournaments[i].contestants.length
                    this.tournaments.push(tournament)
                }
            }
        })
        .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })

        URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/status/1/"
		axios.get(URL, {
			headers: {
				'Authorization': 'Bearer ' + localStorage.getItem("access")
			}
		})
    },
    computed: {
        lang: function() {
            if (localStorage.getItem("lang") === null) {
                localStorage.setItem("lang", 0)
            }
            return localStorage.getItem("lang")
        }
    },
    methods: {
        createTournament() {
            const URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/createtournament/"
            axios.post(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access"),
                    'Content-Type': 'application/json'
                },
                params: {
                    name: this.new_tournament_name,
                    description: this.new_tournament_description,
                    capacity: this.new_tournament_size
                }
            })
            .then(response => {
                location.reload()
            })
        }
    }
}
</script>