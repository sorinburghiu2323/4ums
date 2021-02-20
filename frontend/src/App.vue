<template>
  <div id="app">
    <div class="page">
      <router-view/>
    </div>
    <Navbar />
  </div>
</template>

<script>
import Navbar from "./components/Navbar"

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.page {
  height: 100vh;
  overflow: scroll;
}
</style>
