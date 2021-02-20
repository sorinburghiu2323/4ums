<template>
  <div id="app">
    <router-view/>
    <div class="navbar-container">
      <Navbar />
    </div>
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
body{
  background: rgb(34,25,59);
  background: linear-gradient(180deg, rgba(34,25,59,1) 0%, rgba(22,16,38,1) 35%, rgba(1,0,1,1) 100%);
}
#app {
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}
.navbar-container {
  margin-top: 200px;
}
.navigation-display {
  color: #7E7E7E;
  font-size: 12px;
  position: absolute;
  top:0;
  left: 0;
  padding: 10px;
}
</style>
