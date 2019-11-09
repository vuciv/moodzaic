import React from 'react'
import logo from '../logo.png';
import {
  Container,
  Divider,
  Grid,
  Header,
  Image,
  List,
  Segment,
  Form,
  Button,
  Comment
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';
import Community from './Community.js'
import CommunitiesPage from './MyCommunities.js'
import AllCommunities from './AllCommunities.js'

const getMyCommunityList = (username) => {
  //get the community list of the username from the data
  return;
}

const getAllCommunities = () => {
  //get the info of all the communities
  return;
}

class CommunityPage extends React.Component {
  state = {
        Community: '',
        AddMode: false,
        MyCommunityList: getMyCommunityList(this.props.username),
        CommunityList: getAllCommunities()
        // should these be props?
  }

  toggleAddMode = () => {
    this.setState(prevState => ({
      LoggedIn: !prevState.LoggedIn
    }))
  }

  OpenCommunity = (acommunity) => {
    this.setState(prevState => ({
      Community: acommunity
    }))
  }



  render() {
    const addMode = this.state.AddMode;
    const community = this.state.Community;
    const myCommunityList = this.state.MyCommunityList;
    const communityList = this.state.CommunityList;
    let myPage, myButton;

    if (community !== '') {
      myPage = <Community myCommunity = {community} />;
      myButton =
      <Button color='teal' fluid size='large' onClick = {this.toggleCommunity('')}>
        See My Communities
      </Button>;
    }

    else if (addMode === false) {
      myPage = <CommunitiesPage communityCallback = {this.OpenCommunity} myCommunities = {myCommunityList}/>;
      myButton =
      <Button color='teal' fluid size='large' onClick = {this.toggleAddMode}>
        See All Communities
      </Button>;
    }

    else {
      myPage = <AllCommunities allCommunities = {communityList}/>;
      myButton =
      <Button color='teal' fluid size='large' onClick = {this.toggleAddMode}>
        See My Communities
      </Button>;
    }

    return (
      <div>
        <MyMenu />
        <Container text style={{ marginTop: '7em' }}>
          <p> should call my communities
          unless:
          user chooses to see all communities, then calls AllCommunities
          or a community is selected, then call community and open that community</p>
          {myPage}
          {myButton}
        </Container>
        <Footer />
      </div>
    )
  }
}



export default CommunityPage;
