<template>
    <v-navigation-drawer app
            v-model="drawer"
            :mini-variant.sync="mini"
            permanent
             color="grey darken-4"
             dark
    >
        <v-list-item class="px-2">
            <v-list-item-avatar>
                <v-img :src='user.avatar' ></v-img>
            </v-list-item-avatar>

            <v-list-item-title>{{ userProfile.name }}</v-list-item-title>

            <v-btn
                    icon
                    @click.stop="mini = !mini"
            >
                <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
        </v-list-item>


        <v-list dense>
            <v-list-item
                    v-for="item in items"
                    :key="item.title"
                    link
                    :to="item.to"
                    style="padding: 10px 15px;"
            >
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
    import { mapState } from 'vuex'
    // const firebase = require("@/firebaseConfig");

    export default {
        data () {
            return {
                drawer: true,
                user: { name: 'Soumya Sudipta', avatar: 'https://randomuser.me/api/portraits/men/85.jpg' },
                items: [
                    { title: 'Home', icon: 'mdi-home', to: '/' },
                    { title: 'Dashboard', icon: 'mdi-view-dashboard', to:'/dashboard' },
                    { title: 'Stocks', icon: 'mdi-chart-areaspline', to:'/stock' },
                    { title: 'Forex', icon: 'mdi-cash-multiple', to:'/forex' },
                    { title: 'My Account', icon: 'mdi-account', to:'/myaccount' },
                ],
                mini: true,
            }
        },
        computed: {
            ...mapState(['userProfile', 'currentUser']),
        },
    }
</script>

<style scoped>

</style>