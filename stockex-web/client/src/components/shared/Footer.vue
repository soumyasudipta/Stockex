<template>
    <v-footer>
        <v-spacer></v-spacer>
        <div>&copy; {{ new Date().getFullYear() }}</div>
    </v-footer>
</template>

<script>
    export default {
        data () {
            return {
                activeBtn: 1,
            }
        },
    }
</script>

<style scoped>

</style>