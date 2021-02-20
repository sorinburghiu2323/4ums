<template>
  <div class="container">
      <div class="picture">
          
      </div>
      <div class="details">
          <div class="title">
              <p>Networks and security</p>
          </div>
          <div class="description">
              <p>ECM2433</p>
              
          </div>
      </div>
  </div>
</template>

<script>
export default {
    name: 'CommunityDisplay'
}
</script>

<style scoped>
.container {
    cursor: pointer;
    display: flex;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 10px 3px 10px 3px;
    border: 1px solid black;
    height: 100px;
    border: none;
    border-radius: 25px;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%);
}
.picture {
    height: 50px;
    width: 50px;
    border: 1px solid black;
    margin: auto;
    margin-left: 5px;
    margin-right: 10px;
}

.details {
    margin: auto;
    margin-left: 0;

}

.details p {
    margin: 0;
}

</style>
