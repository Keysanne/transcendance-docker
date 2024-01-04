<template>
    <div class="flex overflow-x-auto max-w-full">
        <TournamentBracketStage class="mr-4" v-for="stage in tree" :stage="stage" />
    </div>
</template>

<style>

</style>

<script>
import TournamentBracketStage from './TournamentBracketStage.vue'

export default {
    data() {
        return {
            nb_turn: 0,
            tree: [],
        }
    },
    props: {
        size: Number,
        players: Array,
    },
    mounted() {
        let bracket = []
        for (let i = this.size; i > 1; i /= 2)
            this.nb_turn++

        for (let i = 0; i < this.players.length; i += 2) {
            let pair = []
            pair.push(this.players[i])
            if (i + 1 < this.players.length)
                pair.push(this.players[i + 1])
            else
                pair.push(null)
            bracket.push(pair)
        }
        while (bracket.length < this.size.length)
            bracket.push([null, null])

        this.tree.push(bracket)
        for (let i = 1; i < this.nb_turn; i++)
        {
            let stage = []
            for (let j = 0; j < this.tree[i - 1].length; j += 2)
            {
                let pair = []
                if (this.tree[i - 1][j][0] != null && this.tree[i - 1][j][0].stage >= i)
                    pair.push(this.tree[i - 1][j][0])
                else if (this.tree[i - 1][j][1] != null && this.tree[i - 1][j][1].stage >= i)
                    pair.push(this.tree[i - 1][j][1])
                else
                    pair.push(null)

                if (this.tree[i - 1][j + 1][0] != null && this.tree[i - 1][j + 1][0].stage >= i)
                    pair.push(this.tree[i - 1][j + 1][0])
                else if (this.tree[i - 1][j + 1][1] != null && this.tree[i - 1][j + 1][1].stage >= i)
                    pair.push(this.tree[i - 1][j + 1][1])
                else
                    pair.push(null) 

                stage.push(pair)
            }
            this.tree.push(stage)
        }

        if (this.tree[this.tree.length - 1][0][0] != null && this.tree[this.tree.length - 1][0][0].stage == this.nb_turn)
            this.tree.push([this.tree[this.tree.length - 1][0][0]])
        else if (this.tree[this.tree.length - 1][0][1] != null && this.tree[this.tree.length - 1][0][1].stage == this.nb_turn)
            this.tree.push([this.tree[this.tree.length - 1][0][1]])
        else
            this.tree.push([null])
    },
    components: {
        TournamentBracketStage,
}
}
</script>