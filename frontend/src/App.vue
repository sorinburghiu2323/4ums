<template>
  <div id="app">
    <router-view/>
    <!--Do not change -->
    <div v-if="this.$route.name !== 'LoginPage' && this.$route.name !== 'RegisterPage' && this.$route.name !==
    'ForgotPassword' && this.$route.name !== 'EnterNewPassword'"
         style="margin-bottom: 11vh;">
      <Navbar/>
    </div>
    <Particles id="tsparticles" :options="{
      fpsLimit: 30,
      particles: {
        number: {
          value: 20
        },
        color: {
          value: '#4CF1C4'
        },
        move: {
          enable: true
        },
        size: {
          random: true,
          value: 3
        }
      }
    }"
    />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
/* Do not change - ensures lower page content is visible above navbar */
body {
  min-height: 100vh;
  height: 100%;
  overflow:visible;
  background: rgb(34,25,59);
  background: linear-gradient(180deg, rgba(34,25,59,1) 0%, rgba(22,16,38,1) 35%, rgba(1,0,1,1) 100%);
  margin-bottom: 11vh;
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
#tsparticles {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: -1;
}

button {
  cursor: pointer;
  outline: none;
}
</style>
