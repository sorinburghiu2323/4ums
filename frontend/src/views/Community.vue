<template>
  <div>
      Community {{ this.id }}
      <CreatePostButton />
  </div>
</template>

<script>
import CreatePostButton from '../components/CreatePostButton.vue'

export default {
    components: {
        CreatePostButton
    },
    created() {
        this.id = this.$route.params.id;
    }
}
</script>

<style>

</style>