<template>
    <v-app app>
        <v-card
                class="mx-auto"
                width="100%"
                outlined
                style="margin-bottom: 10px"
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline mb-1">{{ financials.longName }}</v-list-item-title>
                    <v-list-item-subtitle>{{ financials.symbol }}   NASDAQ</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar
                        tile
                        size="80"
                        color="grey"
                >
                    <v-img :src="financials.logo_url" ></v-img>
                </v-list-item-avatar>
            </v-list-item>
        </v-card>

        <v-card>
            <v-tabs
                    v-model="tab"
                    dark
            >
                <v-tab
                        v-for="item in items"
                        :key="item.tab"
                >
                    {{ item.tab }}
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item
                        v-for="item in items"
                        :key="item.tab"
                        :eager="true"
                >
                    <v-card>
                        <div :id="item.id"></div>
                    </v-card>
                </v-tab-item>
            </v-tabs-items>
        </v-card>

        <v-card
                class="mx-auto"
                width="100%"
                outlined
                style="margin-top: 10px"
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline mb-1"><h3>Financials</h3></v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-slide-group multiple show-arrows>
                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Valuations</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Market Capitalisation: {{ financials.marketCap }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Enterprise Value (MRQ): {{ financials.enterpriseValue }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Enterprice Value/ EBITDA (TTM): {{ financials.enterpriseToEbitda }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Total Shares Outstanding (MRQ): {{ financials.sharesOutstanding }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Number of Employees: {{ financials.fullTimeEmployees }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Number of Shareholders: {{  }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Price to Earnings Ratio (TTM): {{ financials.earningsQuarterlyGrowth }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Price to Revenue Ratio (TTM): {{ financials.enterpriseToRevenue }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Price to Book (FY): {{ financials.priceToBook }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-1">Price to SAles (FY): {{ financials.priceToSalesTrailing12Months }}</v-list-item-subtitle>
                        </v-list-item-content>

                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Price History</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Average Volume (10 Day) {{ financials.averageVolume10days }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">1-Year Beta {{ financials.beta }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">52 Week High {{ financials.fiftyTwoWeekHigh }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-1">52 Week Low {{ financials.fiftyTwoWeekLow }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Balance Sheet</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Quick Ratio (MRQ) {{ null }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Current Ratio (MRQ) {{ null }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Debt to Equity Ratio (MRQ) {{ null }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Net Debt (MRQ) {{ financials.payoutRatio }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Total Debt (MRQ) {{ financials.pegRatio }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-1">Total Assets (MRQ) {{ financials.totalAssets }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Dividends</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Dividends Paid (FY) {{ financials.fiveYearAvgDividendYield }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Dividends Yield (FY) {{ financials.dividendYield }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Dividends per Share (FY) {{ financials.dividendRate }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Operating Metrics</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Return on Assets (TTM) {{ financials.netIncomeToCommon/financials.totalAssets }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Return on Equity (TTM) {{ financials.netIncomeToCommon/financials.sharesOutstanding }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Return on Invested Capital (TTM) {{  }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-1">Revenue per Employee (TTM) {{ financials.enterpriseToRevenue }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Margins</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Net Margins (TTM) {{ financials.profitMargins }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Gross Margin (TTM) {{ financials.earningsQuarterlyGrowth }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Operating Margin (TTM) {{ financials.heldPercentInstitutions }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-1">Pretax Margin (TTM) {{ financials.pegRatio }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>

                <v-slide-item>
                    <v-card
                            height="320px"
                            width="300px"
                            outlined
                            style="margin: 10px 5px; padding-left: 10px"
                    >
                        <v-list-item-content>
                            <v-list-item-title class="heading mb-3"><h3>Income Statement</h3></v-list-item-title>
                            <v-list-item-subtitle class="mb-3">Basic EPS (FY) {{ financials.forwardEps }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Basic EPS (TTM) {{ financials.trailingEps }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">EPS Diluted (FY) {{ financials.revenueQuarterlyGrowth }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Net Income (FY) {{ financials.netIncomeToCommon }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">EBIDTA (TTM) {{ financials.enterpriseToEbitda }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Gross Profit (MRQ) {{ financials.profitMargins }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Gross Profit (FY) {{ financials.profitMargins }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Last Year Revenue (FY) {{ financials.revenueQuarterlyGrowth }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Total Revenue (FY) {{ financials.revenueQuarterlyGrowth }}</v-list-item-subtitle>
                            <v-list-item-subtitle class="mb-3">Free Cash Flow (TTM) {{ financials.revenueQuarterlyGrowth }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-card>
                </v-slide-item>
            </v-slide-group>
        </v-card>

        <v-card
                class="mx-auto"
                width="100%"
                outlined
                style="margin-top: 10px"
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline mb-5"><h3>Profile</h3></v-list-item-title>
                    <v-list-item-subtitle class="mb-3">Sector: <span>{{ financials.sector }}</span></v-list-item-subtitle>
                    <v-list-item-subtitle class="mb-3">Industry: <span>{{ financials.industry }}</span></v-list-item-subtitle>
                    <v-list-item-subtitle class="mb-3">Employees: <span>{{ financials.fullTimeEmployees }}</span></v-list-item-subtitle>
                    <v-list-item-content><span>{{ financials.longBusinessSummary }}</span></v-list-item-content>
                </v-list-item-content>
            </v-list-item>
        </v-card>
    </v-app>
</template>

<script>
    import GetService from "../../../database/GetService";
    import FusionCharts from 'fusioncharts';

    let dataFetch = [null,null,null,null,null,null,null]
    let schemaFetch = [null,null,null,null,null,null,null]

    var schemaSource = [
        {
            "name": "Date",
            "type": "date",
        },
        {
            "name": "Open",
            "type": "number"
        },
        {
            "name": "High",
            "type": "number"
        },
        {
            "name": "Low",
            "type": "number"
        },
        {
            "name": "Close",
            "type": "number"
        },
        {
            "name": "Volume",
            "type": "number"
        }
    ]
    let dataSource = {
        data: null,
        caption: {
            text: null
        },
        extensions: {
            "customRangeSelector": {
                "enabled": "0"
            },
            "standardRangeSelector": {
                "enabled": "0"
            }
        },
        chart: {
            multicanvas: false,
            theme: "fusion"
        },
        yaxis: [
            {
                plot: [
                    {
                        value: {
                            open: "Open",
                            high: "High",
                            low: "Low",
                            close: "Close"
                        },
                        type: "candlestick"
                    }
                ],
                format: {
                    prefix: "$"
                },
                title: "Stock Price"
            },
            {
                plot: [
                    {
                        value: "Volume",
                        type: "column"
                    }
                ],
                max: "90000000"
            }
        ],
        navigator: {
            enabled: 1
        }
    }

    export default {
        components: {},
        data() {
            return {
                financials: null,
                tab:null,
                items: [
                    { tab: '1 Day', period : '1d' ,id: 'id1' },
                    { tab: '5 Day', period : '5d' ,id: 'id2' },
                    { tab: '1 Month', period : '1mo' ,id: 'id3' },
                    { tab: '3 Month', period : '3mo' ,id: 'id4' },
                    { tab: '6 Month', period : '6mo' ,id: 'id5' },
                    { tab: '1 Year', period : '1y' ,id: 'id6' },
                    { tab: 'YTD', period : 'ytd' ,id: 'id7' },
                ],
                charts: [
                    {renderAt: "id1", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id2", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id3", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id4", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id5", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id6", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                    {renderAt: "id7", dataSource: dataSource, dataFormat: "json" , width: "100%", height: "600", type: "timeseries"},
                ],
                chartObj : [null, null, null, null, null, null, null]
            }
        },
        methods: {
            createChart : function(i) {
                this.charts[i].dataSource.data = new FusionCharts.DataStore().createDataTable(
                    dataFetch[i],
                    schemaFetch[i]
                );
                this.chartObj[i] = new FusionCharts(this.charts[i]);
                // Since we are in the `ready` block, the `chart-container-div`
                // element should be available by now.
                this.chartObj[i].render();
            }
        },
        async created() {
            //Get Stock information
            try {
                let fetchedData = null

                fetchedData = await GetService.getFinancials(this.$route.params.id)
                this.financials = fetchedData[0]['data']
            } catch(err){
                console.log(err)
            }

            // Get Stock Prices
            try {
                //Loop for the ticker period
                for(let i = 0; i<this.items.length ; i++) {

                    //Variable Declaration
                    let tickerPeriodData = []
                    let fetchedData = null
                    let data = null

                    //Variable Assignment
                    fetchedData = await GetService.getStockPrice(this.$route.params.id, this.items[i].period)

                    //Loop for the fetched data
                    for(data of fetchedData) {
                        let timeString = new Date(data['timestamp'] * 1000).toLocaleString('en-US', {timeZone: 'America/Detroit'})
                        tickerPeriodData.push([timeString, data['open'], data['high'], data['low'], data['close'], data['volume']])
                    }

                    //Set data
                    dataFetch[i] = tickerPeriodData

                    //Set schema
                    // if(['1d','5d'].includes(this.items[i].period)){
                    //
                    // }
                    schemaFetch[i] = schemaSource
                    this.createChart(i)
                }
            } catch (err) {
                console.log(err.message);
            }
        }
    }

</script>

<style scoped>

</style>