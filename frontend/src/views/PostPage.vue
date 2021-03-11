<template>
  <div v-if="loadedPost" class="container">
    <div class="nav-link" @click.prevent.stop="goBack()">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']"/>
        {{ post.community.name }}
      </p>
    </div>
    <div class="header">
      <div
          class="settings-icon"
          @click="
          $router.push({
            name: 'Settings',
          })
        "
      >
        <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
      </div>
    </div>
    <div class="badges">
      <div v-if="post_type === 'question' && !this.isAnswered">
        <div class="open">
          <div class="oval">
            <font-awesome-icon
                :icon="['fa', 'question-circle']"
            ></font-awesome-icon>
            <p>Open</p>
          </div>
        </div>
      </div>
      <div v-else-if="post_type === 'discussion'">
        <div class="discussion">
          <div class="oval">
            <font-awesome-icon
              :icon="['fa', 'comment-dots']"
            ></font-awesome-icon>
            <p>Discussion</p>
          </div>
        </div>
      </div>
      <div v-else>
        <div class="answer">
          <div class="oval">
            <font-awesome-icon
              :icon="['fa', 'check-circle']"
            ></font-awesome-icon>
            <p>Answered</p>
          </div>
        </div>
      </div>
      <div>
        <div class="lecturer">
          <div class="oval">
            <font-awesome-icon :icon="['fa', 'chalkboard-teacher']" />
            <p>Lecturer</p>
          </div>
        </div>
      </div>
      <div v-if="isByCommunityOwner">
        <div class="community-owner">
          <div class="oval">
            <font-awesome-icon :icon="['fa', 'chalkboard-teacher']" />
            <p>Community Owner</p>
          </div>
        </div>
      </div>
    </div>
    <div class="containers">
      <div class="details">
        <div class="title">
          <p>{{ post.title }}</p>
        </div>
        <div v-if="post.comments_num > 0" style="text-align: left; margin-bottom: 10px; font-size: 14px;">
          {{post.comments_num}} Comments
        </div>
        <div class="post-content">
          <div class="description">
            <p>{{ post.description }}</p>
          </div>
          <div style="display: flex;">
            <div class="likes" @click.stop="likePost">
              <div v-if="this.userLiked" style="color:white">
                <div class="like-icon">
                  <font-awesome-icon
                    :icon="['fa', 'thumbs-up']"
                  ></font-awesome-icon>
                </div>
                <div class="like-count">{{ post["likes_num"] }}</div>
              </div>
              <div v-else>
                <div class="like-icon">
                  <font-awesome-icon
                    :icon="['far', 'thumbs-up']"
                  ></font-awesome-icon>
                </div>
                <div class="like-count">{{ post["likes_num"] }}</div>
              </div>
            </div>
            <div class="date">
              <p>Posted {{ date_time }}</p>
            </div>
          </div>

          <div class="author" @click.stop="navigateToUser">
            <p>
              By
              <span class="author-name">{{ post.user.username }}</span>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="!showInput" class="comment-btn" @click.stop="showCommentInput">
      <div class="comment-icon">
        <font-awesome-icon :icon="['fas', 'comment-dots']"></font-awesome-icon>
      </div>
      <p>Add a comment...</p>
    </div>
    <div v-if="showInput" class="comment-input">
      <div class="close-comment">
        <font-awesome-icon
            :icon="['fa', 'times']"
            @click="
            showInput = false;
            addComment = '';
          "
        />
      </div>
      <label style="color:white">Add a comment...</label>
      <textarea v-model="addComment"></textarea>
      <div class="send-icon" @click.stop="sendComment">
        <font-awesome-icon :icon="['fas', 'paper-plane']"></font-awesome-icon>
      </div>
    </div>
    <div v-if="loadedPost && community" class="comments-list">
      <Comment
        v-for="(comment, index) in allComments"
        :key="index"
        :comment="comment"
        :displayApprove="isUserOwner"
        :hasBeenApproved="isAnswered"
        :isByCommunityOwner="community.creator.id === comment.user.id"
        :isByPostOwner="post.user.id === comment.user.id"
        :isQuestion="post_type === 'question'"
        v-on:update-post="updatePost"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Comment from "@/components/posts/Comment";
import moment from "moment";
import LoginPage from "@/views/LoginPage";

export default {
  name: "PostPage",
  components: {
    Comment,
  },
  watch: {
    showPost() {
      this.currentPage = 1;
      this.allComments = [];
      this.loadedPost = false;
      this.getPost();
    },
  },
  data() {
    return {
      id: this.$route.params.id,
      community: null,
      postId: this.$route.params.postId,
      loadedPost: false,
      currentPage: 1,
      bottomOfPageReached: false,
      errorLoadingPosts: false,
      loadMore: false,
      scrolledToBottom: false,
      allComments: [],
      post: Object,
      post_type: "discussion",
      date_time: "10/20/30",
      isAnswered: true,
      userLiked: false,
      addComment: null,
      showInput: false,
      isUserOwner: false,
    };
  },
  mounted() {
    this.getPost();
    this.getCommunity();
    this.scroll();
  },
  computed: {
    isByCommunityOwner() {
      if (this.community === null || this.post === null) {
        return false;
      }
      return this.community.creator.id === this.post.user.id;
    },
  },
  methods: {
    updatePost() {
      this.currentPage = 1;
      this.allComments = [];
      this.isAnswered = !this.isAnswered;
      this.getPost();
    },
    goBack() {
      this.$router.go(-1);
    },
    getCommunity() {
      axios
        .get("/api/communities/" + this.id)
        .then((response) => {
          this.community = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    sendComment() {
      axios
        .post(
          "/api/communities/" + this.id + "/posts/" + this.postId + "/comments",
          { comment: this.addComment }
        )
        .then(() => {
          this.showInput = false;
          this.allComments = [];
          this.getPost();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    showCommentInput() {
      this.addComment = null;
      this.showInput = !this.showInput;
    },
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          Math.max(
            window.pageYOffset,
            document.documentElement.scrollTop,
            document.body.scrollTop
          ) + window.innerHeight;
        if (bottomOfWindow >= document.documentElement.offsetHeight - 200) {
          if (this.loadMore) {
            this.loadMoreComments();
            this.loadMore = false;
          }
        }
      };
    },
    async getPost() {
      await axios
        .get("/api/communities/" + this.id + "/posts/" + this.postId, {
          params: { page: this.currentPage },
        })
        .then((response) => {
          this.loadedPost = false;
          this.post = response.data.post;
          for (let i = 0; i < response.data.comments.data.length; i++) {
            this.allComments.push(response.data.comments.data[i]);
          }
          this.date_time = moment(this.post["created_at"]).format("DD/MM/YY");
          this.post_type = this.post["post_type"];
          this.loadMore = response.data.comments["next_page"] !== null;
          this.isAnswered = this.post["has_approved"];
          this.loadedPost = true;
          this.userLiked = this.post["is_liked"];
          this.isUserOwner = this.post["is_user_owner"];
        })
        .catch((error) => {
          console.error(error);
          if (error.response.status === 401) {
            this.$router.push(LoginPage);
          }
          this.loadedPosts = false;
        });
    },
    loadMoreComments() {
      this.currentPage++;
      this.getPost();
    },
    navigateToUser() {
      this.$router.push({
        name: "User",
        params: {
          id: this.post["user"]["id"],
        },
      });
    },
    likePost() {
      if (!this.userLiked) {
        axios
          .post(
            "/api/communities/" + this.id + "/posts/" + this.postId + "/likes"
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
            "/api/communities/" + this.id + "/posts/" + this.postId + "/likes"
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
.badges {
  display: flex;
  flex-wrap: wrap;
}

.badges > div {
  width: auto;
  margin-bottom: 10px;
  padding-right: 10px;
}

.lecturer .oval {
  background: rgb(138, 59, 254);
  background: linear-gradient(
    45deg,
    rgba(138, 59, 254, 1) 11%,
    rgba(180, 55, 255, 1) 49%
  );
  box-shadow: 0 0 30px rgba(138, 59, 254, 1);
  font-weight: 600;
}

.lecturer .oval svg,
.community-owner .oval svg,
.thread-owner .oval svg {
  margin-left: 0;
}

.community-owner .oval {
  background: rgb(255, 237, 0);
  background: linear-gradient(
    270deg,
    rgba(255, 237, 0, 1) 15%,
    rgba(253, 248, 98, 1) 100%
  );
  font-weight: 600;
  box-shadow: 0 0 30px rgba(255, 237, 0, 1);
}

.thread-owner .oval {
  background: rgb(20, 90, 246);
  background: linear-gradient(
    90deg,
    rgba(20, 90, 246, 1) 27%,
    rgba(0, 137, 255, 1) 100%
  );
  font-weight: 600;
  box-shadow: 0 0 30px rgba(20, 90, 246, 1);
}

.send-icon {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
  background: white;
  color: black;
  padding: 3px 7px 3px 7px;
  border-radius: 12px;
  margin: auto 0;
}

.header {
  margin-bottom: 20px;
}

.comment-input {
  background: linear-gradient(to right, #272b39, #1e212b) !important;
  position: fixed;
  bottom: 0;
  z-index: 2;
  height: 150px;
  width: inherit;
  margin: 5px;
  display: flex;
  flex-direction: column;
  left: 0;
  right: 0;
  padding-top: 30px;
  border-radius: 20px;
}

.comment-input textarea {
  border: 1px solid #7e7e7e;
  overflow-y: auto;
  background: linear-gradient(to right, #272b39, #1e212b);
  height: 110px;
  color: white;
  width: 90%;
  margin: 5px auto auto;
  outline: none;
  resize: none;
}
.comment-btn {
  position: fixed;
  bottom: 12vh;
  width: 100%;
  background: linear-gradient(to right, #272b39, #1e212b);
  margin-left: -8px;
  height: 50px;
  display: flex;
  border-radius: 10px;
  z-index: 999;
  filter: drop-shadow(0px 0px 5px white);
}

.close-comment {
  position: absolute;
  top: 10px;
  left: 10px;
}
.comment-btn .comment-icon {
  font-size: 30px;
  margin: auto 10px;
}

.comment-btn p {
  margin: auto auto auto 0;
}

.containers {
  z-index: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: auto;
  border: none;
  position: relative;
  margin: 10px 10px 0;
}

.container {
  display: flex;
  flex-direction: column;
}

.post-content {
  background: linear-gradient(to right, #272b39, #1e212b);
  margin-left: -18px;
  margin-right: -18px;
  padding: 10px 10px 0 10px;
  filter: drop-shadow(0px 0px 5px white);
}

.comments-list {
  margin-right: -1px;
  margin-bottom: 80px;
}

.details .title {
  margin-top: 30px;
  margin-bottom: 10px;
  font-size: 20px;
}

.title p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  text-align: left;
}

.details .description {
  font-size: 15px;
  color: #7e7e7e;
  padding: 5px;
}

.description p {
  text-align: left;
  overflow-wrap: break-word;
}

.date {
  color: #7e7e7e;
  font-size: 15px;
}

.oval {
  display: flex;
  height: 20px;
  margin-top: 1px;
  margin-left: 0px;
  border-radius: 20vw 20vw 20vw 20vw;
  color: black;
  padding: 4px 10px 4px 10px;
}

.oval svg {
  margin: auto;
  margin-left: 10px;
  margin-right: 10px;
}

.oval p {
  margin: 0;
  margin-right: 20px;
}

.open .oval {
  background: linear-gradient(to right, #fe6811, #fe982d);
  box-shadow: 0 0 30px #fe6710;
  min-width: 130px;
}

.discussion .oval {
  background: linear-gradient(to right, #e276f4, #d225b1);
  box-shadow: 0 0 30px #da4ed3;
}

.answer .oval {
  background: linear-gradient(to right, #34e7e4, #63fba4);
  box-shadow: 0 0 30px #4cf1c4;
  min-width: 130px;
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
  bottom: 18px;
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

#back {
  text-align: left;
  color: #777779;
}

.settings-icon {
  position: absolute;
  top: 20px;
  right: 15px;
  font-size: 35px;
  color: #7e7e7e;
  cursor: pointer;
}
</style>
