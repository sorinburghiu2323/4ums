<template>
  <div class="container">
    <p id="back" @click="goBack()">
      <font-awesome-icon :icon="['fas', 'arrow-left']" />
      Back
    </p>
    <div id="top-buttons">
      <div
        class="settings-icon"
        @click="
          $router.push({
            name: 'Settings',
          })
        "
      >
        <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
      </div>
    </div>
    <div id="profilePicture" style="margin-bottom: 0px;">
      <p>{{ this.initials }}</p>
    </div>
    <div id="mainProfileInfo">
      <p class="info" style="font-size: 32px; margin-bottom: 0px;">
        {{ this.username }}
      </p>
      <p class="info">{{ this.firstName + " " + this.secondName }}</p>
      <p class="info">
        <font-awesome-icon :icon="['fas', 'star']" /> Points: {{ this.points }}
        <a v-if="this.leaderboardPosition">
          <font-awesome-icon :icon="['fas', 'trophy']" />
          Position:
          {{ this.leaderboardPosition }}
        </a>
      </p>
    </div>
    <p style="width: 100%; text-align: left;"><u>Bio:</u></p>
    <p
      style="position: absolute; margin: auto; margin-top: 10vh;"
      v-if="this.bio === ''"
    >
      {{ this.bio }}
    </p>
    <p v-else>
      This user hasn't filled out a bio yet!
    </p>
    <p style="width: 100%; text-align: left;"><u>Top Communities:</u></p>
    <div class="communities-list">
      <CommunitiesList
        :communities="communities"
        :myCommunities="false"
        communityType="memberof"
      />
    </div>
    <p style="width: 100%; text-align: left;"><u>Engagement Per Week:</u></p>
    <div style="padding-top: 5vh;">
      <div v-if="!displayGraph">No data yet!</div>
      <div v-else>
        <div id="graph">
          <VueBarGraph
            :points="this.leaderboardInfo"
            :height="200"
            :barColor="'#3aeddf'"
            :use-custom-labels="true"
            :customLabels="[
              'This week',
              'Last week',
              '2 Weeks Ago',
              '3 Weeks Ago',
            ]"
            :showYAxis="true"
            :textColor="'white'"
            :textAltColor="'white'"
            :showXAxis="true"
            :showValues="true"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import VueBarGraph from "vue-bar-graph";
import CommunitiesList from "../components/communities/CommunitiesList.vue";

export default {
  components: {
    VueBarGraph,
    CommunitiesList,
  },
  mounted() {
    this.getUserDetails();
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    getWidth() {
      return (
        Math.max(
          document.body.scrollWidth,
          document.documentElement.scrollWidth,
          document.body.offsetWidth,
          document.documentElement.offsetWidth,
          document.documentElement.clientWidth
        ) / 1.5
      );
    },
    getUserDetails() {
      axios
        .get("/api/users/" + this.$route.params.id)
        .then((response) => {
          this.firstName = response.data.first_name;
          this.secondName = response.data.last_name;
          this.username = response.data.username;
          this.isTeacher = response.data.is_teacher;
          this.leaderboardPosition = response.data.leaderboard_position;
          this.points = response.data.points;
          var recents = response.data.graphs.recent;
          this.leaderboardInfo = [
            recents[0].points,
            recents[1].points,
            recents[2].points,
            recents[3].points,
          ];
          if (
            JSON.stringify(this.leaderboardInfo) == JSON.stringify([0, 0, 0, 0])
          ) {
            this.displayGraph = false;
          }
          for (
            var i = 0;
            i < response.data.graphs.top_communities.length;
            i++
          ) {
            this.communities.push(
              response.data.graphs.top_communities[i].community
            );
          }
          this.initials =
            this.firstName.substring(0, 1) + this.secondName.substring(0, 1);
          this.bio = response.data.descrtiption;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  data() {
    return {
      id: 0,
      username: "",
      firstName: "",
      secondName: "",
      isTeacher: false,
      points: 0,
      initials: "",
      leaderboardPosition: 0,
      leaderboardInfo: [],
      communities: [],
      bio: "",
      displayGraph: true,
      labels: ["This week", "Last week", "2 Weeks Ago", "3 Weeks Ago"],
    };
  },
};
</script>

<style scoped>
.communities-list {
  display: flex;
  flex-direction: column;
  text-align: left;
}

#mainProfileInfo {
  width: 100%;
  height: 15vh;
  text-align: center;
}

.container {
  z-index: -1;
  margin-top: 50px;
}

#back {
  position: absolute;
  text-align: left;
  top: 0;
}

#profilePicture {
  width: 100px;
  height: 100px;
  position: relative;
  border-radius: 50%;
  background: linear-gradient(to bottom, #8939fc, #ab35f3);
  display: flex;
  text-align: center;
  margin: auto;
}

#profilePicture p {
  font-size: 50px;
  margin: auto;
  text-transform: uppercase;
}

#graph {
  margin-top: 0;
}

.settings-icon {
  font-size: 35px;
  color: #7e7e7e;
  position: relative;
  cursor: pointer;
}

#top-buttons {
  position: absolute;
  top: 20px;
  right: 15px;
  font-size: 35px;
  color: #7e7e7e;
  display: flex;
  justify-content: space-around;
}
</style>
