<template>
  <div id="app">
    <v-app app>
      <SystemBar></SystemBar>
      <Navigation v-if="currentUser"></Navigation>
      <Header></Header>
      <Contents></Contents>
      <Footer></Footer>
    </v-app>
  </div>
</template>

<script>
  import { mapState } from 'vuex'

  import Navigation from "@/components/shared/Navigation";
  import SystemBar from "@/components/shared/SystemBar";
  import Header from "@/components/shared/Header";
  import Contents from "@/components/shared/Content";
  import Footer from "@/components/shared/Footer";

  export default {
    components:{
      SystemBar,
      Navigation,
      Header,
      Contents,
      Footer
    },
    computed: {
      ...mapState(['currentUser'])
    }
  }
</script>

<style lang="scss">

</style>
