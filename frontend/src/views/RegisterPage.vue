<template>
    <div class="container">
        <div class="register-form">
            <div class="header">
                <div class="logo-container"><img src="@/assets/website-logo.svg"></div>
            </div>
            <div class="pass-requirements" v-if="showRequirements">
                <p>Password requirements: </p>
                <ul>
                    <li :class="{'fulfilled': lowercase}">Atleast 1 lower case</li>
                    <li :class="{'fulfilled': uppercase}">Atleast 1 upper case</li>
                    <li :class="{'fulfilled': containsNumber}">A number</li>
                    <li :class="{'fulfilled': noSpaces}">No spaces</li>
                    <li :class="{'fulfilled': nineChars}">At least 9 characters long</li>
                </ul>
            </div>
            <div class="input">
                <div class="color-bar" style="background: #FFED00"></div>
                <input type="text" placeholder="First name" v-model="firstName"/>
            </div>
            <div class="input">
                <div class="color-bar" style="background: #FFED00"></div>
                <input type="text" placeholder="Last name" v-model="lastName"/>
            </div>
            <div class="input">
                <div class="color-bar" style="background: #B437FF"></div>
                <input type="text" placeholder="Username" v-model="username"/>
            </div>
            <div class="input">
                <div class="color-bar" style="background: #FB6D13"></div>
                <input type="email" placeholder="University Email" v-model="email" />
            </div>
            <div class="input">
                <div class="color-bar" style="background: #D223AF"></div>
                <input type="password" placeholder="Password" v-model="password" >
            </div>
            <div class="input">
                <div class="color-bar" style="background: #D223AF"></div>
                <input type="password" placeholder="Confirm password" v-model="passwordConfirmation">
                <p style="color: red; font-size: 12px;">{{errMessage}}</p>
            </div>
            <div class="terms">
                <div><input type="checkbox" v-model="isTermsAgreed"> <span>I agree to all terms</span></div>
                <p style="color: red; font-size: 12px;">{{termErrMessage}}</p>
            </div>
            <div>
                <button class="register-btn" @click="registerUser()">Register</button>
            </div>
            <div class="text">
                <p>Already have an account? <a class="link" @click="navigate('login')">Sign in</a></p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'RegisterPage',
    data() {
        return {
            firstName: '',
            lastName: '',
            username: '',
            password: '',
            passwordConfirmation: '',
            email: '',
            isTermsAgreed: false,

            // Pass requirements
            showRequirements: false,
            lowercase: false,
            uppercase: false,
            nineChars: false,
            noSpaces: true,
            containsNumber: false,

            errMessage: '',
            termErrMessage: '',
        }
    },
    watch: {
        /*
        * Provide an error message to show the user that the password
        * and their password confirmation do not match.
        **/
        password: function() {
            // Check 9 character password
            if(this.password.length >= 9) {
                this.nineChars = true;
            } else {
                this.nineChars = false;
            }
            // Check for white space
            if(/\s/g.test(this.password)) {
                this.noSpaces = false;
            } else {
                this.noSpaces = true;
            }
            if(/[a-z]/.test(this.password)){
                this.lowercase = true;
            } else {
                this.lowercase = false;
            }
            if(/[A-Z]/.test(this.password)) {
                this.uppercase = true;
            } else {
                this.uppercase = false;
            }
            if(/[0-9]/.test(this.password)) {
                this.containsNumber = true;
            } else {
                this.containsNumber = false;
            }
        },
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
            if(this.validateFields() === false) {
                this.errMessage = 'Please fill in missing fields';
                return false;
            }

            if(this.validatePassword() === false) {
                this.showRequirements = true;
                return false;
            }

            if(!this.isTermsAgreed) {
                this.termErrMessage = 'You must agree to the terms to register.';
                return false;
            }

            axios.post('api/users', {
                email: this.email,
                username: this.username, 
                password: this.password, 
                first_name: this.firstName,
                last_name: this.lastName,
                is_teacher: 'false',
                password_repeat: this.passwordConfirmation,
            })
            .then(() => {
                this.errMessage = '';
                this.termErrMessage = '';
                this.$router.push('feed');
            })
            .catch((error) =>{
                console.error(error);
                this.errMessage = error.response.data;
            })
        },
        validatePassword() {
            if(this.password.length >= 9) {
                this.nineChars = true;
            } else {
                this.nineChars = false;
                return false;
            }
            // Check for white space
            if(/\s/g.test(this.password)) {
                this.noSpaces = false;
                return false;
            } else {
                this.noSpaces = true;
            }
            if(/[a-z]/.test(this.password)){
                this.lowercase = true;
            } else {
                this.lowercase = false;
                return false;
            }
            if(/[A-Z]/.test(this.password)) {
                this.uppercase = true;
            } else {
                this.uppercase = false;
                return false;
            }
            if(/[0-9]/.test(this.password)) {
                this.containsNumber = true;
            } else {
                this.containsNumber = false;
                return false;
            }
        },
        validateFields() {
            if
            (
                this.firstName && this.lastName && 
                this.password && this.passwordConfirmation &&
                this.email
            ) {
                return true;
            }
            return false;
        },
    }
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
}

.input input {
    width: 96%;
    height:46px;
    margin-left: 8px;
    margin-bottom: 15px;
    border-radius: 8px;
    border: none;
    outline: none;
    color: white;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%);
    padding-left: 15px;
}

input::placeholder {
    font-weight: 500;
    color: white;
}

.input p {
    margin-bottom: 3px;
}

.text {
    text-align: left;
    color: white;
    font-weight: 500;
}

.terms {
    display: flex;
    flex-direction: column;
    margin: 10px 0px 10px 0px;
    text-align: left;
    color: white;
    font-weight: 500;
}


.register-btn {
    background: linear-gradient(270deg, rgba(101,255,167,1) 10%, rgba(52,235,233,1) 100%);
    width: 80px;
    height: 40px;
    border-radius: 25px;
    border: 1px solid black;
    outline: none;
    cursor: pointer;
    font-weight: 600;
}

.color-bar {
    height: 48px;
    width: 15px;
    border-radius: 10px 0px 0 10px;
    position: absolute;
}

.link {
    cursor: pointer;
    text-decoration: underline;
}
.error {
    color: red;
}

.pass-requirements ul {
    text-align: left;
    color: red;
}

.fulfilled ul {
    color: green;
}


</style>