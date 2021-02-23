<template>
  <div id="app">
    <div style="margin-bottom: 11vh;">
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
html {
}

body {
  background: rgb(34,25,59);
  background: linear-gradient(180deg, rgba(34,25,59,1) 0%, rgba(22,16,38,1) 35%, rgba(1,0,1,1) 100%);

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
