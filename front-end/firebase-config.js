
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-auth.js";

const firebaseConfig = {
    apiKey: "AIzaSyADLCTmBPD5snkufSuH6PgwSGc7dPHvQJQ",
    authDomain: "muse-ai-e9d39.firebaseapp.com",
    databaseURL: "https://muse-ai-e9d39-default-rtdb.firebaseio.com",
    projectId: "muse-ai-e9d39",
    storageBucket: "muse-ai-e9d39.firebasestorage.app",
    messagingSenderId: "68272920191",
    appId: "1:68272920191:web:724ba01eddb2a5dd4c914a",
    measurementId: "G-GRVFGCSG9C"
};

// initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth, createUserWithEmailAndPassword, signInWithEmailAndPassword };

