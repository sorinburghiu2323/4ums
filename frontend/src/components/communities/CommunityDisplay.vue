<template>
  <div class="container">
      <div class="color-box" :class="{'my-communities': myCommunities}">
          
      </div>
      <div class="details">
          <div class="title">
              <p>{{community.name}}</p>
          </div>
          <div class="description">
              <p>{{community.description}}sdkjfkdjakbf asdjahbdhaasdasd asjdbhdasgasdvasdvajsdvh</p>              
          </div>
      </div>
  </div>
</template>

<script>
export default {
    name: 'CommunityDisplay',
    props: {
        community: Object,
        myCommunities: {
            default: false,
            type: Boolean,
        }
    }
}
</script>

<style scoped>
.container {
    cursor: pointer;
    display: flex;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 0px 3px 10px 0px;
    border: 1px solid black;
    height: 100px;
    border: none;
    border-radius: 25px;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%);
}
.color-box {
    height: 110px;
    width: 20px;
    border-radius: 25px 0px 0 25px;
    position: absolute;
}

.my-communities{
    background: rgb(52,235,233);
    background: linear-gradient(270deg, rgba(52,235,233,1) 0%, rgba(101,255,167,1) 35%);   
}

.details {
    margin: auto;
    margin-left: 25px;

}

.details p {
    margin: 0;
}

.details .title {
    font-size: 20px;
    height: 30%;
    margin-bottom: 4px;
}

.details .description {
    height: 70%;
    font-size: 15px;
    color: #7E7E7E;
}

.description p {
    overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 2; /* number of lines to show */
   -webkit-box-orient: vertical;
}

</style>
