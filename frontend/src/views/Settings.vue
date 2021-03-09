<template>
  <div>
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
      Show me on the leaderboard
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goBack() {
      this.$router.go(-1);
    },
  },
};
</script>

<style>
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
}

#back {
  text-align: left;
  color: #777779;
}
</style>
