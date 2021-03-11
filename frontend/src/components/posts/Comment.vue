<template>
  <div class="containers container">
    <div class="badges">
      <div v-if="is_approved" class="chosen-answer">
        <font-awesome-icon :icon="['fa', 'crown']"></font-awesome-icon>
        <p>Chosen Answer</p>
      </div>
      <div v-if="comment.user.is_teacher" class="lecturer">
        <font-awesome-icon :icon="['fa', 'chalkboard-teacher']" />
        <p>Lecturer</p>
      </div>
      <div v-if="isByCommunityOwner" class="community-owner">
        <font-awesome-icon :icon="['fa', 'hand-peace']" />
        <p>Community Owner</p>
      </div>
      <div v-if="isByPostOwner" class="thread-owner">
        <font-awesome-icon :icon="['fa', 'hand-peace']" />
        <p>Thread Owner</p>
      </div>
      <div
        v-if="displayApprove && !is_approved && isQuestion && !beenApproved"
        class="approve"
        @click="approveAnswer()"
      >
        <p>
          <font-awesome-icon :icon="['fas', 'check-circle']" />
          Approve Answer
        </p>
      </div>
      <div
        v-if="displayApprove && is_approved && isQuestion"
        class="approve"
        @click="unApproveAnswer()"
      >
        <p>
          <font-awesome-icon :icon="['fas', 'times-circle']" />
          Un-Approve Answer
        </p>
      </div>
    </div>
    <div class="details">
      <div v-if="comment.comment" class="description">
        <p>{{ comment.comment }}</p>
      </div>
    </div>
    <div style="display: flex;">
      <div class="likes" @click.stop="likeComment">
        <div v-if="userLiked" style="color:white">
          <div class="like-icon">
            <font-awesome-icon :icon="['fa', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ numLikes }}</div>
        </div>
        <div v-else style="color:grey">
          <div class="like-icon">
            <font-awesome-icon :icon="['far', 'thumbs-up']"></font-awesome-icon>
          </div>
          <div class="like-count">{{ numLikes }}</div>
        </div>
      </div>
      <div class="date">
        <p>Posted {{ date_time }}</p>
      </div>
    </div>

    <div class="author" @click.stop="navigateToUser">
      <p>
        By <span class="author-name">{{ comment.user.username }}</span>
      </p>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";

export default {
  name: "Comment",
  props: {
    comment: Object,
    isByPostOwner: Boolean,
    isByCommunityOwner: Boolean,
    isQuestion: Boolean,
    displayApprove: Boolean,
    hasBeenApproved: Boolean,
  },
  data() {
    return {
      info: 3,
      comment_data: this.comment.comment,
      is_approved: this.comment.is_approved,
      userLiked: this.comment["is_liked"],
      numLikes: this.comment["comment_likes"],
      beenApproved: this.hasBeenApproved,
    };
  },
  computed: {
    communityId() {
      return this.$route.params.id;
    },
    postId() {
      return this.$route.params.postId;
    },
    date_time() {
      return moment(this.comment["created_at"]).format("DD/MM/YY");
    },
  },
  methods: {
    navigateToUser() {
      this.$router.push({
        name: "User",
        params: {
          id: this.comment["user"]["id"],
        },
      });
    },
    async unApproveAnswer() {
      await axios.delete(
          "/api/communities/" +
          this.communityId +
          "/posts/" +
          this.postId +
          "/comments/" +
          this.comment.id +
          "/approve"
      );
      this.is_approved = false;
      this.beenApproved = false;
      this.$emit("update-post");
    },
    async approveAnswer() {
      await axios.post(
          "/api/communities/" +
          this.communityId +
          "/posts/" +
          this.postId +
          "/comments/" +
          this.comment.id +
          "/approve"
      );
      this.is_approved = true;
      this.beenApproved = true;
      this.$emit("update-post");
    },
    likeComment() {
      if (!this.userLiked) {
        axios
          .post(
            "/api/communities/" +
              this.communityId +
              "/posts/" +
              this.postId +
              "/comments/" +
              this.comment.id +
              "/likes"
          )
          .then(() => {
            this.numLikes++;
            this.userLiked = true;
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        axios
          .delete(
            "/api/communities/" +
              this.communityId +
              "/posts/" +
              this.postId +
              "/comments/" +
              this.comment.id +
              "/likes"
          )
          .then(() => {
            this.numLikes--;
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
.approve {
  background-color: white;
}
.containers {
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin: 0 10px 10px;
  height: auto;
  padding: 0 3px 10px 0;
  border: none;
  background: linear-gradient(to right, #272b39, #1e212b);
  position: relative;
}

.container {
  font-size: 15px;
  color: #7e7e7e;
  background: linear-gradient(to right, #272b39, #1e212b);
  margin-left: -8px !important;
  margin-right: -7px !important;
  padding: 10px 10px 0px 10px !important;
}

.badges {
  display: flex;
  flex-wrap: wrap;
}

.badges div {
  border-radius: 25px;
  padding: 2px 15px 2px 15px;
  color: black;
  display: flex;
  margin-right: 10px;
  margin-bottom: 10px;
}

.badges div p {
  margin: auto auto auto 4px;
  font-weight: 600;
}

.badges div svg {
  margin: auto auto auto 0;
}

.lecturer {
  background: rgb(138, 59, 254);
  background: linear-gradient(
    225deg,
    rgba(138, 59, 254, 1) 11%,
    rgba(180, 55, 255, 1) 49%
  );
}

.community-owner {
  background: rgb(255, 237, 0);
  background: linear-gradient(
    270deg,
    rgba(255, 237, 0, 1) 15%,
    rgba(253, 248, 98, 1) 100%
  );
}

.thread-owner {
  background: rgb(20, 90, 246);
  background: linear-gradient(
    90deg,
    rgba(20, 90, 246, 1) 27%,
    rgba(0, 137, 255, 1) 100%
  );
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
  font-size: 15px;
  color: #7e7e7e;
  padding: 5px;
  white-space: pre-wrap;
}

.description p {
  text-align: left;
  overflow-wrap: break-word;
}

.date {
  color: #7e7e7e;
  font-size: 15px;
  margin: auto;
  margin-left: 0px;
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
  background: linear-gradient(to right, #145af6, #0089ff);
  box-shadow: 0 0 30px #0a72fb;
}

.chosen-answer {
  background: linear-gradient(
    270deg,
    rgba(52, 235, 233, 1) 0%,
    rgba(101, 255, 167, 1) 35%
  );
  box-shadow: 0px 5px 40px #268079;
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
  color: white;
}

.author {
  position: absolute;
  bottom: 16px;
  right: 16px;
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
