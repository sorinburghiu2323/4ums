<template>
  <div class="container">
    <button
      v-if="this.buttonVisible"
      id="circleButton"
      v-on:click="postSelect()"
    >
      Create Post
    </button>
    <div v-if="this.selectVisible" id="iconContainer">
      <p id="title">Post to 4um</p>
      <div id="bottomFlex">
        <div>
          <button class="icon2" v-on:click="createPost('question')">
            <font-awesome-icon :icon="['fas', 'question']" />
          </button>
          <p style="color: black; font-size: 10px">Question</p>
        </div>
        <div>
          <button class="icon2" v-on:click="createPost('discussion')">
            <font-awesome-icon :icon="['fas', 'comment-dots']" />
          </button>
          <p style="color: black; font-size: 10px">Discussion</p>
        </div>
      </div>
      <button style="top: 0" class="icon3" v-on:click="close()">
        <font-awesome-icon :icon="['fas', 'times-circle']" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectVisible: false,
      buttonVisible: true,
    };
  },
  methods: {
    postSelect: function() {
      this.selectVisible = true;
      this.buttonVisible = false;
    },
    createPost: function(type) {
      this.$router.push({
        name: "CreatePost",
        params: {
          id: this.id,
          type: type,
        },
      });
    },
    close: function() {
      this.selectVisible = false;
      this.buttonVisible = true;
    },
  },
};
</script>

<style scoped>
#bottomFlex {
  display: flex;
  justify-content: space-around;
}

#circleButton {
  border-radius: 50%;
  background: linear-gradient(to bottom right, #b437ff, #9c39ff);
  height: 15vh;
  width: 15vh;
  position: fixed;
  bottom: 10vh;
  right: 0;
  font-size: 2.5vh;
  border-width: 0;
  z-index: 1;
}

#title {
  color: black;
  font-family: "Trebuchet MS";
  font-size: 2vh;
}

#iconContainer {
  background: linear-gradient(to bottom right, #b437ff, #9c39ff);
  width: 100%;
  border-radius: 20% 20% 0 0;
  height: 23vh;
  position: fixed;
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
