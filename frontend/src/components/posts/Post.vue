<template>
  <div class="containers" @click="navigateToPost">
    <div class="details">
      <div class="title">
        <p>{{ post.title }}</p>
      </div>
      <div class="description">
        <p>{{ post.description }}</p>
      </div>
      <div v-if="post_type === 'question' && !this.approvedAnswer">
        <div class="open">
          <div class="oval"></div>
          <font-awesome-icon
            :icon="['fa', 'question-circle']"
          ></font-awesome-icon>
          <p>Open</p>
        </div>
      </div>
      <div v-else-if="post_type === 'discussion'">
        <div class="discussion">
          <div class="oval"></div>
          <font-awesome-icon :icon="['fa', 'comment-dots']"></font-awesome-icon>
          <p>Discussion</p>
        </div>
      </div>
      <div v-else>
        <div class="answer">
          <div class="oval"></div>
          <font-awesome-icon :icon="['fa', 'check-circle']"></font-awesome-icon>
          <p>Answered</p>
        </div>
      </div>
    </div>
    <div style="display: flex;">
      <div class="likes" @click.stop="likePost">
        <div v-if="this.userLiked" style="color:white">
          <div class="like-icon">
            <font-awesome-icon :icon="['fa', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ post["likes_num"] }}</div>
        </div>
        <div v-else style="color:grey">
          <div class="like-icon">
            <font-awesome-icon :icon="['far', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ post["likes_num"] }}</div>
        </div>
      </div>
      <div class="date">
        <p>Posted {{ date_time }}</p>
      </div>
      <div class="comment-count" v-if="post.comments_num > 0">
        <p>{{post.comments_num}} Comments</p>
      </div>
      <div class="author" @click.stop="navigateToUser">
        <p>
          By <span class="author-name">{{ post["user"]["username"] }}</span>
        </p>
      </div>
    </div>
  </div>
</template>
<script>
import moment from "moment";
import axios from "axios";

export default {
  name: "Post",
  props: {
    post: Object,
  },
  data() {
    return {
      info: 3,
      post_type: this.post.post_type,
      userLiked: this.post["is_liked"],
      approvedAnswer: this.post["has_approved"],
      date_time: moment(this.post["create_at"]).format("DD/MM/YY"),
    };
  },
  methods: {
    navigateToPost() {
      this.$router.push({
        name: "PostPage",
        params: {
          id: this.post.community.id,
          postId: this.post.id,
        },
      });
    },
    navigateToUser() {
      this.$router.push({
        name: "User",
        params: {
          id: this.post.user.id,
        },
      });
    },
    likePost() {
      if (!this.userLiked) {
        axios
          .post(
            "/api/communities/" +
              this.post.community.id +
              "/posts/" +
              this.post.id +
              "/likes"
          )
          .then(() => {
            this.post["likes_num"]++;
            this.userLiked = true;
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        axios
          .delete(
            "/api/communities/" +
              this.post.community.id +
              "/posts/" +
              this.post.id +
              "/likes"
          )
          .then(() => {
            this.post["likes_num"]--;
            this.userLiked = false;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};
</script>

<style scoped>
.containers {
  z-index: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin-top: 10px;
  margin-bottom: 10px;
  height: auto;
  padding: 0 3px 10px 0;
  border: none;
  border-radius: 25px;
  background: linear-gradient(to right, #272b39, #1d2029);
  position: relative;
}

.details {
  margin: 20px auto 20px 25px;
}

.details p {
  margin: 0;
}

.details .title {
  margin-top: 2vh;
  margin-bottom: 4px;
  font-size: 18px;
}

.title p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* number of lines to show */
  -webkit-box-orient: vertical;
  text-align: left;
}

.details .description {
  height: 70%;
  font-size: 15px;
  color: white;
}

.description p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* number of lines to show */
  -webkit-box-orient: vertical;
  text-align: left;
}

.date {
  color: #7e7e7e;
  font-size: 15px;
}
.comment-count {
  position: absolute;
  top: 0px;
  font-weight: 600;
  right: 15px;
  font-size: 13px;
  color: #9C39FF;
}

.open .oval {
  display: -webkit-box;
  position: absolute;
  z-index: -1;
  top: -3px;
  left: 0;
  width: 90px;
  height: 20px;
  margin-top: 1px;
  margin-left: -10px;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #fe6811, #fe982d);
}

.discussion .oval {
  display: -webkit-box;
  position: absolute;
  z-index: -1;
  top: -3px;
  left: 0;
  width: 120px;
  height: 20px;
  margin-top: 1px;
  margin-left: -10px;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #e276f4, #d225b1);
}

.answer .oval {
  display: -webkit-box;
  position: absolute;
  z-index: -1;
  top: -3px;
  left: 0;
  width: 120px;
  height: 20px;
  margin-top: 1px;
  margin-left: -10px;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #34e7e4, #63fba4);
  box-shadow: 0 0 30px #4cf1c4;
}

.open {
  display: flex;
  position: absolute;
  top: 4px;
  left: 0;
  color: black;
  margin-left: 30px;
  margin-top: 1.2vh;
}

.open p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 20px;
}

.discussion {
  display: flex;
  position: absolute;
  top: 4px;
  left: 0;
  color: black;
  margin-left: 30px;
  margin-top: 1.2vh;
}

.discussion p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 20px;
}

.answer {
  display: flex;
  position: absolute;
  top: 4px;
  left: 0;
  color: black;
  margin-left: 30px;
  margin-top: 1.2vh;
}

.answer p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 20px;
}

.likes {
  position: relative;
  width: 60px;
  z-index: 1;
  display: flex;
  margin-left: 8px;
  margin-right: 10px;
}

.likes > div {
  display: flex;
  width: 100%;
}

.like-icon {
  font-size: 20px;
  background: white;
  color: black;
  padding: 3px 7px 3px 7px;
  border-radius: 12px;
  margin: auto;
  margin-left: 0;
  margin-right: 0;
}

.like-count {
  font-size: 18px;
  margin: auto;
  margin-left: 10px;
}

.author {
  position: absolute;
  bottom: 26px;
  right: 0;
  color: #7e7e7e;
  margin-right: 10px;
}

.author p {
  margin: 0;
  font-size: 15px;
  max-width: 120px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.author-name {
  text-decoration: underline;
}
</style>
