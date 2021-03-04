<template>
    <div class="container">
        <div class="header">
            <div class="settings-icon">
                <font-awesome-icon :icon="['fas', 'cog']"></font-awesome-icon>
            </div>
        </div>
        <div class="position">
            <div class="profile-pic">

            </div>
            <div class="position-text">
                <p>Your Position: </p>
            </div>
        </div>
        <div class="top-three">
            <div class="top">
                <div class="first circle" /> 
                <div class="info">
                    <p class="username">Username</p>
                    <p class="points">Points: 103</p>
                </div>    
            </div>
            
            <div class="top-two">
                <div class="second-place">
                    <div class="second circle">
                    <div class="medal">
                        <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
                    </div>
                    </div>
                    <div class="info">
                        <p class="username">Username</p>
                        <p class="points">Points: 103</p>
                    </div>
                    
                </div>
                <div class="third-place">
                    <div class="third circle">
                    <div class="medal">
                        <font-awesome-icon :icon="['fa', 'medal']"></font-awesome-icon>
                    </div>
                    </div>
                    <div class="info">
                        <p class="username">Username</p>
                        <p class="points">Points: 103</p>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Leaderboard'

}
</script>

<style scoped>

.circle {
    height: 140px;
    width: 140px;
    border-radius: 100%;
    border: none;
    background: green;
    margin: auto;
    position: relative;
}

.first {
    height: 150px;
    width: 150px;
}

.top {
    width: 100%;
}

.top-two {
    display: flex;
    justify-content: center;
}

.top-two .circle {
    margin: 20px;
}

.info {
    display: flex;
    flex-direction: column;
    color: white;
    margin: 0;
}

.info p {
    font-size: 20px;
    margin: 0;
}

.info .points {
    font-size: 15px;
    color: #7e7e7e;
}

.medal {
    position: absolute;
    bottom: -15px;
    right: 3px;
    font-size: 35px;
}

</style>