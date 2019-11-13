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

export function getUserByUsername(u) {
  //get all of a user's info by putting in their username
  const ret = {
    username: '',
    name: '',
    etc: ''
  }
  //fill in all the stuff
  return ret;
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

// export default { addCommunity, isMyCommunity, getMyCommunityList, getAllCommunities, getUserByUsername, getPosts, sendPost }
