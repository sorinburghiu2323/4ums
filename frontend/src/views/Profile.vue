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
            <p class="info"><font-awesome-icon :icon="['fas', 'trophy']"/> Leaderboard position: {{ this.leaderboardPosition }}th</p>
            <p class="info"><font-awesome-icon :icon="['fas', 'star']"/> Points: {{ this.points }}</p>
        </div>
        <div v-if="this.editing">
            <input class="edit" v-model=newFirstName placeholder="Enter first name"><br>
            <input class="edit" v-model=newSecondName placeholder="Enter second name"><br>
            <input class="edit" v-model=newUserName placeholder="Enter username"><br>   
            <button id="doneEditing" v-on:click="confirmEdit(newFirstName, newSecondName, newUserName)">Done</button>
        </div>
        <p><u>Top Communities:</u></p>
        <CommunitiesList :communities="this.communities" :myCommunities="true" />
        <p>Leaderboard Position Over Time:</p>
        <div style="padding-top: 5vh;">
        <div style="position: absolute; left: 50%;">
            <div style="position: relative; left: -50%;">
                <div id="graph">
                    <VueBarGraph :points="this.leaderboardInfo"
            :width="250"
            :height="100"/>
                </div>
            </div>
        </div>
        <div id="labels">
            <div id="week1"></div>
            <div id="week2"></div>
            <div id="week3"></div>
            <div id="week4"></div>
        </div>
        <div id="x-axis">
            <div>This Week</div>
            <div>Last Week</div>
            <div>2 Weeks Ago</div>
            <div>3 Weeks Ago</div>
        </div>
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
        generateLabels(info) {
            for (var i=0; i<4; i++) {
                var divName = "week"+(i+1);
                document.getElementById(divName).innerHTML = info[i];
            }
        },
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
                var recents = response.data.graphs.recent;
                this.leaderboardInfo = [recents[0].points, recents[1].points, recents[2].points, recents[3].points];
                console.log(recents[0].points)
                this.communities = [{name: "comm1", id: 0}, {name: "comm2", id: 1}]//response.data.graphs.top_communities;
                this.initials = this.firstName.substring(0,1)+this.secondName.substring(0,1);
                this.generateLabels(this.leaderboardInfo);
            }).catch((error) => {
                console.log(error)
            });
        },
        editPage() {
            this.editing = true;
        },
        confirmEdit(newFirstName, newSecondName, newUserName) {
            this.editing = false;
            try {
                if (newFirstName.length > 0) {
                    this.firstName = newFirstName;
                }
            } catch {
                console.log("No first name");
            }
            try {
                if (newSecondName.length > 0) {
                    this.secondName = newSecondName;
                }
            } catch {
                console.log("No second name");
            }
            try {
                if (newUserName.length > 0) {
                    this.username = newUserName;
                }
            } catch {
                console.log("No user name");
            }

            // add API request to update
        }
    },
    data() {
        return {
            id: 0,
            username: "",
            firstName: "",
            secondName: "",
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
#labels {
    display: flex;
    width: 250px;
    margin: auto;
    position: relative;
    margin-top: -20px;
}

#labels div {
    width: 9vh;
}

#x-axis {
    display: flex;
    width: 250px;
    margin: auto;
    position: relative;
    margin-top: 120px;
}

#x-axis div {
    width: 9vh;
}

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

#graph {
    z-index: 0;
    margin-top: 0;
}



</style>