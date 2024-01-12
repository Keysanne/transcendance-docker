<template>
  <div class="fixed-top">
    <div class="bg-white">
      <nav class="container px-6 py-3 mx-auto md:flex md:justify-between md:items-center">
        <div class="flex items-center justify-between">
          <router-link to="/" class="text-xl font-bold text-gray-800 md:text-2xl hover:text-gray-500 no-underline ease-in-out transition-colors">Home</router-link>

          <!-- Mobile menu button -->
          <div @click="showMenu = !showMenu" class="flex md:hidden">
            <button type="button" class="text-gray-800 hover:text-gray-500 focus:outline-none focus:text-gray-400">
              <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                <path fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
        <ul :class="showMenu ? 'flex' : 'hidden'" class="flex-col mt-8 space-y-4 md:flex md:space-y-0 md:flex-row md:items-center md:space-x-10 md:mt-0 my-0 py-0">
          <li class="md:hidden"></li>
          <li><router-link class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/leaderboard">Leaderboard</router-link></li>
          <li><router-link class="md:text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/tournaments">Tournaments</router-link></li>
          <li class="md:hidden"><router-link class="font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/account">My Account</router-link></li>
          <li class="hidden md:block"><router-link to="/account"><img class="rounded-full h-14 w-14 border-1 border-black" src="../assets/avatars/todo.jpg" alt="profile_pic"></router-link></li>
          <li class="md:hidden"><button @click="logout" class="font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors">Log out</button></li>
          <li class="hidden md:block"><button @click="logout"><font-awesome-icon class="h-6 w-6 text-gray-800 hover:text-gray-500 ease-in-out transition-colors" icon="fa-solid fa-arrow-right-from-bracket"/></button></li> 
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    logout() {
      this.$router.push({path: "/login"})
    }
  }
};
</script>