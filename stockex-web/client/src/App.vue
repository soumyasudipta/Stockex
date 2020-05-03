<template>
  <div id="app">
    <img width="100" height="100" alt="Vue logo" src="./assets/logo.png">
    <GetComponent/>
  </div>
</template>

<script>
import GetComponent from './components/GetComponent.vue'

export default {
  name: 'App',
  components: {
    GetComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
