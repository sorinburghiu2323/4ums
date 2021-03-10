<template>
  <div class="container">
    <button
      v-if="this.buttonVisible"
      id="circleButton"
      v-on:click="postSelect()"
      >
      <div class="curved-text"><img src="@/assets/create-thread.svg"></div>
      <font-awesome-icon :icon="['fa', 'plus']"/>
    </button>
    <div v-if="this.selectVisible" id="iconContainer">
      <p id="title">Post to 4um</p>
      <div class="top-row">
        <div>
          <button class="icon2" v-on:click="createPost('question')">
           <font-awesome-icon :icon="['fas', 'question']"/>
          </button>
          <p class="subtext">Question</p>
        </div>
        <div>
          <button class="icon2" v-on:click="createPost('discussion')">
            <font-awesome-icon :icon="['fas', 'comment-dots']"/>
          </button>
          <p class="subtext">Discussion</p>
        </div>

      </div>
      <div class="bottom-row">
        <button class="icon3" v-on:click="close()">
          <font-awesome-icon :icon="['fa', 'times']"/>
        </button>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  props: {
    community: Object,
  },
  data() {
    return {
      selectVisible: false,
      buttonVisible: true,
    };
  },
  mounted() {
    this.scroll();
  },
  methods: {
    scroll() {
      window.onscroll = () => {
          let bottomOfWindow = document.documentElement.scrollTop +
              window.innerHeight > document.body.scrollHeight + 100;
          if (bottomOfWindow) {
            this.buttonVisible = false;
            // only show button if the select question popup is not displayed
          } else if(!this.selectVisible){
            this.buttonVisible = true;
          }
      }
    },
    postSelect: function() {
      this.selectVisible = true;
      this.buttonVisible = false;
    },
    createPost: function(type) {
      this.$router.push({
        name: "CreatePost",
        params: {
          id: this.community.id,
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
.curved-text {
    position: absolute;
    top: -10px;
    left: 0px;
}

.curved-text img {
    height: 120px;
    transform: rotate(28deg);
}
#circleButton {
  border-radius: 50%;
  background: linear-gradient(to bottom right, #B437FF, #9C39FF);
  height: 14vh;
  width: 14vh;
  position: fixed;
  bottom: 12vh;
  right: 0;
  font-size: 40px;
  font-weight: 600;
  border-width: 0;
  z-index: 1;
  box-shadow: 0px 3px 20px #9C39FF;
  outline: none;

}

#circleButton p {
  font-size: 12px;
  margin: 0;
}

#title {
  color: black;
  font-family: "Trebuchet MS";
  font-size: 2vh;
}

#iconContainer {
  background: rgb(178,50,255);
  background: linear-gradient(180deg, rgba(178,50,255,1) 15%, rgba(155,0,249,1) 100%);
  width: 100%;
  border-radius: 20% 20% 0 0;
  height: 21vh;
  position: fixed;
  bottom: 0;
  left: 0px;
  text-align: center;
  z-index: 1;
}

.icon2 {
  border-radius: 50%;
  background: rgb(40,44,58);
  background: linear-gradient(180deg, rgba(40,44,58,1) 0%, rgba(28,31,40,1) 66%);
  color: #B437FF;
  height: 7vh;
  width: 7vh;
  font-size: 3vh;
  text-align: center;
  vertical-align: middle;
  border-width: 0;
  margin-right: 40px;
  margin-left: 40px;
  display: flex;
}

.icon2 svg, .icon3 svg {
  margin: auto;
}

.subtext{
  color: rgba(28,31,40,1);
  font-size: 15px;
  margin: 0;
}
.icon3 {
  border-radius: 50%;
  background: rgb(40,44,58);
  background: linear-gradient(180deg, rgba(40,44,58,1) 0%, rgba(28,31,40,1) 66%);
  color: #B437FF;
  height: 5vh;
  width: 5vh;
  font-size: 2.5vh;
  text-align: center;
  vertical-align: middle;
  top: 1vh;
  border-width: 0;
  display: flex;
  margin-top: -20px;
}

.top-row, .bottom-row {
  display: flex;
  justify-content: center;
}

</style>
