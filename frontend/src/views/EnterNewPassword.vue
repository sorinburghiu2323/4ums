declare module "particles.vue";
<template>
    <div class="container">
      <div class="forgot-form">
        <div class="header">
          <div class="logo-container">
            <img class="logo-container" src="@/assets/website-logo.png">
          </div>
        </div>
        <div class="info" style="margin-bottom: 10px">
            Reset Your Password:
        </div>
        <div class="input">
            <div class="color-bar" style="background: #FB6D13"></div>
            <input v-model="passwordField1" maxlength="34" placeholder="Enter your new password" spellcheck="false"
                   type="password">
        </div>
        <label v-if="notMatching" style="color:red;display:flex; position:relative; margin-left:37px;"> Passwords don't match</label>
        <div class="input">
            <div class="color-bar" style="background: #8A3BFE"></div>
            <input v-model="passwordField2" maxlength="38" placeholder="Confirm your new password" spellcheck="false"
                   type="password">
        </div>
        <button class="buttonSmart" type="submit" @click.stop="submitPassword()">
            Sign in
        </button>
        <div class="back-button" @click.prevent="goBack()">
            <font-awesome-icon :icon="['fas', 'arrow-left']"/>
            Back to <u>login page</u>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import LoginPage from "@/views/LoginPage";

export default {
    name: "EnterNewPassword",
    data() {
        return {
            passwordField1: '',
            passwordField2: '',
            hover: false,
            notMatching: false,
        };
    },
    methods: {
        submitPassword() {
            if(this.isMatching()){
                this.notMatching = true;
            }else {
              this.notMatching = false;
              axios.post('/api/login/passwordreset', {
                user_id: this.$route.query.id,
                code: this.$route.query.code,
                password: this.passwordField1,
                password_repeat: this.passwordField2,
              })
                  .then(() => {
                    this.$router.push(LoginPage);
                  })
                  .catch((error) => {
                    console.error(error.response.data);
                  });
            }
        },
        goBack() {
            this.$router.push('/login');
        },
        isMatching() {
            return this.passwordField1 !== this.passwordField2;
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
    width: calc(100% - 30px - 30px);
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
    margin: auto;
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