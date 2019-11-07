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



const CommunityPage = ({myCommunities}) => (
  <div>
    <MyMenu />
    <Container text style={{ marginTop: '7em' }}>
    <p> should call my communities
    unless:
    user chooses to see all communities, then calls AllCommunities
    or a community is selected, then call community and open that community</p>
    </Container>
    <Footer />
  </div>
)

export default CommunityPage
