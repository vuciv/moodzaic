import React from 'react'
import {
  Container,
  Button,
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';
import Community from './Community.js'
import CommunitiesPage from './MyCommunities.js'
import AllCommunities from './AllCommunities.js'
import { getMyCommunityList, getAllCommunities } from '../integration_funcs.js'



class CommunityPage extends React.Component {
  state = {
        Community: '',
        AddMode: false,
        MyCommunityList: null,
        CommunityList: null
        // should these be props?
  }

  componentDidMount() {
    fetch('')
      .then(response => response.json())
      .then(data => this.setState({ MyCommunityList : data }));
  }


  toggleAddMode = () => {
    this.setState(prevState => ({
      AddMode: !prevState.AddMode
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
    const username = this.props.username;
    let myPage, myButton;

    if (community !== '') {
      myPage = <Community myCommunity = {community} username = {username} />;
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
    console.log(this.state);

    return (
      <div>
        <MyMenu />
        <Container text style={{ marginTop: '7em' }}>
          <p> should call my communities
          unless:
          user chooses to see all communities, then calls AllCommunities
          or a community is selected, then call community and open that community</p>
          <Community/>
        </Container>
        <Footer />
      </div>
    )
  }
}




export default CommunityPage;
