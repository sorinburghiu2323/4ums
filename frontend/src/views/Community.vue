<template>
    <div class="container">
        <router-link class="nav-link" to="../communities">
            <p id="back">
                <font-awesome-icon :icon="['fas', 'arrow-left']" /> Communities
            </p>
        </router-link>
        <div v-if="loadedCommunity" class="community-content">
            <div class="header">
                <h1>{{community.name}}</h1>
                <div class="settings-icon">
                    <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
                </div>
            </div>
            <div class="description">
              <p>{{community.description}}</p>              
            </div>
            <div class="join-community">
                <button class="join-community-btn" v-if="!joined"
                @click="joinCommunity()">Join Community</button>
            </div>
            <div class="search-section">
                <input type="text" placeholder="Search for a thread..."/>
                <div class="search-icon">
                    <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
                </div>
            </div>
            <div v-if="loadedPosts && joined"> 
              <Post v-for="(post, index) in posts" :key="index"
              :post="post"/>
            </div>
            <div v-else-if="!joined" style="margin-top: 50px;"> 
              Join community to see posts...
            </div>
         
        <button v-if="loadMore" class="load-more-btn" @click="loadMorePosts()">Load more</button>

        </div>
  </div>
</template>

<script>
import axios from 'axios';
import Post from '@/components/posts/Post.vue';
export default {
    name: 'Community',
    components: {
        Post,
    },
    data() {
        return {
            loadedCommunity: false,
            loadedPosts: false,
            community: null,
            currentPage: 1,
            posts: [],
            loadMore: false,
            joined: true,
        }
    },
    mounted() {
        this.getCommunity();
        this.getPosts();
    },
    methods: {
        getCommunity() {
            const community_id = this.$route.params.id;
            const url = 'api/communities/' + community_id;
            axios.get(url)
            .then((response) => {
                this.community = response.data;
                this.loadedCommunity = true;
            })
        },
        getPosts() {
            const community_id = this.$route.params.id;
            const url = 'api/communities/' + community_id + '/posts';
            axios.get(url, {params: {page: this.currentPage}})
            .then((response) => {
                for(var i = 0; i < response.data.data.length; i++) {
                    this.posts.push(response.data.data[i]);
                }
                if(response.data.next_page != null) {
                    this.loadMore = true;
                } else {
                    this.loadMore = false;
                }
                this.loadedPosts = true;
            })
            .catch((error)=>{
                if(error.response.status === 403) {
                    this.joined = false;
                }
                
            })          
        },
        loadMorePosts() {
            this.currentPage += 1;
            this.getPosts();
        },
        joinCommunity() {
            const community_id = this.$route.params.id;
            const url = 'api/communities/' + community_id;
            axios.post(url)
            .then(() => {
                this.joined = true;
                this.getPosts();
            })
            .catch((error)=>{
                console.error('Could not join community', error);
            })
        }
    }
}
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
  margin-left: 2vh;
  padding-top: 2vh;
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
}
.description {
    font-size: 15px;
    color: #7E7E7E;
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
    background: linear-gradient(270deg, rgba(138,59,254,1) 0%, rgba(180,55,255,1) 35%);
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
    border: 1px solid black;
    height: 46px;
    font-size: 15px;
    padding-left: 10px;
    color: white;
    outline: none;
    font-weight: 600;
    border-radius: 25px;
    border: none;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%);
}

.search-section > .search-icon {
    font-size: 28px;
    margin-left: 10px;
    height: 28px;
    padding: 10px;
    border-radius: 15px;
    color: black;
    display: flex;
    cursor: pointer;
    background: rgb(138,59,254);
    background: linear-gradient(225deg, rgba(138,59,254,1) 11%, rgba(180,55,255,1) 49%);
}

.search-icon svg {
    margin: auto;
}

.load-more-btn {
    padding: 8px;
    margin: 5px;
    border-radius: 25px;
    border: none;
    outline: none;
    cursor: pointer;
    width: 150px;
    margin: auto;
    margin-bottom: 10px;
    font-weight: 600;
    background: rgb(254,155,47);
    background: linear-gradient(90deg, rgba(254,155,47,1) 0%, rgba(254,101,15,1) 35%);
    box-shadow: 0px 5px 40px #C35456;
}
</style>