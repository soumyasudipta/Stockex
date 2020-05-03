<template>
  <div class="container">
    <h1>Stock Market</h1>
    <canvas id="myChart" width="400" height="400"></canvas>
  </div>
</template>

<script>
  import GetService from '../GetService';

  export default {
    name: 'GetComponent',
    data() {
      return {
        posts: [],
        error: '',
        text: ''
      }
    },
    async created() {
      try {
        this.posts = await GetService.getPosts();
      } catch(err) {
        this.error = err.message;
      }
    },
    methods: {
      async createPost() {
        await GetService.insertPost(this.text);
        this.posts = await GetService.getPosts();
      },
      async deletePost(id) {
        await GetService.deletePost(id);
        this.posts = await GetService.getPosts();
      }
    }
  }
</script>

<script>
  var Chart = require('chart.js');

  window.onload = function() {
    var ctx = document.getElementById("myChart");
    var lineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
          label: "2015",
          data: [10, 8, 6, 5, 12, 8, 16, 17, 6, 7, 6, 10]
        }]
      }
    })
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  div.container {
    max-width: 800px;
    margin: 0 auto;
  }

  p.error {
    border: 1px solid #ff5b5f;
    background-color: #ffc5c1;
    padding: 10px;
    margin-bottom: 15px;
  }

  div.post {
    position: relative;
    border: 1px solid #5bd658;
    background-color: #bcffb8;
    padding: 10px 10px 30px 10px;
    margin-bottom: 15px;
  }

  div.created-at {
    position: absolute;
    top: 0;
    left: 0;
    padding: 5px 15px 5px 15px;
    background-color: darkgreen;
    color: white;
    font-size: 13px;
  }

  p.text {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 0;
  }
</style>
