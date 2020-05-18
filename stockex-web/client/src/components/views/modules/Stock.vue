<template>
    <v-app app>
        <v-container class="grey lighten-5">
            <v-text-field
                    id="search"
                    name="search"
                    class="mx-4"
                    flat
                    v-on:keyup="searchMatch"
                    hide-details
                    label="Search"
                    style="padding: 10px 0 50px 0 "
            ></v-text-field>
            <v-row no-gutters>
                <v-col cols="3"
                       lg="3"
                       md="4"
                       sm="6"
                       v-for="stock in loadData()"
                       :key="stock"
                        style="padding: 5px;"
                       :id="stock">
                    <v-card
                            class="mx-auto"
                            height="200px"
                            :to="'stock/'+stock"
                            style="padding: 10px 15px;"
                    >
                        <v-list-item-content>
                            <v-list-item-title>{{ stock }}</v-list-item-title>
                        </v-list-item-content>

                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
    export default {
        data : () => {
            return {
                stocks: ['BKNG', 'AVGO', 'CDNS', 'CDW', 'CERN', 'CHTR', 'CHKP', 'CTAS', 'CSCO', 'CTXS',
                'CTSH', 'CMCSA', 'CPRT', 'CSGP', 'COST', 'CSX', 'DLTR', 'EBAY', 'EA', 'EXC',
                'EXPE', 'FB', 'FAST', 'FISV', 'FOXA', 'FOX', 'GILD', 'IDXX', 'ILMN', 'INCY',
                'INTC', 'INTU', 'ISRG', 'JD', 'KLAC', 'KHC', 'LRCX', 'LBTYA', 'LBTYK', 'LULU',
                'MAR', 'MXIM', 'MELI', 'MCHP', 'MU', 'MSFT', 'MDLZ', 'MNST', 'NTAP', 'NTES',
                'NFLX', 'NVDA', 'NXPI', 'ORLY', 'PCAR', 'PAYX', 'PYPL', 'PEP', 'QCOM', 'REGN',
                'ROST', 'SGEN', 'SIRI', 'SWKS', 'SPLK', 'SBUX', 'SNPS', 'TMUS', 'TTWO', 'TSLA',
                'TXN', 'TCOM', 'ULTA', 'UAL', 'VRSN', 'VRSK', 'VRTX', 'WBA', 'WDAY', 'WDC',
                'WLTW', 'XEL', 'XLNX'],
            };
        },

        methods:{
            loadData: function () {
                let data = this.stocks
                return data
            },
            searchMatch: function () {
                const searchText = document.getElementById("search").value.toString();
                const re = new RegExp(searchText, "i");
                const filterstocks = []
                for (const fullstockItem of this.stocks) {
                    let res = fullstockItem.toString().search(re);
                    if (res !== -1) {
                        document.getElementById(fullstockItem).style.display="inline";
                        filterstocks.push(fullstockItem)
                    }
                    else{
                        document.getElementById(fullstockItem).style.display="none";
                    }
                }
                return filterstocks
            }
        }
    }
</script>

<style scoped>

</style>