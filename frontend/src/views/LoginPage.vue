<template>
    <div class="container">
        <form class="login-form">
            <div class="header">
            <p>Login</p>
            <div class="logo-container"><img src="@/assets/logo.png"></div>
            </div>
            <div class="input">
            <p>Email address</p>
            <input type="text"/>
            </div>
            <div class="input">
                <p>Password</p>
                <input type="text">
            </div>
            <div class="text">
                <p>Forgot your password?</p>
            </div>
            <div>
                <button class="login-btn">Login</button>
            </div>
            <div class="text">
                <p>Don't have an account? <a class="link" @click="navigate('register')">Sign up</a></p>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'LoginPage',
    methods: {
        navigate(path) {
            this.$router.push(path);
        }
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

.input{
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
    height:25px;
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
</style>