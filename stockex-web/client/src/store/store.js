import Vue from 'vue'
import Vuex from 'vuex'
const firebase = require('../firebaseConfig')

Vue.use(Vuex);

firebase.auth.onAuthStateChanged(user => {
    if (user) {
        store.commit('setCurrentUser', user)
        store.dispatch('fetchUserProfile')

        firebase.usersCollection.doc(user.email).onSnapshot(doc => {
            store.commit('setUserProfile', doc.data())
        })
    }
})

export const store = new Vuex.Store({
    state: {
        currentUser: null,
        userProfile: {}
    },
    actions: {
        clearData({ commit }) {
            commit('setCurrentUser', null)
            commit('setUserProfile', {})
        },
        fetchUserProfile({ commit, state }) {
                firebase.usersCollection.doc(state.currentUser.email).get().then(res => {
                    commit('setUserProfile', res.data())
                }).catch(err => {
                    console.log(err)
                })
        }
    },
    mutations: {
        setCurrentUser(state, val) {
            state.currentUser = val
        },
        setUserProfile(state, val) {
            state.userProfile = val
        }
    }
})