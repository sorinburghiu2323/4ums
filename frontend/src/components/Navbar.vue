<template>
    <div id="nav">
        <router-link class="nav-link" to="../communities" v-on:click = "goTo('communities')"><div id="communities" v-on:click="goTo('communities')">Communities</div></router-link> 
        <router-link class="nav-link" to="../profile" v-on:click = "goTo('profile')"><div id="profile" v-on:click="goTo('profile')">Profile</div></router-link>
        <router-link class="nav-link" to="../leaderboard" v-on:click = "goTo('leaderboard')"><div id="leaderboard" v-on:click="goTo('leaderboard')">Leaderboard</div></router-link>
    </div>
</template>

<script>

export default {
    name: "Navbar",
    data: function() {
        return {
            pages: ["communities", "profile", "leaderboard"]
        }
    },
    methods: {
        goTo: function(location) {
            // update the text colour depending on which is selected
            document.getElementById(location).style.color = "black";
            // this.$router.replace(location)
            for (var i=0; i<3; i++) {
                if (this.pages[i] != location) {
                    document.getElementById(this.pages[i]).style.color = "white";
                }
            }
        }
    }
}
</script>

<style>
#nav {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    height: 10vh;
    background-color: grey;
    color:white;
    width: 100%;
    position: fixed;
    bottom: 0;
    left: 0;
}
</style>