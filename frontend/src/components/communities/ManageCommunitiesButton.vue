<template>
    <div>
        <button
        id="circleButton"
        @click="navigateToManage()">
        Manage Communities
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
#circleButton {
  border-radius: 50%;
  background: rgb(52,235,233);
  background: linear-gradient(180deg, rgba(52,235,233,1) 0%, rgba(101,255,167,1) 54%);
  height: 15vh;
  width: 15vh;
  position: fixed;
  bottom: 12vh;
  right: 0;
  font-size: 16px;
  font-weight: 600;
  border-width: 0;
  z-index: 1;
  box-shadow: 0px 3px 20px #34EBE9;
}
</style>