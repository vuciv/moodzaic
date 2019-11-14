import React from 'react'
import {
  Container,
  Button,
} from 'semantic-ui-react'
// import { addCommunity, isMyCommunity } from '../integration_funcs.js'
import CommunityService from '../CommunityService.js';
// import UserService from '../UserService.js';
import MakeCommunity from './MakeCommunity.js';




class AllCommunities extends React.Component {
  state = {
    makeMode: false,
    // profile: {}
  }

  // componentDidMount() {
  //   // var  self  =  this;
  //   ProfileService.getProfile(this.props.user.username).then(function (result) {
  //       this.setState({ profile:  result.data, nextPageURL:  result.nextlink})
  //   });
  // }

  handleAddClick(community) {
    CommunityService.updateCommunity(community);
    //do you need both? probably, right? NOPE LOL
  }

  toggleMakeMode = () => {
    this.setState(prevState => ({
      makeMode: !prevState.makeMode
    }))
  }

  render() {
    const communities = this.props.allCommunities.map((com, i) => {
      return <Button
                color='purple' fluid size='large'
                key = {i}
                onClick = {this.handleAddClick({name: com.name, users: com.users.append(this.props.user)})}>
                {com.name}: {this.props.myCommunities.includes(com) ? 'added!' : 'add?'}
              </ Button>;
    })

    const makeCommunityButton = () => {
      return <Button
                color='teal' fluid size='large'
                onClick = {this.toggleMakeMode}>
                {'Create a new community!'}
              </ Button>;
      }


    return (
      <div>
        {this.state.makeMode ?
          <MakeCommunity callback={this.toggleMakeMode()}/> :
          <Container text style={{ marginTop: '7em' }}>
          {communities}
          <p> don't see any you like? </p>
          {makeCommunityButton}
          </Container>
        }
      </div>
    )
  }

}


export default AllCommunities
