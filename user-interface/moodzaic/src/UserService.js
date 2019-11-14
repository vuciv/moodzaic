// Module to call REST API from Django back-end
// for users, unique personal key (pk) is username

import axios from 'axios';
const API_URL = 'http://localhost:8000/api/users/';

export default class UserService{

    //constructor(){}

    getUsers() {
        const url = `${API_URL}`;
        return axios.get(url).then(response => response.data);
    }
    // getUsersByURL(link){
    //     const url = `${API_URL}${link}`;
    //     return axios.get(url).then(response => response.data);
    // }
    getUser(username) {
        const url = `${API_URL}${username}`;
        return axios.get(url).then(response => response.data);
    }
    deleteUser(user){
        const url = `${API_URL}${user.username}`; //should be username instead of pk, since that is the identifier?
        return axios.delete(url);
    }
    createUser(user){
        const url = `${API_URL}`;
        return axios.post(url,user);
    }
    updateUser(user){
        const url = `${API_URL}${user.username}`;
        return axios.put(url,user);
    }
}
