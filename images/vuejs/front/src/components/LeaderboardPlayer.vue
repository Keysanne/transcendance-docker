<template>
    <div :class="is_last ? '' : 'border-1 border-black/0 border-b-gray-700/50'" class="flex items-center h-16">
        <div class="text-xl w-20 flex justify-center items-center h-full text-light">
            <div :class="rank == 1 ? 'bg-yellow-500' : rank == 2 ? 'bg-gray-400' : rank == 3 ? 'bg-orange-700' : ''" class="flex justify-center items-center w-8 h-8 rounded-full">
                {{ rank }}
            </div>
        </div>
        <div class="flex h-full w-full items-center">
            <img v-if="pic == null || pic == ''" class="w-12 h-12 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
            <img v-else class="w-12 h-12 rounded-full" :src="pic" alt="profile_pic">
            <div class="text-lg text-light ml-3">{{ username }}</div>
            <div class="flex-grow"></div>
            <div class="text-lg text-light mr-5">{{ elo }}</div>
        </div>
    </div>
</template>

<style>

</style>

<script>
export default {
    props: {
        rank: Number,
        username: String,
        pic: String,
        elo: Number,
        is_last: Boolean,
    }
}
</script>