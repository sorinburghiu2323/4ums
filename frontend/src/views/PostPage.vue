<template>
  <div v-if="loadedPost" class="container">
    <router-link class="nav-link" to="..">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']"/>
        {{ post.community.name }}
      </p>
    </router-link>
    <div class="header">
      <div class="settings-icon">
        <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
      </div>
    </div>
    <div class="containers">
      <div class="details">
        <div class="title">
          <p>{{ post.title }}</p>
        </div>
        <div class="description">
          <p>{{ post.description }}</p>
        </div>
        <div class="date">
          <p>{{ date_time }}</p>
        </div>

        <div v-if="post_type === 'question' && !this.isAnswered">
          <div class="open">
            <div class="oval">
            </div>
            <font-awesome-icon :icon="['fa', 'question-circle']"></font-awesome-icon>
            <p>Open</p>
          </div>
        </div>
        <div v-else-if="post_type === 'discussion'">
          <div class="discussion">
            <div class="oval">
            </div>
            <font-awesome-icon :icon="['fa', 'comment-dots']"></font-awesome-icon>
            <p>Discussion</p>
          </div>
        </div>
        <div v-else>
          <div class="answer">
            <div class="oval">
            </div>
            <font-awesome-icon :icon="['fa', 'check-circle']"></font-awesome-icon>
            <p>Answered</p>
          </div>
        </div>
      </div>
      <div class="likes" @click.stop='likePost'>
        <div v-if="this.userLiked" style="color:white">
          <div class="like-icon">
            <font-awesome-icon :icon="['fas', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ post["likes_num"] }}</div>
        </div>
        <div v-else style="color:grey">
          <div class="like-icon">
            <font-awesome-icon :icon="['fas', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ post["likes_num"] }}</div>
        </div>
      </div>
      <div class="author" @click.stop="navigateToUser">
        <p>Authored by <span class="author-name">{{ post.user.username }}</span></p>
      </div>
    </div>
    <div class="comment-btn" @click.stop="showCommentInput">
      <p>Add a comment...</p>
      <div class="comment-icon">
        <font-awesome-icon :icon="['fas', 'comment-dots']"></font-awesome-icon>
      </div>
    </div>
    <div v-if="showInput" class="comment-input">
      <md-field style="background:linear-gradient(to right, #272B39, #1E212B);">
        <label style="color:white">Add a comment...</label>
        <md-textarea v-model="addComment" md-autogrow
                     style="background:linear-gradient(to right, #272B39, #1E212B); height: 60px;color:white;"></md-textarea>
        <div class="send-icon" @click.stop="sendComment">
          <font-awesome-icon :icon="['fas', 'paper-plane']"></font-awesome-icon>
        </div>
      </md-field>
    </div>
    <div v-if="loadedPost" class="comments-list">
      <Comment v-for="(comment, index) in allComments" :key="index"
               :comment="comment"/>
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
    Comment
  },
  watch: {
    showPost() {
      this.currentPage = 1;
      this.allComments = [];
      this.loadedPost = false;
      this.getPost();
    }
  },
  data() {
    return {
      id: this.$route.params.id,
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
      date_time: '10/20/30',
      isAnswered: false,
      userLiked: false,
      addComment: null,
      showInput: false
    }
  },
  mounted() {
    this.getPost();
    this.scroll();
  },
  methods: {
    sendComment() {
      axios.post('/api/communities/' + this.id + '/posts/' + this.postId + '/comments', {"comment": this.addComment})
          .then(() => {
            console.log("added comment")
            this.showInput = false;
            this.$router.go(0);
          })
          .catch((error) => {
            console.log(error);
          })
    },
    showCommentInput() {
      console.log(this.showInput);
      this.addComment = null;
      this.showInput = !this.showInput;
    },
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop,
            document.body.scrollTop) + window.innerHeight;
        if (bottomOfWindow >= document.documentElement.offsetHeight - 200) {
          if (this.loadMore) {
            this.loadMoreComments();
            this.loadMore = false;
          }
        }
      }
    },
    async getPost() {
      await axios.get('/api/communities/' + this.id + '/posts/' + this.postId, {params: {page: this.currentPage}})
          .then((response) => {
            this.loadedPost = false;
            this.post = response.data.post;
            for (let i = 0; i < response.data.comments.data.length; i++) {
              this.allComments.push(response.data.comments.data[i]);
            }
            this.date_time = moment((this.post["created_at"])).format('DD/MM/YY');
            this.post_type = this.post["post_type"];
            this.loadMore = response.data.comments["next_page"] !== null;
            this.isAnswered = this.post["has_approved"];
            this.loadedPost = true;
            this.userLiked = this.post["is_liked"];
          }).catch((error) => {
            console.error(error);
            if (error.response.status === 401) {
              this.$router.push(LoginPage);
            }
            this.loadedPosts = false;
          })
    },
    loadMoreComments() {
      this.currentPage++;
      this.getPost();
    },
    navigateToUser() {
      this.$router.push({
        name: 'User',
        params: {
          id: this.post["user"]["id"]
        }
      })
    },
    likePost() {
      if (!this.userLiked) {
        axios.post('/api/communities/' + this.id + '/posts/' + this.postId + '/likes')
            .then(() => {
              this.post["likes_num"]++;
              this.userLiked = true;
            })
            .catch((error) => {
              console.log(error);
            })
      } else {
        axios.delete('/api/communities/' + this.id + '/posts/' + this.postId + '/likes')
            .then(() => {
              this.post["likes_num"]--;
              this.userLiked = false;
            }).catch((error) => {
          console.log(error);
        })
      }
    }
  }
}
</script>

<style scoped>

.send-icon {
  position: absolute;
  top: -10px;
  right: 0;
  color: dodgerblue;
  font-size: 25px;
}

.comment-input {
  background: linear-gradient(to right, #272B39, #1E212B) !important;
  z-index: 2;
  min-width: 94vw;
  min-height: 100px;
  height: auto;
  bottom: 10px;
  line-height: 20px;
  margin-left: 10px;
  position: fixed;
  padding: 10px;
  color: white;
  box-shadow: 0 0 30px black;
}

.comment-btn {
  position: relative;
  background: linear-gradient(to right, #272B39, #1E212B);
  width: auto;
  height: auto;
  outline: none;
  cursor: pointer;
  font-weight: 600;
  padding: 10px;
  margin: 10px 10px 0;
}

.comment-btn .comment-icon {
  position: relative;
  bottom: 10px;
  width: auto;
  left: -81px;
}

.comment-btn p {
  position: relative;
  margin: auto;
  color: white;
  top: 7px;
}

.containers {
  z-index: 0;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin: 10px;
  height: auto;
  padding: 0 3px 10px 0;
  border: none;
  background: linear-gradient(to right, #272B39, #1E212B);
  position: relative;
}

.details {
  margin: 20px auto 20px 25px;
}

.comments-list {
  padding-bottom: 85px;
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
  -webkit-box-orient: vertical;
  text-align: left;
}

.details .description {
  height: 70%;
  font-size: 15px;
  color: #7e7e7e;
}

.description p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  text-align: left;
}

.date {
  display: flex;
  position: absolute;
  top: 0;
  right: 0;
  color: #7e7e7e;
  font-style: italic;
  margin-right: 10px;
  margin-top: 1vh;
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
  background: linear-gradient(to right, #FE6811, #FE982D);
  box-shadow: 0 0 30px #FE6710;
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
  background: linear-gradient(to right, #E276F4, #D225B1);
  box-shadow: 0 0 30px #DA4ED3;
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
  background: linear-gradient(to right, #34E7E4, #63FBA4);
  box-shadow: 0 0 30px #4CF1C4;
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
  margin-left: 25px;
}

.like-icon {
  font-size: 20px;
}

.like-count {
  font-size: 20px;
  margin-left: 10px;
}

.author {
  position: absolute;
  bottom: 0;
  right: 0;
  color: #7e7e7e;
  font-style: italic;
  margin-right: 10px;
}

.author-name {
  text-decoration: underline;
}
</style>