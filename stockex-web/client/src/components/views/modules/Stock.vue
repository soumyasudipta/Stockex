<template>
    <v-app app>
        <v-container class="grey lighten-5">

            <!--     Search bar       -->
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

            <!--     Contents       -->
            <v-row no-gutters>
                <v-col cols="3"
                       lg="3"
                       md="4"
                       sm="6"
                       v-for="stock in stocks"
                       :key="stock.symbol"
                        style="padding: 5px;"
                       :id="stock.symbol">

                    <!--        Stock Card            -->
                    <v-card
                            class="mx-auto"
                            height="200px"
                            style="padding: 10px 15px;"
                    >
                        <v-list-item-content>
                            <v-list-item-title>{{ stock.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ stock.symbol }}</v-list-item-subtitle>
                        </v-list-item-content>

                        <!--         Buttons               -->
                        <v-card-actions
                            style="bottom: 0; padding-top:65px"
                        >
                            <v-btn
                                text large
                                :to="'stock/'+stock.symbol"
                                >Go to Stock
                            </v-btn>

                            <v-btn
                                text large
                            >
                                <v-icon
                                        :id="'wish'+stock.symbol"
                                        style="color: grey"
                                        @click="toggleWishlist('wish'+stock.symbol)"
                                >mdi-heart</v-icon>
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>

    import {mapState} from "vuex";
    const firebase = require('../../../database/FirebaseConfig')

    export default {
        data : () => {
            return {
                stocks: [
                    {
                        "name":"ANSYS",
                        "symbol":"ANSS"
                    },
                    {
                        "name":"ASML Holding",
                        "symbol":"ASML"
                    },
                    {
                        "name":"Activision Blizzard",
                        "symbol":"ATVI"
                    },
                    {
                        "name":"Adobe Inc.",
                        "symbol":"ADBE"
                    },
                    {
                        "name":"Advanced Micro Devices",
                        "symbol":"AMD"
                    },
                    {
                        "name":"Alexion Pharmaceuticals",
                        "symbol":"ALXN"
                    },
                    {
                        "name":"Align Technology, Inc.",
                        "symbol":"ALGN"
                    },
                    {
                        "name":"Alphabet Inc. (Class A)",
                        "symbol":"GOOGL"
                    },
                    {
                        "name":"Alphabet Inc. (Class C)",
                        "symbol":"GOOG"
                    },
                    {
                        "name":"Amazon.com",
                        "symbol":"AMZN"
                    },
                    {
                        "name":"Amgen Inc.",
                        "symbol":"AMGN"
                    },
                    {
                        "name":"Analog Devices",
                        "symbol":"ADI"
                    },
                    {
                        "name":"Apple Inc.",
                        "symbol":"AAPL"
                    },
                    {
                        "name":"Applied Materials, Inc.",
                        "symbol":"AMAT"
                    },
                    {
                        "name":"Autodesk, Inc.",
                        "symbol":"ADSK"
                    },
                    {
                        "name":"Automatic Data Processing, Inc.",
                        "symbol":"ADP"
                    },
                    {
                        "name":"Baidu.com, Inc.",
                        "symbol":"BIDU"
                    },
                    {
                        "name":"BioMarin Pharmaceutical, Inc.",
                        "symbol":"BMRN"
                    },
                    {
                        "name":"Biogen, Inc",
                        "symbol":"BIIB"
                    },
                    {
                        "name":"Booking Holdings",
                        "symbol":"BKNG"
                    },
                    {
                        "name":"Broadcom Inc.",
                        "symbol":"AVGO"
                    },
                    {
                        "name":"CDW",
                        "symbol":"CDW"
                    },
                    {
                        "name":"CSX Corporation",
                        "symbol":"CSX"
                    },
                    {
                        "name":"Cadence Design Systems",
                        "symbol":"CDNS"
                    },
                    {
                        "name":"Cerner Corporation",
                        "symbol":"CERN"
                    },
                    {
                        "name":"Charter Communications, Inc.",
                        "symbol":"CHTR"
                    },
                    {
                        "name":"Check Point Software Technologies Ltd.",
                        "symbol":"CHKP"
                    },
                    {
                        "name":"Cintas Corporation",
                        "symbol":"CTAS"
                    },
                    {
                        "name":"Cisco Systems",
                        "symbol":"CSCO"
                    },
                    {
                        "name":"Citrix Systems",
                        "symbol":"CTXS"
                    },
                    {
                        "name":"CoStar Group",
                        "symbol":"CSGP"
                    },
                    {
                        "name":"Cognizant Technology Solutions Corporation",
                        "symbol":"CTSH"
                    },
                    {
                        "name":"Comcast Corporation",
                        "symbol":"CMCSA"
                    },
                    {
                        "name":"Copart",
                        "symbol":"CPRT"
                    },
                    {
                        "name":"Costco Wholesale Corporation",
                        "symbol":"COST"
                    },
                    {
                        "name":"Dexcom",
                        "symbol":"DXCM"
                    },
                    {
                        "name":"Dollar Tree, Inc.",
                        "symbol":"DLTR"
                    },
                    {
                        "name":"Electronic Arts",
                        "symbol":"EA"
                    },
                    {
                        "name":"Exelon Corporation",
                        "symbol":"EXC"
                    },
                    {
                        "name":"Expedia Group",
                        "symbol":"EXPE"
                    },
                    {
                        "name":"Facebook, Inc.",
                        "symbol":"FB"
                    },
                    {
                        "name":"Fastenal Company",
                        "symbol":"FAST"
                    },
                    {
                        "name":"Fiserv, Inc.",
                        "symbol":"FISV"
                    },
                    {
                        "name":"Fox Corporation (Class A)",
                        "symbol":"FOXA"
                    },
                    {
                        "name":"Fox Corporation (Class B)",
                        "symbol":"FOX"
                    },
                    {
                        "name":"Gilead Sciences, Inc.",
                        "symbol":"GILD"
                    },
                    {
                        "name":"IDEXX Laboratories",
                        "symbol":"IDXX"
                    },
                    {
                        "name":"Illumina, Inc.",
                        "symbol":"ILMN"
                    },
                    {
                        "name":"Incyte Corporation",
                        "symbol":"INCY"
                    },
                    {
                        "name":"Intel Corporation",
                        "symbol":"INTC"
                    },
                    {
                        "name":"Intuit, Inc.",
                        "symbol":"INTU"
                    },
                    {
                        "name":"Intuitive Surgical Inc.",
                        "symbol":"ISRG"
                    },
                    {
                        "name":"JD.com",
                        "symbol":"JD"
                    },
                    {
                        "name":"KLA Corporation",
                        "symbol":"KLAC"
                    },
                    {
                        "name":"Kraft Heinz",
                        "symbol":"KHC"
                    },
                    {
                        "name":"Lam Research, Inc.",
                        "symbol":"LRCX"
                    },
                    {
                        "name":"Liberty Global (Class A)",
                        "symbol":"LBTYA"
                    },
                    {
                        "name":"Liberty Global (Class C)",
                        "symbol":"LBTYK"
                    },
                    {
                        "name":"Lululemon athletica",
                        "symbol":"LULU"
                    },
                    {
                        "name":"Marriott International, Inc.",
                        "symbol":"MAR"
                    },
                    {
                        "name":"Maxim Integrated Products",
                        "symbol":"MXIM"
                    },
                    {
                        "name":"MercadoLibre",
                        "symbol":"MELI"
                    },
                    {
                        "name":"Microchip Technology",
                        "symbol":"MCHP"
                    },
                    {
                        "name":"Micron Technology, Inc.",
                        "symbol":"MU"
                    },
                    {
                        "name":"Microsoft Corporation",
                        "symbol":"MSFT"
                    },
                    {
                        "name":"Mondelēz International",
                        "symbol":"MDLZ"
                    },
                    {
                        "name":"Monster Beverage Corporation",
                        "symbol":"MNST"
                    },
                    {
                        "name":"NVIDIA Corporation",
                        "symbol":"NVDA"
                    },
                    {
                        "name":"NXP Semiconductors N.V.",
                        "symbol":"NXPI"
                    },
                    {
                        "name":"NetApp",
                        "symbol":"NTAP"
                    },
                    {
                        "name":"NetEase, Inc.",
                        "symbol":"NTES"
                    },
                    {
                        "name":"Netflix",
                        "symbol":"NFLX"
                    },
                    {
                        "name":"O'Reilly Automotive, Inc.",
                        "symbol":"ORLY"
                    },
                    {
                        "name":"PACCAR Inc.",
                        "symbol":"PCAR"
                    },
                    {
                        "name":"PayPal Holdings, Inc.",
                        "symbol":"PYPL"
                    },
                    {
                        "name":"Paychex, Inc.",
                        "symbol":"PAYX"
                    },
                    {
                        "name":"PepsiCo, Inc.",
                        "symbol":"PEP"
                    },
                    {
                        "name":"QUALCOMM Incorporated",
                        "symbol":"QCOM"
                    },
                    {
                        "name":"Regeneron Pharmaceuticals",
                        "symbol":"REGN"
                    },
                    {
                        "name":"Ross Stores Inc.",
                        "symbol":"ROST"
                    },
                    {
                        "name":"Seattle Genetics",
                        "symbol":"SGEN"
                    },
                    {
                        "name":"Sirius XM Radio, Inc.",
                        "symbol":"SIRI"
                    },
                    {
                        "name":"Skyworks Solutions, Inc.",
                        "symbol":"SWKS"
                    },
                    {
                        "name":"Splunk",
                        "symbol":"SPLK"
                    },
                    {
                        "name":"Starbucks Corporation",
                        "symbol":"SBUX"
                    },
                    {
                        "name":"Synopsys, Inc.",
                        "symbol":"SNPS"
                    },
                    {
                        "name":"T-Mobile US",
                        "symbol":"TMUS"
                    },
                    {
                        "name":"Take-Two Interactive, Inc.",
                        "symbol":"TTWO"
                    },
                    {
                        "name":"Tesla, Inc.",
                        "symbol":"TSLA"
                    },
                    {
                        "name":"Texas Instruments, Inc.",
                        "symbol":"TXN"
                    },
                    {
                        "name":"Trip.com Group",
                        "symbol":"TCOM"
                    },
                    {
                        "name":"Ulta Beauty",
                        "symbol":"ULTA"
                    },
                    {
                        "name":"United Airlines Holdings",
                        "symbol":"UAL"
                    },
                    {
                        "name":"VeriSign",
                        "symbol":"VRSN"
                    },
                    {
                        "name":"Verisk Analytics",
                        "symbol":"VRSK"
                    },
                    {
                        "name":"Vertex Pharmaceuticals",
                        "symbol":"VRTX"
                    },
                    {
                        "name":"Walgreen Boots Alliance, Inc.",
                        "symbol":"WBA"
                    },
                    {
                        "name":"Western Digital",
                        "symbol":"WDC"
                    },
                    {
                        "name":"Workday, Inc.",
                        "symbol":"WDAY"
                    },
                    {
                        "name":"Xcel Energy, Inc.",
                        "symbol":"XEL"
                    },
                    {
                        "name":"Xilinx, Inc.",
                        "symbol":"XLNX"
                    },
                    {
                        "name":"Zoom Video Communications",
                        "symbol":"ZM"
                    },
                    {
                        "name":"eBay Inc.",
                        "symbol":"EBAY"
                    }
                ]
            };
        },
        computed: {
            ...mapState(['userProfile', 'currentUser']),
        },

        methods:{
            searchMatch: function () {
                const searchText = document.getElementById("search").value.toString();
                const re = new RegExp(searchText, "i");
                const filterstocks = []
                for (const fullstockItem of this.stocks) {
                    let res = fullstockItem.symbol.toString().search(re);
                    if (res !== -1) {
                        document.getElementById(fullstockItem.symbol).style.display="inline";
                        filterstocks.push(fullstockItem.symbol)
                    }
                    else{
                        document.getElementById(fullstockItem.symbol).style.display="none";
                    }
                }
                return filterstocks
            },

            toggleWishlist: function(id) {
                console.log(this.userProfile.email)
                var db = firebase.usersCollection.doc(this.userProfile.email)
                const index = this.userProfile.wishlist.indexOf(id.substring(4,));

                if(document.getElementById(id).style.color.toString() === "grey"){
                    if (index === -1) {
                        this.userProfile.wishlist.push(id.substring(4,))
                    }

                    db.update({
                        wishlist : this.userProfile.wishlist
                    })

                    document.getElementById(id).style.color = "red"
                }
                else{

                    if (index > -1) {
                        this.userProfile.wishlist.splice(index, 1);
                    }

                    db.update({
                        wishlist : this.userProfile.wishlist
                    })

                    document.getElementById(id).style.color = "grey"
                }

            }
        },
        mounted: function (){
            for (let wish of this.userProfile.wishlist) {
                for (let stock of this.stocks) {
                    if (wish === stock.symbol.toString()) {
                        document.getElementById("wish"+wish).style="color : red"
                    }
                }
            }
        }
        }
</script>

<style scoped>

</style>