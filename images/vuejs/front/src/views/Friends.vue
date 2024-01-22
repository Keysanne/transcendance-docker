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
    components: {
        FriendsElt,
        Navbar,
    }
}
</script>