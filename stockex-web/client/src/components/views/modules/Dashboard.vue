<template>
    <v-app app>
        <v-card
                class="mx-auto"
                width="100%"
                outlined
                style="margin-top: 10px"
        >
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="headline mb-1"><h3>Wishlist</h3></v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-slide-group multiple show-arrows>
                <v-slide-item
                        v-for = "wish in userProfile.wishlist"
                        :key = wish
                >
                    <v-list-item-content
                        style="margin: 5px;"
                    >
                        <v-card
                                class="mx-auto"
                                height="200px"
                                style="padding: 10px 15px"
                                outlined
                        >
                            <v-list-item-content>
                                <v-list-item-title>{{ wish }}</v-list-item-title>
                            </v-list-item-content>

                            <v-card-actions
                                    style="bottom: 0; padding-top:65px"
                            >
                                <v-btn
                                        text large
                                        :to="'stock/'+wish"
                                >Go to Stock
                                </v-btn>

                            </v-card-actions>
                        </v-card>
                    </v-list-item-content>
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
                    <v-list-item-title class="headline mb-1"><h3>News</h3></v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-slide-group multiple show-arrows>
                <v-slide-item
                        v-for = "element in this.news"
                        :key = element.id
                >
                    <v-list-item-content>
                        <v-card
                                class="mx-auto"
                                max-width="300px"
                                height="500px"
                                outlined
                                style="padding: 10px 15px;"
                        >
                            <v-list-item-content>
                                <h4 >{{ element.headline }}</h4>
                            </v-list-item-content>
                            <v-list-item-content>
                                <v-img height="200px" :src="element.image"></v-img>
                            </v-list-item-content>
                            <v-list-item-content
                                style="height: 150px"
                            >
                                <p>{{ element.summary }}</p>
                            </v-list-item-content>

                            <v-card-actions>
                                <v-btn
                                        text large
                                        :href="element.url"
                                        target="_blank"
                                >Go to News
                                </v-btn>

                            </v-card-actions>

                        </v-card>
                    </v-list-item-content>
                </v-slide-item>
            </v-slide-group>
        </v-card>
    </v-app>
</template>

<script>
    import { mapState } from 'vuex'

    var jsonify = res => res.json();
    var data = fetch("https://finnhub.io/api/v1/news?category=general&token=bqit20frh5r89luqqa4g").then(jsonify);

    export default {
        data() {
            return {
                news: null
            }
        },

        computed: {
            ...mapState(['userProfile', 'currentUser']),
        },
        mounted() {
            this.news = data
            Promise.all([data]).then(res => {
                this.news = res[0]
                console.log(this.news)
            })
        }
    }
</script>