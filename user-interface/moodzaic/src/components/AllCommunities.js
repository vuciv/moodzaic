import React from 'react'
import {
  Container,
  Button,
} from 'semantic-ui-react'
// import { addCommunity, isMyCommunity } from '../integration_funcs.js'
import CommunityService from '../CommunityService.js';
import UserService from '../UserService.js';
import MakeCommunity from './MakeCommunity.js';




class AllCommunities extends React.Component {
  state = {
    makeMode: false
  }

  handleAddClick(community) {
    var username = this.state.Username;
    var user_plus_community = {
      User: username,
      Community: community
    }
    CommunityService.updateCommunity(community);
    UserService.updateUser({user_plus_community})
    //do you need both? probably, right?
    //and how are we gonna change the whole user if we only have the username big fucking rip
  }

  toggleMakeMode = () => {
    this.setState(prevState => ({
      makeMode: !prevState.makeMode
    }))
  }

  render() {
    const communities = this.props.allCommunities.map((com, i) => {
      return /*<Button
                color='purple' fluid size='large'
                key = {i}
                onClick = {this.handleAddClick({some_community_object_with_added_user})}>
                {com.name}: {this.props.myCommunities.includes(com) ? 'added!' : 'add?'}
              </ Button>;*/
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
