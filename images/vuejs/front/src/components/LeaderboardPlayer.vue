<template>
    <div class="flex items-center h-16 bg-primary">
        <div class="rank-container" :class="rank == 1 ? 'rank1' : rank == 2 ? 'rank2' : rank == 3 ? 'rank3' : 'bg-white text-primary border-bottom border-primary'">
            {{ rank }}
        </div>

        <div class="flex border-b-white border-b-[1px] h-full w-full items-center">
            <img class="pic" :class="pic == 0 ? '' : 'hidden'" src="../assets/avatars/cursed_womb2.jpg" alt="">
            <img class="pic" :class="pic == 1 ? '' : 'hidden'" src="../assets/avatars/nobara2.jpg" alt="">
            <img class="pic" :class="pic == 2 ? '' : 'hidden'" src="../assets/avatars/megumi.jpg" alt="">
            <img class="pic" :class="pic == 3 ? '' : 'hidden'" src="../assets/avatars/maki.jpg" alt="">
            <img class="pic" :class="pic == 4 ? '' : 'hidden'" src="../assets/avatars/yuji.jpeg" alt="">
            <img class="pic" :class="pic == 5 ? '' : 'hidden'" src="../assets/avatars/sheko.jpg" alt="">
            <img class="pic" :class="pic == 6 ? '' : 'hidden'" src="../assets/avatars/todo.jpg" alt="">
            
            <div class="text-xl ml-2 text-white">{{ username }}</div>
            
            <div class="flex-grow"></div>
            
            <div class="text-xl text-white mr-3">{{ elo }}</div>
        </div>
    </div>
</template>

<style scoped>
    .pic {
        @apply w-12 rounded-full ml-2;
    }

    .rank-container {
        @apply text-2xl w-16 flex justify-center items-center h-full;
    }

    .rank1 {
        @apply bg-yellow-500 text-white;
    }

    .rank2 {
        @apply bg-gray-400 text-white;
    }

    .rank3 {
        @apply bg-orange-700 text-white;
    }

    /* .rank {
        @apply bg-white text-primary;
    } */

    
</style>

<script>
export default {
    data() {
        return {

        }
    },
    props: {
        rank: Number,
        username: String,
        pic: Number,
        elo: Number,
    }
}
</script>