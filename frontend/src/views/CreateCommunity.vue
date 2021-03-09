<template>
  <div>
    <router-link class="nav-link" to="../manage">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" /> Manage Communities
      </p>
    </router-link>
    <p id="pageTitle">Create a<br />Community</p>
    <br />
    <div v-if="createVisible">
      <input
        v-model="name"
        class="inputBox"
        maxlength="25"
        placeholder="Write a community title (max 25 characters)..."
      /><br />
      <br />
      <textarea
        id="descriptionBox"
        v-model="description"
        class="inputBox"
        placeholder="(Optional) Write a community description..."
      ></textarea>
      <p id="label">(Optional) Choose a colour</p>
      <div id="colourSelect">
        <button id="blueButton" v-on:click="setColour('blue')"></button>
        <button id="orangeButton" v-on:click="setColour('orange')"></button>
        <button id="purpleButton" v-on:click="setColour('purple')"></button>
      </div>
      <button id="preview" v-on:click="preview()">Preview</button>
    </div>

    <div v-if="!this.createVisible" class="container">
      <div v-if="colour" :class="colour" class="color-box"></div>
      <div class="details">
        <div class="title">
          <p>{{ name }}</p>
        </div>
        <div class="description">
          <p>{{ description }}</p>
        </div>
      </div>
    </div>

    <div v-if="!this.createVisible" id="submitScrap">
      <button id="submit" v-on:click="submit()">
        Create
      </button>
      <button id="scrap" v-on:click="preview()">
        Back
      </button>
    </div>

    <p style="color: red; font-size: 12px;">{{ errorMessage }}</p>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateCommunity",
  methods: {
    setColour: function(colour) {
      for (let i = 0; i < 3; i++) {
        document.getElementById(this.colours[i] + "Button").style = "";
      }

      document.getElementById(colour + "Button").style =
        "border-color: white; border-width: 1vh; border: 3px solid white;";
      this.colour = colour;
      this.hexCode = this.hex[this.colours.indexOf(colour)];
    },
    changeBackground: function() {
      document.getElementById("previewDiv").style =
        "background-image: linear-gradient(to right, " +
        this.hexCode +
        ", #1c1f29);";
    },
    preview: function() {
      this.errorMessage = null;
      this.createVisible = !this.createVisible;
      this.changeBackground();
    },
    submit: function() {
      axios
        .post("/api/communities", {
          name: this.name,
          description: this.description,
          colour: this.colour,
        })
        .then(() => {
          this.$router.push({name: 'Communities'});
        })
        .catch((error) => {
          this.errorMessage = error.response.data;
          console.error(error);
        });
    },
  },
  data() {
    return {
      name: "",
      description: "",
      colour: "",
      colours: ["blue", "orange", "purple"],
      hex: ["#4af4cb", "#fa7e1f", "#a038fe"],
      hexCode: "#4af4cb",
      createVisible: true,
      errorMessage: null,
    };
  },
};
</script>

<style scoped>
button {
  outline: none;
}

#submit {
  border-radius: 15px;
  width: 33%;
  height: 7.5%;
  font-family: "Trebuchet MS";
  color: black;
  background-image: linear-gradient(to right, #348be9, #65ffa7);
  padding: 1vh;
  border: none;
}

#scrap {
  border-radius: 15px;
  width: 33%;
  height: 7.5%;
  font-family: "Trebuchet MS";
  color: black;
  background-image: linear-gradient(to right, #fe6911, #fe9b2f);
  padding: 1vh;
  margin-left: 2vh;
  border: none;
}

#previewDiv {
  background-image: linear-gradient(to right, #232733, #1c1f29);
  border-radius: 15px;
  height: 15vh;
  width: 75%;
  margin: auto;
  left: 20vh;
  padding: 2vh;
  text-align: left;
  padding-left: 6vh;
  font-family: "Trebuchet MS";
  border-width: 2vh;
}

#label {
  color: white;
  font-family: "Trebuchet MS";
  text-align: left;
  padding: 2vh;
}

#preview {
  border-radius: 15px;
  border: none;
  width: 75%;
  height: 7.5%;
  font-family: "Trebuchet MS";
  font-weight: 600;
  font-size: 15px;
  color: black;
  background-image: linear-gradient(to right, #348be9, #65ffa7);
  padding: 1vh;
}

#blueButton {
  border-radius: 50%;
  background-color: #4af4cb;
  filter: drop-shadow(0px 0px 5px #4af4cb);
  height: 5vh;
  width: 5vh;
  margin: 1vh;
}

#orangeButton {
  border-radius: 50%;
  background-color: #fa7e1f;
  filter: drop-shadow(0px 0px 5px #fa7e1f);
  height: 5vh;
  width: 5vh;
  margin: 1vh;
}

#purpleButton {
  border-radius: 50%;
  background-color: #a038fe;
  filter: drop-shadow(0px 0px 5px #a038fe);
  height: 5vh;
  width: 5vh;
  margin: 1vh;
}

#colourSelect {
  display: flex;
  padding: 2vh;
}

#colourSelect button{
  border: none;
  outline: none;
  cursor: pointer;
}

#back {
  text-align: left;
  color: #777779;
}

#descriptionBox {
  height: 25vh;
  resize: none;
}

#pageTitle {
  color: white;
  text-align: left;
  font-size: 4vh;
  font-family: "Trebuchet MS";
  margin-left: 2vh;
  padding-top: 2vh;
}

::placeholder {
  color: white;
}

.fieldDesc {
  font-family: "Trebuchet MS";
}

.inputBox {
  width: 90%;
  border-radius: 10px;
  padding: 10px;
  border: none;
  color: white;
  background: linear-gradient(to right, #262b38, #1d2029);
  font-family: "Trebuchet MS";
  outline: none;
}

.innerText {
  color: white;
}

.container {
  text-align: left;
  display: flex;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 0 3px 10px 0;
  height: 100px;
  border: none;
  border-radius: 25px;
  background: rgb(40, 44, 58);
  background: linear-gradient(90deg, rgba(40, 44, 58, 1) 0%, rgba(27, 30, 40, 1) 35%, rgba(8, 9, 11, 1) 100%);
}
.details {
  margin: auto 0 auto 25px;
  padding-right: 10px;
  width: 100%;
  position: relative;
}
.color-box {
  height: 108px;
  width: 20px;
  border-radius: 25px 0 0 25px;
  position: absolute;
}
.orange {
  background: rgb(254,155,47);
  background: linear-gradient(90deg, rgba(254,155,47,1) 0%, rgba(254,101,15,1) 35%);
}
.blue {
  background: rgb(52, 235, 233);
  background: linear-gradient(270deg, rgba(52, 235, 233, 1) 0%, rgba(101, 255, 167, 1) 35%);
}
.purple {
  background: rgb(188, 98, 253);
  background: linear-gradient(270deg, rgb(144, 98, 253) 0%, rgb(149, 0, 255) 35%);
}

</style>
