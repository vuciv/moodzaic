import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export function addCommunity(c) {
    //add the community c to the list of all communities in the overall data
    //unless it's already added lol
  }

  export function isMyCommunity(c) {
    //check if the community c is in your personal list of communities
  }

  export const getMyCommunityList = (username) => {
    //get the community list of the username from the data
    return [];
  }

  export const getAllCommunities = () => {
    //get the info of all the communities
    return [];
  }

  function getUsers() {
    return axios.get(`${API_URL}community/all`).then(response => response.data).catch(error => console.log(error));
  }

  export function createUser(){
    return axios.post(`${API_URL}community/`, {
      name: "jerseysCommunity"
    })
      .then(response => {
        console.log(response);
        console.log(response.data);
      })
      .catch(error => console.log(error))
  }

  export function getUserByUsername(u) {
    //get all of a user's info by putting in their username
    return getUsers().then(data => {
        console.log(data)
        return data.find(user => user.username === u);
    });

  }


  export const getPosts = (com) => {
    //get a list of all the posts from the community
    const ret = [];
    // for each in com.posts {
    //   ret.append({
    //     poster: post.poster lol so like this is not in the class diagram
    //     message: post.post,
    //     time: post.post_time,
    //     comment_list: post.comment_list (list of objects: poster (string) and message (string))
    //   })
    // }
    return ret;
  }

  export const sendPost = (post) => {
    //add a post to the backend
    //complete with poster, message, time, and comment_list
    //adds it to the correct list -- the og list of posts or whatever comment post or whatever
    return;
  }
