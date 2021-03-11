<template>
    <div class="container">
      <div class="forgot-form">
        <div class="header">
          <div class="logo-container">
            <img class="logo-container" src="@/assets/website-logo.png">
          </div>
        </div>
        <div v-if="!sentEmail && invalidEmail">
        <div class="info" style="margin-bottom: 10px">
            Reset Your Password:
        </div>
            <div style="color:red; z-index: 2; text-align: left; margin-bottom: 5px;">{{this.errorMessage}}</div>
        <div class="input">
            <div class="color-bar" style="background: #FB6D13"></div>
            <input v-model="emailField" placeholder="Email address" type="email">
        </div>
        <div class="details">
            Unfortunately if you are unable to access your email account we will not
            be able to reset your password.
        </div>
        <button class="buttonSmart" type="submit" @click.stop="submitEmail">
            Email Me
        </button>
        </div>
        <div v-else>
            The reset link has been sent to your email address, this link will expire in 30 minutes.
        </div>
        <div class="back-button" @click.prevent="goBack()">
            <font-awesome-icon :icon="['fas', 'arrow-left']"/>
            Back to <u>login page</u>
        </div>
      </div>
    </div>
</template>

<script>
import LoginPage from "@/views/LoginPage";
import axios from "axios";

export default {
    name: "ForgotPassword",
    data() {
        return {
          emailField: "",
          hover: false,
          sentEmail: false,
          invalidEmail: true,
          errorMessage: ''
        };
    },
    methods: {
        submitEmail() {
          axios.post('/api/login/sendreset', {email: this.emailField})
              .then(() => {
                this.sentEmail = true;
                this.invalidEmail = false;
                this.errorMessage = '';
              }).catch((error) => {
            this.invalidEmail = true;
            this.errorMessage = "We couldn't find any account with that email address";
            console.error(error.response.data);
          })
        },
        goBack() {
            this.$router.push(LoginPage);
        }
    }
}
</script>
<style scoped>
.container{
    display: flex;
    width: 100%;
    height: 100vh;
    animation: fade-in-move-down 0.7s;
}
.logo-container {
    width: 300px;
    height:auto;
    background:None;
    margin: auto;
}

.forgot-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: auto;
}

.info {
    position: relative;
    font-size: 15px;
    margin-left: 20px;
    color: white;
    font-weight: 600;
}

.input {
  text-align: left;
  margin: auto;
  width: 280px;
}

.input input {
  width: inherit;
  height: 46px;
  margin-left: 8px;
  margin-bottom: 15px;
  border-radius: 8px;
  border: none;
  outline: none;
  color: white;
  background: rgb(40, 44, 58);
  background: linear-gradient(
    90deg,
    rgba(40, 44, 58, 1) 0%,
    rgba(27, 30, 40, 1) 35%,
    rgba(8, 9, 11, 1) 100%
  );
  padding-left: 15px;
}

input::placeholder {
  font-weight: 500;
  color: white;
}

.input p {
  margin-bottom: 3px;
}

.color-bar {
  height: 48px;
  width: 15px;
  border-radius: 10px 0px 0 10px;
  position: absolute;
}

.details {
    z-index: 2;
    position: relative;
    font-size: 15px;
    margin: auto;
    color: white;
    font-weight: 600;
    width: 300px;
}

.buttonSmart {
    z-index: 2;
    border: none;
    background: linear-gradient(to bottom, #FB9C30, #FA7E1E);
    box-shadow: 0 0 10px #FB8D11;
    height: 40px;
    color: black;
    width: 100px;
    border-radius: 20px;
    margin-top: 25px;
    cursor: pointer;
    font-weight: 600;
    outline: none;
    font-size: 15px;
}

.buttonSmart:hover {
    background: #FB9C30;
    box-shadow: 0 0 30px #FB9C30;
}

.back-button {
    position: relative;
    cursor: pointer;
    font-weight: 600;
    margin-top: 20px;
}
@keyframes fade-in-move-down {
  0% {
    opacity: 0;
    transform: translateY(-3rem);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>