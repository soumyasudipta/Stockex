<template>
    <v-app app>
        <card>
            <div class="d-flex justify-center" style="overflow: hidden;">
                <p>
                    <span class="font-italic font-weight-light display-3 float-left pr-4">Welcome to</span>
                    <span class="font-italic font-weight-black display-3 float-left">Stockex</span>
                </p>
            </div>
            <div class="d-flex justify-center mb-3 " style="overflow: hidden;">
                <p class="font-italic font-weight-medium float-left">-"the ultimate stock page"</p>
            </div>
            <div>
                <v-parallax src="https://theintercept.imgix.net/wp-uploads/sites/1/2020/03/GettyImages-1209906120-1583169660-e1583169779296.jpg?auto=compress%2Cformat&q=90&fit=crop&w=1200&h=800" ></v-parallax>
            </div>
            <div class="d-flex justify-center mb-3 " style="overflow: hidden;">
                <p class=" font-regular float-left pa-4">We are implementing "Nasdaq" stocks at the moment and will further implement other stock exchanges as well.
                    It stands for the National Association of Securities Dealers Automated Quotations System and is the world's second-largest stock exchange based on market capitalization. It trades listed stocks as well as over-the-counter (OTC) stocks. As a general rule of thumb, it is where most technology stocks are traded. A quick way to tell if a company is listed on the NASDAQ is to check out the ticker symbol. (e.g. Microsoft = MSFT, Dell Computers = DELL, Cisco = CSCO).
                    Major stocks that trade on the NASDAQ include Apple, Amazon, Microsoft, Facebook, Gilead Sciences, Starbucks, Tesla, Intel, and Oracle.
                </p>
            </div>
            <div class="pb-10">
                <v-parallax src="https://miro.medium.com/max/1200/1*M9HxSAV4HjhX4mjbFh4K2A.jpeg"></v-parallax>
            </div>
            <div class="d-flex justify-center mb-3 " style="overflow: hidden;">
                <p class=" font-regular float-left pa-4">We have foreign exchange rates shown with the lates updates. The foreign exchange market (Forex, FX, or currency market) is a global decentralized or over-the-counter (OTC) market for the trading of currencies. This market determines foreign exchange rates for every currency. It includes all aspects of buying, selling and exchanging currencies at current or determined prices. In terms of trading volume, it is by far the largest market in the world, followed by the credit market.</p>
            </div>

            <div>
                <v-container class="grey lighten-5">
                    <v-row
                            class="mb-2"
                            justify="center"

                    >
                        <v-col lg="5">
                            <v-hover v-slot:default="{ hover }">
                                <v-card
                                        class="mx-auto "
                                        color="grey lighten-4"
                                        width="400"
                                        height="400"
                                        to="/stock"
                                >
                                    <v-img
                                            src="https://content4.jdmagicbox.com/comp/kanpur/78/0512p512std294578/catalogue/uttar-pradesh-stock-exchange-assn-ltd-kanpur-jvpimpamqj.jpg?fit=around%7C400%3A400&crop=400%3A400%3B%2A%2C%2A"
                                    >
                                        <v-expand-transition>
                                            <div
                                                    v-if="hover"
                                                    class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal display-3 white--text"
                                                    style="height: 100%;"
                                            >
                                                Goto Stockex Page
                                            </div>
                                        </v-expand-transition>
                                    </v-img>
                                </v-card>
                            </v-hover>
                        </v-col>
                        <v-col md="auto">
                            <v-hover v-slot:default="{ hover }">
                                <v-card
                                        class="mx-auto "
                                        color="grey lighten-4"
                                        width="400"
                                        height="400"
                                        to="/forex"
                                >
                                    <v-img
                                            src="https://2.imimg.com/data2/SX/KH/MY-1776496/foreign-exchange-money-tran-500x500.jpg"
                                    >
                                        <v-expand-transition>
                                            <div
                                                    v-if="hover"
                                                    class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal display-3 white--text"
                                                    style="height: 100%;"
                                            >
                                                Goto Forex Page
                                            </div>
                                        </v-expand-transition>
                                    </v-img>
                                </v-card>
                            </v-hover>
                        </v-col>
                    </v-row>
                </v-container>
            </div>
            <div class="d-flex justify-center" style="overflow: hidden;">
                <p class="font-regular display-1 float-left pr-4">Feedback Form</p>
            </div>
            <form>
                <v-text-field
                        v-model="name"
                        :error-messages="nameErrors"
                        :counter="10"
                        label="Name"
                        required
                        @input="$v.name.$touch()"
                        @blur="$v.name.$touch()"
                ></v-text-field>
                <v-text-field
                        v-model="email"
                        :error-messages="emailErrors"
                        label="E-mail"
                        required
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                ></v-text-field>
                <v-select
                        v-model="select"
                        :items="items"
                        :error-messages="selectErrors"
                        label="Topic"
                        required
                        @change="$v.select.$touch()"
                        @blur="$v.select.$touch()"
                ></v-select>
                <v-text-field
                        label="Feedback"
                        required
                ></v-text-field>
                <v-checkbox
                        v-model="checkbox"
                        :error-messages="checkboxErrors"
                        label="Do you agree to the filled information?"
                        required
                        @change="$v.checkbox.$touch()"
                        @blur="$v.checkbox.$touch()"
                ></v-checkbox>


                <!-- <v-btn class="mr-4" @click="submit">submit</v-btn> -->
                <v-btn @click="clear">submit</v-btn>
            </form>
        </card>
    </v-app>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength, email } from 'vuelidate/lib/validators'

    export default {
        mixins: [validationMixin],

        validations: {
            name: { required, maxLength: maxLength(10) },
            email: { required, email },
            select: { required },
            checkbox: {
                checked (val) {
                    return val
                },
            },
        },

        data: () => ({
            name: '',
            email: '',
            select: null,
            items: [
                'Stockex',
                'Forex',
                'General',
            ],
            checkbox: false,
        }),

        computed: {
            checkboxErrors () {
                const errors = []
                if (!this.$v.checkbox.$dirty) return errors
                !this.$v.checkbox.checked && errors.push('You must agree to continue!')
                return errors
            },
            selectErrors () {
                const errors = []
                if (!this.$v.select.$dirty) return errors
                !this.$v.select.required && errors.push('Item is required')
                return errors
            },
            nameErrors () {
                const errors = []
                if (!this.$v.name.$dirty) return errors
                !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
                !this.$v.name.required && errors.push('Name is required.')
                return errors
            },
            emailErrors () {
                const errors = []
                if (!this.$v.email.$dirty) return errors
                !this.$v.email.email && errors.push('Must be valid e-mail')
                !this.$v.email.required && errors.push('E-mail is required')
                return errors
            },
        },

        methods: {
            submit () {
                this.$v.$touch()
            },
            clear () {
                this.$v.$reset()
                this.name = ''
                this.email = ''
                this.select = null
                this.checkbox = false
            },
        },
    }
</script>

<style scoped>
    .v-card--reveal {
        align-items: center;
        bottom: 0;
        justify-content: center;
        opacity: .5;
        position: absolute;
        width: 100%;
    }
</style>