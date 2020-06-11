const express = require('express');
const mongodb = require('mongodb');

const router = express.Router();
// const connection_string = 'mongodb://localhost:27017'
const connection_string = encodeURI('mongodb+srv://stockex-webserver:419azSmIlayzKArc@stockexcluster-beopo.gcp.mongodb.net/test?retryWrites=true&w=majority')


// Get Posts
router.get('/financials/:stock', async (req, res) => {
    const gets = await loadStockCollection('info');
    res.send(await gets.find({_id:{$regex:req.params.stock}},{ projection:{_id:0,'data':1}}).toArray());
});

router.get('/prediction/:stock', async (req, res) => {
    const gets = await loadStockCollection('prediction');
    res.send(await gets.find({_id:{$regex:req.params.stock}},{ projection:{_id:0,'value':1}}).toArray());
});

router.get('/:stock/:ticker', async (req, res) => {
    const gets = await loadStockCollection(req.params.ticker);
    res.send(await gets.find({_id:{$regex:req.params.stock}},{ projection:{_id:0,'open':1,'high':1,'close':1,'low':1,'timestamp':1,'volume':1}}).toArray());
});

async function loadStockCollection(collection){
    const client = await mongodb.MongoClient.connect(connection_string, {
        useUnifiedTopology: true,
        useNewUrlParser: true
    });

    return client.db('stockex').collection(collection);
}

module.exports = router;