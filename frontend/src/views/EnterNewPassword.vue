declare module "particles.vue";
<template>
    <div class="container">
        <div class="header">
            <img class="logo-container" src="@/assets/website-logo.png">
        </div>
        <div class="info">
            Reset Your Password:
        </div>
        <div class="inputBox">
            <div class="color-bar1"></div>
            <input v-model="passwordField1" maxlength="34" placeholder="Enter your new password" spellcheck="false"
                   type="password">
        </div>
        <label v-if="notMatching" style="color:red;display:flex; position:relative; margin-left:37px;"> Passwords don't match</label>
        <div class="inputBox" style = "margin-top: 20px;">
            <div class="color-bar2"></div>
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
</template>

<script>
import axios from "axios";

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
                    body : {
                      user_id: this.$route.query.id,
                      code: this.$route.query.code,
                      password: this.passwordField1,
                      password_repeated: this.passwordField2,
                    }})
                .then((response) =>{
                    console.log(response);
                })
                .catch((error) =>{
                    console.error(error);
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
    padding-top: 10vh;
    padding-left: 10vw;
    animation: fade-in-move-down 0.7s;
    overflow: hidden;
}
.logo-container {
    width: 333px;
    padding-top: 6vh;
    height: auto;
    background: None;
}

.header {
    z-index: 1;
    width: auto;
    margin-left: -40px;
    left: calc(50vw - 160px);
    margin-bottom: 10px;
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
    cursor: pointer;
    font-weight: 600;
}

.inputBox {
    background: linear-gradient(to right, #272B39, #1E212B) !important;
    position: relative;
    margin: 10px;
    z-index: 2;
    height: 20px;
    width: calc(100% - 55px);
    display: flex;
    flex-direction: column;
    left: 0;
    color: white;
    right: 0;
    padding-top: 30px;
    border-radius: 20px;
    resize: none;
    cursor: pointer;
    font-weight: 600;
}

.inputBox .color-bar1 {
    height: 50px;
    width: 20px;
    top: 0;
    left: 0;
    border-radius: 20px 0 0 20px;
    position: absolute;
    background: linear-gradient(45deg, #F78826, #F4781E);
}
.inputBox .color-bar2 {
    height: 50px;
    width: 20px;
    top: 0;
    left: 0;
    border-radius: 20px 0 0 20px;
    position: absolute;
    background: linear-gradient(125deg, #D64DCF, #D465DE);
}

.inputBox input {
    border: none;
    resize: none;
    background: none;
    position: relative;
    cursor: pointer;
    font-weight: 600;
    top: -15px;
    left: 5%;
    right: 10%;
    color: white;
    height: 30px;
    width: calc(100% - 55px);
    margin: auto auto auto 20px;
    outline: none;
    font-size: 15px;
}

.buttonSmart {
    z-index: 2;
    border: none;
    background: linear-gradient(270deg, rgba(101,255,167,1) 10%, rgba(52,235,233,1) 100%);
    box-shadow: 0 0 10px #34E7E4;
    height: 40px;
    color: black;
    width: 100px;
    border-radius: 20px;
    margin-top: 25px;
    margin-left: -40px;
    outline: none;
    font-size: 15px;
    cursor: pointer;
    font-weight: 600;
}

.buttonSmart:hover {
    background: #55F4B6;
    box-shadow: 0 0 30px #55F4B6;
}

.back-button {
    position: relative;
    margin-top: 20px;
    margin-left: -50px;
    cursor: pointer;
    font-weight: 600;
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