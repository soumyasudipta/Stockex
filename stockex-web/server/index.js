const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

// Middleware
app.use(bodyParser.json());
app.use(cors());

const gets = require('./routes/api/gets');

app.use('/api/gets',gets);


// Handle Production

if(process.env.NODE_ENV === 'production') {
//        Static Folder
    app.use(express.static(__dirname + '/public/'));

//    Handle SPA
    app.get(/.*/, (req, res) => res.sendFile(__dirname + '/public/index.html'))
}


const port = process.env.PORT || 3000;

app.listen(port, () => console.log(`Server started on port ${port}`));