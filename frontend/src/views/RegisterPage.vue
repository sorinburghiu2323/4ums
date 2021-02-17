<template>
    <div class="container">
        <form class="register-form">
            <div class="header">
                <p>Register</p>
                <div class="logo-container"><img src="@/assets/logo.png"></div>
            </div>
            <div class="input">
                <input type="text" placeholder="Username" v-model="username"/>
            </div>
            <div class="input">
                <input type="email" placeholder="Email" v-model="email" />
            </div>
            <div class="input">
                <input type="password" placeholder="Password" v-model="password" >
            </div>
            <div class="input">
                <input type="password" placeholder="Confirm password" v-model="passwordConfirmation">
                <p style="color: red; font-size: 12px;">{{errMessage}}</p>
            </div>
            <div class="terms">
                <div><input type="checkbox" v-model="isTermsAgreed"> <span>I aggree to all terms</span></div>
                <p style="color: red; font-size: 12px;">{{termErrMessage}}</p>
            </div>
            <div>
                <button class="register-btn" @click="registerUser()">Register</button>
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
    data() {
        return {
            username: '',
            password: '',
            passwordConfirmation: '',
            email: '',
            isTermsAgreed: false,

            errMessage: '',
            termErrMessage: '',
        }
    },
    watch: {
        /*
        * Provide an error message to show the user that the password
        * and their password confirmation do not match.
        **/
        passwordConfirmation: function() {
            if(this.passwordConfirmation != '' 
            && this.passwordConfirmation !== this.password) {
                this.errMessage = 'Passwords do not match';
            } else {
                this.errMessage = '';
            }
            
        },
        /**
         * Clear any error messages related to the agreed terms checkbox
         * if the user agrees with the terms
         */
        isTermsAgreed: function() {
            if(this.termErrMessage != '' && this.isTermsAgreed) {
                this.termErrMessage = '';
            }
        }
    },
    methods: {
        navigate(path) {
            this.$router.push(path);
        },
        registerUser() {
            alert('Registration functionality not yet implemented');
            if(!this.isTermsAgreed) {
                this.termErrMessage = 'You must agree to the terms to register.';
            }
        }
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
    flex-direction: column;
    margin: 10px 0px 10px 0px;
    text-align: left;
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