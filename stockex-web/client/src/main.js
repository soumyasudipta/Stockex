import Vue from 'vue'
import App from './App.vue'
import vuetify from "@/plugins/vuetify";
import Vuelidate from 'vuelidate'
import Chart from "chart.js";
import router from "@/router/router";
import { store } from './store/store.js'
const firebase =  require("./firebaseConfig")

Vue.use(Vuelidate)

Vue.config.productionTip = false

let app
// eslint-disable-next-line no-unused-vars
firebase.auth.onAuthStateChanged(user => {
    if (!app) {
        app = new Vue({
            el: '#app',
            vuetify,
            Chart,
            router,
            store,
            render: h => h(App)
        })
    }
})