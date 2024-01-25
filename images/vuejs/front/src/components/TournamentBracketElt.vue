<template>
    <div class="card">
        <ul class="list-group list-group-flush">
            <li class="list-group-item min-w-[8rem]">
                <div class="flex items-center justify-center">
                    <img v-if="player1.nickname != '...' && (player1.image == null || player1.image == '')" class="w-8 h-8 rounded-full mr-3" src="../assets/default_profile.png" alt="profile_pic">
                    <img v-else-if="player1.nickname != '...'" class="w-12 h-12 rounded-full mr-2" :src="players1.image" alt="profile_pic">
                    <div class="text-center">{{ player1.nickname }}</div>
                </div>
            </li>
            <li v-if="is_last == false" class="list-group-item min-w-[8rem]">
                <div class="flex items-center justify-center">
                    <img v-if="player2.nickname != '...' && (player2.image == null || player2.image == '')" class="w-8 h-8 rounded-full mr-3" src="../assets/default_profile.png" alt="profile_pic">
                    <img v-else-if="player2.nickname != '...'" class="w-12 h-12 rounded-full mr-2" :src="players2.image" alt="profile_pic">
                    <div class="text-center">{{ player2.nickname }}</div>
                </div>
            </li>
        </ul>
    </div>
</template>

<style>

</style>

<script>
export default {
    data() {
        return {
            player1: {},
            player2: {},
            is_last: false,
        }
    },
    props: {
        players: {
            required: false,
        },
    },
    mounted() {
        if (this.players == null)
        {
            this.is_last = true
            let player = {
                username: "...",
                nickname: "...",
                image: "",
            }
            this.player1 = player
            return
        }
        if (!Array.isArray(this.players))
        {
            this.is_last = true
            this.player1 = this.players
            return
        }
        if (this.players[0] == null)
        {
            let player = {
                username: "...",
                nickname: "...",
                image: "",
            }
            this.player1 = player
        }
        else
            this.player1 = this.players[0]
        
        if (this.players[1] == null)
        {
            let player = {
                username: "...",
                nickname: "...",
                image: "",
            }
            this.player2 = player
        }
        else
            this.player2 = this.players[1]

    },
}
</script>