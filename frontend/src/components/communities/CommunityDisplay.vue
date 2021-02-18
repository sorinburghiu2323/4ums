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
    display: flex;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 10px 3px 10px 3px;
    border: 1px solid black;
    height: 100px;
    
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
