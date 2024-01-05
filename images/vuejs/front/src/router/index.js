import { createRouter, createWebHistory } from 'vue-router'

import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
import Leaderboard from '../views/Leaderboard.vue'
import Tournaments from '../views/Tournaments.vue'
import TournamentView from '../views/TournamentView.vue'
import Matchmaking from '../views/Matchmaking.vue'
import Home from '../views/Home.vue'
import NotFound from '../views/NotFound.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'Home', component: Home},
        {path: '/login', name: 'Login', component: Login},
        {path: '/account', name: 'Account', component: Account},
        {path: '/leaderboard', name: 'Leaderboard', component: Leaderboard},
        {path: '/tournaments', name: 'Tournaments', component: Tournaments},
        {path: '/tournament/:id', name: 'TournamentView', component: TournamentView},
        {path: '/matchmaking', name: 'Matchmaking', component: Matchmaking},
        {path: '/:notFound', component: NotFound},  
    ]
})

export default router