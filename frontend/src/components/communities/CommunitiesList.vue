<template>
  <div class="container">
      <CommunityDisplay v-for="(community,index) in communities" :key="index"
      :community="community" :myCommunity="myCommunities"/>
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
        myCommunities: {
            default: true,
            type: Boolean,
        }
    }

}
</script>

<style scoped>

</style>