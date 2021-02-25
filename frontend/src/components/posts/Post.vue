<template>
  <div class="container" @click="navigateToPost()">
        <div class="details">
          <div class="title">
            <p>{{ post.title }}</p>
          </div>
          <div class="description">
            <p>{{ post.description }}</p>
          </div>
          <div class="date">
            <p>{{ post.created_at }}</p>
          </div>

          <div v-if="this.info === 1">
            <div class="open">
              <div class="oval">
              </div>
              <font-awesome-icon :icon="['fa', 'question-circle']"></font-awesome-icon>
              <p>Open</p>
            </div>
          </div>
          <div v-if="this.info === 2">
            <div class="discussion">
              <div class="oval">
              </div>
              <font-awesome-icon :icon="['fa', 'question-circle']"></font-awesome-icon>
              <p>Discussion</p>
            </div>
          </div>
          <div v-if="this.info === 3">
            <div class="answer">
              <div class="oval">
              </div>
              <font-awesome-icon :icon="['fa', 'question-circle']"></font-awesome-icon>
              <p>Answered</p>
            </div>
          </div>
        </div>
    <div class="likes">
      <div class="like-icon">
        <font-awesome-icon :icon="['fa', 'thumbs-up']"></font-awesome-icon>
      </div>
      <div class="like-count">{{ post.likes_num }}</div>
    </div>
    <div class="author">
      <p>Authored by <span class="author-name">{{ post.user.username }}</span></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Post',
  props: {
    post: Object,
  },
  data() {
    return {
      info: 1
    }
  },
  methods: {
    navigateToPost() {

    },
  }

}
</script>

<style scoped>
.container {
  z-index: -1;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin-top: 10px;
  margin-bottom: 10px;
  height: 20vh;
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
}

.open .oval {
  display: -webkit-box;
  position: absolute;
  z-index: -1;
  top: 0;
  left: 0;
  width: 20vw;
  height: 2.5vh;
  margin-top: -0.2vh;
  margin-left: -2.5vw;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #FE6710, #FE6710);
}

.discussion .oval {
  display: -webkit-box;
  position: absolute;
  top: 0;
  left: 0;
  width: 20vw;
  height: 2.5vh;
  margin-top: 1vh;
  margin-left: 5vw;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #FE6710, #FE6710);
}

.question .oval {
  display: -webkit-box;
  position: absolute;
  top: 0;
  left: 0;
  width: 20vw;
  height: 2.5vh;
  margin-top: 1vh;
  margin-left: 5vw;
  border-radius: 20vw 20vw 20vw 20vw;
  background: linear-gradient(to right, #FE6710, #FE6710);
}

.open {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  color: black;
  margin-left: 8vw;
  margin-top: 1.2vh;
}

.open p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 5vw;
}

.discussion {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  color: black;
  margin-left: 8vw;
  margin-top: 1.2vh;
}

.discussion p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 5vw;
}

.answer {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  color: black;
  margin-left: 8vw;
  margin-top: 1.2vh;
}

.answer p {
  font-family: "Trebuchet MS", serif;
  position: absolute;
  top: 0;
  margin-top: -0.1vh;
  left: 5vw;
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