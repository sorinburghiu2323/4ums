<template>
  <div class="container" @click="navigateToPost()">
        <div class="details">
            <div class="title">
                <p>{{post.title}}</p>
            </div>
            <div class="description">
                <p>{{post.description}}</p>              
            </div>
        </div>
        <div class="likes">
            <div class="like-icon">
                <font-awesome-icon :icon="['fa', 'thumbs-up']"></font-awesome-icon>
            </div>
            <div class="like-count">{{post.likes_num}}</div>
        </div>
        <div class="author">
            <p>Authored by <span class="author-name">{{post.user.username}}</span></p>
        </div>
  </div>
</template>

<script>
export default {
    name: 'Post',
    props: {
        post: Object,
    },
    methods: {
        navigateToPost() {

        },
    }

}
</script>

<style scoped>
.container {
    cursor: pointer;
    display: flex;
    flex-direction: column;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 120px;
    padding: 0px 3px 10px 0px;
    border: 1px solid black;
    height: 100px;
    border: none;
    border-radius: 25px;
    background: rgb(40,44,58);
    background: linear-gradient(90deg, rgba(40,44,58,1) 0%, rgba(27,30,40,1) 35%, rgba(8,9,11,1) 100%);
    position: relative;
}

.details {
    margin: auto;
    margin-left: 25px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.details p {
    margin: 0;
}

.details .title {
    margin-bottom: 4px;
    font-size: 18px;
}

.title p {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2; /* number of lines to show */
    -webkit-box-orient: vertical;
    text-align: left;
}

.details .description {
    height: 70%;
    font-size: 15px;
    color: white;
}

.description p {
    overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 3; /* number of lines to show */
   -webkit-box-orient: vertical;
   text-align: left;
}

.likes {
    display: flex;
    margin-left: 25px;
}
.like-icon {
    font-size: 20px;
}
.like-count {
    margin-left: 10px;
    font-size: 20px;
    margin: auto;
    margin-left: 10px;
}
.author {
    position: absolute;
    bottom: 0;
    right: 0;
    color: #7e7e7e;
    font-style: italic;
    margin-right: 10px;
}

.author-name {
    text-decoration: underline;
}
</style>