<template>
    <div id="nav">
        <a href="/communtites"><div id="communities" v-on:click="goTo('communities')">Communities</div></a>   
        <a href="/profile"><div id="profile" v-on:click="goTo('profile')">Profile</div></a>
        <a href="/leaderboard"><div id="leaderboard" v-on:click="goTo('leaderboard')">Leaderboard</div></a>
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
}
</style>