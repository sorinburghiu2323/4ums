<template>
    <div id="nav">
        <router-link class="nav-link" to="../" v-on:click = "goTo('homepage')"><div id="homepage" v-on:click="goTo('homepage')"><font-awesome-icon :icon="['fas', 'home']" /></div></router-link>
        <router-link class="nav-link" to="../communities" v-on:click = "goTo('communities')"><div id="communities" v-on:click="goTo('communities')"><font-awesome-icon :icon="['fas', 'users']" /></div></router-link> 
        <router-link class="nav-link" to="../profile" v-on:click = "goTo('profile')"><div id="profile" v-on:click="goTo('profile')"><font-awesome-icon :icon="['fas', 'user']" /></div></router-link>
        <router-link class="nav-link" to="../leaderboard" v-on:click = "goTo('leaderboard')"><div id="leaderboard" v-on:click="goTo('leaderboard')"><font-awesome-icon :icon="['fas', 'trophy']" /></div></router-link>
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
                    document.getElementById(this.pages[i]).style.color = "white";
                }
            }
        }
    },
    mounted() {
        for (var i=0; i<4; i++) {
            document.getElementById(this.pages[i]).style.color = "white";
        }
    }
}
</script>

<style>
#nav {
    font-family: 'Trebuchet MS';
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    height: 10vh;
    background-color: #161626;
    color:white;
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
    border-radius: 25px;
}
</style>