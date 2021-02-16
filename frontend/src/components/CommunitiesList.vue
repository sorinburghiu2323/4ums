<template>
  <div class="container">
      {{userId}}
      <div class="community">
           <p>1</p>
      </div>
      <div class="community" id="box">
           2
      </div>
      <div class="community">
           3
      </div>
      <div class="community">
           4
      </div>

  </div>
</template>

<script>
export default {
    name: 'CommuntiesList',
    props: {
        userId: Number,
    },

}
</script>

<style>

.container {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;

}
.community {
    border: 1px solid #84beea; 
    height: 90px;
    width: 40px;
    
    display: flex;
}

.community > p {
    margin: auto;
}

#box {
    position: absolute; 
    top: 0;
    right: 0;
}
</style>