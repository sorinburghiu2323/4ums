<template>
    <div id="form">
        <div id="communityBox"><font-awesome-icon style="color: #5ff9ab" :icon="['fas', 'users']"/> Community {{ this.id }}</div>
        <input id="title" v-model="title" placeholder="Add an interesting title..."> 
        <br>
        <textarea class="inputBox" v-model="description" placeholder="Post text (optional)..."></textarea>
        <br>
        <p id="success" style="color: green;"></p>
        <button id="submit" v-on:click="createPost()">Submit Post</button>
    </div>
</template>

<script>
//import router from '../router/router'
import axios from 'axios';

export default {
    name: 'CreatePost',
    created() {
        this.id = this.$route.params.id;
        this.type = this.$route.params.type;
    },
    methods: {
        createPost: function() {

            // Get the inputs from the form and send it to backend

            console.log("Hello")
            var post_url = "api/communities/"+this.id.toString()+"/posts"
            axios.post(post_url, {
                title: this.title,
                description: this.description,
                post_type: this.type
            }).then((response) => {
                console.log(response);
                document.getElementById("success").innerHTML = "Posted!";
            }).catch((error) => {
                document.getElementById("success").innerHTML = error.response.data;
                document.getElementById("success").style = "color: red;"
            })
        }
    },
    data() {
        return {
            title: '',
            description: '',
            type: ''
        }
    }
}
</script>

<style scoped>

#communityBox {
    width: 100%;
    background-color: #222531;
    padding: 1vh;
    color: white;
    font-family: 'Trebuchet MS';
}

.inputBox {
    font-family: 'Trebuchet MS';
    background-color: #222531;
    width: 100%;
    border: 0;
    color: white;
    margin-top:1vh;
    height: 75vh;
}

#title {
    font-family: 'Trebuchet MS';
    height: 5vh;
    color: white;
    font-family: 'Trebuchet MS';
    background-color: #222531;
    width: 100%;
    border: 0;
    color: white;
    margin-top: 1vh;
    font-size: 3vh;
}

#submit {
    border-radius: 50%;
    background-image: linear-gradient(to bottom right,#d333bb, #e06ceb);
    height: 11vh;
    width: 11vh;
    position: fixed;
    bottom: 10vh;
    right: 2vh;
    font-size: 2.5vh;
    border-width: 0;
    outline: none;
    cursor: pointer;
}

</style>