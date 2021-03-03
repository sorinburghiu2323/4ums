<template>
  <div id="infinite" class="container">
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
      <input placeholder="Search for a community..." type="text"/>
      <div class="search-icon">
        <font-awesome-icon :icon="['fas', 'search']"></font-awesome-icon>
      </div>
    </div>
    <div class="communities-list">
      <div class="filter">
        <button id="your-communities-btn"
                :class="{'active': !showAllCommunities}"
                @click="showAllCommunities = false;">
          Your communities
        </button>
        <button id="all-communities-btn"
                :class="{'active': showAllCommunities}"
                @click="showAllCommunities = true;">
          Other communities
        </button>
      </div>

      <!--Communities user created-->
      <p v-if="!showAllCommunities">Created by you: </p>
      <CommunitiesList v-if="loadedCommunities && !showAllCommunities"
                       :communities="createdCommunities" communityType="created"/>

      <!--Communities user is a member of -->
      <p v-if="!showAllCommunities">Communities you have joined: </p>
      <CommunitiesList v-if="loadedCommunities && !showAllCommunities"
                       :communities="myCommunities" communityType="memberof"/>

      <!-- all Communities -->
      <CommunitiesList v-if="loadedCommunities && showAllCommunities"
                       :communities="allCommunities" communityType="all"/>

      <ManageCommunitiesButton v-if="showManageButton && !showAllCommunities"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommunitiesList from '@/components/communities/CommunitiesList.vue'
import ManageCommunitiesButton from '@/components/communities/ManageCommunitiesButton.vue'

export default {
    name: 'CommunitiesPage',
    components: {
      CommunitiesList,
      ManageCommunitiesButton,
    },
    watch: {
      showAllCommunities(newVal) {
        this.currentPage = 1;
        if (newVal === true) {
          this.loadedCommunities = false;
          this.myCommunities = [];
          this.createdCommunities = [];
          this.getAllCommunities();
        }
        if (newVal === false) {
          this.loadedCommunities = false;
          this.allCommunities = [];
          this.getMyCommunities();
          this.getCreatedCommunities();
          this.loadMore = false;
        }
      },
    },
    data() {
        return {
          loadedCommunities: false,
          myCommunities: [],
          allCommunities: [],
          createdCommunities: [],
          currentPage: 1,
          bottomOfPageReached: false,
          errorLoadingCommunities: false,
          showAllCommunities: false,
          loadMore: false,
          showManageButton: true,
        }
    },
    mounted() {
      this.getMyCommunities();
      this.getCreatedCommunities();
      this.$root.$on('updateCommunities', () => {
        this.myCommunities = [];
        this.allCommunities = [];
        this.getMyCommunities();
        this.getCreatedCommunities();
      });

      this.scroll();
    },
    methods: {
      scroll() {
        window.onscroll = () => {
          let bottomOfWindow = document.documentElement.scrollTop +
              window.innerHeight > document.body.scrollHeight - 200;
          if (bottomOfWindow) {
            if (this.loadMore) {
              this.loadMoreCommunities();
              this.loadMore = false;
            }
            this.showManageButton = false;
          } else {
            this.showManageButton = true;
          }
        }
      },
      getMyCommunities() {
        axios.get('api/communities?type=memberof', {params: {page: 'all'}})
            .then((response) => {
              this.loadedCommunities = false;
              for (var i = 0; i < response.data.data.length; i++) {
                this.myCommunities.push(response.data.data[i]);
              }
              this.loadedCommunities = true;
            }).catch((error) => {
          console.error(error);
          this.loadedCommunities = false;
        })
      },
      getCreatedCommunities() {
        axios.get('api/communities?type=created', {params: {page: 'all'}})
            .then((response) => {
              this.loadedCommunities = false;
              for (let i = 0; i < response.data.data.length; i++) {
                this.createdCommunities.push(response.data.data[i]);
              }
              this.loadedCommunities = true;
            }).catch((error) => {
          console.error(error);
          this.loadedCommunities = false;
        })
      },
      getAllCommunities() {
        axios.get('api/communities?type=other', {params: {page: this.currentPage}})
            .then((response) => {
              this.loadedCommunities = false;
              for (let i = 0; i < response.data.data.length; i++) {
                this.allCommunities.push(response.data.data[i]);
              }
              this.loadMore = response.data["next_page"] != null;
              this.loadedCommunities = true;
            }).catch((error) => {
          console.error(error);
          this.loadedCommunities = false;
        })
      },
      loadMoreCommunities() {
        this.currentPage += 1;
        this.getAllCommunities();
      }
    },

}
</script>

<style scoped>
.container {
  margin: 10px;
  height: 100%;
}
h1 {
    font-size: 20px;
}

.header {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 30px;
}

.header h1 {
  margin-top: 50px;
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
  height: 46px;
  font-size: 15px;
  padding-left: 10px;
  color: white;
  outline: none;
  font-weight: 600;
  border-radius: 25px;
  border: none;
  background: rgb(40, 44, 58);
  background: linear-gradient(90deg, rgba(40, 44, 58, 1) 0%, rgba(27, 30, 40, 1) 35%, rgba(8, 9, 11, 1) 100%);
}

.search-section > .search-icon {
  font-size: 28px;
  height: 29px;
  padding: 10px;
  border-radius: 15px;
  position: relative;
  color: black;
  margin: 10px;
  display: flex;
  cursor: pointer;
  background: rgb(138, 59, 254);
  background: linear-gradient(225deg, rgba(138, 59, 254, 1) 11%, rgba(180, 55, 255, 1) 49%);
}

.search-icon svg {
  margin-top: -9px;
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
  background: linear-gradient(270deg, rgba(52, 235, 233, 1) 0%, rgba(101, 255, 167, 1) 35%);
  box-shadow: 0px 5px 40px #268079;
}

#all-communities-btn {
  background: rgb(254, 155, 47);
  background: linear-gradient(90deg, rgba(254, 155, 47, 1) 0%, rgba(254, 101, 15, 1) 35%);
  box-shadow: 0px 5px 40px #C35456;
}

.active {
  border: 3px solid white !important;
}
</style>