<template>
    <v-app app>
        <v-container class="grey lighten-5" >
            <v-row no-gutters>
                <v-col
                       lg="8"
                       md="10"
                       sm="12">
                    <h1>I m in Stock {{this.id = $route.params.id}} </h1>
                    <v-card>
                        <h1>{{ $route.params.id }}</h1>
                        <canvas id="myChart" :width="100" :height="100"></canvas>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>

<script>
    import GetService from "@/database/GetService";
    import Chart from 'chart.js';

    export default {
        components:{

        },
        data() {
            return {
                posts: [],
                error: '',
                open : [],
                close : [],
                high : [],
                low : [],
                volume : [],
                time : []
            }
        },
        async created() {
            try {
                this.posts = await GetService.getPosts(this.$route.params.id,'6mo');

                for (let i = 0; i < this.posts.length; i++) {
                    this.open.push(this.posts[i]['open'])
                    this.close.push(this.posts[i]['close'])
                    this.high.push(this.posts[i]['high'])
                    this.low.push(this.posts[i]['low'])

                    let dateObj = new Date(this.posts[i]['timestamp']*1000);
                    // var utcString = dateObj.toUTCString();
                    // var time = utcString.slice(-11, -4);
                    let date = dateObj.getFullYear() + "-" +("0" + (dateObj.getMonth() + 1)).slice(-2) + "-" +("0" + dateObj.getDate()).slice(-2);


                    this.time.push(date)
                }
                this.createChart(this.open,this.high,this.low,this.close,this.time)
            } catch(err) {
                this.error = err.message;
            }
        },
        methods: {
            createChart: (open, high, low, close, time) => {
                new Chart(document.getElementById("myChart"), {
                    type: 'line',
                    backgroundColor:'3567645',
                    data: {
                        labels: time,
                        datasets: [{
                            data: open,
                            label: "Open",
                            borderColor: "#B0BEC5",
                            fill: false
                        }, {
                            data: high,
                            label: "High",
                            borderColor: "#B2FF59",
                            fill: false
                        }, {
                            data: low,
                            label: "Low",
                            borderColor: "#EF5350",
                            fill: false
                        }, {
                            data: close,
                            label: "Close",
                            borderColor: "#90CAF9",
                            fill: false
                        }
                        ]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'Stocks'
                        }
                    }
                });
            }
        }
    }

</script>

<style scoped>

</style>