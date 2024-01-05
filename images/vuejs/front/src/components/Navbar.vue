<!-- <template>
  <nav class="navbar navbar-expand-lg bg-primary fixed-top" data-bs-theme="dark">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">Game</router-link>
      <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <div class="navbar-nav">
          <router-link to="/account" active-class="active" class="nav-link text-light">Account</router-link>
          <router-link to="/leaderboard" active-class="active" class="nav-link text-light">Leaderboard</router-link>
          <router-link to="/tournaments" active-class="active" class="nav-link text-light">Tournaments</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>

</style>

<script>
export default {
    data() {
        return {

        }
    },
}
</script> -->

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
          <li><router-link class="text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/leaderboard">Leaderboard</router-link></li>
          <li><router-link class="text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/tournaments">Tournaments</router-link></li>
          <li class="md:hidden"><router-link class="text-lg font-semibold text-gray-800 hover:text-gray-500 no-underline ease-in-out transition-colors" to="/account">My Account</router-link></li>
          <li class="hidden md:block"><router-link to="/account"><img class="rounded-full h-14 w-14 border-1 border-black" src="../assets/avatars/todo.jpg" alt="profile_pic"></router-link></li>
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
};
</script>