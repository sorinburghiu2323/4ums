<template>
  <div id="app">
    <router-view/>
    <Navbar />
  </div>
</template>

<script>
//import Navbar from "./components/Navbar"

export default {
  name: 'App',
  components: {
    //Navbar
  }
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-image: linear-gradient(#22193B, #09090E);
  height: 100vh;
  width: 100;
  margin: 0;
  top: 0;
}

</style>
