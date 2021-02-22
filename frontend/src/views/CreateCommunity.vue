<template>
  <div>
        <input v-model="message" placeholder="edit me">
        <p>Message is: {{ this.message }}</p>
  </div>
</template>

<script>
export default {
    name: 'CreateCommunity',
    data() {
        return {
            message: "",

        }
    }
}
</script>

<style>

</style>