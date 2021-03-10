<template>
  <div>
    <div @click="goBack()">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
        Profile
      </p>
    </div>
    <h1 style="text-align: left">Edit Your Profile</h1>
    <div class="titleBox" style="height: 6.5vh">
      <p
        class="titleBox"
        style="position: relative; float: left; margin-left: 2vh"
      >
        Description
      </p>
      <br />
      <font-awesome-icon
        :icon="['fas', 'edit']"
        class="titleBox"
        style="position: relative; float: right; margin-right: 2vh"
      />
    </div>
    <textarea
      v-model="description"
      class="inputBox"
      placeholder="Enter a bio"
    ></textarea>
    <button id="submit" @click="submit()">Submit</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      description: "",
      hideLeaderboard: true,
    };
  },
  created() {
    axios.get("/api/users/me")
    .then(response => {
      this.description = response.data.description;
    })
    .catch(error => {
      console.error(error);
    })
  },
  methods: {
    submit() {
      axios.get("/api/users/me").then((response) => {
        axios
          .put("/api/users/me", {
            email: response.data.email,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            hide_leaderboard: !this.hideLeaderboard,
            username: response.data.username,
            description: this.description,
          })
          .then(() => {
            this.goBack();
          })
          .catch((error) => {
            console.error(error.response.data);
          });
      });
    },
    goBack() {
      this.$router.push({
        name: "Profile",
      });
    },
  },
};
</script>

<style scoped>
.switch {
  padding-bottom: 2px;
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
  margin: auto;
  margin-right: 0;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196f3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196f3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
#submit {
  margin-top: 1vh;
  border-radius: 15px;
  width: 33%;
  height: 7.5%;
  font-family: "Trebuchet MS";
  color: black;
  background-image: linear-gradient(to right, #348be9, #65ffa7);
  padding: 1vh;
  border: none;
  cursor: pointer;
}

#back {
  text-align: left;
}

.titleBox {
  background-color: #222531;
}

.inputBox {
  font-family: "Trebuchet MS";
  background-color: #222531;
  width: 90%;
  border: 0;
  color: white;
  margin-top: 1vh;
  height: 25vh;
  padding: 2vh;
}
</style>
