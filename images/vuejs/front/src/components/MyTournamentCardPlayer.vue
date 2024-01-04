<template>
    <div class="flex w-full mt-3">
        <img v-if="image == ''" class="w-14" src="../assets/default_profile.png" alt="player_image">
        <img v-else :src="image" class="w-14" alt="player_image">
        <div class="flex flex-col ml-3">
            <div class="text-lg font-semibold">{{ nickname }}</div>
            <div>{{ username }}</div>
        </div>
    </div>
</template>

<style>

</style>

<script>
export default {
    props: {
        username: String,
        nickname: String,
        image: String,
    }
}
</script>