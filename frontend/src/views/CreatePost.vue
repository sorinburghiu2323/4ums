<template>
  <div id="form">
    <router-link class="nav-link" :to="'/communities/' + community.id">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']"/>
        Back to threads
      </p>
    </router-link>
    <div id="communityBox" v-if="community">
      <div class="community-name">
        <p>{{community.name}}</p>
        <p style="font-size: 23px;">new Thread</p>
      </div>

    </div>

    <p id="errorMessage" v-if="message !== ''">{{message}}</p>

    <div class="title-input-container">
      <input
      id="title-input"
      v-model="title"
      placeholder="Add an interesting title..."
      />
    </div>
  
    <div class="post-content-container">
        <textarea
        v-model="description"
        class="inputBox"
        placeholder="Post text (optional)..."
        ></textarea>
    </div>

    <button id="submit" v-on:click="createPost()">
      <div class="curved-text"><img src="@/assets/post.svg"></div>
      <font-awesome-icon :icon="['fa', 'comment-dots']"/>
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreatePost",
  created() {
    this.type = this.$route.params.type;
    this.communityId = this.$route.params.id;
    // Fetch and set the data of the community which the post is being created for
    const url = "/api/communities/" + this.communityId.toString();
    axios.get(url)
    .then(response => {
      this.community = response.data;
    });
  },
  methods: {
    createPost: function() {
      // Get the inputs from the form and send it to backend
      if (this.title === "") {
        this.message = "Title is required";
        return
      } else {
        this.message = "";
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
          this.$router.push({
            name: "Community",
            params: {
              id: this.community.id,
            },
          });
        })
        .catch((error) => {
          this.message = error.response.data;
        });
    },
  },
  data() {
    return {
      title: "",
      description: "",
      type: "",
      communityId: null,
      showCommunitiesFlag: false,
      community: null,
      message: "",
    };
  },
};
</script>

<style scoped>
.curved-text {
    position: absolute;
    top: -10px;
    left: 0px;
}

.curved-text img {
    height: 120px;
    transform: rotate(-5deg);
}

#communityBox {
  padding: 5px;
  color: white;
  font-family: "Trebuchet MS";
  border-radius: 0px;
  font-size: 27px;
  text-align: left;
  width: inherit;
  display: flex;
}

.community-name {
  width: 80%;
}
.community-name p {
    white-space: nowrap;
    overflow: hidden;
    display: block;
    text-overflow: ellipsis;
    margin: 10px;
}


.inputBox {
  font-family: "Trebuchet MS";
  font-size: 15px;
  padding-left: 10px;
  padding-top: 10px;
  color: white;
  outline: none;
  background-color: #222531;
  width: 100%;
  border: 0;
  color: white;
  margin-top: 1vh;
  height: 75vh;
  resize: none;
}

.inputBox::placeholder {
  color: white;
}

.title-input-container, .post-content-container {
  display: flex;
  width: 100%;
}

#title-input {
  font-family: "Trebuchet MS";
  height: 5vh;
  color: white;
  font-family: "Trebuchet MS";
  background-color: #222531;
  width: 100%;
  border: 0;
  color: white;
  margin-top: 1vh;
  font-size: 15px;
  padding: 10px;
}

#title-input::placeholder {
  color: white;
}

#submit {
  border-radius: 50%;
  background: linear-gradient(to bottom right, #B437FF, #9C39FF);
  height: 14vh;
  width: 14vh;
  position: fixed;
  bottom: 12vh;
  right: 0;
  font-size: 40px;
  font-weight: 600;
  border-width: 0;
  z-index: 1;
  box-shadow: 0px 3px 20px #9C39FF;
}
#submit p {
  font-size: 16px;
  margin: 0;
}

#errorMessage {
  color: red;
  text-align: left;
  margin: 10px 10px 0 0;
}

#back {
  text-align: left;
  color: #777779;
}
</style>
