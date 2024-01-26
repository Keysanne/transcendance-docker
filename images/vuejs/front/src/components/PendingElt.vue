<template>
    <div :class="is_last ? '' : 'border-1 border-black/0 border-b-gray-700/50'" class="flex items-center h-16">
        <div class="flex h-full w-full items-center">
            <img v-if="pic == null || pic == ''" class="w-12 h-12 rounded-full ml-5" src="../assets/default_profile.png" alt="profile_pic">
            <img v-else class="w-12 h-12 rounded-full ml-5" :src="pic" alt="profile_pic">
            <div class="text-lg text-light ml-3">{{ username }}</div>
            <div class="flex-grow"></div>
            <div class="text-lg text-light mr-5 flex items-center">
                <button @click="accept"><font-awesome-icon class="h-6 w-6 text-success hover:opacity-75 ease-in-out transition-opacity mr-2" icon="fa-solid fa-check"/></button>
                <button @click="decline"><font-awesome-icon class="h-6 w-6 text-danger hover:opacity-75 ease-in-out transition-opacity mr-2" icon="fa-solid fa-xmark"/></button>
                <button @click="block"><font-awesome-icon class="h-5 w-5 text-danger hover:opacity-75 ease-in-out transition-opacity" icon="fa-solid fa-ban"/></button>
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

        }
    },
    props: {
        username: String,
        pic: String,
        is_last: Boolean,
    },
    methods: {
        accept() {
            const URL = import.meta.env.VITE_URL_BASE + "friend/" + localStorage.getItem("pk") + "/accept/" + this.username + "/" 
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                location.reload()
            })
        },
        decline() {
            const URL = import.meta.env.VITE_URL_BASE + "friend/" + localStorage.getItem("pk") + "/deny/" + this.username + "/" 
            axios.delete(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                location.reload()
            })
        },
        block() {
            const URL = import.meta.env.VITE_URL_BASE + "friend/" + localStorage.getItem("pk") + "/block/" + this.username + "/" 
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                location.reload()
            })
        }
    }
}
</script>