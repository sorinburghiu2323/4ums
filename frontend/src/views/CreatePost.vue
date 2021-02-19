<template>
    <div>
        Create a post
        <br>
        Title <br>
        <input v-model="title" placeholder="Post Title"> 
        <br>
        Post Content <br>
        <textarea v-model="description" placeholder="What do you want to post?"></textarea>
        <br>
        <input type="radio" id="discussion" value="Discussion" v-model="type">
        <label for="discussion">Discussion</label>
        <br>
        <input type="radio" id="question" value="Question" v-model="type">
        <label for="question">Question</label>
        <br>
        <p id="success" style="color: green;"></p>
        <button v-on:click="createPost()">Submit Post</button>
    </div>
</template>

<script>
//import router from '../router/router'
import axios from 'axios';

export default {
    name: 'CreatePost',
    created() {
        this.id = this.$route.params.id;
    },
    methods: {
        createPost: function() {
            console.log("Hello")
            var post_url = "/communities/" + this.id + "/post"
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

<style>

</style>