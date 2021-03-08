<template>
  <div>
    <div @click="goBack()">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
        Communities
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
      email: "",
      firstName: "",
      lastName: "",
      username: "",
    };
  },
  methods: {
    submit() {
      axios.get("/api/users/me").then((response) => {
        console.log(response);
        axios
          .put("/api/users/me", {
            email: response.data.email,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            hide_leaderboard: true,
            username: response.data.username,
            description: this.description,
          })
          .then((response) => {
            console.log(response);
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
#submit {
  margin-top: 1vh;
  border-radius: 15px;
  width: 33%;
  height: 7.5%;
  font-family: "Trebuchet MS";
  color: black;
  background-image: linear-gradient(to right, #348be9, #65ffa7);
  padding: 1vh;
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
