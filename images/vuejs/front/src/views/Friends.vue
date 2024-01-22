<template>
    <div class="d-flex flex-column align-items-center">
        <Navbar />
        <div class="d-flex flex-column align-items-center mt-36">
            <h1 class="text-4xl text-light">Friends</h1>
            <div class="flex flex-col mt-6 w-[90vw] max-w-[722px] rounded-lg border-1 border-gray-700/50">
            <FriendsElt v-for="player in players" :status="player.status" :username="player.username" :pic="player.pic" :is_last="player.is_last"/>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
import FriendsElt from '../components/FriendsElt.vue';
import Navbar from '../components/Navbar.vue';
import axios from 'axios';

export default {
    data() {
        return {
            players: [
                {
                    status: 2,
                    username: "SkibidiPlayer1",
                    pic: "",
                    is_last: false
                },
                {
                    status: 2,
                    username: "Player2",
                    pic: "",
                    is_last: false
                },
                {
                    status: 1,
                    username: "Player3",
                    pic: "",
                    is_last: false
                },
                {
                    status: 1,
                    username: "Player4",
                    pic: "",
                    is_last: false
                },
                {
                    status: 0,
                    username: "Player5",
                    pic: "",
                    is_last: true
                },
                
            ]
        }
    },
    mounted() {
        if (localStorage.getItem("access") === null) {
    		this.$router.push({path: '/login'})
    	}
        const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/"
        axios.get(URL, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("access")
            }
        })
        .catch(error => {
		    if (error.response.status == 401) {
                localStorage.removeItem("access");
                localStorage.removeItem("pk");
                this.$router.push({path: "/login"})
            }
	    })
    },
    components: {
        FriendsElt,
        Navbar,
    }
}
</script>