const express = require('express');
const mongodb = require('mongodb');

const router = express.Router();
// const connection_string = 'mongodb://localhost:27017'
const connection_string = encodeURI('mongodb+srv://stockex-webserver:419azSmIlayzKArc@stockexcluster-beopo.gcp.mongodb.net/test?retryWrites=true&w=majority')


// Get Posts
router.get('/:stock/:ticker', async (req, res) => {
    const gets = await loadPostsCollection(req.params.ticker);
    res.send(await gets.find({_id:{$regex:req.params.stock}},{ projection:{_id:0,'open':1,'high':1,'close':1,'low':1,'timestamp':1,'volume':1}}).toArray());
});


async function loadPostsCollection(ticker){
    const client = await mongodb.MongoClient.connect(connection_string, {
        useNewUrlParser: true
    });

    return client.db('stockex').collection(ticker);
}

module.exports = router;