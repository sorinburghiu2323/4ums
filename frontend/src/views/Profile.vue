<template>
    <div>
        <p id="title">Profile</p>
         <p class="info" style="text-align: right" v-on:click="editPage()"><font-awesome-icon :icon="['fas', 'edit']"/></p>
        <div id="profilePicture" v-if="!this.editing">
            <p>{{ this.firstName.substring(0,1)+this.secondName.substring(0,1)}}</p>
        </div>
        <div v-if="!this.editing" id="mainProfileInfo">
            <p class="info">{{ this.firstName+" "+this.secondName }}</p>
            <p class="info">{{ this.username }}</p>
        </div>
        <div v-if="this.editing">
            <input class="edit" v-model=newFirstName placeholder="Enter first name"><br>
            <input class="edit" v-model=newSecondName placeholder="Enter second name"><br>
            <input class="edit" v-model=newUserName placeholder="Enter username"><br>   
            <button id="doneEditing" v-on:click="confirmEdit(newFirstName, newSecondName, newUserName)">Done</button>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    mounted() {
        this.getUserDetails();
    },
    methods: {
        getUserDetails() {
            axios.get("/api/users/1")
            .then((response) => {
                console.log(response);
            }).catch((error) => {
                console.log(error)
            })
        },
        editPage() {
            this.editing = true;
        },
        confirmEdit(newFirstName, newSecondName, newUserName) {
            this.editing = false;
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
        }
    },
}
</script>

<style>

#mainProfileInfo {
    float: left;
    width:66%;
    height: 15vh;
    margin-left: 2vh;
    text-align: left;
}

#profilePicture {
    float: left;
    width: 100px;
    height: 100px;
    position: relative;
    border-radius: 50%;
    background-color: green;
}

#profilePicture p {
    position: absolute;
    left: 22px;
    top: -35px;
    font-size: 50px;
}


</style>