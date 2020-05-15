import Vue from 'vue'
import Router from 'vue-router'
import firebase from "firebase";

import Home from "@/components/views/Home";
import Dashboard from "@/components/views/Dashboard";
import Stock from "@/components/views/Stock";
import SubStock from "@/components/views/SubStock";
import Forex from "@/components/views/Forex";
import MyAccount from "@/components/views/MyAccount";
import Login from "@/components/views/users/Login";
import Register from "@/components/views/users/Register";

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        // { path: '*', name: 'Home', component: Home},
        { path: '/', name: 'Home', component: Home, meta: { requiresAuth: true }},
        { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true }},
        { path: '/stock', name: 'Stocks', component: Stock, meta: { requiresAuth: true }},
        { path: '/stock/:id', name: 'SubStocks', component: SubStock, meta: { requiresAuth: true }},
        { path: '/forex', name: 'Forex', component: Forex, meta: { requiresAuth: true }},
        { path: '/myaccount', name: 'MyAccount', component: MyAccount, meta: { requiresAuth: true }},
        { path: '/register', name: 'Register', component: Register},
        { path: '/login', name: 'Login', component: Login},
    ]
})

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const currentUser = firebase.auth().currentUser;

    if (requiresAuth && !currentUser) next('login');
    else if (!requiresAuth && currentUser) next('home');
    else next();
});

export default router