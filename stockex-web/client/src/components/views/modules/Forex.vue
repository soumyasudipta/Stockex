<template>
    <v-app app>
        <div>
            <v-card class="mx-auto" max-width="1400" outlined>
                <v-toolbar color="grey darken-4" dark>
                    <v-icon class="pr-2">mdi-calculator</v-icon>
                    <v-toolbar-title>Currency Converter</v-toolbar-title>
                </v-toolbar>
                <v-list-item-content>
                    <v-row class="mb-6" justify="center">
                        <v-col lg="2">
                            <v-subheader>Amount:</v-subheader>
                            <v-text-field v-model="numberValue" defaultValue="1" hide-details single-line type="number"/>
                        </v-col>
                        <v-col md="auto">
                            <v-subheader>From:</v-subheader>
                            <v-select v-model="select" :hint="`${select.state}, ${select.abbr}`" :items="items"
                                      item-text="state" item-value="abbr" label="Select" persistent-hint
                                      return-object single-line></v-select>
                        </v-col>
                        <v-col md="auto">
                            <v-subheader>To:</v-subheader>
                            <v-select v-model="select1" :hint="`${select1.state}, ${select1.abbr}`" :items="items1"
                                      item-text="state" item-value="abbr" label="Select" persistent-hint
                                      return-object single-line></v-select>
                        </v-col>
                    </v-row>
                </v-list-item-content>
                <div class="d-flex justify-center mb-3 " v-if="seen">
                    {{amt}} {{from}} is {{ tot }} {{to}}
                </div>
                <v-card-actions>
                    <v-col class="text-right">
                        <v-btn color="grey darken-4" dark v-on:click="convert(numberValue,select.abbr,select1.abbr);seen = !seen;">Convert</v-btn>
                    </v-col>
                </v-card-actions>
            </v-card>
        </div>
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
                seen:false,
                tot: null,
                to:null,
                from:null,
                amt:null,
                select: { state: 'US Dollar', abbr: 'USD' },
                items: [
                    { state: 'US Dollar', abbr: 'USD' },
                    { state: 'Euro', abbr: 'EUR' },
                    { state: 'Indian Ruppee', abbr: 'INR' },
                    { state: 'Japanese Yen', abbr: 'JPY' },
                    { state: 'British Pound', abbr: 'GBP' },
                ],
                select1: { state: 'Indian Ruppee', abbr: 'INR' },
                items1: [
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
                    { text: 'USD', value: 'USD' },
                    { text: 'EUR', value: 'EUR' },
                    { text: 'JPY', value: 'JPY' },
                    { text: 'GBP', value: 'GBP' },
                    { text: 'INR', value: 'INR' },
                ],
                desserts: [
                    {
                        name: 'USD',
                        USD: 1,
                        EUR: 0.92420,
                        JPY: 107.59413,
                        GBP: 0.81045,
                        INR: 75.5552,

                    },
                    {
                        name: 'EUR',
                        USD: 1.08202,
                        EUR: 1,
                        JPY: 116.41900,
                        GBP: 0.87702,
                        INR: 0.92420,

                    },
                    {
                        name: 'JPY',
                        USD: 0.00929,
                        EUR: 0.00859,
                        JPY: 1,
                        GBP: 0.00753,
                        INR: 107.59413,

                    },
                    {
                        name: 'GBP',
                        USD: 1.23388,
                        EUR: 1.14022,
                        JPY: 132.74384,
                        GBP: 1,
                        INR: 0.81045,

                    },
                    {
                        name: 'INR',
                        USD: 0.01324,
                        EUR: 0.01222,
                        JPY: 1.4217,
                        GBP: 0.01071,
                        INR:1,

                    },
                ],
            }
        },
        methods: {

            convert: function (n,t,x) {
                for (let i=0;i<this.desserts.length;i++){
                    if(this.desserts[i].name === t){
                        var y=this.desserts[i][x];
                        this.amt=n
                        this.from=t
                        this.to=x
                        this.tot = n*y

                    }
                }
                console.log(n,t,x);

            }
        }
    }
</script>

<style scoped>

</style>