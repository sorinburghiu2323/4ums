<template>
  <div>
    <button v-if = this.buttonVisible id="circleButton" v-on:click="postSelect()">Create Post</button>
    <div v-if = this.selectVisible>
        <button v-on:click="createPost('question')">Question</button>
        <button v-on:click="createPost('discussion')">Discussion</button>
        <br>
        <button v-on:click="close()">X</button>
    </div>  
  </div>
</template>

<script>
import router from '../router/router'

export default {
    data() {
        return {
            selectVisible: false,
            buttonVisible: true
        }
    },
    methods: {
        postSelect: function() {
            this.selectVisible = true;
            this.buttonVisible = false;
        },
        createPost: function(type) {
            router.push(this.$route.path+"post/"+type)
        },
        close: function() {
            this.selectVisible = false;
            this.buttonVisible = true;
        }
    }
}
</script>

<style>

#circleButton {
    border-radius: 50%;
    background-image: linear-gradient(to bottom right,#d333bb, #e06ceb);
    height: 15vh;
    width: 15vh;
    position: fixed;
    bottom: 10vh;
    right: 0;
    font-size: 2.5vh;
}

</style>