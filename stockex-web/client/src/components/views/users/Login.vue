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
                    <v-btn class="mr-4" @click="submit">submit</v-btn>
                    <v-btn @click="clear">clear</v-btn>
                    <p>You don't have an account ? You can <router-link to="/register">create one</router-link></p>
                </v-container>
            </v-form>
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

    import { validationMixin } from 'vuelidate'
    import { required, minLength, maxLength, email} from 'vuelidate/lib/validators'

    export default {

        mixins: [validationMixin],

        data() {
            return {
                email: '',
                password: '',
                performingRequest: false,
                errorMsg: ''
            }
        },
        validations:{
            email: {
                required: required,
                email: email,
                maxLength: maxLength(50)
            },
            password: {
                required,
                minLength: minLength(6)
            }
        },
        computed: {
            emailErrors () {
                const errors = []
                if (!this.$v.email.$dirty) return errors
                !this.$v.email.email && errors.push('Must be valid e-mail')
                !this.$v.email.required && errors.push('E-mail is required')
                !this.$v.email.maxLength && errors.push('Email must be at most 30 characters long')
                return errors
            },
            passwordErrors () {
                const errors = []
                if (!this.$v.password.$dirty) return errors
                !this.$v.password.required && errors.push('Password is required')
                !this.$v.password.minLength && errors.push('Must be valid password')
                return errors
            }
        },
        methods: {
            submit () {
                this.performingRequest = true
                firebase.auth.signInWithEmailAndPassword(this.email, this.password).then(user => {
                    this.$store.commit('setCurrentUser', user.user)
                    this.$store.dispatch('fetchUserProfile')
                    this.performingRequest = false
                    this.$router.push('/dashboard')
                }).catch(err => {
                    console.log(err)
                    this.performingRequest = false
                    this.errorMsg = err.message
                })
            },
            clear () {
                this.$v.$reset()
                this.email = ''
                this.password = ''
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