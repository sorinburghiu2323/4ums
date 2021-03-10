<template>
  <div class="container">
    <CreatePostButton v-if="showCreateButton" :community="community" />
    <router-link class="nav-link" to="/communities">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
        Communities
      </p>
    </router-link>
    <div v-if="loadedCommunity" class="community-content">
      <div class="header">
        <h1>{{ community.name }}</h1>
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
      <div class="description">
        <p>{{ community.description }}</p>
      </div>
      <div class="join-community">
        <button
          v-if="!joined"
          class="join-community-btn"
          @click="joinCommunity()"
        >
          Join Community
        </button>
      </div>
      <div class="search-section">
        <input id="search" v-model="query" placeholder="Search for a thread..." type="text"
               @keyup.enter="getSearchPosts()"/>
        <div v-if="query === '' && firstGet">
          {{ getSearchPosts() }}
          {{ this.firstGet = false }}
        </div>
        <div class="search-icon" @click.stop.prevent="getSearchPosts()">
          <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
        </div>
      </div>
      <div v-if="loadedPosts && joined && !noPosts">
        <Post v-for="(post, index) in posts" :key="index" :post="post"/>
      </div>
      <div v-else-if="!joined" style="margin-top: 50px;">
        Join community to see posts...
      </div>
      <div v-else-if="noPosts">
        <h3>
          Sorry we couldn't find any threads matching your search.
        </h3>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Post from "@/components/posts/Post.vue";
import CreatePostButton from "../components/CreatePostButton.vue";

export default {
  name: "Community",
  components: {
    Post,
    CreatePostButton,
  },
  data() {
    return {
      loadedCommunity: false,
      loadedPosts: false,
      showCreateButton: true,
      community: null,
      currentPage: 1,
      posts: [],
      loadMore: false,
      joined: true,
      id: null,
      query: '',
      firstGet: false,
      noPosts: false,
    };
  },
  created() {
    this.id = this.$route.params.id;
  },
  mounted() {
    this.getCommunity();
    this.getPosts();
    this.scroll();
  },

  methods: {
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight >
          document.body.scrollHeight;
        if (bottomOfWindow) {
          this.showCreateButton = false;
          if (this.loadMore) {
            this.loadMorePosts();
            this.loadMore = false;
          }
        } else {
          this.showCreateButton = true;
        }
      };
    },
    getCommunity() {
      const community_id = this.$route.params.id;
      const url = "/api/communities/" + community_id;
      axios.get(url).then((response) => {
        this.community = response.data;
        this.loadedCommunity = true;
      });
    },
    getSearchPosts() {
      this.posts = [];
      this.noPosts = false;
      this.currentPage = 1;
      this.firstGet = true;
      if (this.query === "") {
        this.getPosts();
        this.firstGet = false;
      } else {
        document.getElementById('search').blur();
        const community_id = this.$route.params.id;
        const url = "/api/communities/" + community_id + "/posts";
        axios
            .get(url, {params: {page: this.currentPage, phrase: this.query}})
            .then((response) => {
              for (let i = 0; i < response.data.data.length; i++) {
                this.posts.push(response.data.data[i]);
              }
              if (this.currentPage === 1 && response.data.data.length === 0) {
                this.noPosts = true;
              }
              this.loadMore = response.data["next_page"] !== null;
              this.loadedPosts = true;
            })
            .catch((error) => {
              if (error.response.status === 403) {
                this.joined = false;
              }
            });

      }
    },
    getPosts() {
      this.noPosts = false;
      const community_id = this.$route.params.id;
      const url = "/api/communities/" + community_id + "/posts";
      axios
          .get(url, {params: {page: this.currentPage}})
          .then((response) => {
            for (let i = 0; i < response.data.data.length; i++) {
              this.posts.push(response.data.data[i]);
            }
            if (this.currentPage === 1 && response.data.data.length === 0) {
              this.noPosts = true;
            }
            this.loadMore = response.data["next_page"] !== null;
            this.loadedPosts = true;
          })
        .catch((error) => {
          if (error.response.status === 403) {
            this.joined = false;
          }
        });
    },
    loadMorePosts() {
      this.currentPage++;
      this.getPosts();
    },
    joinCommunity() {
      const community_id = this.$route.params.id;
      const url = "/api/communities/" + community_id;
      axios
        .post(url)
        .then(() => {
          this.joined = true;
          this.getPosts();
        })
        .catch((error) => {
          console.error("Could not join community", error);
        });
    },
  },
};
</script>

<style scoped>
.container {
  height: 100%;
}
.community-content {
  display: flex;
  flex-direction: column;
}
#back {
  text-align: left;
  color: #777779;
}
.header {
  display: flex;
  justify-content: flex-start;
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
.description {
  font-size: 15px;
  color: #7e7e7e;
  text-align: left;
}

.description p {
  display: flex;
  overflow-wrap: anywhere;
}
.join-community {
  display: flex;
  justify-content: flex-start;
}
.join-community-btn {
  padding: 8px;
  margin: 5px;
  width: 150px;
  border-radius: 25px;
  border: none;
  outline: none;
  cursor: pointer;
  font-weight: 600;
  background: linear-gradient(
    270deg,
    rgba(138, 59, 254, 1) 0%,
    rgba(180, 55, 255, 1) 35%
  );
  box-shadow: 0px 5px 40px #268079;
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

.load-more-btn {
  padding: 8px;
  border-radius: 25px;
  border: none;
  outline: none;
  cursor: pointer;
  width: 150px;
  margin: auto;
  font-weight: 600;
  background: rgb(254, 155, 47);
  background: linear-gradient(
    90deg,
    rgba(254, 155, 47, 1) 0%,
    rgba(254, 101, 15, 1) 35%
  );
  box-shadow: 0px 5px 40px #c35456;
}
</style>
