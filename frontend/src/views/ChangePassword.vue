<template>
  <div class="container">
    <div>
      <h1 style="text-align: left; display: block;">Update your password</h1>
    </div>
    <div style="display: block" class="register-form">
      <div v-if="showRequirements" class="pass-requirements">
        <p>Password requirements:</p>
        <ul>
          <li :class="{ fulfilled: lowercase }">Atleast 1 lower case</li>
          <li :class="{ fulfilled: uppercase }">Atleast 1 upper case</li>
          <li :class="{ fulfilled: containsNumber }">A number</li>
          <li :class="{ fulfilled: noSpaces }">No spaces</li>
          <li :class="{ fulfilled: nineChars }">At least 9 characters long</li>
        </ul>
      </div>
      <div class="input">
        <div class="color-bar" style="background: #D223AF"></div>
        <input v-model="password" placeholder="Password" type="password" />
      </div>
      <div class="input">
        <div class="color-bar" style="background: #D223AF"></div>
        <input
          v-model="passwordConfirmation"
          placeholder="Confirm password"
          type="password"
        />
        <p style="color: red; font-size: 12px;">{{ errMessage }}</p>
      </div>

      <div>
        <p style="color: red; font-size: 12px;">{{ termErrMessage }}</p>
      </div>
      <div>
        <button class="register-btn" @click="registerUser()">
          Update
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterPage",
  data() {
    return {
      password: "",
      passwordConfirmation: "",

      // Pass requirements
      showRequirements: false,
      lowercase: false,
      uppercase: false,
      nineChars: false,
      noSpaces: true,
      containsNumber: false,

      errMessage: "",
      termErrMessage: "",
    };
  },
  watch: {
    /*
     * Provide an error message to show the user that the password
     * and their password confirmation do not match.
     **/
    password: function() {
      // Check 9 character password
      this.nineChars = this.password.length >= 9;
      // Check for white space
      this.noSpaces = !/\s/g.test(this.password) ? true : false;
      this.lowercase = /[a-z]/.test(this.password) ? true : false;
      this.uppercase = /[A-Z]/.test(this.password) ? true : false;
      this.containsNumber = /[0-9]/.test(this.password) ? true : false;
    },
    passwordConfirmation: function() {
      if (
        this.passwordConfirmation !== "" &&
        this.passwordConfirmation !== this.password
      ) {
        this.errMessage = "Passwords do not match";
      } else {
        this.errMessage = "";
      }
    },
    /**
     * Clear any error messages related to the agreed terms checkbox
     * if the user agrees with the terms
     */
    isTermsAgreed: function() {
      if (this.termErrMessage !== "" && this.isTermsAgreed) {
        this.termErrMessage = "";
      }
    },
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    },
    registerUser() {
      if (this.validatePassword() === false) {
        this.showRequirements = true;
        return false;
      }

      axios
        .get("/api/users/me")
        .then((response) => {
          axios
            .put("/api/users/me", {
              email: response.data.email,
              username: response.data.username,
              password: this.password,
              first_name: response.data.firstName,
              last_name: response.data.lastName,
              is_teacher: response.data.isTeacher,
              password_repeat: this.passwordConfirmation,
            })
            .then(() => {
              this.errMessage = "";
              this.termErrMessage = "";
              this.$router.push({ name: "LoginPage" });
            })
            .catch((error) => {
              this.errMessage = error.response.data;
              console.log(error);
            });
        })
        .catch((error) => {
          this.errMessage = error.response.data;
        });
    },

    validatePassword() {
      if (this.password.length >= 9) {
        this.nineChars = true;
      } else {
        this.nineChars = false;
        return false;
      }
      // Check for white space
      if (/\s/g.test(this.password)) {
        this.noSpaces = false;
        return false;
      } else {
        this.noSpaces = true;
      }
      if (/[a-z]/.test(this.password)) {
        this.lowercase = true;
      } else {
        this.lowercase = false;
        return false;
      }
      if (/[A-Z]/.test(this.password)) {
        this.uppercase = true;
      } else {
        this.uppercase = false;
        return false;
      }
      if (/[0-9]/.test(this.password)) {
        this.containsNumber = true;
      } else {
        this.containsNumber = false;
        return false;
      }
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  position: relative;
}
.register-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
  width: 100%;
}

.input {
  text-align: left;
}

.input input {
  width: 94%;
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
  background: linear-gradient(
    270deg,
    rgba(101, 255, 167, 1) 10%,
    rgba(52, 235, 233, 1) 100%
  );
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

.fulfilled {
  color: green;
}
</style>
