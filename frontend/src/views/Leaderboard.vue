<template>
  <div class="container">
    <div class="header">
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
    <div class="position">
      <div class="profile-pic"></div>
      <div class="position-text">
        <font-awesome-icon :icon="['fa', 'user']"></font-awesome-icon>
        <p>Your Position: {{ leaderboardPosition | ordinal_suffix }}</p>
      </div>
    </div>
    <div class="top-three" v-if="loaded">
      <div class="top">
        <p class="title">1st</p>
        <div
          class="first circle"
          @click="navigateToProfile(leaderboardUsers[0].id)"
        >
          <div class="crown">
            <font-awesome-icon :icon="['fa', 'crown']"></font-awesome-icon>
          </div>
          <p class="initials">
            {{ leaderboardUsers[0] | initials }}
          </p>
        </div>
        <div class="info">
          <p class="username">{{ leaderboardUsers[0].username }}</p>
          <p class="points">Points: {{ leaderboardUsers[0].points }}</p>
        </div>
      </div>

      <div class="top-two">
        <div class="second-place">
          <p class="title">2nd</p>
          <div
            class="second circle"
            @click="navigateToProfile(leaderboardUsers[1].id)"
          >
            <div class="medal">
              <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
            </div>
            <p class="initials">
              {{ leaderboardUsers[1] | initials }}
            </p>
          </div>
          <div class="info">
            <p class="username">{{ leaderboardUsers[1].username }}</p>
            <p class="points">Points: {{ leaderboardUsers[1].points }}</p>
          </div>
        </div>
        <div class="third-place">
          <p class="title">3rd</p>
          <div
            class="third circle"
            @click="navigateToProfile(leaderboardUsers[2].id)"
          >
            <div class="medal">
              <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
            </div>
            <p class="initials">
              {{ leaderboardUsers[2] | initials }}
            </p>
          </div>
          <div class="info">
            <p class="username">{{ leaderboardUsers[2].username }}</p>
            <p class="points">Points: {{ leaderboardUsers[2].points }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="leaderboard-table-container" v-if="loaded">
      <table class="table">
        <tr v-for="(user, index) in leaderboardUsers.slice(3)" :key="index">
          <td>{{ user.leaderboard_position | ordinal_suffix }}</td>
          <td>
            <p style="margin: 0;" @click="navigateToProfile(user.id)">
              {{ user.username }}
            </p>
          </td>
          <td class="points">Points: {{ user.points }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Leaderboard",
  filters: {
    ordinal_suffix(i) {
      var j = i % 10,
        k = i % 100;
      if (j == 1 && k != 11) {
        return i + "st";
      }
      if (j == 2 && k != 12) {
        return i + "nd";
      }
      if (j == 3 && k != 13) {
        return i + "rd";
      }
      return i + "th";
    },
    initials(user) {
      return user.first_name.charAt(0) + user.last_name.charAt(0);
    },
  },
  data() {
    return {
      leaderboardUsers: [],
      loaded: false,
      currentPage: 0,
      loadMore: false,
      leaderboardPosition: null,
    };
  },
  mounted() {
    // Fetch logged in user information
    this.getUserDetails();
    // Load first page of leaderboard user details
    this.loadMoreUsers();
    // Call scroll event function for infinite scrolling
    this.scroll();
  },
  methods: {
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight >
          document.body.scrollHeight;
        if (bottomOfWindow) {
          if (this.loadMore) {
            this.loadMoreUsers();
            this.loadMore = false;
          }
        }
      };
    },
    navigateToProfile(id) {
      this.$router.push({
        name: "User",
        params: {
          id: id,
        },
      });
    },
    loadMoreUsers() {
      // On page scroll to bottom of page, display next page of users
      this.currentPage += 1;
      axios
        .get("/api/users/leaderboard", { params: { page: this.currentPage } })
        .then((response) => {
          var i;
          for (i = 0; i < response.data.data.length; i++) {
            this.leaderboardUsers.push(response.data.data[i]);
          }
          if (response.data.next_page === null) {
            this.loadMore = false;
          } else {
            this.loadMore = true;
          }
          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getUserDetails() {
      axios
        .get("/api/users/me")
        .then((response) => {
          this.leaderboardPosition = response.data.leaderboard_position;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.header > .settings-icon {
  position: absolute;
  top: 20px;
  right: 15px;
  font-size: 35px;
  color: #7e7e7e;
  cursor: pointer;
}

.position-text {
  display: flex;
  color: #7e7e7e;
  font-size: 25px;
  margin-bottom: 50px;
}

.position-text p {
  font-size: 15px;
  margin: auto;
  margin-left: 20px;
}

.circle {
  height: 140px;
  width: 140px;
  border-radius: 100%;
  border: none;
  margin: auto;
  position: relative;
  display: flex;
}

.first {
  height: 150px;
  width: 150px;
}

.circle.first {
  background: rgb(254, 109, 19);
  background: linear-gradient(
    180deg,
    rgba(254, 109, 19, 1) 0%,
    rgba(254, 154, 46, 1) 66%
  );
}

.circle.second {
  background: rgb(140, 59, 254);
  background: linear-gradient(
    180deg,
    rgba(140, 59, 254, 1) 0%,
    rgba(177, 55, 255, 1) 66%
  );
}

.circle.third {
  background: rgb(211, 38, 177);
  background: linear-gradient(
    180deg,
    rgba(211, 38, 177, 1) 0%,
    rgba(226, 117, 242, 1) 66%
  );
}

.top {
  width: 100%;
}

.top-two {
  display: flex;
  justify-content: center;
}

.top-two .circle {
  margin: 20px;
  margin-top: 0px;
}

.top-two .title {
  font-size: 20px;
}

.initials {
  margin: auto;
  font-size: 60px;
  text-transform: uppercase;
}

.first .initials {
  font-size: 70px;
}

.title {
  margin: 0;
  font-size: 25px;
}

.info {
  display: flex;
  flex-direction: column;
  color: white;
  margin: 0;
}

.info p {
  font-size: 20px;
  margin: 0;
}

.points {
  font-size: 15px !important;
  color: #7e7e7e;
}

.medal {
  position: absolute;
  bottom: -15px;
  right: 3px;
  font-size: 35px;
}

.crown {
  position: absolute;
  top: -23px;
  left: -10px;
  font-size: 45px;
  transform: rotate(320deg);
  filter: drop-shadow(0px 0px 20px white);
}

.table {
  width: 100%;
  table-layout: fixed;
  text-align: left;
  margin-top: 40px;
  border-collapse: separate;
  border-spacing: 0px 5px;
}

.table td {
  text-overflow: ellipsis;
  overflow: hidden;
  border: none;
  padding: 0px 10px 0px 10px;
}

.table tr {
  height: 33px;
  font-size: 20px;
  background: #161626;
}

.table tr:hover {
  background: linear-gradient(
    270deg,
    rgba(52, 235, 233, 1) 0%,
    rgba(101, 255, 167, 1) 35%
  );
  color: #161626 !important;
}
</style>
