<template>
    <div class="container">
        <p class="title">Terms and conditions:</p>
        <p class="point">
            1. Upon registration, a user consents to the share of their personal data used for the application. 
            This includes: email address, name and whether or not the user is a teacher/lecturer. 
            This data can be used throughout the app.
        </p>
        <p class="point">
            2. The website uses cookies to store session data. By continuing to use the application, 
            the user consents to session cookies being stored to better improve their experience. This includes features as login, 
            most used communities and possible recommended communities.
        </p>
        <div>
            <p class="point">3. The user consents to their interaction with the website to be visible to other users:
            </p>
            <div class="subpoints">
                <p class="point">a. Posting in a community will make that post visible to all members in that specific community.</p>
                <p class="point">b. Liking a post or a comment in a community will make that like visible to all members in that specific community.</p>
                <p class="point">c. Commenting on a post in a community will make that comment visible to all members in that community. </p>
            </div>
        </div>

        <p class="point">
            4. Posting in a community will make that post visible to all members in that specific community.
        </p>
    
        <p class="point">
            5. Liking a post or a comment in a community will make that like visible to all members in that specific community.
        </p>

        <p class="point">
            6. Commenting on a post in a community will make that comment visible to all members in that community.
        </p>

        <p class="point">
            7. In addition to all data in (3) being visible to the members of the community, this data will also be able to be utilised 
            by the application owners in order to better improve user experience.
        </p>

        <p class="point">
            9. Upon logging out, all the session cookies are removed.
        </p>

        <p class="point">
            10. Upon deleting your account, the account becomes inactive so it cannot be used anymore. 
            The data left from the user (including any created communities,  posts, likes and further interaction) will still 
            be visible to other users because community interaction is vital to the use of the application, thus any content which 
            other users have interacted with will be kept. 
        </p>

        <p class="point">
            11. Upon deleting your account, your personal information will no longer be visible to other users 
            - including your profile and name tagged on any posts/comments/and other interactions. 
        </p>
  </div>
</template>

<script>
export default {
    name: 'TermsAndConditionsPopup'

}
</script>

<style scoped>

.container {
    width: inherit !important;
    background: black;
    display: flex;
    flex-direction: column;
    border-radius: 25px;
    box-shadow: 0px 3px 20px #D223AF;
    padding-bottom: 30px;
}

.point {
    padding: 3px;
    padding-left: 20px;
    text-align: left;
}

.subpoints{
    margin-left: 25px;
}

</style>