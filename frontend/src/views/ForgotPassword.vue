declare module "particles.vue";
<template>
    <div class="container">
        <div class="header">
            <img src="@/assets/website-logo.png" class="logo-container">
        </div>
        <div class="info">
            Reset Your Password:
        </div>
        <div class="inputBox">
            <div class="color-bar"></div>
            <input v-model="emailField" maxlength="34" spellcheck="false" type="text"
                   placeholder="Email Address">
        </div>
        <div class="details">
            Unfortunately if you are unable to access your email account we will not
            be able to reset your password.
        </div>
        <button class="buttonSmart" type="submit" @click.stop="submitEmail">
            Email Me
        </button>
        <div class="back-button" @click.prevent="goBack()">
            <font-awesome-icon :icon="['fas', 'arrow-left']"/>
            Back to <u>login page</u>
        </div>
    </div>
</template>

<script>
import LoginPage from "@/views/LoginPage";
import EnterNewPassword from "../views/EnterNewPassword";
export default {
    name: "ForgotPassword",
    data() {
        return {
            emailField: '',
            hover: false,
        };
    },
    methods: {
        submitEmail() {
            this.$router.push(EnterNewPassword);
        },
        goBack() {
            this.$router.push(LoginPage);
        }
    }
}
</script>
<style scoped>
.container{
    margin-top: 10vh;
    padding-left: 10vw;
    animation: fade-in-move-down 0.7s;
    overflow: hidden;
}
.logo-container {
    width: 333px;
    padding-top: 6vh;
    height: auto;
    background: None;
    z-index: 3;
}

.header {
    width: auto;
    margin-left: -35px;
    left: calc(50vw - 160px);
    margin-bottom: 10px;
    z-index: 2;
}

.header h1 {
    font-size: 30px;
    text-align: left;
    margin: 10px 10px 0;
    color: white;
}

.info {
    position: relative;
    font-size: 15px;
    margin-left: 20px;
    color: white;
    text-align: left;
    font-weight: 600;
}

.inputBox {
    background: linear-gradient(to right, #272B39, #1E212B) !important;
    position: relative;
    margin: 10px;
    z-index: 2;
    height: 20px;
    width: calc(100% - 60px);
    display: flex;
    flex-direction: column;
    left: 0;
    color: white;
    right: 0;
    padding-top: 30px;
    border-radius: 20px;
    resize: none;
}

.inputBox .color-bar {
    height: 50px;
    width: 20px;
    top: 0;
    left: 0;
    border-radius: 20px 0 0 20px;
    position: absolute;
    background: linear-gradient(to bottom, #1372FA, #0F5BEE);
}

.inputBox input {
    border: none;
    resize: none;
    background: none;
    position: relative;
    top: -15px;
    left: 5%;
    right: 10%;
    color: white;
    height: 30px;
    width: calc(100% - 60px);
    margin: auto auto auto 20px;
    outline: none;
    cursor: pointer;
    font-weight: 600;
    font-size: 17px;
}

.details {
    z-index: 2;
    position: relative;
    font-size: 15px;
    margin-left: 30px;
    color: white;
    font-weight: 600;
    width: calc(100% - 30px - 30px);
    text-align: left;
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
    margin-left: -40px;
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
    margin-left: -50px;
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