<template>
    <div :class="is_alert ? 'flex' : 'hidden'" class="fixed-top mt-4 w-full justify-center">
        <div class="alert alert-danger alert-dismissible fade show w-64 flex justify-center items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 fill-red-400" viewBox="0 0 16 16" role="img" aria-label="Danger:">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </svg>
            <div class="ml-2">{{ text.failed[lang] }}</div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    </div>

    <button type="button" class="hidden" data-bs-toggle="modal" data-bs-target="#twoFA_modal" id="open_modal"></button>
    <div class="modal fade" id="twoFA_modal"  data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="twoFA_modal_label" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-light" id="twoFA_modal_label">{{ text.enter_2fa[lang] }}</h1>
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

    <div class="flex justify-content-center items-center">
        <div :class="signup_display ? 'hidden 2xl:flex' : 'flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[60vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">{{ text.login[lang] }}</h1>

            <div class="form-floating mt-16 w-[90%] max-w-xl">
                <input v-model="login_username" type="text" :class="login_username_label != text.username[lang] ? 'is-invalid' : ''" class="form-control" id="login_username" placeholder="username">
                <label for="login_username">{{ login_username_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="login_password" type="password" :class="login_password_label != text.password[lang] ? 'is-invalid' : ''" class="form-control" id="login_password" placeholder="password">
                <label for="login_password">{{ login_password_label }}</label>
            </div>

            <!-- <div class="form-check w-[90%] max-w-xl mt-3">
                <input v-model="login_remember_me" type="checkbox" class="form-check-input" id="login_remember_me">
                <label class="form-check-label text-light" for="login_remember_me">{{ text.remember[lang] }}</label>
            </div> -->
            
            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10" @click="login">{{ text.log_in[lang] }}</button>
            <a href="https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-81d49bc94d932815eff49672933b8ab64b722a244e6fb161bdcc83d2a6807f0c&redirect_uri=https%3A%2F%2F127.0.0.1%3A8080%2Flogin&response_type=code" type="button" class="btn btn-dark w-[90%] max-w-xl mt-3 d-flex justify-content-center align-items-center h-10">
                {{ text.login_42[lang] }}
                <img src="../assets/42_logo_png.png" class="ml-2 w-10"/>
            </a>

            <p class="mt-16 2xl:hidden text-light">{{ text.no_account[lang] }}<button v-on:click="signupDisplay" class="btn btn-link text-light">{{ text.signup[lang] }}</button></p>
        </div>

        <div class="hidden 2xl:block w-[1px] h-[60vh] bg-gray-700/50"></div>

        <div :class="signup_display ? 'flex' : 'hidden 2xl:flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[40vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">{{ text.new_here[lang] }}</h1>

            <div class="form-floating mt-16 w-[90%] max-w-xl">
                <input v-model="signup_username" type="text" :class="signup_username_label != text.username[lang] ? 'is-invalid' : ''" class="form-control" id="signup_username" placeholder="username">
                <label for="login_username">{{ signup_username_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="signup_password" type="password" :class="signup_password_label != text.password[lang] ? 'is-invalid' : ''" class="form-control" id="signup_password" placeholder="password">
                <label for="signup_password">{{ signup_password_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="signup_confirm_password" type="password" :class="signup_confirm_password_label != text.confirm_password[lang] ? 'is-invalid' : ''" class="form-control" id="signup_confirm_password" placeholder="confirm password">
                <label for="signup_confirm_password">{{ signup_confirm_password_label }}</label>
            </div>
            
            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10" @click="signUp">{{ text.signup[lang] }}</button>

            <p class="mt-16 text-light 2xl:hidden">{{ text.already_account[lang] }}<button v-on:click="signupDisplay" class="btn btn-link text-light">{{ text.login[lang] }}</button></p>
        </div>
    </div>
</template>

<style scoped>
label {
    color:#6c757d
}
</style>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            text: {
                login: ["Login", "Se connecter", "ログイン"],
                username: ["Username", "Nom d'utilisateur", "ユーザー名"],
                password: ["Password", "Mot de passe", "パスワード"],
                remember: ["Remember me", "Se souvenir de moi", "私を覚えている"],
                log_in: ["Log in", "Se connecter", "ログイン"],
                login_42: ["Log in with", "Se connecter avec", "でログイン"],
                new_here: ["New here?", "Nouveau ici ?", "ここ新しく？"],
                confirm_password: ["Confirm password", "Confirmation du mot de passe", "パスワードの確認"],
                signup: ["Sign up", "Creer mon compte", "サインアップ"],
                at_least: ["Username must be at least 5 characters", "Le nom d'utilisateur doit faire au moins 5 caracteres", "ユーザー名は少なくとも 5 文字でなければなりません"],
                at_most: ["Username must be at most 14 characters", "Le nom d'utilisateur ne doit pas faire plus de 14 caracteres", "ユーザー名は最大 14 文字でなければなりません"],
                alphanumeric: ["Username must be alphanumeric", "Le nom d'utilisateur doit etre compose de lettres et/ou de chiffres", "ユーザー名は英数字でなければなりません"],
                at_least_8: ["Password must be at least 8 characters", "Le mot de passe doit faire au moins 8 caracteres", "パスワードは少なくとも 8 文字でなければなりません"],
                same_confirm: ["Confirm password must be the same as password", "Doit etre le meme que le mot de passe", "確認パスワードはパスワードと同じである必要があります"],
                already_used: ["Username already used", "Nom d'utilisateur deja utilise", "すでに使用されているユーザー名"],
                incorrect_username: ["Incorrect username", "Nom d'utilisateur incorrect", "ユーザー名が間違っています"],
                incorrect_password: ["Incorrect password", "Mot de passe incorrect", "間違ったパスワード"],
                failed: ["Log in with 42 failed", "La connection avec 42 a echoue", "42 でログインに失敗しました"],
                no_account: ["Don't have an account?", "Vous n'avez pas encore de compte ?", "アカウントをお持ちではありませんか？"],
                already_account: ["Already have an account?", "Vous avez deja un compte ?", "すでにアカウントをお持ちですか？"],
                enter_2fa: ["Enter the code", "Entrez le code", "コードを入力する"],
                send: ["Send", "Envoyer", "送信"],
            },

            signup_display: false,
            signup_username: "",
            signup_password: "",
            signup_confirm_password: "",
            signup_username_label: "",
            signup_password_label: "",
            signup_confirm_password_label: "",
            login_remember_me: false,
            login_username: "",
            login_password: "",
            login_username_label: "",
            login_password_label: "",
            is_alert: false,
            twoFA_code: "",
            pk: ""
        }
    },

    methods: {
        signupDisplay() {
            this.signup_display = !this.signup_display
            if (this.signup_display) {
                this.login_username = ""
                this.login_password = ""
                this.login_remember_me = false
                this.login_username_label = this.text.username[this.lang]
                this.login_password_label = this.text.password[this.lang]
            }
            else {
                this.signup_display = false
                this.signup_username = ""
                this.signup_password = ""
                this.signup_confirm_password = ""
                this.signup_username_label = this.text.username[this.lang]
                this.signup_password_label = this.text.password[this.lang]
                this.signup_confirm_password_label = this.text.confirm_password[this.lang]
            }
        },
        checkUsername() {
            if (this.signup_username.length < 5) {
                this.signup_username_label = this.text.at_least[this.lang]
                return false
            }
            if (this.signup_username.length > 14) {
                this.signup_username_label = this.text.at_most[this.lang]
                return false
            }
            if (!(/^[a-zA-Z0-9]+$/.test(this.signup_username))) {
                this.signup_username_label = this.text.alphanumeric[this.lang]
                return false
            }
            this.signup_username_label = this.text.username[this.lang]
            return true
        },
        checkPassword() {
            if (this.signup_password.length < 8) {
                this.signup_password_label = this.text.at_least_8[this.lang]
                return false
            }
            this.signup_password_label = this.text.password[this.lang]
            if (this.signup_password != this.signup_confirm_password)
            {
                this.signup_confirm_password_label = this.text.same_confirm[this.lang]
                return false
            }
            this.signup_confirm_password_label = this.text.confirm_password[this.lang]
            return true
        },
        signUp() {
            if (this.checkUsername() && this.checkPassword())
            {
                const BASE_URL = "http://127.0.0.1:8000/"
                const CREATE_ENDPOINT = "user/create/"
                const TOKEN_ENDPOINT = "api/token/"
                axios.post(BASE_URL + CREATE_ENDPOINT, {
                    headers: {
                    'Content-Type': 'application/json'
                },
                    params: {
                        username: this.signup_username,
                        password: this.signup_password
                    }
                }).then(response => {
                    this.pk = response.data.pk
                    axios.post(BASE_URL + TOKEN_ENDPOINT, {
                        username: this.signup_username,
                        password: this.signup_password
                    }).then(response_token => {
                        console.log(response_token)
                        localStorage.setItem("access", response_token.data.access)
                        localStorage.setItem("pk", this.pk)
                        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/status/1/"
                        axios.get(URL, {
                            headers: {
                                'Authorization': 'Bearer ' + localStorage.getItem("access")
                            }
                        })
                        localStorage.setItem("lang", 0)
                        this.$router.push({path: '/'})
                    })
                })
                .catch(error => {
                    this.signup_username_label = this.text.already_used[this.lang]
                })
            }
        },
        login() {
            const BASE_URL = "http://127.0.0.1:8000/"
    		const CONNECT_ENDPOINT = "user/connect/"
	    	const TOKEN_ENDPOINT = "api/token/"
            axios.post(BASE_URL + CONNECT_ENDPOINT, {
                headers: {
                    'Content-Type': 'application/json'
                },
                params: {
                    username: this.login_username,
                    password: this.login_password
                }
            }).then(response => {
                this.pk = response.data.pk
                localStorage.setItem("lang", response.data.lang)
                if (response.data.twoFA == true){
                    this.openModal()
                }
                else {
                    axios.post(BASE_URL + TOKEN_ENDPOINT, {
                        username: this.login_username,
                        password: this.login_password
                    }).then(response_token => {
                        localStorage.setItem("access", response_token.data.access)
                        localStorage.setItem("pk", this.pk)
                        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/status/1/"
                        axios.get(URL, {
                            headers: {
                                'Authorization': 'Bearer ' + localStorage.getItem("access")
                            }
                        })
                        this.$router.push({path: '/'})
                    })
                }
            })
            .catch(error => {
                if (error.response.data.problem == "username") {
                    this.login_username_label = this.text.incorrect_username[this.lang]
                    this.login_password_label = this.text.password[this.lang]
                }
                else {
                    this.login_username_label = this.text.username[this.lang]
                    this.login_password_label = this.text.incorrect_password[this.lang]
                }
            })
        },
        sendCode() {
            const BASE_URL = "http://127.0.0.1:8000/"
    		const KEY_ENDPOINT = "user/" + this.pk + "/key/?code=" + this.twoFA_code + "&username=" + this.login_username + "&password=" + this.login_password
            const TOKEN_ENDPOINT = "api/token/"
            axios.get(BASE_URL + KEY_ENDPOINT).then(reponse => {
                this.closeModal()
                axios.post(BASE_URL + TOKEN_ENDPOINT, {
                    username: this.login_username,
                    password: this.login_password
                }).then(response_token => {
                    localStorage.setItem("access", response_token.data.access)
                    localStorage.setItem("pk", this.pk)
                    const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/status/1/"
                    axios.get(URL, {
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem("access")
                        }
                    })
                    this.$router.push({path: '/'})
                })
            })
            .catch(error => {
                console.log(error)
            })
        },
        openModal() {
            document.getElementById("open_modal").click()
        },
        closeModal() {
            document.getElementById("close_modal").click()
        },
    },
    mounted() {
        this.signup_username_label = this.text.username[this.lang]
        this.signup_password_label = this.text.password[this.lang]
        this.signup_confirm_password_label = this.text.confirm_password[this.lang]
        this.login_username_label = this.text.username[this.lang]
        this.login_password_label = this.text.password[this.lang]

        if (window.location.search != '') {
            var code = window.location.search.search(/\?code=[A-Za-z0-9]/)
            if (code != -1) {
                code = window.location.search.split('=')[1]
                const URL = "http://127.0.0.1:8000/user/remote-login/?code=" + code
                const BASE_URL = "http://127.0.0.1:8000/"
                const TOKEN_ENDPOINT = "api/token/"
                axios.get(URL).then(response => {
                    axios.post(BASE_URL + TOKEN_ENDPOINT, {
                        username: response.data.username,
                        password: response.data.password
                    }).then(response_token => {
                        localStorage.setItem("access", response_token.data.access)
                        localStorage.setItem("pk", response.data.pk)
                        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/status/1/"
                        axios.get(URL, {
                            headers: {
                                'Authorization': 'Bearer ' + localStorage.getItem("access")
                            }
                        })
                        this.$router.push({path: '/'})
                    })
                })
                .catch(error => {
                    this.is_alert = true
                }) 
            }
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
