<template>
    <div>
        <p class="info" style="text-align: right" v-on:click="editPage()"><font-awesome-icon :icon="['fas', 'edit']"/></p>
        <p id="title">Profile</p>
        <div id="profilePicture" v-if="!this.editing">
            <p>{{ this.initials }}</p>
        </div>
        <div v-if="!this.editing" id="mainProfileInfo">
            <p class="info">{{ this.firstName+" "+this.secondName }}</p>
            <p class="info">{{ this.username }}</p>
            <p class="info">{{ this.points }} points</p>
        </div>
        <div v-if="this.editing">
            <input class="edit" v-model=newFirstName placeholder="Enter first name"><br>
            <input class="edit" v-model=newSecondName placeholder="Enter second name"><br>
            <input class="edit" v-model=newUserName placeholder="Enter username"><br>   
            <button id="doneEditing" v-on:click="confirmEdit(newFirstName, newSecondName, newUserName)">Done</button>
        </div>
        <div id="communities" v-for="comm in this.communities" :key="comm">
            <CommunitiesList/>
        </div>
        <div style="padding-top: vh;">
        <p>Leaderboard Position Over Time</p>
        <VueBarGraph :points="this.leaderboardInfo"
  :width="200"
  :height="100"/>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import VueBarGraph from 'vue-bar-graph';
import CommunitiesList from '../components/communities/CommunitiesList.vue'

export default {
    components: {
        VueBarGraph,
        CommunitiesList
    },
    mounted() {
        this.getUserDetails();
    },
    methods: {
        getUserDetails() {
            axios.get("/api/users/1")
            .then((response) => {
                console.log(response.data)
                this.firstName = response.data.first_name;
                this.secondName = response.data.last_name;
                this.username = response.data.username;
                this.isTeacher = response.data.is_teacher;
                this.leaderboardPosition = response.data.leaderboard_position;
                this.points = response.data.points;
                this.leaderboardInfo = [5,6,3,2]//response.data.graphs.recent;
                this.communities = ["comm1", "comm2"]//response.data.graphs.top_communities;
                this.initials = this.firstName.substring(0,1)+this.secondName.substring(0,1);
            }).catch((error) => {
                console.log(error)
            })
        },
        editPage() {
            this.editing = true;
        },
        confirmEdit(newFirstName, newSecondName, newUserName) {
            this.editing = true;
            this.firstName = newFirstName;
            this.secondName = newSecondName;
            this.username = newUserName;

            // add API request to update
        }
    },
    data() {
        return {
            id: 0,
            username: "",
            firstName: "O",
            secondName: "B",
            isTeacher: false,
            points: 0,
            editing: false,
            leaderboardPosition: 0,
            leaderboardInfo: [],
        }
    },
}
</script>

<style>
#title {
    font-size: 3vh;
}

#mainProfileInfo {
    width: 100%;
    height: 15vh;
    text-align: center;
}

#profilePicture {
    width: 100px;
    height: 100px;
    position: relative;
    border-radius: 50%;
    background-color: green;
    display: flex;
    text-align: center;
    margin: auto;
}

#profilePicture p {
    position: absolute;
    left: 19px;
    top: -33px;
    font-size: 50px;
}


</style>