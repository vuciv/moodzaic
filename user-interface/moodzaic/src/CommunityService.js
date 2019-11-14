// Module to call REST API from Django back-end

import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class CommunityService{

    //constructor(){}

    getAllCommunities() {
        const url = `${API_URL}/api/customers/`;
        return axios.get(url).then(response => response.data);
    }
    getCommunitiesByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getCommunity(pk) {
        const url = `${API_URL}/api/customers/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteCommunity(community){
        const url = `${API_URL}/api/customers/${community.pk}`;
        return axios.delete(url);
    }
    createCommunity(community){
        const url = `${API_URL}/api/customers/`;
        return axios.post(url,community);
    }
    updateCommunity(community){
        const url = `${API_URL}/api/customers/${community.pk}`;
        return axios.put(url,community);
    }
}
