<template>
    <div>
        <button
        id="circleButton"
        @click="navigateToCreate()">
        <div class="curved-text"><img src="@/assets/create-community.svg"></div>
        <font-awesome-icon :icon="['fa', 'plus']"></font-awesome-icon>
        </button>
    </div>
</template>

<script>
export default {
    name: 'CreateCommunityButton',
    methods: {
        navigateToCreate() {
            this.$router.push({name:'CreateCommunity'});
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
  transform: rotate(20deg);
}

#circleButton {
  border-radius: 50%;
  background: rgb(210, 35, 175);
  background: linear-gradient(180deg, rgba(210, 35, 175, 1) 0%, rgba(227, 122, 247, 1) 75%);
  height: 12vh;
  width: 12vh;
  position: fixed;
  bottom: 12vh;
  right: 0;
  font-size: 40px;
  font-weight: 600;
  border-width: 0;
  z-index: 1;
  box-shadow: 0px 3px 20px #D223AF;
}


#circleButton p {
  font-size: 12px;
  margin: 0;
}
</style>
