<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-36">
            <div class="d-flex align-items-center w-[90%]">
                <input type="file" class="hidden" id="image_upload" ref="image_upload" accept="image/png, image/jpeg" @change="uploadImage">
                <div class="group w-2/5 max-w-[10rem] relative rounded-circle" @click="changeImage">
                    <div class="border-2 border-primary rounded-circle w-full h-full bg-black absolute opacity-[0.01] group-hover:opacity-70 transition ease-in-out"></div>
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" class="text-white opacity-[0.01] group-hover:opacity-70 w-[50%] h-[50%] top-[50%] left-[50%] translate-y-[-50%] translate-x-[-50%] absolute transition ease-in-out"/>
                    <img class="border-2 border-light rounded-circle w-full" src="../assets/avatars/todo.jpg" alt="profile_pic">
                </div>
                
                <div class="d-flex flex-column ml-6">
                    <h1 class="text-2xl font-semibold text-light">{{ username }}</h1>
                    <button type="button" class="btn btn-sm btn-danger" data-bs-toggle="modal" data-bs-target="#password_modal">{{ text.change_password[lang] }}</button>
                    <button type="button" v-if="twoFA == false" class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#twoFA_mail_modal">{{ text.enable_2fa[lang] }}</button>
                    <button type="button" v-else class="btn btn-sm btn-primary" @click="disable_2fa">{{ text.disable_2fa[lang] }}</button>
    
                    <div class="modal fade" id="password_modal" tabindex="-1" aria-labelledby="password_modal_label" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5 text-light" id="password_modal_label">{{ text.change_password[lang] }}</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="text.close[lang]"></button>
                                </div>
                                <div class="modal-body">
                                    <div class="form-floating">
                                        <input v-model="current_password" type="text" :class="current_password_label != text.current_password[lang] ? 'is-invalid' : ''" class="form-control" id="current_password" placeholder="current password">
                                        <label for="current_password">{{ current_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="new_password" type="text" :class="new_password_label != text.new_password[lang] ? 'is-invalid' : ''" class="form-control" id="new_password" placeholder="new password">
                                        <label for="new_password">{{ new_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="confirm_new_password" type="text" :class="confirm_new_password_label != text.confirm_new_password[lang] ? 'is-invalid' : ''" class="form-control" id="confirm_new_password" placeholder="confirm new password">
                                        <label for="confirm_new_password">{{ confirm_new_password_label }}</label>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ text.close[lang] }}</button>
                                    <button type="button" class="btn btn-primary">{{ text.save_changes[lang] }}</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="modal fade" id="twoFA_mail_modal" tabindex="-1" aria-labelledby="twoFA_mail_modal_label" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5 text-light" id="twoFA_mail_modal_label">{{ text.mail[lang] }}</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="text.close[lang]"></button>
                                </div>
                                <div class="modal-body">
                                    <input v-model="twoFA_mail" type="email" class="form-control" id="twoFA_mail">
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ text.close[lang] }}</button>
                                    <button type="button" class="btn btn-primary" @click="sendMail">{{ text.send[lang] }}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <button type="button" class="hidden" data-bs-toggle="modal" data-bs-target="#twoFA_modal_code" id="open_modal"></button>
                    <div class="modal fade" id="twoFA_modal_code"  data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="twoFA_modal_code_label" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5 text-light" id="twoFA_modal_code_label">{{ text.enter_2fa[lang] }}</h1>
                                </div>
                                <div class="modal-body">
                                    <input v-model="twoFA_code" type="text" class="form-control" id="twoFA_code">
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="hidden" data-bs-dismiss="modal" id="close_modal"></button>
                                    <button type="button" class="btn btn-primary" @click="sendCode">{{ text.send[lang] }}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
            <div class="card w-[90%] mt-6 text-bg-dark border-secondary">
                <div class="card-header text-xl font-semibold">
                    Stats
                </div>
                <div class="card-body">
                    <div class="container text-center">
                        <div class="row row-cols-2">
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ totalGame }}</h5>
                                        <p class="card-text">{{ text.total_games[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ winRate }}%</h5>
                                        <p class="card-text">{{ text.win_rate[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ elo }}</h5>
                                        <p class="card-text">{{ text.elo[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ rank }}</h5>
                                        <p class="card-text">{{ text.rank[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ best_elo }}</h5>
                                        <p class="card-text">{{ text.best_elo[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <div class="card border-dark">
                                    <div class="card-body">
                                        <h5 class="card-title text-3xl">{{ best_rank }}</h5>
                                        <p class="card-text">{{ text.best_rank[lang] }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
            <div class="card text-bg-dark border-secondary w-[90%] mt-6 mb-6">
                <div class="card-header text-xl font-semibold">
                    {{ text.match_history[lang] }}
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
            text: {
                change_password: ["Change password", "Changer le mot de passe"],
                enable_2fa: ["Enable 2FA", "Activer l'A2F"],
                disable_2fa: ["Disable 2FA", "Desactiver l'A2F"],
                close: ["Close", "Fermer"],
                current_password: ["Current password", "Mot de passe actuel"],
                new_password: ["New password", "Nouveau mot de passe"],
                confirm_new_password: ["Confirm new password", "Confirmation du nouveau mot de passe"],
                save_changes: ["Save changes", "Sauvegarder les changements"],
                total_games: ["Total games", "Nombre de parties"],
                win_rate: ["Win rate", "Taux de victoire"],
                elo: ["Elo", "Elo"],
                rank: ["Rank", "Classement"],
                best_elo: ["Best elo", "Meilleur elo"],
                best_rank: ["Best rank", "Meilleur classement"],
                match_history: ["Match history", "Historique des matchs"],
                mail: ["Enter your email address", "Entrez votre adresse email"],
                send: ["Send", "Envoyer"],
                enter_2fa: ["Enter the code", "Entrez le code"],
            },

            twoFA_mail: "",
            twoFA_code: "",
            twoFA: false,
            username: "Username",
            wins: 12,
            losses: 5,
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
        },
        lang: function() {
            if (localStorage.getItem("lang") === null) {
                localStorage.setItem("lang", 0)
            }
            return localStorage.getItem("lang")
        }
    },
    methods: {
        changeImage() {
            document.getElementById("image_upload").click()
        },

        uploadImage() {
            let image = this.$refs.image_upload.files[0];
            let formData = new FormData();
            formData.append('image_upload', image);
            // formData.append('_method', 'PATCH');

            axios.post('http://127.0.0.1:8000/user/update/' + localStorage.getItem("pk") + "/",
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': 'Bearer ' + localStorage.getItem("access")
                    }
                }).then(response => {
                    console.log(response)
                    const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/"
                    axios.get(URL, {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem("access")
                        }
                    })
                    .then(response => {
                        this.image_url = response.data.pfp;
                    })
                }).catch(response => {
                    console.log(response)
            });
        },
        enable_2fa() {
            const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/update-2fa/?mode=true"
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.twoFA = true
            })
            .catch(error => {
                console.log(error)
            })
        },
        disable_2fa() {
            const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/update-2fa/?mode=false"
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.twoFA = false
            })
            .catch(error => {
                console.log(error)
            })
        },
        sendMail() {
            const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/verif_mail/?email=" + this.twoFA_mail
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                document.getElementById("open_modal").click()
            })
            .catch(error => {
                console.log(error)
            })
        },
        sendCode() {
            const URL =  "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/verif_mail_key/?email=" + this.twoFA_mail + "&code=" + this.twoFA_code
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.enable_2fa()
                document.getElementById("close_modal").click()
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        this.current_password_label = this.text.current_password[this.lang]
        this.new_password_label = this.text.new_password[this.lang]
        this.confirm_new_password_label = this.text.confirm_new_password[this.lang]

        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            this.username = response.data.username;
            this.wins = response.data.wins;
            this.losses = response.data.losses;
            this.rank = response.data.rank;
            this.best_rank = response.data.best_rank;
            this.elo = response.data.elo;
            this.best_elo = response.data.best_elo;
            this.image_url = response.data.pfp;
            this.twoFA = response.data.twoFA
        }) 
    },
    components: {
        Navbar,
        MatchHistoryElt,
    }
}
</script>