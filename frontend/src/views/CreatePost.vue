<template>
  <div id="form">
    <div id="communityBox" v-if="communities">
      <font-awesome-icon :icon="['fas', 'users']" style="color: #5ff9ab" />
      Select a Community
      <select v-model="community">
        <option
          v-for="(comm, index) in this.communities"
          :key="index"
          :value="comm"
        >
          {{ comm.name }}
        </option>
      </select>
    </div>

    <p id="success"></p>

    <input
      id="title"
      v-model="title"
      placeholder="Add an interesting title..."
    />
    <br />
    <textarea
      v-model="description"
      class="inputBox"
      placeholder="Post text (optional)..."
    ></textarea>
    <br />
    <p id="success" style="color: green;"></p>
    <button id="submit" v-on:click="createPost()">Submit Post</button>
  </div>
</template>

<script>
import axios from "axios";
//import params from "./params.json";

export default {
  name: "CreatePost",
  created() {
    this.type = this.$route.params.type;
  },
  methods: {
    createPost: function() {
      // Get the inputs from the form and send it to backend

      if (this.title === "") {
        document.getElementById("success").innerHTML = "Title is required";
        document.getElementById("success").style = "color: red";
        return;
      } else if (this.community.name === "") {
        document.getElementById("success").innerHTML = "TCommunity is required";
        document.getElementById("success").style = "color: red";
        return;
      }
      var post_url =
        "/api/communities/" + this.community.id.toString() + "/posts";
      axios
        .post(post_url, {
          title: this.title,
          description: this.description,
          post_type: this.type,
        })
        .then(() => {
          document.getElementById("success").innerHTML = "Posted!";
          this.$router.push({
            name: "Community",
            params: {
              id: this.community.id,
            },
          });
        })
        .catch((error) => {
          document.getElementById("success").innerHTML = error.response.data;
          document.getElementById("success").style = "color: red;";
        });
    },
  },
  data() {
    return {
      title: "",
      description: "",
      type: "",
      communities: [],
      showCommunitiesFlag: false,
      community: { name: "" },
    };
  },
  mounted() {
    axios
      .get("/api/communities?type=memberof", {
        type: "memberof",
      })
      .then((response) => {
        this.communities = response.data.data;
      });
  },
};
</script>

<style scoped>
#communityBox {
  width: 99%;
  background-color: #222531;
  padding: 1vh;
  color: white;
  font-family: "Trebuchet MS";
}

.inputBox {
  font-family: "Trebuchet MS";
  background-color: #222531;
  width: 100%;
  border: 0;
  color: white;
  margin-top: 1vh;
  height: 75vh;
}

#title {
  font-family: "Trebuchet MS";
  height: 5vh;
  color: white;
  font-family: "Trebuchet MS";
  background-color: #222531;
  width: 100%;
  border: 0;
  color: white;
  margin-top: 1vh;
  font-size: 3vh;
}

#submit {
  border-radius: 50%;
  background-image: linear-gradient(to bottom right, #7632be, #7632be);
  height: 11vh;
  width: 11vh;
  position: fixed;
  bottom: 10vh;
  right: 2vh;
  font-size: 2.5vh;
  border-width: 0;
  outline: none;
  cursor: pointer;
  z-index: 1;
}
</style>
