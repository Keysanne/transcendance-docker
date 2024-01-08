<template>
    <div class="card bg-dark border-secondary border-opacity-50 text-light w-full sm:w-[47.5%] my-3">
        <div class="card-body flex flex-col justify-between">
            <div>
                <h5 class="card-title">{{ name }}</h5>
                <p class="card-text">{{ description }}</p>
            </div>
            <div class="flex justify-between items-center mt-3">
                <div>{{ nb_players }} / {{ max_players }}</div>
                <button v-if="registered" class="btn btn-danger">Unregister</button>
                <button v-else class="btn btn-secondary" :disabled="nb_players >= max_players">Register</button>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script>
export default {
    props: {
        id: Number,
        name: String,
        description: String,
        nb_players: Number,
        max_players: Number,
        registered: Boolean,
    }
}
</script>