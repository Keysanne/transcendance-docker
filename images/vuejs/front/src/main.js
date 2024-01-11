import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import './style.css'
import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPenToSquare, faArrowRightFromBracket } from '@fortawesome/free-solid-svg-icons'

library.add(faPenToSquare, faArrowRightFromBracket)

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.use(router)
.use(bootstrap)
.mount('#app')
