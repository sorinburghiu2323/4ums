<template>
  <div id="nav">
    <router-link class="nav-link" to="/" v-on:click="goTo('feed')">
      <div id="feed" style="color: gray" v-on:click="goTo('feed')">
        <font-awesome-icon :icon="['fas', 'home']" />
        <p class="nav-icon">Feed</p>
      </div>
    </router-link>
    <router-link
      class="nav-link"
      to="/communities"
      v-on:click="goTo('communities')"
    >
      <div
        id="communities"
        style="color: gray"
        v-on:click="goTo('communities')"
      >
        <font-awesome-icon :icon="['fas', 'users']" />
        <p class="nav-icon">Communities</p>
      </div>
    </router-link>
    <router-link class="nav-link" to="/profile" v-on:click="goTo('profile')">
      <div id="profile" style="color: gray" v-on:click="goTo('profile')">
        <font-awesome-icon :icon="['fas', 'user']" />
        <p class="nav-icon">Profile</p>
      </div>
    </router-link>
    <router-link
      class="nav-link"
      to="/leaderboard"
      v-on:click="goTo('leaderboard')"
    >
      <div
        id="leaderboard"
        style="color: gray"
        v-on:click="goTo('leaderboard')"
      >
        <font-awesome-icon :icon="['fas', 'trophy']" />
        <p class="nav-icon">Leaderboard</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data: function() {
    return {
      pages: ["feed", "communities", "profile", "leaderboard"],
    };
  },
  mounted() {
    let pageName = this.$route.fullPath;
    let pageName2 = pageName.substring(1).split("/")[0];
    for (let i = 1; i < 4; i++) {
      document.getElementById(this.pages[i]).style.color = "rgb(126, 126, 126)";
    }

    if (pageName2 === "") {
      document.getElementById(this.pages[0]).style.color = "#5FF9AB";
    } else {
      document.getElementById(pageName2).style.color = "#5FF9AB";
    }
  },
  methods: {
    goTo: function(location) {
      // update the text colour depending on which is selected
      document.getElementById(location).style.color = "#5FF9AB";
      // this.$router.replace(location)
      for (let i = 0; i < 4; i++) {
        if (this.pages[i] !== location) {
          document.getElementById(this.pages[i]).style.color =
            "rgb(126, 126, 126)";
        }
      }
    },
  },
};
</script>

<style>
#nav {
  font-size: 4vh;
  font-family: "Trebuchet MS";
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  height: 11vh;
  background-color: #161626;
  color: rgb(126, 126, 126);
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  border-radius: 25px 25px 0 0;
}

.nav-link {
  text-decoration: none !important;
  text-align: center;
}

.nav-icon {
  font-size: 2vh;
  margin-top: 1vh;
  margin-bottom: 1vh;
  text-align: center;
}
</style>
