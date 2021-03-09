<template>
    <div>
        <router-link class="nav-link" to="/communities">
        <p id="back">
          <font-awesome-icon :icon="['fas','arrow-left']"/>
          Back
        </p>
        </router-link>
        <div class="header">
            <h1>Settings</h1>
        </div>
        <div>
            SignOut
        </div>
        <div>
            Privacy Settings
            Display (publically) your leader baord position.
            
        </div>
        <div>
            Delete Your Account
        </div>





    </div>
    
</template>

<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
})
</script>

<style scoped>
#back {
  text-align: left;
  margin-left: 2vh;
  padding-top: 2vh;
  color: #777779;
}

</style>
