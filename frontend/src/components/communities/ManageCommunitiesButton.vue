<template>
    <div>
        <button
        id="circleButton"
        @click="navigateToManage()">
        <div class="curved-text"><img src="@/assets/manage-communities.svg"></div>
        <font-awesome-icon :icon="['fa', 'pencil-alt']"/>
        </button>
    </div>
</template>

<script>
export default {
    name: 'ManageCommunitiesButton',
    methods: {
        navigateToManage() {
            this.$router.push('manage');
        }
    }
}
</script>

<style scoped>
.curved-text {
    position: absolute;
    top: -10px;
    left: 0px;
}

.curved-text img {
  height: 12vh;
  transform: rotate(28deg);
}

#circleButton {
  border-radius: 50%;
  background: rgb(52, 235, 233);
  background: linear-gradient(180deg, rgba(52, 235, 233, 1) 0%, rgba(101, 255, 167, 1) 54%);
  height: 12vh;
  width: 12vh;
  position: fixed;
  bottom: 12vh;
  right: 0;
  font-size: 40px;
  font-weight: 600;
  border-width: 0;
  z-index: 1;
  box-shadow: 0px 3px 20px #34EBE9;
}

#circleButton p {
    font-size: 12px;
    margin: 0;
}
</style>
