<template>
  <div>
    <p id="title">
      <font-awesome-icon :icon="['fas', 'arrow-left']"/>
      {{ this.title }}
    </p>
    <br>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Post",
  data() {
    return {
      id: this.$route.params.id,
      title: this.getTitle(this.id),
    }
  },
  methods: {
    getData(id) {
      let bigUrl = 'api/communities/' + id + '/posts'; //+ '?page=' + pageNum;
      axios.get(bigUrl)
          .then((response) => {
            return response;
          })
          .catch((error) => {
            console.error(error);
            return null;
          })
    },
    getTitle(id) {
      try {
        let dataValues = this.getData(id);
        console.log(dataValues);
        return dataValues.data.data[0].title;
      } catch (error) {
        return "Goat";
      }
    }
  }
}
</script>

<style scoped>

#title {
  text-align: left;
  margin-left: 2vh;
  padding-top: 2vh;
  color: #777779;
}

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

.input {
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
  height: 25px;
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

.error-message {
  color: red;
  font-size: 14px;
}
</style>