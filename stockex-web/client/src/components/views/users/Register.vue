<template>
    <v-app app>
        <v-card
                class="mx-auto text-center"
                width="500"
                min-width="40%"
                outlined
        >
            <transition name="fade">
                <div v-if="performingRequest" class="loading">
                    <p>Loading...</p>
                </div>
            </transition>
            <v-form>
                <v-container>
                    <v-text-field
                            v-model="name"
                            :error-messages="nameErrors"
                            :counter="25"
                            label="Name"
                            type="name"
                            @input="$v.name.$touch()"
                            @blur="$v.name.$touch()"
                            required
                    ></v-text-field>
                    <v-text-field
                            v-model="email"
                            :error-messages="emailErrors"
                            :counter="50"
                            label="E-mail"
                            type="email"
                            @input="$v.email.$touch()"
                            @blur="$v.email.$touch()"
                            required
                    ></v-text-field>
                    <v-text-field
                            v-model="password"
                            :error-messages="passwordErrors"
                            label="Password"
                            type="password"
                            @input="$v.password.$touch()"
                            @blur="$v.password.$touch()"
                            required
                    ></v-text-field>
                    <v-text-field
                            v-model="repeatPassword"
                            :error-messages="repeatPasswordErrors"
                            label="Retype - Password"
                            type="password"
                            @input="$v.password.$touch()"
                            @blur="$v.password.$touch()"
                            required
                    ></v-text-field>
                    <v-btn class="mr-4" @click="submit" :disabled="$v.$invalid">submit</v-btn>
                    <v-btn @click="clear">clear</v-btn>
                </v-container>
            </v-form>
            <span>or go back to <router-link to="/login">login</router-link>.</span>
            <transition name="fade">
                <div v-if="errorMsg !== ''" class="error-msg">
                    <p>{{ errorMsg }}</p>
                </div>
            </transition>
        </v-card>
    </v-app>
</template>

<script>
    const firebase = require('../../../firebaseConfig')
    import { required, minLength, maxLength, email, sameAs} from 'vuelidate/lib/validators'

    export default {

        data() {
            return {
                name: '',
                email: '',
                password: '',
                repeatPassword: '',
                performingRequest: false,
                errorMsg: ''
            }
        },
        validations:{
            name: {
                required: required,
                maxLength: maxLength(25)
            },
            email: {
                required: required,
                email: email,
                maxLength: maxLength(50),
            },
            password: {
                required,
                minLength: minLength(6)
            },
            repeatPassword: {
                sameAsPassword: sameAs('password')
            }
        },
        computed: {
            nameErrors () {
                const errors = []
                if (!this.$v.name.$dirty) return errors
                !this.$v.name.maxLength && errors.push('Name must be at most 25 characters long')
                !this.$v.name.required && errors.push('Name is required.')
                return errors
            },
            emailErrors () {
                const errors = []
                if (!this.$v.email.$dirty) return errors
                !this.$v.email.email && errors.push('Must be valid e-mail')
                !this.$v.email.required && errors.push('E-mail is required')
                !this.$v.email.maxLength && errors.push('Email must be at most 30 characters long')
                // !this.$v.email.unique && errors.push('Email already exists')
                return errors
            },
            passwordErrors () {
                const errors = []
                if (!this.$v.password.$dirty) return errors
                !this.$v.password.required && errors.push('Must be valid e-mail')
                !this.$v.password.minLength && errors.push('E-mail is required')
                return errors
            },
            repeatPasswordErrors () {
                const errors = []
                if (!this.$v.password.$dirty) return errors
                !this.$v.repeatPassword.sameAsPassword && errors.push('Passwords do not match')
                return errors
            }
        },
        methods: {
            submit () {
                this.performingRequest = true
                firebase.auth.createUserWithEmailAndPassword(this.email, this.password).then(user => {
                    this.$store.commit('setCurrentUser',user)

                    firebase.usersCollection.doc(this.email).set({
                        name: this.name
                    }).then(() => {
                        this.$store.dispatch('fetchUserProfile')
                        this.performingRequest = false
                        this.$router.push('/dashboard')
                    }).catch(err => {
                        console.log(err)
                        this.performingRequest = false
                        this.errorMsg = err.message
                    })
                }).catch(err => {
                    console.log(err)
                    this.performingRequest = false
                    this.errorMsg = err.message
                })
            },
            // resetPassword() {
            //     this.performingRequest = true
            //     fb.auth.sendPasswordResetEmail(this.passwordForm.email).then(() => {
            //         this.performingRequest = false
            //         this.passwordResetSuccess = true
            //         this.passwordForm.email = ''
            //     }).catch(err => {
            //         console.log(err)
            //         this.performingRequest = false
            //         this.errorMsg = err.message
            //     })
            // },
            clear () {
                this.$v.$reset()
                this.name = ''
                this.email = ''
                this.password = ''
                this.repeatPassword = ''
            },
        },
    }
</script>

<style scoped>
    .invalid{
        border:1px solid red;
        background-color: #ffc9aa;
    }
</style>