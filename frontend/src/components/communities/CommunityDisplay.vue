<template>
  <div class="container" @click="navigateToCommunity()">
    <div v-if="community.colour" :class="community.colour" class="color-box"></div>
    <div v-else class="color-box"></div>
    <div class="details">
      <div class="title">
        <p>{{ community.name }}</p>
      </div>

      <div v-if="editMode" class="editBtn">
        <button
          v-if="communityType === 'memberof'"
          class="leave"
          @click.stop.prevent="leaveCommunity()"
        >
          Leave
        </button>
        <button
          v-if="communityType === 'created'"
          class="delete"
          @click.stop.prevent="deleteCommunity()"
        >
          Delete
        </button>
      </div>

      <div class="description">
        <p>{{ community.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommunityDisplay",
  props: {
    community: Object,
    communityType: String,
    editMode: {
      default: false,
      type: Boolean,
    },
  },
  methods: {
    navigateToCommunity() {
      this.$router.push({
        name: "Community",
        params: {
          id: this.community.id,
        },
      });
    },
    leaveCommunity() {
      this.$root.$emit("updateCommunities");
    },
    deleteCommunity() {
      this.$root.$emit("updateCommunities");
    },
  },
};
</script>

<style scoped>
.container {
  cursor: pointer;
  display: flex;
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 0 3px 10px 0;
  height: 100px;
  border: none;
  border-radius: 25px;
  background: rgb(40, 44, 58);
  background: linear-gradient(
    90deg,
    rgba(40, 44, 58, 1) 0%,
    rgba(27, 30, 40, 1) 35%,
    rgba(8, 9, 11, 1) 100%
  );
  z-index: 999;
}
.color-box {
  height: 108px;
  width: 20px;
  border-radius: 25px 0 0 25px;
  position: absolute;
}

.orange {
  background: rgb(254,155,47);
  background: linear-gradient(90deg, rgba(254,155,47,1) 0%, rgba(254,101,15,1) 35%);
}
.blue {
  background: rgb(52, 235, 233);
  background: linear-gradient(
    270deg,
    rgba(52, 235, 233, 1) 0%,
    rgba(101, 255, 167, 1) 35%
  );
}
.purple {
  background: rgb(188, 98, 253);
  background: linear-gradient(270deg, rgb(144, 98, 253) 0%, rgb(149, 0, 255) 35%);
}

.details {
  margin: auto 0 auto 25px;
  padding-right: 10px;
  width: 100%;
  position: relative;
}

.details p {
  margin: 0;
}

.details .title {
  font-size: 19px;
  height: 30%;
  margin-top: 4px;
  margin-bottom: 4px;
  display: flex;
  justify-content: space-between;
  width: 80%;
}

.details .description {
  height: 70%;
  font-size: 15px;
  color: #7e7e7e;
}

.description p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* number of lines to show */
  -webkit-box-orient: vertical;
}

.editBtn {
  position: absolute;
  top: -22px;
  right: 20px;
}

.editBtn button {
  width: 100px;
  height: 25px;
  border-radius: 25px;
  text-align: center;
  font-weight: 600;
  border: none;
  outline: none;
  cursor: pointer;
}

.leave {
  background: linear-gradient(
    270deg,
    rgba(52, 235, 233, 1) 0%,
    rgba(101, 255, 167, 1) 35%
  );
}

.delete {
  background: rgb(254, 155, 47);
  background: linear-gradient(
    90deg,
    rgba(254, 155, 47, 1) 0%,
    rgba(254, 101, 15, 1) 35%
  );
}
</style>
