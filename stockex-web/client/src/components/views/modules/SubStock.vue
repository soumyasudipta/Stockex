<template>
    <v-app app>
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
    </v-app>
</template>

<script>
    import GetService from "../../../database/GetService";
    import FusionCharts from 'fusioncharts';

    let dataFetch = [null,null,null,null,null,null,null]
    let schemaFetch = [null,null,null,null,null,null,null]

    var schemaSource = [
        {
            "name": "Timestamp",
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
        subcaption: {
            text: "Stock prices from May 2014 - November 2018"
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
                tab: null,
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
            try {

                //Loop for the ticker period
                for(let i = 0; i<this.items.length ; i++) {

                    //Variable Declaration
                    let tickerPeriodData = []
                    let fetchedData = null
                    let data = null

                    //Variable Assignment
                    fetchedData = await GetService.getPosts(this.$route.params.id, this.items[i].period)

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