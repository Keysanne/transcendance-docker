<template>
    <div class="card bg-dark border-secondary border-opacity-50 text-light w-full sm:w-[47.5%] my-3">
        <div class="card-body flex flex-col justify-between">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <p class="card-text">{{ description }}</p>
            </div>
            <div class="flex justify-between items-center mt-3">
                <div>{{ nb_players }} / {{ max_players }}</div>
                <button v-if="registered" class="btn btn-danger" @click="unregister">{{ text.unregister[lang] }}</button>
                <button v-else class="btn btn-secondary" :disabled="nb_players >= max_players" data-bs-toggle="modal" data-bs-target="#nickname_modal">{{ text.register[lang] }}</button>

                <div class="modal fade" id="nickname_modal" tabindex="-1" aria-labelledby="nickname_modal_label" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5 text-light" id="nickname_modal_label">{{ text.nickname[lang] }}</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" :aria-label="text.close[lang]"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating">
                                    <input v-model="nickname" type="text" :class="nickname_label != text.nickname[lang] ? 'is-invalid' : ''" class="form-control" id="nickname" placeholder="nickname">
                                    <label for="nickname">{{ nickname_label }}</label>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ text.close[lang] }}</button>
                                <button type="button" :disabled="nickname == ''" class="btn btn-primary" @click="register">{{ text.register[lang] }}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            text: {
                unregister: ["Unregister", "Me desinscrire", "登録解除"],
                register: ["Register", "M'inscrire", "登録"],
                nickname: ["Nickname", "Surnom", "ニックネーム"],
                close: ["Close", "Fermer", "閉じる"],
                alphanumeric: ["Nickname must be alphanumeric", "Le surnom doit etre compose de lettres et/ou de chiffres", "ニックネームは英数字でなければなりません"],
                already: ["Nickname already used", "Le surnom est deja utilise", "すでに使用されているニックネーム"]
            },

            nickname: "",
            nickname_label: "" 
        }
    },
    props: {
        id: Number,
        name: String,
        description: String,
        nb_players: Number,
        max_players: Number,
        registered: Boolean,
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
        register() {
            if (!(/^[a-zA-Z0-9]+$/.test(this.nickname))) {
                this.nickname_label = this.text.alphanumeric[this.lang]
                return
            }
            const URL = "http://127.0.0.1:8000/tournament/" + this.id + "/add-contestant/" + localStorage.getItem("pk") + "/?nickname=" + this.nickname
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                location.reload()
            })
            .catch(error => {
                if (error.response.status == 409) {
                    this.nickname_label = this.text.already[this.lang]
                }
            })
        },
        unregister() {
            const URL = "http://127.0.0.1:8000/tournament/" + this.id + "/remove-contestant/" + localStorage.getItem("pk") + "/"
            axios.delete(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                location.reload()
            })
        }
    },
    mounted() {
        this.nickname_label = this.text.nickname[this.lang]
    }
}
</script>