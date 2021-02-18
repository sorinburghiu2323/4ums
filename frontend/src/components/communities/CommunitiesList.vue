<template>
  <div class="container">
      <CommunityDisplay />
      <CommunityDisplay />
      <CommunityDisplay />
      <CommunityDisplay />
      <CommunityDisplay />
      <CommunityDisplay />
  </div>
</template>

<script>
import CommunityDisplay from '@/components/communities/CommunityDisplay.vue'
export default {
    name: 'CommunitiesList',
    components: {
        CommunityDisplay,
    }

}
</script>

<style scoped>

</style>