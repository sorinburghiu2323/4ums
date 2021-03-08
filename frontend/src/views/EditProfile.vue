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
      email: "Hello",
      firstName: "",
      lastName: "",
      username: "",
    };
  },
  methods: {
    submit() {
      axios.get("/api/user/me").then((response) => {
        //this.email = response.data.email;
        this.firstName = response.data.first_name;
        this.lastName = response.data.last_name;
        this.username = response.data.username;
      });
      axios
        .put("/api/users/me", {
          email: this.email,
          first_name: this.firstName,
          last_name: this.lastName,
          hide_leaderboard: true,
          username: this.username,
          description: this.description,
        })
        .then((response) => {
          console.log(response);
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
