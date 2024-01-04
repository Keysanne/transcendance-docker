<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center">
            <div class="d-flex mt-20 align-items-center w-[90%]">
                <input type="file" class="hidden" id="image_upload" ref="image_upload" accept="image/png, image/jpeg" @change="uploadImage">
                <div class="group w-2/5 max-w-[10rem] relative rounded-circle" @click="changeImage">
                    <div class="border-2 border-primary rounded-circle w-full h-full bg-black absolute opacity-[0.01] group-hover:opacity-70 transition ease-in-out"></div>
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" class="text-white opacity-[0.01] group-hover:opacity-70 w-[50%] h-[50%] top-[50%] left-[50%] translate-y-[-50%] translate-x-[-50%] absolute transition ease-in-out"/>
                    <img class="border-2 border-primary rounded-circle w-full" :src="image_url" alt="profile_pic">
                </div>
                
                <div class="d-flex flex-column ml-6">
                    <h1 class="text-2xl font-semibold">{{ username }}</h1>
                    <button type="button" class="btn btn-sm btn-danger" data-bs-toggle="modal" data-bs-target="#password_modal">Change password</button>
    
                    <div class="modal fade" id="password_modal" tabindex="-1" aria-labelledby="password_modal_label" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="password_modal_label">Change password</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <div class="form-floating">
                                        <input v-model="current_password" type="text" :class="current_password_label != 'Current password' ? 'is-invalid' : ''" class="form-control" id="current_password" placeholder="current password">
                                        <label for="current_password">{{ current_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="new_password" type="text" :class="new_password_label != 'New password' ? 'is-invalid' : ''" class="form-control" id="new_password" placeholder="new password">
                                        <label for="new_password">{{ new_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="confirm_new_password" type="text" :class="confirm_new_password_label != 'Confirm new password' ? 'is-invalid' : ''" class="form-control" id="confirm_new_password" placeholder="confirm new password">
                                        <label for="confirm_new_password">{{ confirm_new_password_label }}</label>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" class="btn btn-primary">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
            <div class="card w-[90%] mt-6 text-bg-primary border-light">
                <div class="card-header text-xl font-semibold">
                    Stats
                </div>
                <div class="card-body">
                    <div class="container text-center">
                        <div class="row row-cols-2">
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ totalGame }}</h5>
                                        <p class="card-text">Total games</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ winRate }}%</h5>
                                        <p class="card-text">Win rate</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ elo }}</h5>
                                        <p class="card-text">Elo</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ rank }}</h5>
                                        <p class="card-text">Rank</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ best_elo }}</h5>
                                        <p class="card-text">Best elo</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card text-bg-primary border-primary">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ best_rank }}</h5>
                                        <p class="card-text">Best rank</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
            <div class="card w-[90%] text-bg-primary mt-6 mb-6 border-light">
                <div class="card-header text-xl font-semibold">
                    Match history
                </div>
                <ul class="list-group list-group-flush">
                    <MatchHistoryElt v-for="match in match_history" :username_player1="username" :username_player2="match.username_player2" :score_player1="match.score_player1" :score_player2="match.score_player2" :date="match.date" />
                </ul>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import Navbar from '../components/Navbar.vue';
import MatchHistoryElt from '../components/MatchHistoryElt.vue';
import axios from 'axios';

export default {
    data() {
        return {
            username: "Username",
            wins: 12,
            losses: 5,
            // coins:10245,
            rank: 23,
            best_rank: 4,
            elo: 566,
            best_elo: 1076,
            current_password: "",
            new_password: "",
            confirm_new_password: "",
            current_password_label: "Current password",
            new_password_label: "New password",
            confirm_new_password_label: "Confirm new password",
            image_url: "",
            match_history: [
                {
                    score_player1: 5,
                    score_player2: 3,
                    username_player2: "player24",
                    date: "12-04-2023",
                },
                {
                    score_player1: 5,
                    score_player2: 2,
                    username_player2: "player23",
                    date: "12-04-2023",
                },
                {
                    score_player1: 2,
                    score_player2: 5,
                    username_player2: "player22",
                    date: "11-04-2023",
                },
                {
                    score_player1: 5,
                    score_player2: 4,
                    username_player2: "player21",
                    date: "09-04-2023",
                },
                {
                    score_player1: 1,
                    score_player2: 5,
                    username_player2: "player20",
                    date: "09-04-2023",
                },
            ],          
        }
    },
    computed: {
        winRate: function() {
            return (this.wins / (this.losses + this.wins)).toFixed(3) * 100
        },
        totalGame: function() {
            return this.wins + this.losses
        }
    },
    methods: {
        changeImage: function() {
            document.getElementById("image_upload").click()
        },

        uploadImage: function() {
            let image = this.$refs.image_upload.files[0];
            let formData = new FormData();
            formData.append('image_upload', image);
            // formData.append('_method', 'PATCH');

            axios.post('http://127.0.0.1:8000/user/update/18/',
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    }
                }).then(response => {
                    console.log(response)
                    const URL = "http://127.0.0.1:8000/user/18/"
                    axios.get(URL)
                    .then(response => {
                        this.image_url = response.data.pfp;
                    })
                }).catch(response => {
                    console.log(response)
                });
        },

    },
    mounted() {
        const URL = "http://127.0.0.1:8000/user/18/"
        axios.get(URL)
        .then(response => {
            this.username = response.data.username;
            this.wins = response.data.wins;
            this.losses = response.data.losses;
            this.rank = response.data.rank;
            this.best_rank = response.data.best_rank;
            this.elo = response.data.elo;
            this.best_elo = response.data.best_elo;
            this.image_url = response.data.pfp;
        }) 
    },
    components: {
        Navbar,
        MatchHistoryElt,
    }
}
</script>