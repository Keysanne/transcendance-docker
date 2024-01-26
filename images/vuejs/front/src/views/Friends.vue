<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />
        <div class="d-flex flex-column align-items-center mt-36">

            <div :class="is_alert_failed ? 'flex' : 'hidden'" class="fixed w-full justify-center">
                <div class="alert alert-danger alert-dismissible fade show w-96 flex justify-center items-center" role="alert">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 fill-red-400" viewBox="0 0 16 16" role="img" aria-label="Danger:">
                        <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                    </svg>
                    <div class="ml-2">{{ text.failed[lang] }}</div>
                    <button type="button" class="btn-close" @click="is_alert_failed = false"></button>
                </div>
            </div>

            <div :class="is_alert_already ? 'flex' : 'hidden'" class="fixed w-full justify-center">
                <div class="alert alert-danger alert-dismissible fade show w-[28rem] flex justify-center items-center" role="alert">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 fill-red-400" viewBox="0 0 16 16" role="img" aria-label="Danger:">
                        <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                    </svg>
                    <div class="ml-2">{{ text.already[lang] }}</div>
                    <button type="button" class="btn-close" @click="is_alert_already = false"></button>
                </div>
            </div>

            <div :class="is_alert_success ? 'flex' : 'hidden'" class="fixed w-full justify-center">
                <div class="alert alert-success alert-dismissible fade show w-48 flex justify-center items-center" role="alert">
                    <div class="ml-2">{{ text.success[lang] }}</div>
                    <button type="button" class="btn-close" @click="is_alert_success = false"></button>
                </div>
            </div>

            <h1 class="text-4xl text-light">{{ text.friends[lang] }}</h1>

            <div v-if="invites.length > 0" class="flex flex-col mt-6 w-[90vw] max-w-[722px] rounded-lg border-1 border-gray-700/50">
                <PendingElt v-for="invite in invites" :username="invite.username" :pic="invite.pic" :is_last="invite.is_last"/>
            </div>

            <div class="input-group mt-6">
                <input type="text" class="form-control" v-model="search_username" :placeholder="text.search[lang]" aria-describedby="button-add">
                <button class="btn btn-outline-secondary" type="button" id="button-add" @click="add">{{ text.add[lang] }}</button>
            </div>

            <div v-if="friends == null || friends.length == 0" class="w-[90vw] max-w-[722px]">
                <div class="card bg-dark border-secondary border-opacity-50 text-light w-full my-3">
                    <div class="card-body">
                        <div class="card-text text-center">{{ text.no_friends[lang] }}</div>
                    </div>
                </div>
            </div>
            <div v-else class="flex flex-col mt-6 w-[90vw] max-w-[722px] rounded-lg border-1 border-gray-700/50">
                <FriendsElt v-for="friend in friends" :status="friend.status" :username="friend.username" :pic="friend.pic" :elo="friend.elo" :is_last="friend.is_last"/>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import FriendsElt from '../components/FriendsElt.vue';
import PendingElt from '../components/PendingElt.vue'
import Navbar from '../components/Navbar.vue';
import axios from 'axios';

export default {
    data() {
        return {
            text: {
                "friends": ["Friends", "Amis", "友達"],
                "add": ["Add friend", "Ajouter un ami", "友達を追加"],
                "search": ["Search", "Chercher", "検索"],
                "no_friends": ["No friends yet...", "Pas encore d'amis ...", "まだ友達がいない..."],
                "failed": ["This username does not exist", "Le nom d'utilisateur n'existe pas", "このユーザー名は存在しません"],
                "success": ["Invitation sent", "Invitation envoyee", "招待状発送済み"],
                "already": ["Your are already friend with this user", "Tu es deja ami avec cet utilisateur", "あなたはすでにこのユーザーと友達です"],
            },

            search_username: "",
            friends: [],
            invites: [],
            is_alert_failed: false,
            is_alert_success: false,
            is_alert_already: false,
        }
    },
    mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        var URL = import.meta.env.VITE_BASE_URL + "friend/" + localStorage.getItem("pk") + "/list/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            this.friends = []
            for (var i in response.data.friends) {
                var friend = {}
                friend["username"] = response.data.friends[i].username
                friend["pic"] = response.data.friends[i].pfp
                friend["elo"] = response.data.friends[i].elo
                friend["status"] = response.data.friends[i].status
                friend["is_last"] = false
                this.friends.push(friend)
            }
            this.friends.sort(function (a, b) {
                if (b.status == 0 && a.status > 0) {
                    return -1
                }
                else if (a.status == 0 && b.status > 0) {
                    return 1
                }
                else {
                    return a.username - b.username
                }
            })
            if (this.friends.length > 0) {
                this.friends[this.friends.length - 1]["is_last"] = true
            }
        })
        .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })

        URL = import.meta.env.VITE_BASE_URL + "friend/" + localStorage.getItem("pk") + "/pending/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .then(response => {
            this.invites = []
            for (var i in response.data.pending) {
                var invite = {}
                invite["username"] = response.data.pending[i].username
                invite["pic"] = response.data.pending[i].pfp
                invite["is_last"] = false
                this.invites.push(invite)
            }
            if (this.invites.length > 0) {
                this.invites[this.invites.length - 1]["is_last"] = true
            }
        })
    },
    components: {
        FriendsElt,
        PendingElt,
        Navbar,
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
        add() {
            const URL = import.meta.env.VITE_BASE_URL + "friend/" + localStorage.getItem("pk") + "/invite/" + this.search_username + "/" 
            axios.get(URL, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem("access")
                }
            })
            .then(response => {
                this.is_alert_failed = false
                this.is_alert_success = true
                this.is_alert_already = false
            })
            .catch(error => {
                if (error.response.status == 409) {
                    this.is_alert_failed = false
                    this.is_alert_success = false
                    this.is_alert_already = true
                }
                else {
                    this.is_alert_failed = true
                    this.is_alert_success = false
                    this.is_alert_already = false
                }
            })
        }
    }
}
</script>