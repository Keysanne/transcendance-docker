<template>
    <div class="card">
        <ul class="list-group list-group-flush">
            <li class="list-group-item min-w-[8rem]">
                <div class="flex items-center justify-center">
                    <div class="text-center">{{ player1.nickname }}</div>
                </div>
            </li>
            <li v-if="is_last == false" class="list-group-item min-w-[8rem]">
                <div class="flex items-center justify-center">
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