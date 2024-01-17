<template>
    <div :class="is_alert ? 'flex' : 'hidden'" class="fixed-top mt-4 w-full justify-center">
        <div class="alert alert-danger alert-dismissible fade show w-64 flex justify-center items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 fill-red-400" viewBox="0 0 16 16" role="img" aria-label="Danger:">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </svg>
            <div class="ml-2">
                Login with 42 failed
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    </div>
    <div class="flex justify-content-center items-center">
        <div :class="signup_display ? 'hidden 2xl:flex' : 'flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[60vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">Login</h1>

            <div class="form-floating mt-16 w-[90%] max-w-xl">
                <input v-model="login_username" type="text" :class="login_username_label != 'Username' ? 'is-invalid' : ''" class="form-control" id="login_username" placeholder="username">
                <label for="login_username">{{ login_username_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="login_password" type="password" :class="login_password_label != 'Password' ? 'is-invalid' : ''" class="form-control" id="login_password" placeholder="password">
                <label for="login_password">{{ login_password_label }}</label>
            </div>

            <div class="form-check w-[90%] max-w-xl mt-3">
                <input v-model="login_remember_me" type="checkbox" class="form-check-input" id="login_remember_me">
                <label class="form-check-label text-light" for="login_remember_me">Remember me</label>
            </div>
            
            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10" @click="login">Log in</button>
            <a href="https://api.intra.42.fr/oauth/authorize?client_id=u-s4t2ud-81d49bc94d932815eff49672933b8ab64b722a244e6fb161bdcc83d2a6807f0c&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Flogin&response_type=code" type="button" class="btn btn-dark w-[90%] max-w-xl mt-3 d-flex justify-content-center align-items-center h-10">
                Log in with
                <img src="../assets/42_logo_png.png" class="ml-2 w-10"/>
            </a>

            <p class="mt-16 2xl:hidden text-light">Don't have an account?<button v-on:click="signupDisplay" class="btn btn-link text-light">Sign up</button></p>
        </div>

        <div class="hidden 2xl:block w-[1px] h-[60vh] bg-gray-700/50"></div>

        <div :class="signup_display ? 'flex' : 'hidden 2xl:flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[40vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">New here?</h1>

            <div class="form-floating mt-16 w-[90%] max-w-xl">
                <input v-model="signup_username" type="text" :class="signup_username_label != 'Username' ? 'is-invalid' : ''" class="form-control" id="signup_username" placeholder="username">
                <label for="login_username">{{ signup_username_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="signup_password" type="password" :class="signup_password_label != 'Password' ? 'is-invalid' : ''" class="form-control" id="signup_password" placeholder="password">
                <label for="signup_password">{{ signup_password_label }}</label>
            </div>
            <div class="form-floating mt-3 w-[90%] max-w-xl">
                <input v-model="signup_confirm_password" type="password" :class="signup_confirm_password_label != 'Confirm password' ? 'is-invalid' : ''" class="form-control" id="signup_confirm_password" placeholder="confirm password">
                <label for="signup_confirm_password">{{ signup_confirm_password_label }}</label>
            </div>
            
            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10" @click="signUp">Sign up</button>

            <p class="mt-16 text-light 2xl:hidden">Already have an account?<button v-on:click="signupDisplay" class="btn btn-link text-light">Log in</button></p>
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
import { toHandlers } from 'vue';

export default {
    data() {
        return {
            signup_display: false,
            signup_username: "",
            signup_password: "",
            signup_confirm_password: "",
            signup_username_label: "Username",
            signup_password_label: "Password",
            signup_confirm_password_label: "Confirm password",
            login_remember_me: false,
            login_username: "",
            login_password: "",
            login_username_label: "Username",
            login_password_label: "Password",
            is_alert: false
        }
    },

    methods: {
        signupDisplay() {
            this.signup_display = !this.signup_display
            if (this.signup_display) {
                this.login_username = ""
                this.login_password = ""
                this.login_remember_me = false
                this.login_username_label = "Username"
                this.login_password_label = "Password"
            }
            else {
                this.signup_display = false
                this.signup_username = ""
                this.signup_password = ""
                this.signup_confirm_password = ""
                this.signup_username_label = "Username"
                this.signup_password_label = "Password"
                this.signup_confirm_password_label = "Confirm password"
            }
        },
        checkUsername() {
            if (this.signup_username.length < 5) {
                this.signup_username_label = "Username must be at least 5 characters"
                return false
            }
            if (this.signup_username.length > 15) {
                this.signup_username_label = "Username must be at most 15 characters"
                return false
            }
            if (!(/^[a-zA-Z0-9]+$/.test(this.signup_username))) {
                this.signup_username_label = "Username must be alphanumeric"
                return false
            }
            this.signup_username_label = "Username"
            return true
        },
        checkPassword() {
            if (this.signup_password.length < 8) {
                this.signup_password_label = "Password must be at least 8 characters"
                return false
            }
            this.signup_password_label = "Password"
            if (this.signup_password != this.signup_confirm_password)
            {
                this.signup_confirm_password_label = "Confirm password must be the same as password"
                return false
            }
            this.signup_confirm_password_label = "Confirm password"
            return true
        },
        signUp() {
            if (this.checkUsername() && this.checkPassword())
            {
		const BASE_URL = "http://127.0.0.1:8000/"
		const CREATE_ENDPOINT = "user/create/"
		const TOKEN_ENDPOINT = "api/token/"
		const PARAMS = "?username="+this.signup_username+"&password="+this.signup_password
                axios.post(BASE_URL + CREATE_ENDPOINT + PARAMS).then(response => {
                   axios.post(BASE_URL + TOKEN_ENDPOINT, {
			  username: this.signup_username,
			  password: this.signup_password
			}).then(response_token => {
                   console.log(response_token)
                    localStorage.setItem("access", response_token.data.access)
                    this.$router.push({path: '/'})
                })
                })
                .catch(error => {
                    this.signup_username_label = "Username already used"
                })
            }
        },
        login() {
            const BASE_URL = "http://127.0.0.1:8000/"
    		const CONNECT_ENDPOINT = "user/connect/"
	    	const TOKEN_ENDPOINT = "api/token/"
		    const PARAMS = "?username="+this.login_username+"&password="+this.login_password
            axios.get(BASE_URL + CONNECT_ENDPOINT + PARAMS).then(response => {
                axios.post(BASE_URL + TOKEN_ENDPOINT, {
			        username: this.login_username,
			        password: this.login_password
			    }).then(response_token => {
                    localStorage.setItem("access", response_token.data.access)
                    this.$router.push({path: '/'})
                })
            })
            .catch(error => {
                if (error.response.data.problem == "username") {
                    this.login_username_label = "Incorrect username"
                    this.login_password_label = "Password"
                }
                else {
                    this.login_username_label = "Username"
                    this.login_password_label = "Incorrect password"
                }
            })
        },
    },
    mounted() {
        if (window.location.search != '') {
            var code = window.location.search.search(/\?code=[A-Za-z0-9]/)
            if (code != -1) {
                code = window.location.search.split('=')[1]
                const URL = "http://127.0.0.1:8000/user/remote-login/?code=" + code
                axios.get(URL).then(response => {

                })
                .catch(error => {
                    this.is_alert = true
                }) 
            }
        }
    }
}
</script>
