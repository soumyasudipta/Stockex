import axios from 'axios';

const url = 'api/gets/'

class GetService {
    // Get Posts
    static getPosts() {
        return new Promise ((resolve,reject) => {
            axios.get(url).then((res) => {
                const data = res.data;
                resolve(
                    data.map(post => ({
                        ...post,
                        createdAt: new Date(post.createdAt)
                    }))
                );
            })
                .catch((err)=> {
                    reject(err);
                })

        });
    }


    // Created Post
    static insertPost(text) {
        return axios.post(url, {
            text
        });
    }


    // Delete Post
    static deletePost(id) {
        return axios.delete(`${url}${id}`);
    }
}

export default GetService;