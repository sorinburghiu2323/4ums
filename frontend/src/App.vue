<template>
  <div id="app">
    <div>
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

* {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: linear-gradient(to bottom, #22193b, #161626);
  height: 100vh;
}

</style>
