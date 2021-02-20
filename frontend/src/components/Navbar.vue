<template>
    <div id="nav">
        <router-link class="nav-link" to="../" v-on:click = "goTo('homepage')"><div id="homepage" v-on:click="goTo('homepage')"><font-awesome-icon :icon="['fas', 'home']" /><p class="icon">Feed</p></div></router-link>
        <router-link class="nav-link" to="../communities" v-on:click = "goTo('communities')"><div id="communities" v-on:click="goTo('communities')"><font-awesome-icon :icon="['fas', 'users']" /><p class="icon">Communities</p></div></router-link> 
        <router-link class="nav-link" to="../profile" v-on:click = "goTo('profile')"><div id="profile" v-on:click="goTo('profile')"><font-awesome-icon :icon="['fas', 'user']" /><p class="icon">Profile</p></div></router-link>
        <router-link class="nav-link" to="../leaderboard" v-on:click = "goTo('leaderboard')"><div id="leaderboard" v-on:click="goTo('leaderboard')"><font-awesome-icon :icon="['fas', 'trophy']" /><p class="icon">Leaderboard</p></div></router-link>
    </div>
</template>

<script>

export default {
    name: "Navbar",
    data: function() {
        return {
            pages: ["homepage", "communities", "profile", "leaderboard"]
        }
    },
    methods: {
        goTo: function(location) {
            // update the text colour depending on which is selected
            document.getElementById(location).style.color = "#5FF9AB";
            // this.$router.replace(location)
            for (var i=0; i<4; i++) {
                if (this.pages[i] != location) {
                    document.getElementById(this.pages[i]).style.color = "rgb(126, 126, 126)";
                }
            }
        }
    },
    mounted() {
        document.getElementById('homepage').style.color = "#5FF9AB";
        for (var i=1; i<4; i++) {
            document.getElementById(this.pages[i]).style.color = "rgb(126, 126, 126)";
        }
    }
}
</script>

<style>
#nav {
    font-size: 4vh;
    font-family: 'Trebuchet MS';
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    height: 11vh;
    background-color: #161626;
    color:rgb(126, 126, 126);
    width: 100%;
    position: static;
    bottom: 0;
    left: 0;
    border-radius: 25px;
}

.nav-link{
    text-decoration: none !important;
}

.icon {
    font-size: 2vh;
    margin-top: 1vh;
    margin-bottom: 1vh;
}
</style>