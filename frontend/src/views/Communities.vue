<template>
  <div class="container">
      <div class="header">
          <h1>Communities</h1>
          <div class="settings-icon">
              <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
        </div>  
      </div>
      <div class="search-section">
          <input type="text" />
          <div class="search-icon">
              <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
          </div>
      </div>
      <div class="communities-list">
          <div class="title">
                <h1>Your communities</h1>
          </div>
          <CommunitiesList />
      </div>
      
  </div>
</template>

<script>
import CommunitiesList from '@/components/communities/CommunitiesList.vue'
export default {
    name: 'Communities',
    components: {
        CommunitiesList,
    }

}
</script>

<style scoped>
h1 {
    font-size: 20px;
}

.header {
    display: flex;
    justify-content: flex-start;
    
}

.header > .settings-icon {
    position: absolute;
    top: 20px;
    right: 15px;
    font-size: 30px;
}

.search-section {
    display: flex;
    width: 100%;

}

.search-section input {
    width: 100%;
    border: 1px solid black;
    height: 30px;
    border-radius: 8px;
}

.search-section > .search-icon {
    font-size: 30px;
    margin-left: 10px;
}

.communities-list {
    display: flex;
    flex-direction: column;
    text-align: left;
}
</style>