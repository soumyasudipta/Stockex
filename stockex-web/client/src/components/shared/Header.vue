<template>
    <v-app-bar app
            absolute
            color="grey darken-4"
            elevate-on-scroll
            dark
    >

        <v-toolbar-title>Stockex</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-btn @click="logout" v-if="currentUser">Logout</v-btn>
    </v-app-bar>
</template>

<script>
    import {mapState} from "vuex";

    const firebase =  require('../../database/FirebaseConfig');

    export default {
        data: () => ({
            drawer: false,
        }),
        methods: {
            logout () {
                firebase.auth.signOut().then(() => {
                    this.$store.dispatch('clearData')
                    this.$router.push('/login')
                }).catch(err => {
                    console.log(err)
                })
            }
        },
        computed: {
            ...mapState(['currentUser'])
        }
    }
</script>

<style scoped>

</style>