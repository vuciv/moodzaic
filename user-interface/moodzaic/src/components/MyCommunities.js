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
import Community from './Community.js';
import MyMenu from './Menu.js';
import Footer from './Footer.js';


// const CommunitiesPage = ({myCommunities}) => (
//   <div>
//     <MyMenu />
//     <Container text style={{ marginTop: '7em' }}>
//     <p> should show all the communities and allow you to select one to look at,
//     and then pass that info for the specific community page</p>
//     </Container>
//     <Footer />
//   </div>
// )

class CommunitiesPage extends React.Component {
  state = {
    openCommunity: false
  }

  // openCommunity(c) {
  //   return <Community communityName = {c} />
  // }
  openCommunity = (c) => {
         this.props.communityCallback(c);
    }

  render() {
    const myCommunities = this.props.myCommunities;
    const communities = myCommunities.map((com, i) => {
      return <Button
                color='teal' fluid size='large'
                key = {i}
                onClick = {this.openCommunity(com)}>
                {com}
              </ Button>;
    })

    return (
      <div>
        <Container text style={{ marginTop: '7em' }}>
          <p> should show all the communities and allow you to select one to look at,
          and then pass that info for the specific community page</p>
          {communities}
        </Container>
      </div>
    )
  }
}

export default CommunitiesPage
