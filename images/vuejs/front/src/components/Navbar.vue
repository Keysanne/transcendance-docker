<template>
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
</script>