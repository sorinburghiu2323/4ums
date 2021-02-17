<template>
    <div class="container">
        <form class="register-form">
            <div class="header">
                <p>Register</p>
                <div class="logo-container"><img src="@/assets/logo.png"></div>
            </div>
            <div class="input">
                <input type="text" placeholder="Username"/>
            </div>
            <div class="input">
                <input type="email" placeholder="Email">
            </div>
            <div class="input">
                <input type="text" placeholder="Password" >
            </div>
            <div class="input">
                <input type="text" placeholder="Confirm password" >
            </div>
            <div class="terms">
                <input type="checkbox"> <span>I aggree to all terms</span>
            </div>
            <div>
                <button class="register-btn">register</button>
            </div>
            <div class="text">
                <p>Already have an account? <a class="link" @click="navigate('login')">Sign in</a></p>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: 'RegisterPage',
    methods: {
        navigate(path) {
            this.$router.push(path);
        },
    },

}
</script>

<style scoped>
.container {
    display: flex;
    width: 100%;
}
.register-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin: auto;
}

.input{
    text-align: left;
    margin: 10px 0px 10px 0px;
}

.input p {
    margin-bottom: 3px;
}

.text {
    text-align: left;
}

.terms {
    display: flex;
    flex-direction: row;
    margin: 10px 0px 10px 0px;
}
.input input {
    width: 100%;
    height:25px;
    border-radius: 8px;
    border: 1px solid black;
    outline: none;
}

.register-btn {
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