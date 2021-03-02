<template>
    <div class="container">
        <div class="login-form">
            <div class="header">
                <div class="logo-container"><img src="@/assets/website-logo.svg"></div>
            </div>
            <div>
                <p v-if="failedLogin" class="error-message">Incorrect password or email</p>
            </div>

            <div class="input">
                <div class="color-bar" style="background: #FB6D13"></div>
                <input v-model="email" placeholder="Email address" type="text"/>
            </div>
            <div class="input">
                <div class="color-bar" style="background: #8A3BFE"></div>
                <input v-model="password" placeholder="Password" type="password"
                @keyup.enter="loginUser()">
            </div>
            <div>
                <button class="login-btn" @click="loginUser()">Sign in</button>
            </div>
            <div class="text">
                <p class="link">Forgot your password?</p>
            </div>
            <div class="text" style="margin-top: 40px;">
                <p>Don't have an account? <a class="link" @click="navigate('register')">Sign up</a></p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Feed from "@/views/Feed.vue";

export default {
  name: 'LoginPage',
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
            
            axios.post('/api/login', {email: this.email, password: this.password})
            .then(() => {
              this.failedLogin = false;
              this.$router.push(Feed);
            })
            .catch((error) =>{
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
    height: 100vh;
}
.login-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: auto;
    margin-top: 10vh;
}

.input{
    text-align: left;
}

.text {
    text-align: center;
    color: white;
    font-weight: 500;
}
input {
    width: 96%;
    height:46px;
    margin-left: 8px;
    margin-bottom: 15px;
    border-radius: 8px;
    border: none;
    outline: none;
    color: white;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%) !important;
    padding-left: 15px;
}

.input input {
    padding-left: 15px;
}

.color-bar {
    height: 48px;
    width: 15px;
    border-radius: 10px 0px 0 10px;
    position: absolute;
}

.login-btn {
    background: linear-gradient(270deg, rgba(101,255,167,1) 10%, rgba(52,235,233,1) 100%);
    width: 80px;
    height: 40px;
    border-radius: 25px;
    border: 1px solid black;
    outline: none;
    cursor: pointer;
    font-weight: 600;
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