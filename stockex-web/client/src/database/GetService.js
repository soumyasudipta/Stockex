import axios from 'axios';

const url = '/api/gets'

class GetService {
    // Get Posts
    static getStockPrice(stock, ticker) {
        return new Promise ((resolve,reject) => {
            axios.get(`${url}/${stock}/${ticker}`).then((res) => {
                const data = res.data;
                resolve(
                    data.map(get => ({
                        ...get,
                    }))
                );
            })
                .catch((err)=> {
                    reject(err);
                })

        });
    }

    static getFinancials(stock) {
        return new Promise((resolve, reject) => {
            axios.get(`${url}/financials/${stock}`).then((res) => {
                const data = res.data;
                resolve(
                    data.map(get => ({
                        ...get,
                    }))
                )
            })
                .catch((err)=>{
                    reject(err)
                })
        })
    }

    static getPrediction(stock) {
        return new Promise((resolve, reject) => {
            axios.get(`${url}/prediction/${stock}`).then((res) => {
                const data = res.data;
                resolve(
                    data.map(get => ({
                        ...get,
                    }))
                )
            })
                .catch((err)=>{
                    reject(err)
                })
        })
    }
}


export default GetService;