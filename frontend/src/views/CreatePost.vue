<template>
    <div id="form">
        <div id="communityBox"><font-awesome-icon :icon="['fas', 'users']" style="color: #5ff9ab"/> Community {{ this.id }}</div>
        <input class="inputBox" id="title" v-model="title" placeholder="Add an interesting title..."> 
        <br>
        <textarea class="inputBox" v-model="description" placeholder="Post text (optional)..."></textarea>
        <br>
        <!--<input type="radio" id="discussion" value="Discussion" v-model="type">
        <label for="discussion">Discussion</label>
        <br>
        <input type="radio" id="question" value="Question" v-model="type">
        <label for="question">Question</label>
        <br> -->
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
            var post_url = "/communities/" + this.id + "/posts"
            axios.post(post_url, {
                title: this.title,
                description: this.description,
                type: this.type
            }).then((response) => {
                console.log(response);
                document.getElementById("success").innerHTML = "Posted!";
            }).catch((error) => {
                console.log(error);
                document.getElementById("success").innerHTML = "Post failed";
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
}

</style>