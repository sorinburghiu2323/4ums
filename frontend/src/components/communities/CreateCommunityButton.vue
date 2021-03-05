<template>
    <div>
        <button
        id="circleButton"
        @click="navigateToCreate()">
        Create Community
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
#circleButton {
    border-radius: 50%;
    background: rgb(210,35,175);
    background: linear-gradient(180deg, rgba(210,35,175,1) 0%, rgba(227,122,247,1) 75%);
    height: 15vh;
    width: 15vh;
    position: fixed;
    bottom: 12vh;
    right: 0;
    font-size: 16px;
    font-weight: 600;
    border-width: 0;
    z-index: 1;
    box-shadow: 0px 3px 20px #D223AF;
}
</style>