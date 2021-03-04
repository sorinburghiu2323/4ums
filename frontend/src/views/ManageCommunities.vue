<template>
    <div class="container">
        <router-link class="nav-link" to="/communities">
            <p id="back">
            <font-awesome-icon :icon="['fas', 'arrow-left']"/>
            Communities
            </p>
        </router-link>
        <div class="header">
            <h1>Manage Communities</h1>
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
            <!--Communities user created-->
            <p>Created by you: </p>
            <CommunitiesList v-if="loadedCommunities"
            :communities="createdCommunities" communityType="created"/>

            <!--Communities user is a member of -->
            <p>Communities you have joined: </p>
            <CommunitiesList v-if="loadedCommunities"
            :communities="myCommunities" communityType="memberof"/>
        </div>
        <CreateCommunityButton v-if="showCreateButton" />
    </div>
</template>

<script>
import axios from 'axios'
import CommunitiesList from '@/components/communities/CommunitiesList.vue'
import CreateCommunityButton from '@/components/communities/CreateCommunityButton.vue'

export default {
    name: 'ManageCommunities',
    components: {
        CommunitiesList,
        CreateCommunityButton,
    },
    data() {
        return {
            loadedCommunities: false, 
            myCommunities: [],
            createdCommunities: [],
            showCreateButton: true,
        }
    },
    mounted() {
        this.getMyCommunities();
        this.getCreatedCommunities();
        this.scroll();
    },
    methods: {
        scroll() {
            window.onscroll = () => {
                let bottomOfWindow = document.documentElement.scrollTop +
                    window.innerHeight > document.body.scrollHeight;
                if (bottomOfWindow) {
                    this.showCreateButton = false;
                } else {
                    this.showCreateButton = true;
                }
            }
        },
        getMyCommunities() {
            axios.get('api/communities?type=memberof' , {params: {page: 'all'}})
            .then((response) => {
                this.loadedCommunities = false;
                for(var i = 0; i < response.data.data.length; i++) {
                    this.myCommunities.push(response.data.data[i]);
                }
                this.loadedCommunities = true;
            }).catch((error) => {
                console.error(error);
                this.loadedCommunities = false;
            })
        },
        getCreatedCommunities() {
            axios.get('api/communities?type=created' , {params: {page: 'all'}})
            .then((response) => {
                this.loadedCommunities = false;
                for(var i = 0; i < response.data.data.length; i++) {
                    this.createdCommunities.push(response.data.data[i]);
                }
                this.loadedCommunities = true;
            }).catch((error) => {
                console.error(error);
                this.loadedCommunities = false;
            })
        },
    }
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
  margin-bottom: 30px;
  line-height: 30px;
  width: 50%;
  text-align: left;
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
  margin: auto;
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
  margin: auto;
}
.communities-list {
    display: flex;
    flex-direction: column;
    text-align: left;
}

#back {
    text-align: left;
}
</style>

