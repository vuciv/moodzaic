// Module to call REST API from Django back-end
// for users, unique personal key (pk) is username

import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class UserService{

    //constructor(){}

    getUsers() {
        const url = `${API_URL}/api/users/`;
        return axios.get(url).then(response => response.data);
    }
    getUsersByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getUser(pk) {
        const url = `${API_URL}/api/users/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteUser(user){
        const url = `${API_URL}/api/users/${user.pk}`; //should be username instead of pk, since that is the identifier?
        return axios.delete(url);
    }
    createUser(user){
        const url = `${API_URL}/api/users/`;
        return axios.post(url,user);
    }
    updateUser(user){
        const url = `${API_URL}/api/customers/${user.pk}`;
        return axios.put(url,user);
    }
}
