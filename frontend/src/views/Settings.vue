<template>
  <div class="container">
    <p id="back" @click="goBack()">
      <font-awesome-icon :icon="['fas', 'arrow-left']" />
      Back
    </p>
    <h1 style="text-align: left; margin-left: 20px; margin-bottom: 1vh">
      Settings
    </h1>
    <div class="sign-out" @click="signOut()">
      <p>Sign out</p>
    </div>
    <div class="sign-out">
      <p>
        Privacy
      </p>
      <div
        style="left: 20px; top: -10px; position: relative; margin-bottom: 10px"
      >
        Show me on the leaderboard
      </div>
      <div style="float: right; position: relative; top: -50px;">
        <label class="switch" v-if="hideLeaderboard !== null">
          <input type="checkbox" v-model="hideLeaderboard" />
          <span class="slider round"></span>
        </label>
      </div>
    </div>
    <div class="small-sign-out" @click="changePassword()">
      <p>Change your password</p>
    </div>
    <div class="small-sign-out" @click="deleteAccount()">
      <p>Delete your account</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      hideLeaderboard: null,
    };
  },
  mounted() {
    this.toggle();
    axios.get('/api/users/me').then((response) => {
      this.hideLeaderboard = !response.data.hide_leaderboard;
    });
  },
  watch: {
    hideLeaderboard: function() {
      axios.get("/api/users/me").then((response) => {
        axios
          .put("/api/users/me", {
            email: response.data.email,
            first_name: response.data.first_name,
            last_name: response.data.last_name,
            hide_leaderboard: !this.hideLeaderboard,
            username: response.data.username,
            description: response.data.description,
          })
          .then(() => {})
          .catch((error) => {
            console.error(error.response.data);
          });
      });
    },
  },
  methods: {
    changePassword() {
      this.$router.push({ name: "ChangePassword" });
    },
    deleteAccount() {
      this.$router.push({ name: "DeleteCheck" });
    },
    signOut() {
      axios.post("/api/logout");
      this.$router.push("/login");
    },
    toggle() {
      axios.get("/api/users/me").then((response) => {
        this.hideLeaderboard = response.data.hideLeaderboard;
      });
    },
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>

.container {
  width: 100%;
  overflow: hidden;
}
.switch {
  padding-bottom: 2px;
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
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

.sign-out {
  width: 100%;
  font-family: "Trebuchet MS";
  color: white;
  background-color: #222531;
  border: 0;
  margin-top: -20px;
  text-align: left;
}

.sign-out p {
  font-weight: 600;
  font-size: 24px;
  padding-top: 5px;
  margin-left: 20px;
  padding-bottom: 10px;
}

.small-sign-out {
  width: 100%;
  font-family: "Trebuchet MS";
  color: white;
  background-color: #222531;
  border: 0;
  margin-top: -12px;
  text-align: left;
}

.small-sign-out p {
  font-size: 16px;
  padding-top: 5px;
  margin-left: 20px;
  padding-bottom: 10px;
}

#back {
  text-align: left;
  color: #777779;
  cursor: pointer;
}
</style>
