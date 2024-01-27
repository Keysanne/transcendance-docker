<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />

        <div class="d-flex flex-column align-items-center mt-[8.5rem]">
            <div class="d-flex align-items-center w-[90%]">
                <input type="file" class="hidden" id="image_upload" ref="image_upload" accept="image/png, image/jpeg" @change="uploadImage">
                <div class="group w-2/5 max-w-[10rem] relative rounded-circle" @click="changeImage">
                    <div class="border-2 border-light rounded-circle w-full h-full bg-black absolute opacity-[0.01] group-hover:opacity-70 group-hover:cursor-pointer transition ease-in-out"></div>
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" class="text-white opacity-[0.01] group-hover:opacity-70 w-[50%] h-[50%] top-[50%] left-[50%] translate-y-[-50%] translate-x-[-50%] absolute transition ease-in-out"/>
                    <img v-if="image_url == null || image_url == ''" class="border-2 border-light rounded-circle w-full" src="../assets/default_profile.png" alt="profile_pic">
                    <img v-else class="border-2 border-light rounded-circle w-full" :src="image_url" alt="profile_pic">
                </div>
                
                <div class="d-flex flex-column ml-6">
                    <h1 class="text-2xl font-semibold text-light">{{ username }}</h1>
                    <button type="button" class="btn btn-sm btn-danger mb-2" data-bs-toggle="modal" data-bs-target="#password_modal">{{ text.change_password[lang] }}</button>
                    <button type="button" v-if="is_remote == false && twoFA == false" class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#twoFA_mail_modal">{{ text.enable_2fa[lang] }}</button>
                    <button type="button" v-else-if="is_remote == false" class="btn btn-sm btn-primary" @click="disable_2fa">{{ text.disable_2fa[lang] }}</button>
    
                    <div class="modal fade" id="password_modal" tabindex="-1" aria-labelledby="password_modal_label" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5 text-light" id="password_modal_label">{{ text.change_password[lang] }}</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="text.close[lang]"></button>
                                </div>
                                <div class="modal-body">
                                    <div class="form-floating">
                                        <input v-model="current_password" type="password" :class="current_password_label != text.current_password[lang] ? 'is-invalid' : ''" class="form-control" id="current_password" placeholder="current password">
                                        <label for="current_password">{{ current_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="new_password" type="password" :class="new_password_label != text.new_password[lang] ? 'is-invalid' : ''" class="form-control" id="new_password" placeholder="new password">
                                        <label for="new_password">{{ new_password_label }}</label>
                                    </div>
                                    <div class="form-floating mt-3">
                                        <input v-model="confirm_new_password" type="password" :class="confirm_new_password_label != text.confirm_new_password[lang] ? 'is-invalid' : ''" class="form-control" id="confirm_new_password" placeholder="confirm new password">
                                        <label for="confirm_new_password">{{ confirm_new_password_label }}</label>
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close_password_modal">{{ text.close[lang] }}</button>
                                    <button type="button" class="btn btn-primary" :disabled="current_password == '' || new_password == '' || confirm_new_password == ''" @click="updatePassword">{{ text.save_changes[lang] }}</button>
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
                                    <button type="button" class="hidden" data-bs-dismiss="modal" id="close_code_modal"></button>
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
                <div v-if="match_history.length == 0" class="card-body flex justify-center">
                    {{ text.no_games[lang] }}
                </div>
                <ul v-else class="list-group list-group-flush">
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
                change_password: ["Change password", "Changer le mot de passe", "パスワード変更"],
                enable_2fa: ["Enable 2FA", "Activer l'A2F", "可能にする A2F"],
                disable_2fa: ["Disable 2FA", "Désactiver l'A2F", "無効にし A2F"],
                close: ["Close", "Fermer", "閉じる"],
                current_password: ["Current password", "Mot de passe actuel", "現在のパスワード"],
                new_password: ["New password", "Nouveau mot de passe", "新しいパスワード"],
                confirm_new_password: ["Confirm new password", "Confirmation du nouveau mot de passe", "新しいパスワードの確認"],
                save_changes: ["Save changes", "Sauvegarder les changements", "変更を保存し"],
                total_games: ["Total games", "Nombre de parties", "総ゲーム"],
                win_rate: ["Win rate", "Taux de victoire", "勝率"],
                elo: ["Elo", "Elo", "エロ"],
                rank: ["Rank", "Classement", "ランク"],
                best_elo: ["Best elo", "Meilleur elo", "最高エロ"],
                best_rank: ["Best rank", "Meilleur classement", "最高ランク"],
                match_history: ["Match history", "Historique des matchs", "試合履歴"],
                mail: ["Enter your email address", "Entrez votre adresse email", "メールアドレスを入力してください"],
                send: ["Send", "Envoyer", "送信"],
                enter_2fa: ["Enter the code", "Entrez le code", "コードを入力する"],
                no_games: ["No games yet...", "Pas encore de parties ...", "まだゲームはありません..."],
                at_least_8: ["Password must be at least 8 characters", "Le mot de passe doit faire au moins 8 caractères", "パスワードは少なくとも 8 文字でなければなりません"],
                same_confirm: ["Confirm password must be the same as password", "Doit être le même que le mot de passe", "確認パスワードはパスワードと同じである必要があります"], 
            },

            twoFA_mail: "",
            twoFA_code: "",
            twoFA: false,
            username: "",
            wins: 0,
            losses: 0,
            rank: 0,
            best_rank: 0,
            elo: 0,
            best_elo: 0,
            current_password: "",
            new_password: "",
            confirm_new_password: "",
            current_password_label: "Current password",
            new_password_label: "New password",
            confirm_new_password_label: "Confirm new password",
            image_url: "",
            match_history: [],
            is_remote: false,
        }
    },
    computed: {
        totalGame: function() {
            return this.wins + this.losses
        },
        winRate: function() {
            if (this.totalGame == 0) {
                return 0
            }
            return ((this.wins / this.totalGame) * 100).toFixed(1)
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

            axios.post(import.meta.env.VITE_URL_BASE + 'user/update/' + localStorage.getItem("pk") + "/",
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                        'Authorization': 'Bearer ' + localStorage.getItem("access")
                    }
                }).then(response => {
                    const URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/"
                    axios.get(URL, {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem("access")
                        }
                    })
                    .then(response => {
                        location.reload()
                    })
                }).catch(response => {
            });
        },
        enable_2fa() {
            const URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/update-2fa/?mode=true"
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.twoFA = true
            })
            .catch(error => {
            })
        },
        disable_2fa() {
            const URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/update-2fa/?mode=false"
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.twoFA = false
            })
            .catch(error => {
            })
        },
        sendMail() {
            const URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/verif_mail/?email=" + this.twoFA_mail
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                document.getElementById("open_modal").click()
            })
            .catch(error => {
            })
        },
        sendCode() {
            const URL =  import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/verif_mail_key/?email=" + this.twoFA_mail + "&code=" + this.twoFA_code
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            }).then(response => {
                this.enable_2fa()
                document.getElementById("close_code_modal").click()
            })
            .catch(error => {
            })
        },
        checkPassword() {
            if (this.new_password.length < 8) {
                this.new_password_label = this.text.at_least_8[this.lang]
                return false
            }
            this.new_password_label = this.text.new_password[this.lang]
            if (this.new_password != this.confirm_new_password)
            {
                this.confirm_new_password_label = this.text.same_confirm[this.lang]
                return false
            }
            this.confirm_new_password_label = this.text.confirm_new_password[this.lang]
            return true
        },
        updatePassword() {
            if (this.checkPassword()) {
                const URL = import.meta.env.VITE_URL_BASE + "user/update/" + localStorage.getItem("pk") + "/?password=" + this.new_password
                axios.get(URL, {
                    headers: {
                        'Authorization': 'Bearer ' + localStorage.getItem("access")
                    }
                })
                .then(response => {
                    document.getElementById("close_password_modal").click()
                    localStorage.removeItem("access");
                    localStorage.removeItem("pk");
                    this.$router.push({path: "/login"})
                })
            }
        }
    },
    mounted() {
        this.current_password_label = this.text.current_password[this.lang]
        this.new_password_label = this.text.new_password[this.lang]
        this.confirm_new_password_label = this.text.confirm_new_password[this.lang]

        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        var URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            this.username = response.data.username
            this.wins = response.data.wins
            this.losses = response.data.losses
            this.rank = response.data.rank
            this.best_rank = response.data.best_rank
            this.elo = response.data.elo
            this.best_elo = response.data.best_elo
            this.image_url = response.data.pfp
            this.twoFA = response.data.twoFA
            this.is_remote = response.data.remote
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

        URL = import.meta.env.VITE_URL_BASE + "user/" + localStorage.getItem("pk") + "/gamehistory/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            for (var elt in response.data.history) {
                var match = {}
                match["score_player1"] = response.data.history[elt].hostscore
                match["score_player2"] = response.data.history[elt].guestscore
                match["username_player2"] = response.data.history[elt].guest
                match["date"] = response.data.history[elt].date
                this.match_history.push(match)
            }
        }) 
    },
    components: {
        Navbar,
        MatchHistoryElt,
    }
}
</script>
