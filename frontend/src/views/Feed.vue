<template>
  <div id="infinite" class="container">
    <div class="header">
      <h1>Feed</h1>
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
    <div class="search-section">
      <input placeholder="Search for a thread..." type="text" />
      <div class="search-icon">
        <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
      </div>
    </div>
    <div v-if="loadedPosts && !noPosts">
      <div class="post-content">
        <Post v-for="(post, index) in allPosts" :key="index" :post="post" />
      </div>
    </div>
    <div v-else-if="noPosts">
      <h3>
        There are no posts left for you to view, maybe join more communities?
      </h3>
    </div>
    <div><br /><br /><br /><br /></div>
  </div>
</template>
<script>
import axios from "axios";
import Post from "@/components/posts/Post";

export default {
  name: "feed",
  components: {
    Post,
  },
  watch: {
    showPosts() {
      this.currentPage = 1;
      this.loadedPosts = false;
      this.allPosts = [];
      this.getPosts();
    },
  },
  data() {
    return {
      loadedPosts: false,
      allPosts: [],
      currentPage: 1,
      bottomOfPageReached: false,
      errorLoadingPosts: false,
      loadMore: false,
      scrolledToBottom: false,
      noPosts: false,
    };
  },
  mounted() {
    this.getPosts();
    this.scroll();
  },
  methods: {
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight >
          document.body.scrollHeight - 200;
        if (bottomOfWindow) {
          if (this.loadMore) {
            this.loadMorePosts();
            this.loadMore = false;
          }
        }
      };
    },
    async getPosts() {
      await axios
        .get("api/users/feed", { params: { page: this.currentPage } })
        .then((response) => {
          this.loadedPosts = false;
          if (this.currentPage === 1 && response.data.data.length === 0) {
            this.noPosts = true;
          }
          for (let i = 0; i < response.data.data.length; i++) {
            this.allPosts.push(response.data.data[i]);
          }
          this.loadMore = response.data.next_page !== null;
          this.loadedPosts = true;
        })
          .catch((error) => {
            console.error(error);
            this.loadedPosts = false;
          });
    },
    loadMorePosts() {
      this.currentPage += 1;
      this.getPosts();
    },
  },
};
</script>
<style scoped>
.container {
  height: 100%;
}

.post-content {
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 30px;
}

.header h1 {
  font-size: 30px;
  text-align: left;
  margin-bottom: 0;
}

.header > .settings-icon {
  position: absolute;
  top: 20px;
  right: 15px;
  font-size: 35px;
  color: #7e7e7e;
  cursor: pointer;
}

.search-section {
  display: flex;
  width: 100%;
}

::placeholder {
  color: white;
}

.search-section input {
  width: 100%;
  height: 46px;
  font-size: 15px;
  padding-left: 10px;
  color: white;
  outline: none;
  font-weight: 600;
  border-radius: 25px;
  border: none;
  background: rgb(40, 44, 58);
  background: linear-gradient(
    90deg,
    rgba(40, 44, 58, 1) 0%,
    rgba(27, 30, 40, 1) 35%,
    rgba(8, 9, 11, 1) 100%
  );
  margin: auto;
}

.search-section > .search-icon {
  font-size: 28px;
  height: 29px;
  padding: 10px;
  border-radius: 15px;
  position: relative;
  color: black;
  margin: 10px;
  display: flex;
  cursor: pointer;
  background: rgb(138, 59, 254);
  background: linear-gradient(
    225deg,
    rgba(138, 59, 254, 1) 11%,
    rgba(180, 55, 255, 1) 49%
  );
}

.search-icon svg {
  margin: auto;
}
</style>
