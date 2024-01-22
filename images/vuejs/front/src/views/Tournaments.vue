<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-36 max-w-[722px]">
            <h1 class="text-4xl text-light">Tournaments</h1>

            <div class="flex justify-between items-center w-[90%] xl:w-full mt-16">
                <h3 class="text-light">My Tournaments</h3>
                <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#new_tournament_modal">New</button>

                <div class="modal fade" id="new_tournament_modal" tabindex="-1" aria-labelledby="new_tournament_modal_label" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5 text-light" id="new_tournament_modal_label">New tournament</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating">
                                    <input v-model="new_tournament_name" type="text" class="form-control" id="new_tournament_name" placeholder="name">
                                    <label for="new_tournament_name">Name</label>
                                </div>
                                <div class="form-floating mt-3">
                                    <textarea v-model="new_tournament_description" class="form-control" style="height: 128px;" id="new_tournament_description" placeholder="description"></textarea>
                                    <label for="new_tournament_description">Description</label>
                                </div>
                                <div class="form-floating">
                                    <select v-model="new_tournament_size" class="form-select mt-3" id="new_tournament_size">
                                        <option>4</option>
                                        <option>8</option>
                                        <option>16</option>
                                    </select>
                                    <label for="new_tournament_size">Select a size</label>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" :disabled="new_tournament_name == '' || new_tournament_description == '' || new_tournament_size == ''">Create tournament</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="flex justify-between flex-wrap w-[90%] xl:w-full">
                <MyTournamentCard v-for="tournament in my_tournaments" :id="tournament.id" :name="tournament.name" :description="tournament.description" :max_players="tournament.max_players" :players="tournament.players" />
            </div>

            <div class="w-[90%] xl:w-full bg-gray-700/50 h-[2px] mt-16 mb-16"></div>
 
            <div class="flex justify-start w-[90%] xl:w-full">
                <h2 class="text-light">Join a tournament</h2>
            </div>
            <div class="flex justify-between flex-wrap w-[90%] xl:w-full">
                <TournamentCard v-for="tournament in tournaments" :id="tournament.id" :name="tournament.name" :description="tournament.description" :nb_players="tournament.nb_players" :max_players="tournament.max_players" :registered="tournament.registered" />
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

export default {
    data() {
        return {
            new_tournament_name: "",
            new_tournament_description: "",
            new_tournament_size: "",
            tournaments: [
                {
                    id: 5,
                    name: "Name",
                    description: "Simple tournament description",
                    nb_players: 9,
                    max_players: 16,
                    registered: true,
                },
                {
                    id: 6,
                    name: "Another name",
                    description: "Another simple tournament description",
                    nb_players: 3,
                    max_players: 8,
                    registered: false,
                },
                {
                    id: 7,
                    name: "Another name",
                    description: "Another simple tournament description sdlkjflksajd kalsdj fklasj dflkaj",
                    nb_players: 3,
                    max_players: 8,
                    registered: false,
                },
                {
                    id: 8,
                    name: "Another name",
                    description: "Another simple tournament description",
                    nb_players: 8,
                    max_players: 8,
                    registered: false,
                },
                {
                    id: 9,
                    name: "Another name",
                    description: "Another simple tournament description",
                    nb_players: 3,
                    max_players: 8,
                    registered: false,
                },
            ],
            my_tournaments: [
                {
                    id: 10,
                    name: "My tournament",
                    description: "My tournament description",
                    max_players: 16,
                    players: [
                        {
                            username: "player1",
                            nickname: "Player1 nick",
                            image: "",
                        },
                        {
                            username: "player2",
                            nickname: "Player2 nick",
                            image: "",
                        },
                        {
                            username: "player3",
                            nickname: "Player3 nick",
                            image: "",
                        },
                        {
                            username: "player1",
                            nickname: "Player1 nick",
                            image: "",
                        },
                        {
                            username: "player2",
                            nickname: "Player2 nick",
                            image: "",
                        },
                        {
                            username: "player3",
                            nickname: "Player3 nick",
                            image: "",
                        },
                        {
                            username: "player1",
                            nickname: "Player1 nick",
                            image: "",
                        },
                        {
                            username: "player2",
                            nickname: "Player2 nick",
                            image: "",
                        },
                        {
                            username: "player3",
                            nickname: "Player3 nick",
                            image: "",
                        },
                        {
                            username: "player1",
                            nickname: "Player1 nick",
                            image: "",
                        },
                        {
                            username: "player2",
                            nickname: "Player2 nick",
                            image: "",
                        },
                        {
                            username: "player3",
                            nickname: "Player3 nick",
                            image: "",
                        },
                    ],
                },
                {
                    id: 11,
                    name: "My tournament 2",
                    description: "My tournament 2 description",
                    max_players: 16,
                    players: [
                        {
                            username: "player1",
                            nickname: "Player1 nick",
                            image: "",
                        },
                        {
                            username: "player2",
                            nickname: "Player2 nick",
                            image: "",
                        },
                        {
                            username: "player3",
                            nickname: "Player3 nick",
                            image: "",
                        },
                    ],
                },
            ]
        }
    },
    components:{
        Navbar,
        TournamentCard,
        MyTournamentCard,
    }
}
</script>