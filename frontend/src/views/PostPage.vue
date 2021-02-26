<template>
  <div id="infinite" class="container">
    <div class="header">
      <h1>Feed</h1>
      <div class="settings-icon">
        <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
      </div>
    </div>
    <div class="search-section">
      <input placeholder="Search for a thread..." type="text"/>
      <div class="search-icon">
        <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
      </div>
    </div>
    <div v-if="loadedPosts">
      <div class="post-content">
        <Post v-for="(post, index) in allPosts" :key="index"
              :post="post"/>
      </div>
    </div>
  </div>
</template>

<script>
import Post from "@/components/posts/Post";

export default {
  name: "PostPage",
  components: {
    Post,
  },
}
</script>

<style scoped>

</style>