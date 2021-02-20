<template>
  <div class="container">
      <div class="navigation-display">
          Communities
      </div>
      <div class="header">
          <h1>Communities</h1>
          <div class="settings-icon">
              <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
        </div>  
      </div>
      <div class="search-section">
          <input type="text" placeholder="Search for a community..."/>
          <div class="search-icon">
              <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
          </div>
      </div>
      <div class="community-filter-count">
          <p>10 Communities</p>
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
    name: 'IndividualCommunitiesPage',
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

.header h1 {
    font-size: 30px;
}

.header > .settings-icon {
    position: absolute;
    top: 20px;
    right: 15px;
    font-size: 35px;
    color: #7e7e7e;
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
    border-radius: 8px;
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
.community-filter-count {
    text-align: left;
}
.search-icon svg {
    margin: auto;
}
.communities-list {
    display: flex;
    flex-direction: column;
    text-align: left;
}
</style>