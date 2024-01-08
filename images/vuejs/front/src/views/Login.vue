<template>
    <div class="flex justify-content-center items-center">
        <div :class="signup_display ? 'hidden 2xl:flex' : 'flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[60vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">Login</h1>

            <input v-model="login_username" type="text" :class="login_username_label != 'Username' ? 'is-invalid' : ''" class="mt-16 w-[90%] max-w-xl form-control bg-dark border-secondary border-opacity-50 text-light" :placeholder="login_username_label">
            
            <input v-model="login_password" type="password" :class="login_password_label != 'Password' ? 'is-invalid' : ''" class="mt-3 w-[90%] max-w-xl form-control bg-dark border-secondary border-opacity-50 text-light" :placeholder="login_password_label">

            <div class="form-check w-[90%] max-w-xl mt-3">
                <input v-model="login_remember_me" type="checkbox" class="form-check-input bg-dark border-secondary border-opacity-50 text-light" id="login_remember_me">
                <label class="form-check-label text-light" for="login_remember_me">Remember me</label>
            </div>
            
            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10">Log in</button>
            <button type="button" class="btn btn-dark w-[90%] max-w-xl mt-3 d-flex justify-content-center align-items-center h-10">
                Log in with
                <img src="../assets/42_logo_png.png" class="ml-2 w-10"/>
            </button>

            <p class="mt-16 2xl:hidden text-light">Don't have an account?<button v-on:click="signupDisplay" class="btn btn-link text-light">Sign up</button></p>
        </div>

        <div class="hidden 2xl:block w-[1px] h-[60vh] bg-gray-700/50"></div>

        <div :class="signup_display ? 'flex' : 'hidden 2xl:flex'" class="flex-column align-items-center justify-content-center vh-100 w-[100vw] 2xl:w-[40vw]">
            <h1 class="text-5xl font-medium tracking-wider text-light">New here?</h1>

            <input v-model="signup_username" type="text" :class="signup_username_label != 'Username' ? 'is-invalid' : ''" class="mt-16 w-[90%] max-w-xl form-control bg-dark border-secondary border-opacity-50 text-light" id="signup_username" :placeholder="signup_username_label">
            
            <input v-model="signup_password" type="password" :class="signup_password_label != 'Password' ? 'is-invalid' : ''" class="mt-3 w-[90%] max-w-xl form-control bg-dark border-secondary border-opacity-50 text-light" id="signup_password" :placeholder="signup_password_label">
            
            <input v-model="signup_confirm_password" type="password" :class="signup_confirm_password_label != 'Confirm password' ? 'is-invalid' : ''" class="mt-3 w-[90%] max-w-xl form-control bg-dark border-secondary border-opacity-50 text-light" id="signup_confirm_password" :placeholder="signup_confirm_password_label">

            <button type="button" class="btn btn-secondary w-[90%] max-w-xl mt-8 h-10">Sign up</button>

            <p class="mt-16 text-light 2xl:hidden">Already have an account?<button v-on:click="signupDisplay" class="btn btn-link text-light">Log in</button></p>
        </div>
    </div>
</template>

<style scoped>
input::placeholder {
    color:#6c757d
}
</style>

<script>
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
    }
}
</script>