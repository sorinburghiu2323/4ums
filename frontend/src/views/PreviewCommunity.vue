<template>
  <div>
    <router-link class="nav-link" to="../communities/create">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" /> Edit Community
      </p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "PreviewCommunity",
};
</script>

<style></style>
