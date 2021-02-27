<template>
  <div class="container">
      <CommunityDisplay v-for="(community,index) in communities" :key="index"
      :community="community" :communityType="communityType"
      :editMode="editMode"/>
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
        communityType: String,
    },
    computed: {
        editMode() {
            if(this.$route.name === 'Manage') {
                return true;
            } else {
                return false;
            }
        }
    }

}
</script>

<style scoped>

</style>