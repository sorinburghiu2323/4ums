<template>
  <div class="container">
    <div id="top-buttons">
      <div class="edit-icon backgroundSquare" @click="edit()">
        <font-awesome-icon :icon="['fas', 'pencil-alt']"  />
      </div>
      <div class="share-icon backgroundSquare">
        <font-awesome-icon :icon="['fas', 'share']"></font-awesome-icon>
      </div>
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
    <div id="info">
      <div id="profilePicture">
        <p>{{ this.initials }}</p>
      </div>
      <div id="mainProfileInfo">
        <p class="info" style="font-size: 32px; margin-bottom: -10px;">
          {{ this.username }}
        </p>
        <p class="info">{{ this.firstName + " " + this.secondName }}</p>
        <p class="info">
          <font-awesome-icon :icon="['fas', 'star']" style="color:grey" />
          Points: {{ this.points }}
          <a v-if="this.leaderboardPosition">
            <font-awesome-icon :icon="['fas', 'trophy']" style="color:grey" />
            Position:
            {{ this.leaderboardPosition }}
          </a>
        </p>
      </div>
      <div class="bio">
        <p style="width: 100%; text-align: left; margin-top:-10px;">
          Bio
        </p>
        <div class="lines"></div>
        <div>
          <p v-if="this.bio !== ''" style="padding-top: 0">
            {{ this.bio }}
          </p>
          <p v-else>
            You haven't filled out a bio yet. Click the
            <font-awesome-icon
              :icon="['fas', 'pencil-alt']"
              style="color:grey"
            />
            button to make one!
          </p>
        </div>
      </div>
      <div class="comm">
        <p style="width: 100%; text-align: left;">Top Communities</p>
        <div class="lines"></div>
      </div>
      <div class="communities-list">
        <CommunitiesList
          :communities="communities"
          :communityType="'memberof'"
          :myCommunities="false"
        />
      </div>
      <div class="engage">
        <p style="width: 100%; text-align: left;">Engagement Per Week:</p>
        <div class="lines"></div>
      </div>
      <div>
        <div v-if="!displayGraph">No data yet!</div>
        <div v-else>
          <div id="graph">
            <VueBarGraph
              :barColor="'#3aeddf'"
              :customLabels="[
                'This week',
                'Last week',
                '2 Weeks Ago',
                '3 Weeks Ago',
              ]"
              :height="200"
              :points="this.leaderboardInfo"
              :showValues="true"
              :showXAxis="true"
              :showYAxis="true"
              :textAltColor="'white'"
              :textColor="'white'"
              :use-custom-labels="true"
              :width="widthCalc()"
            />
          </div>
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
    goToSettings() {
      this.$router.push({
        name: "Settings",
      });
    },
    edit() {
      this.$router.push({
        name: "EditProfile",
      });
      this.getUserDetails();
    },
    widthCalc() {
      return window.innerWidth - 100;
    },
    getUserDetails() {
      axios
        .get("/api/users/me")
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
          this.bio = response.data.description;
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
#info {
  position: relative;
  margin-top: 60px;
}

#top-buttons {
  position: absolute;
  right: 15px;
  top: 10px;
  display: flex;
  justify-content: space-around;
  padding: 2px;
}

.settings-icon {
  font-size: 35px;
  top: 5px;
  right: 75px;
  color: #7e7e7e;
  cursor: pointer;
  margin: auto;
}

.edit-icon {
  font-size: 32px;
  display: flex;
  top: 8px;
  right: 70px;
  color: black;
  border-radius: 10px;
}

.backgroundSquare {
  margin-right: 10px;
  padding: 10px;
  border-radius: 15px;
  background: linear-gradient(45deg, #5ffcaf, #39eade);
  box-shadow: 0 0 10px #4cf3c7;
}

.share-icon {
  font-size: 32px;
  display: flex;
  top: 6px;
  right: 90px;
  background: none;
  color: black;
  border-radius: 10px;
}

.share-icon.backgroundSquare {
  background: linear-gradient(45deg, #1262f4, #0379e9);
  box-shadow: 0 0 10px #0b6eef;
}

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

.bio .lines {
  border: 1px solid #4f4c55;
  position: relative;
  top: -25px;
  left: 20px;
  margin: 10px;
  width: calc(100% - 30px);
  height: 0;
  color: black;
}

.comm .lines {
  border: 1px solid #4f4c55;
  position: relative;
  top: -25px;
  left: 120px;
  margin: 10px;
  width: calc(100% - 130px);
  height: 0;
  color: black;
}

.engage .lines {
  border: 1px solid #4f4c55;
  position: relative;
  top: -25px;
  left: 160px;
  margin: 10px;
  width: calc(100% - 170px);
  height: 0;
  color: black;
}

#profilePicture {
  width: 120px;
  height: 120px;
  position: relative;
  border-radius: 50%;
  top: 20px;
  background: linear-gradient(to bottom, #8a3afe, #b237fe);
  display: flex;
  text-align: center;
  margin: auto;
  box-shadow: 0 0 30px #9e39fe;
}

#profilePicture p {
  font-size: 50px;
  margin: auto;
  text-transform: uppercase;
}

#graph {
  margin-top: 0;
}
</style>
