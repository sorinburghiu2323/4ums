<template>
  <div class="containers" @click='navigateToPost'>
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

      <div v-if="post_type === 'question'&& !this.approvedAnswer">
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
    <div class="author" @click.stop='navigateToUser'>
      <p>Authored by <span class="author-name">{{ post["user"]["username"] }}</span></p>
    </div>
  </div>
</template>
<script>
import moment from 'moment'
import axios from "axios";


export default {
  name: 'Post',
  props: {
    post: Object,
  },
  data() {
    return {
      info: 3,
      post_type: this.post.post_type,
      userLiked: this.post["is_liked"],
      approvedAnswer: this.post["has_approved"],
      date_time: moment((this.post["create_at"])).format('DD/MM/YY'),
    }
  },
  methods: {
    navigateToPost() {
      this.$router.push({
        name: 'PostPage',
        params: {
          id: this.post.community.id,
          postId: this.post.id
        }
      })
    },
    navigateToUser() {
      this.$router.push({
        name: 'User',
        params: {
          id: this.post.user.id
        }
      })
    },
    likePost() {
      if (!this.userLiked) {
        axios.post('/api/communities/' + this.post.community.id + '/posts/' + this.post.id + '/likes')
            .then(() => {
              this.post["likes_num"]++;
              this.userLiked = true;
            })
            .catch((error) => {
              console.log(error);
            })
      } else {
        axios.delete('/api/communities/' + this.post.community.id + '/posts/' + this.post.id + '/likes')
            .then(() => {
              this.post["likes_num"]--;
              this.userLiked = false;
            }).catch((error) => {
          console.log(error);
        })
      }
    },
  }
}
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
  background: linear-gradient(to right, #272B39, #1D2029);
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
  z-index: 0;
  width: 60px;
  display: flex;
  margin-left: 25px;
}

.like-icon {
  font-size: 20px;
}

.like-count {
  margin-left: 10px;
  font-size: 20px;
}
.author {
  position: absolute;
  z-index: 1;
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