<template>
  <div class="fixed-top">
    <div class="bg-white">
      <nav class="container px-6 py-3 mx-auto md:flex md:justify-between md:items-center">
        <div class="flex items-center justify-between">
          <router-link to="/" class="text-xl font-bold text-gray-800 md:text-2xl hover:text-gray-500 no-underline ease-in-out transition-colors">{{ text.home[lang] }}</router-link>

          <div @click="showMenu = !showMenu" class="flex md:hidden">
            <button type="button" class="text-gray-800 hover:text-gray-500 focus:outline-none focus:text-gray-400">
              <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                <path fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
              </svg>
            </button>
          </div>
        </div>

        <ul :class="showMenu ? 'flex' : 'hidden'" class="flex-col mt-8 space-y-4 md:flex md:space-y-0 md:flex-row md:items-center md:space-x-10 md:mt-0 my-0 py-0">
          <li class="md:hidden"></li>
          <li><router-link class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/leaderboard">{{ text.leaderboard[lang] }}</router-link></li>
          <li><router-link class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/tournaments">{{ text.tournaments[lang] }}</router-link></li>
          <li><router-link class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/friends">{{ text.friends[lang] }}</router-link></li>
          <li class="md:hidden"><router-link class="font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/account">{{ text.account[lang] }}</router-link></li>
          <li v-if="img == null || img == ''" class="hidden md:block"><router-link to="/account"><img class="rounded-full h-14 w-14 border-1 border-black" src="../assets/default_profile.png" alt="profile_pic"></router-link></li>
          <li v-else class="hidden md:block"><router-link to="/account"><img class="rounded-full h-14 w-14 border-1 border-black" :src="img" alt="profile_pic"></router-link></li>
          <li class="md:hidden"><button @click="logout" class="font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors">{{ text.logout[lang] }}</button></li>
          <li class="hidden md:block"><button @click="logout"><font-awesome-icon class="h-6 w-6 text-gray-800 hover:text-gray-500 ease-in-out transition-colors" icon="fa-solid fa-arrow-right-from-bracket"/></button></li> 
          <li>
            <div class="dropdown">
              <a class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                {{ text.lang[lang] }}
              </a>
              <ul class="dropdown-menu">
                <li v-if="lang != 0"><button class="dropdown-item" @click="changeLang(0)">{{ text.lang[0] }}</button></li>
                <li v-if="lang != 1"><button class="dropdown-item" @click="changeLang(1)">{{ text.lang[1] }}</button></li>
                <!-- <li v-if="lang != 2"><button class="dropdown-item" @click="changeLang(2)">{{ text.lang[2] }}</button></li> -->
              </ul>
            </div>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      text: {
        home: ["Home", "Accueil"],
        leaderboard: ["Leaderboard", "Classement"],
        tournaments: ["Tournaments", "Tournois"],
        friends: ["Friends", "Amis"],
        account: ["My account", "Mon compte"],
        logout: ["Log out", "Se deconnecter"],
        lang: ["English", "Francais"]
      },

      showMenu: false,
      img: "",
    };
  },
  methods: {
    logout() {
      const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/status/0/"
      axios.get(URL, {
          headers: {
              'Authorization': 'Bearer ' + localStorage.getItem("access")
          }
      })
      localStorage.removeItem("access");
      localStorage.removeItem("pk");
      this.$router.push({path: "/login"})
    },
    changeLang(i) {
      const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/lang/" + i + "/"
      axios.get(URL, {
          headers: {
              'Authorization': 'Bearer ' + localStorage.getItem("access")
          }
      })
      .then(response => {
        localStorage.setItem("lang", i)
        location.reload()
      })
    }
  },
  computed: {
    lang: function() {
        if (localStorage.getItem("lang") === null) {
            localStorage.setItem("lang", 0)
        }
        return localStorage.getItem("lang")
    }
  },
  mounted() {
    const URL = "http://127.0.0.1:8000/user/" + localStorage.getItem("pk") + "/"
    axios.get(URL, {
      headers: {
        'Authorization': 'Bearer ' + localStorage.getItem("access")
      }
    })
    .then(response => {
      this.img = response.data.pfp;
      localStorage.setItem("lang", response.data.language)
    })
    .catch(error => {
      if (error.response.status == 401) {
          this.logout()
        }
    })
  },
};
</script>