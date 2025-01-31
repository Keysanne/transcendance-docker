import { createRouter, createWebHistory } from 'vue-router'

import Login from '../views/Login.vue'
import Account from '../views/Account.vue'
import Leaderboard from '../views/Leaderboard.vue'
import Tournaments from '../views/Tournaments.vue'
import TournamentView from '../views/TournamentView.vue'
import Home from '../views/Home.vue'
import NotFound from '../views/NotFound.vue'
import Play from '../views/Play.vue'
import Pong from '../views/Pong.vue'
import PongAI from '../views/PongAI.vue'
import Pong4P from '../views/Pong4P.vue'
import Friends from '../views/Friends.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'Home', component: Home},
        {path: '/login', name: 'Login', component: Login},
        {path: '/account', name: 'Account', component: Account},
        {path: '/leaderboard', name: 'Leaderboard', component: Leaderboard},
        {path: '/tournaments', name: 'Tournaments', component: Tournaments},
        {path: '/tournament/:id', name: 'TournamentView', component: TournamentView},
        {path: '/play', name: 'Play', component: Play},
        {path: '/pong/:ids(\\d+)*', name: 'Pong', component: Pong},
        {path: '/friends', name: 'Friends', component: Friends},
        {path: '/pong4p', name: 'Pong4P', component: Pong4P},
        {path: '/pongAI', name: 'PongAI', component: PongAI},
        {path: '/friends', name:'Friends', component: Friends},
        {path: '/:notFound*', component: NotFound},  
    ]
})

export default router
