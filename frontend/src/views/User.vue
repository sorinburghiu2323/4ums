<template>
  <div class="containers">
    <router-link class="nav-link" to="..">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']"/>
        User
      </p>
    </router-link>
    <div class="header">
      <div class="settings-icon">
        <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "User",
  data() {
    return {
      id: this.$route.params.id
    }
  }
}
</script>

<style scoped>
.containers {
  z-index: -1;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  margin-top: 10px;
  margin-bottom: 10px;
  height: auto;
  padding: 0 3px 10px 0;
  border: none;
  background: linear-gradient(to right, #272B39, #1E212B);
  position: relative;
}
</style>