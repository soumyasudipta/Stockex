<template>
    <v-app app>
        <v-card class="mx-auto" max-width="1400" outlined>
            <v-toolbar color="grey darken-4" dark>
                <v-icon class="pr-2">mdi-calculator</v-icon>
                <v-toolbar-title>Currency Converter</v-toolbar-title>
            </v-toolbar>
            <v-list-item-content>
                <v-row class="mb-6" justify="center">
                    <v-col lg="2">
                        <v-subheader>Amount:</v-subheader>
                        <v-text-field  type="number" :rules="numberRule" step="any"
                                       min="0"/>
                    </v-col>
                    <v-col md="auto">
                        <v-subheader>From:</v-subheader>
                        <v-select v-model="select1" :hint="`${select1.state}, ${select1.abbr}`" :items="items1"
                                  item-text="state" item-value="abbr" label="Select" persistent-hint
                                  return-object single-line></v-select>
                    </v-col>
                    <v-col md="auto">
                        <v-subheader>To:</v-subheader>
                        <v-select v-model="select2" :hint="`${select2.state}, ${select2.abbr}`" :items="items2"
                                  item-text="state" item-value="abbr" label="Select" persistent-hint
                                  return-object single-line></v-select>
                    </v-col>
                </v-row>
            </v-list-item-content>
            <v-card-actions>
                <v-col class="text-right">
                    <v-btn color="grey darken-4" dark >Convert</v-btn>
                </v-col>
            </v-card-actions>
        </v-card>
        <p>&nbsp;</p>
        <div>
            <v-card class="mx-auto" max-width="1400" outlined>
                <v-toolbar color="grey darken-4" dark>
                    <v-icon class="pr-2">mdi-cash</v-icon>
                    <v-toolbar-title>Exchange Rates</v-toolbar-title>
                </v-toolbar>
                <v-list-item-content>
                    <v-data-table
                            :headers="headers"
                            :items="desserts"
                    >
                    </v-data-table>
                </v-list-item-content>
            </v-card>
        </div>
    </v-app>
</template>

<script>
    export default {
        data () {
            return {
                numberRule: val => {
                    if(val < 0) return 'Please enter a positive number'
                    return true
                },
                select1: { state: 'None', abbr: 'None' },
                select2: { state: 'None', abbr: 'None' },
                items1: [
                    { state: 'None', abbr: 'None' },
                    { state: 'US Dollar', abbr: 'USD' },
                    { state: 'Euro', abbr: 'EUR' },
                    { state: 'Indian Ruppee', abbr: 'INR' },
                    { state: 'Japanese Yen', abbr: 'JPY' },
                    { state: 'British Pound', abbr: 'GBP' },
                ],
                items2:[
                    { state: 'None', abbr: 'None' },
                    { state: 'US Dollar', abbr: 'USD' },
                    { state: 'Euro', abbr: 'EUR' },
                    { state: 'Indian Ruppee', abbr: 'INR' },
                    { state: 'Japanese Yen', abbr: 'JPY' },
                    { state: 'British Pound', abbr: 'GBP' },
                ],

                headers: [
                    {
                        text: '',
                        align: 'start',
                        sortable: false,
                        value: 'name',
                    },
                    { text: 'USD', value: 'usd' },
                    { text: 'EUR', value: 'eur' },
                    { text: 'JPY', value: 'jpy' },
                    { text: 'GBP', value: 'gbp' },
                    { text: 'INR', value: 'inr' },
                ],
                desserts: [
                    {
                        name: 'USD',
                        usd: 1,
                        eur: 0.92420,
                        jpy: 107.59413,
                        gbp: 0.81045,
                        inr: 75.5552
                    },
            {
                name: 'EUR',
                usd: 1.08202,
                eur: 1,
                jpy: 116.41900,
                gbp: 0.87702,
                inr: 0.92420
            },
            {
                name: 'JPY',
                usd: 0.00929,
                eur: 0.00859,
                jpy: 1,
                gbp: 0.00753,
                inr: 107.59413
            },
            {
                name: 'GBP',
                usd: 1.23388,
                eur: 1.14022,
                jpy: 132.74384,
                gbp: 1,
                inr: 0.81045,
            },
            {
                name: 'INR',
                    usd: 0.01324,
                eur: 0.01222,
                jpy: 1.4217,
                gbp: 0.01071,
                inr:1,
            },
        ],
        }
        },
    }
</script>

<style scoped>

</style>