<template>
  <div class="container">
      <CommunityDisplay v-for="(community,index) in communities" :key="index"
      :community="community" :myCommunities="true"/>
  </div>
</template>

<script>
import CommunityDisplay from '@/components/communities/CommunityDisplay.vue'
export default {
    name: 'CommunitiesList',
    components: {
        CommunityDisplay,
    },
    props: {
        communities: Array,
    }

}
</script>

<style scoped>

</style>