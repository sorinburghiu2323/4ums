<template>
  <div class="containers">
    <div class="details">
      <div class="description">
        <p>{{ this.comment.comment }}</p>
      </div>
      <div class="date">
        <p>{{ date_time }}</p>
      </div>
      <div v-if="is_approved">
        <div class="answer">
          <div class="oval">
          </div>
          <font-awesome-icon :icon="['fa', 'check-circle']"></font-awesome-icon>
          <p>Chosen Answer</p>
        </div>
      </div>
    </div>
    <div class="likes" @click.stop="likeComment">
      <div v-if="this.userLiked" style="color:white">
        <div class="like-icon">
          <font-awesome-icon :icon="['fas', 'thumbs-up']"></font-awesome-icon>
        </div>
        <div class="like-count">{{ this.numLikes }}</div>
      </div>
      <div v-else style="color:grey">
        <div class="like-icon">
          <font-awesome-icon :icon="['fas', 'thumbs-up']"></font-awesome-icon>
        </div>
        <div class="like-count">{{ this.numLikes }}</div>
      </div>
    </div>
    <div class="author" @click.stop="navigateToUser">
      <p>Authored by <span class="author-name">{{ comment.user.username }}</span></p>
    </div>
  </div>
</template>

<script>
import moment from 'moment'
import axios from "axios";

export default {
  name: 'Comment',
  props: {
    comment: Object
  },
  data() {
    return {
      info: 3,
      comment_data: this.comment.comment,
      is_approved: this.comment.is_approved,
      date_time: moment((this.comment["created_at"])).format('DD/MM/YY'),
      userLiked: this.comment["is_liked"],
      commentId: this.comment.id,
      numLikes: this.comment["comment_likes"],
      postId: this.$route.params.postId,
      communityId: this.$route.params.id,
    }
  },
  methods: {
    navigateToUser() {
      this.$router.push({
        name: 'User',
        params: {
          id: this.comment["user"]["id"]
        }
      })
    },
    likeComment() {
      if (!this.userLiked) {
        axios.post('/api/communities/' + this.communityId + '/posts/' + this.postId + '/comments/' + this.commentId +
            '/likes')
            .then(() => {
              this.numLikes++;
              this.userLiked = true;
            })
            .catch((error) => {
              console.error(error);
            })
      } else {
        axios.delete('/api/communities/' + this.communityId + '/posts/' + this.postId + '/comments/' + this.commentId +
            '/likes')
            .then(() => {
              this.numLikes--;
              this.userLiked = false;
            }).catch((error) => {
          console.error(error);
        })
      }
    }
  }
}
</script>

<style scoped>
.containers {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin: 0 10px 10px;
  height: auto;
  padding: 0 3px 10px 0;
  border: none;
  background: linear-gradient(to right, #272B39, #1E212B);
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
  color: #7e7e7e;
}

.details .description {
  height: 70%;
  font-size: 15px;
  color: #7e7e7e;
}

.description p {
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
  top: 10px;
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

.answer .oval {
  display: -webkit-box;
  position: absolute;
  z-index: -1;
  top: -3px;
  left: 0;
  width: 150px;
  height: 20px;
  margin-top: 1px;
  margin-left: -10px;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #145AF6, #0089FF);
  box-shadow: 0 0 30px #0A72FB;
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
  position: relative;
  top: 0;
  margin-top: -0.1vh;
  left: 5px;
}

.likes {
  display: flex;
  margin-left: 25px;
}

.like-icon {
  font-size: 20px;
}

.like-count {
  margin-left: 10px;
  font-size: 20px;
  margin: auto;
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