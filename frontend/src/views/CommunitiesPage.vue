<template>
  <div class="container" id="infinite">
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
      <div class="communities-list">
          <div class="filter">
                <button id="your-communities-btn" 
                @click="showAllCommunities = false;">
                Your communities</button>
                <button id="all-communities-btn"
                @click="showAllCommunities = true;">
                All communities</button>
          </div>

          <!--Communities user is a member of -->
          <CommunitiesList v-if="loadedCommunities && !showAllCommunities"
          :communities="myCommunities" :myCommunities="true"/>

          <!-- all Communities -->
          <CommunitiesList v-if="loadedCommunities && showAllCommunities"
          :communities="allCommunities" :myCommunities="false"/>

          <button v-if="loadMore" class="load-more-btn" @click="loadMoreCommunities">Load more</button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommunitiesList from '@/components/communities/CommunitiesList.vue'
export default {
    name: 'CommunitiesPage',
    components: {
        CommunitiesList,
    },
    watch: {
        showAllCommunities(newVal) {
            this.currentPage = 1;
            if(newVal === true) {
                this.loadedCommunities = false;
                this.myCommunities = [];
                this.getAllCommunities();
            }
            if(newVal === false) {
                this.loadedCommunities = false;
                this.allCommunities = [];
                this.getMyCommunities();
            }
        },
    },
    data() {
        return {
            loadedCommunities: false, 
            myCommunities: [],
            allCommunities: [],
            currentPage: 1,
            bottomOfPageReached: false,
            errorLoadingCommunities: false,
            showAllCommunities: false,
            loadMore: false,
        }
    },
    mounted() {
        this.getMyCommunities();
    },
    methods: {
        async getMyCommunities() {
            await axios.get('api/communities?type=memberof' , {params: {page: this.currentPage}})
            .then((response) => {
                this.loadedCommunities = false;
                for(var i = 0; i < response.data.data.length; i++) {
                    this.myCommunities.push(response.data.data[i]);
                }
                if(response.data.next_page != null) {
                    this.loadMore = true;
                } else {
                    this.loadMore = false;
                }
                this.loadedCommunities = true;
            }).catch((error) => {
                console.error(error);
                this.loadedCommunities = false;
            })
        },
        getAllCommunities() {
            axios.get('api/communities?type=all', {params: {page: this.currentPage}})
            .then((response) => {
                this.loadedCommunities = false;
                for(var i = 0; i < response.data.data.length; i++) {
                    this.allCommunities.push(response.data.data[i]);
                }
                if(response.data.next_page != null) {
                    this.loadMore = true;
                } else {
                    this.loadMore = false;
                }
                this.loadedCommunities = true;
            }).catch((error) => {
                console.error(error);
                this.loadedCommunities = false;
            })
        },
        loadMoreCommunities() {
            this.currentPage += 1;
            if(this.showAllCommunities) {
                this.getAllCommunities();
            } else {
                this.getMyCommunities();
            }
        }
    },

}
</script>

<style scoped>
.container {
    height: 100%;
}
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

.search-icon svg {
    margin: auto;
}
.communities-list {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.filter {
    display: flex;
    justify-content: center;
    margin: 20px;
}

.filter button {
    padding: 8px;
    margin: 5px;
    border-radius: 25px;
    border: none;
    outline: none;
    cursor: pointer;
    font-weight: 600;
}

#your-communities-btn {
    background: linear-gradient(270deg, rgba(52,235,233,1) 0%, rgba(101,255,167,1) 35%);
    box-shadow: 0px 5px 40px #268079;
}

#all-communities-btn {
    background: rgb(254,155,47);
    background: linear-gradient(90deg, rgba(254,155,47,1) 0%, rgba(254,101,15,1) 35%);
    box-shadow: 0px 5px 40px #C35456;
}

.load-more-btn {
    padding: 8px;
    margin: 5px;
    border-radius: 25px;
    border: none;
    outline: none;
    cursor: pointer;
    width: 150px;
    margin: auto;
    margin-bottom: 10px;
    font-weight: 600;
    background: rgb(254,155,47);
    background: linear-gradient(90deg, rgba(254,155,47,1) 0%, rgba(254,101,15,1) 35%);
    box-shadow: 0px 5px 40px #C35456;
}
</style>