const express = require('express');
const mongodb = require('mongodb');

const router = express.Router();

// Get Posts
router.get('/', async (req, res) => {
    const gets = await loadPostsCollection();
    res.send(await gets.find({_id:{$regex:'MSFT'}}).toArray());
});


async function loadPostsCollection(){
    const client = await mongodb.MongoClient.connect('mongodb://localhost:27017', {
        useNewUrlParser: true
    });

    return client.db('stockex').collection('1d');
}

module.exports = router;