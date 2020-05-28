<template>
    <v-app app>
        <v-sheet
                class="mx-auto ma-5 "
                elevation="8"
                max-width="1000"
        >
            <v-slide-group
                    v-model="model"
                    class="pa-4"
                    center-active
                    show-arrows
            >
                <v-slide-item
                        v-slot:default="{ active, toggle }"
                > <v-hover v-slot:default="{ hover }">
                    <v-card
                            :color="active ? 'black' : 'black'"
                            class="ma-auto my-10 mx-10"
                            height="450"
                            width="350"
                            @click="toggle"
                    >
                        <v-img
                                :aspect-ratio="16/15"
                                src="https://image.freepik.com/free-vector/digital-money-transfer-technology-background_1017-17454.jpg"
                        >
                            <v-expand-transition>
                                <div
                                        v-if="hover"
                                        class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal display-3 white--text"
                                        style="height: 100%;"
                                >
                                    Learn more about Foreign Exchange
                                </div>
                            </v-expand-transition>
                        </v-img>
                        <v-card-text
                                class="pt-5"
                                style="position: absolute;background-color: white;bottom: 10px;"
                        >
                            <v-btn
                                    absolute
                                    color="white"
                                    class="black--text"
                                    fab
                                    large
                                    right
                                    top
                            >
                                <v-icon>mdi-cash</v-icon>
                            </v-btn>
                            <h3 class="display-1 font-weight-light black--text mb-2" >Learn more about Foreign Exchange</h3>
                        </v-card-text>
                    </v-card>
                </v-hover>
                </v-slide-item>
                <v-slide-item
                        v-slot:default="{ active, toggle }"
                > <v-hover v-slot:default="{ hover }">
                    <v-card
                            :color="active ?  'black' : 'black'"
                            class="ma-auto my-10 mx-12"
                            height="450"
                            width="350"
                            @click="toggle"
                    >
                        <v-img
                                :aspect-ratio="16/15"
                                src="https://wallpaperaccess.com/full/1393719.jpg"
                        >
                            <v-expand-transition>
                                <div
                                        v-if="hover"
                                        class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal display-3 white--text"
                                        style="height: 100%;"
                                >
                                    Learn more about Stocks
                                </div>
                            </v-expand-transition>
                        </v-img>
                        <v-card-text
                                class="pt-5"
                                style="position: absolute;background-color: white;bottom: 10px;"
                        >
                            <v-btn
                                    absolute
                                    color="white"
                                    class="black--text"
                                    fab
                                    large
                                    right
                                    top
                            >
                                <v-icon>mdi-chart-line</v-icon>
                            </v-btn>
                            <h3 class="display-1 font-weight-light black--text mb-2">Learn more about Stocks</h3>
                        </v-card-text>
                    </v-card>
                </v-hover>
                </v-slide-item>

                <v-slide-item
                        v-slot:default="{ active, toggle }"
                > <v-hover v-slot:default="{ hover }">
                    <v-card
                            :color="active ? 'black' : 'black'"
                            class="ma-auto my-10 mx-12"
                            height="450"
                            width="350"
                            @click="toggle"
                    >
                        <v-img
                                :aspect-ratio="16/15"
                                src="https://cdn.vuetifyjs.com/images/cards/kitchen.png"
                        >
                            <v-expand-transition>
                                <div
                                        v-if="hover"
                                        class="d-flex transition-fast-in-fast-out black darken-2 v-card--reveal display-3 white--text"
                                        style="height: 100%;"
                                >
                                    Learn more about Forex
                                </div>
                            </v-expand-transition>
                        </v-img>
                        <v-card-text
                                class="pt-5"
                                style="position: absolute; background-color: white;bottom: 10px;"
                        >
                            <v-btn
                                    absolute
                                    color="white"
                                    class="black--text"
                                    fab
                                    large
                                    right
                                    top
                            >
                                <v-icon>mdi-mixer</v-icon>
                            </v-btn>
                            <h3  class="display-1 font-weight-light black--text mb-2">Learn more about Stockex</h3>
                        </v-card-text>
                    </v-card>
                </v-hover>
                </v-slide-item>
            </v-slide-group>

            <v-expand-transition>
                <v-sheet
                        v-if="model != null"
                        color="grey lighten-4"
                        height="200"
                        tile
                >
                    <v-row
                            class="fill-height"
                            align="center"
                            justify="center"
                    >
                        <v-card  height="auto"
                                 width="1000" v-if="model === 0">
                            <v-carousel hide-delimiters>
                                <v-carousel-item>

                                    <div>
                                        <h3 class="pa-4" style="color:black;">What is Foreign Exchange?</h3>
                                        <p class=" font-regular  pa-4">Foreign Exchange (forex or FX) is the trading of one currency for another. For example, one can swap the U.S. dollar for the euro. Foreign exchange transactions can take place on the foreign exchange market, also known as the Forex Market.

                                            The forex market is the largest, most liquid market in the world, with trillions of dollars changing hands every day. There is no centralized location, rather the forex market is an electronic network of banks, brokers, institutions, and individual traders (mostly trading through brokers or banks).
                                        </p>
                                        <p class=" font-regular  pa-4">KEY TAKEAWAYS</p>
                                        <p class=" font-regular  pa-4">
                                            Foreign Exchange (forex or FX) is a global market for exchanging national currencies with one another.
                                            Foreign exchange venues comprise the largest securities market in the world by nominal value, with trillions of dollars changing hands each day.
                                            Foreign exchange trading utilizes currency pairs, priced in terms of one versus the other.
                                            Forwards and futures are another way to participate in the forex market.

                                        </p>
                                    </div>
                                </v-carousel-item>
                                <v-carousel-item>
                                    <div>
                                        <h3 class="pa-4" style="color:black;">How Does Foreign Exchange Work? </h3>
                                        <p class=" font-regular  pa-4">The market determines the value, also known as an exchange rate, of the majority of currencies. Foreign exchange can be as simple as changing one currency for another at a local bank. It can also involve trading currency on the foreign exchange market. For example, a trader is betting a central bank will ease or tighten monetary policy and that one currency will strengthen versus the other.

                                            When trading currencies, they are listed in pairs, such as USD/CAD, EUR/USD, or USD/JPY. These represent the U.S. dollar (USD) versus the Canadian dollar (CAD), the Euro (EUR) versus the USD and the USD versus the Japanese Yen (JPY).

                                            There will also be a price associated with each pair, such as 1.2569. If this price was associated with the USD/CAD pair it means that it costs 1.2569 CAD to buy one USD. If the price increases to 1.3336, then it now costs 1.3336 CAD to buy one USD. The USD has increased in value (CAD decrease) because it now costs more CAD to buy one USD.

                                            In the forex market currencies trade in lots, called micro, mini, and standard lots. A micro lot is 1000 worth of a given currency, a mini lot is 10,000, and a standard lot is 100,000. This is different than when you go to a bank and want $450 exchanged for your trip. When trading in the electronic forex market, trades take place in set blocks of currency, but you can trade as many blocks as you like. For example, you can trade seven micro lots (7,000) or three mini lots (30,000) or 75 standard lots (750,000), for example.</p>
                                    </div>
                                </v-carousel-item>
                            </v-carousel>
                        </v-card>
                        <v-card  height="auto"
                                 width="1000" v-if="model === 1">
                            <v-carousel hide-delimiters>
                                <v-carousel-item>
                                    <div>
                                        <h3 class="pa-4" style="color:black;">What is Stock Exchange?</h3>
                                        <p class=" font-regular  pa-4">The stock market refers to the collection of markets and exchanges where regular activities of buying, selling, and issuance of shares of publicly-held companies take place. Such financial activities are conducted through institutionalized formal exchanges or over-the-counter (OTC) marketplaces which operate under a defined set of regulations. There can be multiple stock trading venues in a country or a region which allow transactions in stocks and other forms of securities.

                                            While both terms - stock market and stock exchange - are used interchangeably, the latter term is generally a subset of the former. If one says that she trades in the stock market, it means that she buys and sells shares/equities on one (or more) of the stock exchange(s) that are part of the overall stock market. The leading stock exchanges in the U.S. include the New York Stock Exchange (NYSE), Nasdaq, and the Chicago Board Options Exchange (CBOE). These leading national exchanges, along with several other exchanges operating in the country, form the stock market of the U.S.

                                            Though it is called a stock market or equity market and is primarily known for trading stocks/equities, other financial securities - like exchange traded funds (ETF), corporate bonds and derivatives based on stocks, commodities, currencies, and bonds - are also traded in the stock markets. (For related reading, see "What's the Difference Between the Equity Market and the Stock Market?")</p>
                                    </div>
                                </v-carousel-item>
                                <v-carousel-item>
                                    <div>
                                        <h3 class="pa-4" style="color:black;">Understanding the Stock Market</h3>
                                        <p class=" font-regular  pa-4">While today it is possible to purchase almost everything online, there is usually a designated market for every commodity. For instance, people drive to city outskirts and farmlands to purchase Christmas trees, visit the local timber market to buy wood and other necessary material for home furniture and renovations, and go to stores like Walmart for their regular grocery supplies.

                                            Such dedicated markets serve as a platform where numerous buyers and sellers meet, interact and transact. Since the number of market participants is huge, one is assured of a fair price. For example, if there is only one seller of Christmas trees in the entire city, he will have the liberty to charge any price he pleases as the buyers won’t have anywhere else to go. If the number of tree sellers is large in a common marketplace, they will have to compete against each other to attract buyers. The buyers will be spoiled for choice with low- or optimum-pricing making it a fair market with price transparency. Even while shopping online, buyers compare prices offered by different sellers on the same shopping portal or across different portals to get the best deals, forcing the various online sellers to offer the best price.

                                            A stock market is a similar designated market for trading various kinds of securities in a controlled, secure and managed the environment. Since the stock market brings together hundreds of thousands of market participants who wish to buy and sell shares, it ensures fair pricing practices and transparency in transactions. While earlier stock markets used to issue and deal in paper-based physical share certificates, the modern day computer-aided stock markets operate electronically.</p>
                                    </div>
                                </v-carousel-item>

                            </v-carousel>
                        </v-card>
                        <v-card height="auto"
                                width="1000" v-if="model === 2">
                            <v-carousel hide-delimiters>
                                <v-carousel-item>

                                    <div>
                                        <h3 class="pa-4" style="color:black;">What is Stockex?</h3>
                                        <p class=" font-regular  pa-4">We are implementing "Nasdaq" stocks at the moment and will further implement other stock exchanges as well.
                                            It stands for the National Association of Securities Dealers Automated Quotations System and is the world's second-largest stock exchange based on market capitalization. It trades listed stocks as well as over-the-counter (OTC) stocks. As a general rule of thumb, it is where most technology stocks are traded. A quick way to tell if a company is listed on the NASDAQ is to check out the ticker symbol. (e.g. Microsoft = MSFT, Dell Computers = DELL, Cisco = CSCO).
                                            Major stocks that trade on the NASDAQ include Apple, Amazon, Microsoft, Facebook, Gilead Sciences, Starbucks, Tesla, Intel, and Oracle.
                                        </p>
                                    </div>
                                </v-carousel-item>
                            </v-carousel>
                        </v-card>
                    </v-row>
                </v-sheet>
            </v-expand-transition>
        </v-sheet>
    </v-app>
</template>

<script>
    export default {
        data: () => ({
            model: null,
        }),
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

