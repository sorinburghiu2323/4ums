<template>
  <div class="container">
    <div class="header">
      <h1>
        You are dumb cause u forgot ur password
      </h1>
    </div>
    <div class="inputBox">
      <label style="color:#7e7e7e; font-size:25px;">Please enter your email below</label>
      <br>
      <input v-model="emailField" maxlength="34" spellcheck="false" type="text">
      <button class="buttonSmart" type="submit" @click.stop="submitEmail">
        Submit
      </button>
    </div>
  </div>
</template>

<script>
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
      console.log("hi");
    }
  }
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 30px;
}

.header h1 {
  font-size: 30px;
  text-align: left;
  margin: 10px 10px 0;
  color: white;
}

.inputBox {
  background: linear-gradient(to right, #272B39, #1E212B) !important;
  position: absolute;
  margin: 10px;
  z-index: 2;
  height: 150px;
  width: inherit;
  display: flex;
  flex-direction: column;
  left: 0;
  right: 0;
  padding-top: 30px;
  border-radius: 20px;
  resize: none;
}

.inputBox input {
  border: none;
  resize: none;
  background: linear-gradient(to right, #272B39, #1E212B);
  height: 30px;
  color: white;
  width: 90%;
  margin: 5px auto auto;
  outline: none;
  font-size: 17px;
}

.inputBox .buttonSmart {
  z-index: 2;
  border: none;
  background: none;
  height: 110px;
  color: white;
  width: 180px;
  border-radius: 20px;
  margin: 5px auto auto;
  outline: none;
  font-size: 20px;
}

.buttonSmart:hover {
  background: #7e7e7e;
}


</style>