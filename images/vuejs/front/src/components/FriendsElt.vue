<template>
    <div :class="is_last ? '' : 'border-1 border-black/0 border-b-gray-700/50'" class="flex items-center h-16">
        <div class="flex h-full w-full items-center ml-5">
            <div class= "relative">
                <div :class="status == 1 ? 'bg-success' : status == 2 ? 'bg-orange-600' : status == 0 ? 'bg-secondary' : ''" class="w-6 h-6 rounded-full absolute mt-[-5px] ml-[-5px] border-4 border-dark">
                </div>
                <img v-if="pic == null || pic == ''" class="w-12 h-12 rounded-full" src="../assets/default_profile.png" alt="profile_pic">
                <img v-else class="w-12 h-12 rounded-full" :src="pic" alt="profile_pic">
            </div>
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
    data() {
        return {

        }
    },
    props: {
        status: Number,
        username: String,
        pic: String,
        elo: Number,
        is_last: Boolean,
    }
}
</script>