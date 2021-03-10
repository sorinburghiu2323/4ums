<template>
  <div>
    <p id="back" @click="$router.go(-1)">
      <font-awesome-icon :icon="['fas', 'arrow-left']" />
      Back
    </p>
    <h1 style="text-align: left; left: 20px;">
      Are you sure you want to delete your account?
    </h1>
    <button id="confirm" @click="deleteAccount()">
      Delete
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  methods: {
    deleteAccount() {
      axios.delete("/api/users/me");
    },
  },
};
</script>

<style>
#confirm {
  background: rgb(254, 155, 47);
  background: linear-gradient(
    90deg,
    rgba(254, 155, 47, 1) 0%,
    rgba(254, 101, 15, 1) 35%
  );
  box-shadow: 0px 5px 40px #c35456;
  padding: 8px;
  margin: 5px;
  border-radius: 25px;
  border: none;
  outline: none;
  cursor: pointer;
  font-weight: 600;
  width: 100px;
}

#back {
  text-align: left;
  color: #777779;
}
</style>
