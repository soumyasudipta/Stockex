//Main components
import Vue from 'vue'
import App from './App.vue'
import vuetify from "./plugins/vuetify";
import Vuelidate from 'vuelidate'

// Database and Router
import router from "./router/router";
import { store } from './store/store.js'
const firebase =  require("./database/FirebaseConfig")

// Fusion Chart
import VueFusionCharts from 'vue-fusioncharts';
import FusionCharts from 'fusioncharts';
import TimeSeries from 'fusioncharts/fusioncharts.timeseries';



Vue.use(Vuelidate)
// register VueFusionCharts component
Vue.use(VueFusionCharts, FusionCharts, TimeSeries);

Vue.config.productionTip = false

let app
// eslint-disable-next-line no-unused-vars
firebase.auth.onAuthStateChanged(user => {
    if (!app) {
        app = new Vue({
            el: '#app',
            vuetify,
            router,
            store,
            render: h => h(App)
        })
    }
})