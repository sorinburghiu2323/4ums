<template>
  <div>
    <button v-if = this.buttonVisible id="circleButton" v-on:click="postSelect()">Create Post</button>
    <div id="iconContainer" v-if = this.selectVisible>
        <p id="title">Post to 4um</p>
        <button class="icon2" v-on:click="createPost('question')"><font-awesome-icon :icon="['fas', 'question']" /></button>
        <button class="icon2" v-on:click="createPost('discussion')"><font-awesome-icon :icon="['fas', 'align-left']" /></button>
        <br>
        <button class="icon3" v-on:click="close()"><font-awesome-icon :icon="['fas', 'times-circle']" /></button>
    </div>  
  </div>
</template>

<script>

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
            this.$router.push({
            name: 'CreatePost',
            params: {
                type: type,
                }
            })
        },
        close: function() {
            this.selectVisible = false;
            this.buttonVisible = true;
        }
    }
}
</script>

<style>
#title {
    color: black;
    font-family: 'Trebuchet MS';
    font-size: 2vh;
}

#circleButton {
    border-radius: 50%;
    background-image: linear-gradient(to bottom right,#d333bb, #e06ceb);
    height: 15vh;
    width: 15vh;
    position: absolute;
    bottom: 10vh;
    right: 0;
    font-size: 2.5vh;
    border-width: 0;
    z-index: 1;
}

#iconContainer {
    background-color: #8a3bfe;
    width: 100%;
    border-radius: 20% 20% 0 0;
    height: 21vh;
    position: absolute;
    bottom: 0;
    left: 0px;
    text-align: center;
    z-index: 1;
}

.icon2 {
    border-radius: 50%;
    background-color: #21242f;
    color: #8a3bfe;
    height: 7vh;
    width: 7vh;
    font-size: 3vh;
    text-align: center;
    vertical-align: middle;
    border-width: 0;
}

.icon3 {
    border-radius: 50%;
    background-color: #21242f;
    color: #8a3bfe;
    height: 5vh;
    width: 5vh;
    font-size: 2.5vh;
    text-align: center;
    vertical-align: middle;
    top: 1vh;
    border-width: 0;
}
</style>