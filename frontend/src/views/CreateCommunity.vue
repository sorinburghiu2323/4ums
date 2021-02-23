<template>
    <div>
        <router-link class="nav-link" to="../communities">
        <p id="back"><font-awesome-icon :icon="['fas', 'arrow-left']"/> Communities</p>
        </router-link>
        <p id="pageTitle">Create a<br>Community</p><br>
        <div v-if="createVisible">      
            <input class="inputBox" v-model="name" placeholder="Write a community title (max 25 characters)..." maxlength="25"><br>
            <br>
            <textarea class="inputBox" id="descriptionBox" v-model="description" placeholder="Write a community description..."></textarea>
            <p id="label">Choose a colour</p>
            <div id="colourSelect">
                <button id="blueButton" v-on:click='setColour("blue")'></button>
                <button id="orangeButton" v-on:click='setColour("orange")'></button>
                <button id="purpleButton" v-on:click='setColour("purple")'></button>
            </div>
            <button id="preview" v-on:click="preview()">Preview</button>
        </div>
        <div v-if="!this.createVisible">
            <div id="previewDiv">
                <p id="previewTitle">{{ this.name }}</p>
                <p id="previewDesc">{{ this.description }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: 'CreateCommunity',
    methods: {
        setColour: function(colour) {
            for (var i=0; i<3; i++) {
                document.getElementById(this.colours[i]+"Button").style = "";
            }
            document.getElementById(colour+"Button").style = "border-color: white; border-width: 1vh;";
            this.colour = colour;
            this.hexCode = this.hex[this.colours.indexOf(colour)];
        },
        preview: function() {
            this.createVisible = false;
            console.log(this.hexCode);
        },
        submit: function() {
            axios.post("/api/communities", {
                name: this.name,
                description: this.description
            }).then((response) => {
                console.log(response)
            }).catch((error) => {
                console.log(error)
            })
        }
    },
    data() {
        return {
            name: "",
            description: "",
            colour: "",
            colours: ["blue", "orange", "purple"],
            hex: ["#4af4cb", "#fa7e1f", "#a038fe"],
            hexCode: "#4af4cb",
            createVisible: true
        }
    },
    computed: {
        cssProps() {
            return {
                '--hex': this.hexCode
            }
        }
    }
}
</script>

<style>
#previewDesc {
    color: #4d4f56;
}

#previewTitle {
    color: white;
    padding-bottom: 2vh;
    font-size: 3vh;
}

#previewDiv {
    background-image: var(--hex);/*linear-gradient(to right, #232733, #1c1f29);*/
    border-radius: 15px;
    height: 15vh;
    width: 75%;
    margin: auto;
    left: 20vh;
    padding: 2vh;
    text-align: left;
    padding-left: 6vh;
    font-family: 'Trebuchet MS';
    border-width: 2vh;
    border-color: var(--hex);
}

#label {
    color: white;
    font-family: 'Trebuchet MS';
    text-align: left;
    padding: 2vh;
}

#preview {
    border-radius: 15px;
    width: 75%;
    height: 7.5%;
    font-family: 'Trebuchet MS';
    color: black;
    background-image: linear-gradient(to right, #348be9, #65ffa7);
    padding: 1vh;
}

#blueButton {
    border-radius: 50%;
    background-color: #4af4cb;
    height: 5vh;
    width: 5vh;
    margin: 1vh;
}

#orangeButton {
    border-radius: 50%;
    background-color: #fa7e1f;
    height: 5vh;
    width: 5vh;
    margin: 1vh;
}

#purpleButton {
    border-radius: 50%;
    background-color: #a038fe;
    height: 5vh;
    width: 5vh;
    margin: 1vh;
}

#colourSelect {
    display: flex;
    padding: 2vh;
}

#back {
    text-align: left;
    margin-left: 2vh;
    padding-top: 2vh;
    color: #777779;
}

#descriptionBox {
    height: 25vh;
}

#pageTitle {
    color: white;
    text-align: left;
    font-size: 4vh;
    font-family: 'Trebuchet MS';
    margin-left: 2vh;
    padding-top: 2vh;
}

::placeholder {
    color: white;

}

.fieldDesc {
    font-family: 'Trebuchet MS';
}

.inputBox {
    width: 99%;
    border: 0;
    color: white;
    background-image: linear-gradient(to right, #262b38, #1d2029);
    font-family: 'Trebuchet MS';
    min-height: 5vh;
    padding-left: 2vh;
    padding-top: 2vh;
    padding-bottom: 2vh;
}

.innerText {
    color: white;
}
</style>