<template>
    <v-app app>
        <v-card
                class="mx-auto"
                width="100%"
                outlined
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline mb-1">My Account</v-list-item-title>

                </v-list-item-content>

                <v-list-item-avatar
                        tile
                        size="80"
                >
                    <v-img src="https://randomuser.me/api/portraits/men/85.jpg" ></v-img>
                </v-list-item-avatar>
            </v-list-item>

            <v-card
                style="margin-top: 10px"
            >
                <v-tabs>
                    <v-tab>
                        Profile
                    </v-tab>
                    <v-tab>
                        WishList
                    </v-tab>
                    <v-tab>
                        Change Password
                    </v-tab>

                    <v-tab-item>
                        <v-card>
                            <v-card-text>
                                <v-text-field
                                        label="Name"
                                        placeholder="Name"
                                        :value="userProfile.name"
                                        disabled
                                ></v-text-field>
                            </v-card-text>
                            <v-card-text>
                                <v-text-field
                                        label="Email"
                                        placeholder="Email"
                                        :value="userProfile.email"
                                        disabled
                                ></v-text-field>
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                    <v-tab-item>
                        <v-card>
                            <v-card-actions v-for = "wish in userProfile.wishlist"
                                            :key="wish">
                                <v-card-text>{{wish}}</v-card-text>
                                <v-btn v-on:click="deleteWishlist(wish)">Remove</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-tab-item>
                    <v-tab-item>
                        <v-card
                                class="mx-auto text-center"
                                width="1000"
                                max-width="100%"
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
                            <transition name="fade">
                                <div v-if="errorMsg !== ''" class="error-msg">
                                    <p>{{ errorMsg }}</p>
                                </div>
                            </transition>
                        </v-card>
                    </v-tab-item>
                </v-tabs>
            </v-card>

        </v-card>
    </v-app>
</template>

<script>
    import {mapState} from "vuex";
    import { required, minLength, sameAs} from 'vuelidate/lib/validators'
    const firebase = require('../../../database/FirebaseConfig')

    export default {
        data() {
            return {
                password: '',
                repeatPassword: '',
                performingRequest: false,
                errorMsg: '',
                user: { name: 'User', avatar: 'https://randomuser.me/api/portraits/men/85.jpg' },
            }
        },
        validations:{
            password: {
                required,
                minLength: minLength(6)
            },
            repeatPassword: {
                sameAsPassword: sameAs('password')
            }
        },
        computed: {
            ...mapState(['userProfile', 'currentUser']),

            passwordErrors () {
                const errors = []
                if (!this.$v.password.$dirty) return errors
                !this.$v.password.required && errors.push('Password is required')
                !this.$v.password.minLength && errors.push('Must be a valid Password')
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
            deleteWishlist (wish) {

                var db = firebase.usersCollection.doc(this.userProfile.email)

                const index = this.userProfile.wishlist.indexOf(wish);
                if (index > -1) {
                    this.userProfile.wishlist.splice(index, 1);
                }

                db.set({
                    wishlist : this.userProfile.wishlist
                })
            },
            submit () {
                this.performingRequest = true

                this.currentUser.updatePassword(this.password).then(() =>{
                    this.performingRequest = false
                    this.$router.push('/myaccount')
                }).catch(err => {
                    console.log(err)
                    this.performingRequest = false
                    this.errorMsg = err.message
                });
            },
            clear () {
                this.$v.$reset()
                console.log(this.userProfile)
                this.password = ''
                this.repeatPassword = ''
            },
        },
    }
</script>

<style scoped>

</style>