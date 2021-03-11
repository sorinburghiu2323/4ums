<template>
  <div>
    <router-link class="nav-link" to="/manage">
      <p id="back">
        <font-awesome-icon :icon="['fas', 'arrow-left']" />
        Manage
      </p>
    </router-link>
    <div class="community-content">
      <div class="header">
        <h1>Leave a Community</h1>
        <div class="settings-icon">
          <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
        </div>
      </div>
    </div>
    Are you sure you want to leave {{ this.community.name }}?
    <CommunityDisplay
      style="text-align: left"
      :community="this.community"
      :communityType="'memberof'"
      :editMode="false"
    />
    <button id="leave-button" @click="leave()">Leave Community</button>
  </div>
</template>

<script>
import CommunityDisplay from "../components/communities/CommunityDisplay.vue";
import axios from "axios";
export default {
  name: "LeaveCommunity",
  mounted() {
    this.getCommunity();
  },
  methods: {
    leave() {
      axios.post("/api/communities/" + this.id + "/leave")
        .catch((error) => {
          console.error(error.response.data)
        })
      this.$router.push({
        name: "Manage",
      })
    },
    getCommunity() {
      axios
        .get("/api/communities/" + this.id)
        .then((response) => {
          this.community = {
            name: response.data.name,
            description: response.data.description,
            created_at: response.data.created_at,
            colour: response.data.colour,
            id: this.id,
          };
        })
        .catch((error) => {
          console.error(error.response.data);
        });
    },
  },
  data() {
    return {
      id: this.$route.params.id,
      community: {},
    };
  },
  components: {
    CommunityDisplay,
  },
};
</script>

<style>
#leave-button {
  background: linear-gradient(
    270deg,
    rgba(52, 235, 233, 1) 0%,
    rgba(101, 255, 167, 1) 35%
  );
  box-shadow: 0px 5px 40px #268079;
  padding: 8px;
  margin: 5px;
  border-radius: 25px;
  border: none;
  outline: none;
  cursor: pointer;
  font-weight: 600;
}
#back {
  text-align: left;
  margin-left: 0;
  color: #777779;
}
.community-content {
  display: flex;
  flex-direction: column;
}
.header {
  display: flex;
  justify-content: flex-start;
}
.header > .settings-icon {
  position: absolute;
  top: 20px;
  right: 15px;
  font-size: 35px;
  color: #7e7e7e;
}
</style>
