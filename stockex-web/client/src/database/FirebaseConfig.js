import firebase from 'firebase'
import 'firebase/firestore'


const config = {
    apiKey: "AIzaSyAx74C9R7qNyrrPC8LxoZgBDvSlPG8T-OY",
    authDomain: "stockex-soumyasudipta.firebaseapp.com",
    databaseURL: "https://stockex-soumyasudipta.firebaseio.com",
    projectId: "stockex-soumyasudipta",
    storageBucket: "stockex-soumyasudipta.appspot.com",
    messagingSenderId: "240783026657",
    appId: "1:240783026657:web:12f342497d047e434f4aa0",
    measurementId: "G-VBJZJ47HR3"
}

firebase.initializeApp(config)
firebase.firestore.setLogLevel('debug')

const db = firebase.firestore()
const auth = firebase.auth()
const currentUser = auth.currentUser

// firebase collections
const usersCollection = db.collection('users')

export {
    db,
    auth,
    currentUser,
    usersCollection,
}