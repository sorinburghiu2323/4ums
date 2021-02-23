<template>
  <div class="container">
    <div class="login-form">
      <div class="header">
        <p>Login</p>
        <div class="logo-container"><img src="@/assets/logo.png"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DisplayPost',
  data() {
    return {
      email: '',
      password: '',
      failedLogin: false,
    }
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    },
    loginUser() {

      axios.post('api/login', {email: this.email, password: this.password})
          .then((response) => {
            console.log(response);
            this.failedLogin = false;
            this.$router.push('homepage');
          })
          .catch((error) => {
            console.error(error);
            this.failedLogin = true;
          })

    },
  }

}
</script>

<style scoped>
.container {
  display: flex;
  width: 100%;
}

.login-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
}

.input {
  text-align: left;
}

.input p {
  margin-bottom: 3px;
}

.text {
  text-align: left;
}

input {
  width: 100%;
  height: 25px;
  border-radius: 8px;
  border: 1px solid black;
  outline: none;
}

.login-btn {
  background: white;
  width: 80px;
  height: 40px;
  border-radius: 8px;
  border: 1px solid black;
  outline: none;
  cursor: pointer;
}

.link {
  cursor: pointer;
  text-decoration: underline;
}

.error-message {
  color: red;
  font-size: 14px;
}
</style>