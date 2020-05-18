<template>
    <v-app app>
        <h1>I m in My Account of {{ userProfile.name }}</h1>
    </v-app>
</template>

<script>
    import {mapState} from "vuex";

    export default {
        computed: {
            ...mapState(['userProfile', 'currentUser']),
        },
    }
</script>

<style scoped>

</style>