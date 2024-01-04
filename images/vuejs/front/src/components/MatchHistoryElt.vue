<template>
    <li :class="score_player1 > score_player2 ? 'text-bg-success' : 'text-bg-danger'" class="list-group-item">
        <div class="text-sm text-center">{{ date }}</div>
        <div class="row row-cols-3 align-items-center text-center">
            <div class="col">{{ username_player1 }}</div>
            <div class="col text-2xl font-semibold">{{ score_player1 }} - {{ score_player2 }}</div>
            <div class="col">{{ username_player2 }}</div>
        </div>
    </li>
</template>

<style>

</style>

<script>
export default {
    props: {
        username_player1: String,
        username_player2: String,
        score_player1: Number,
        score_player2: Number,
        date: Date,
    }
}
</script>