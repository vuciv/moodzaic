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

const AllCommunities = ({myCommunities}) => (
  <div>
    <MyMenu />
    <Container text style={{ marginTop: '7em' }}>
    <p> should show all the communities and allow you to select any to join</p>
    </Container>
    <Footer />
  </div>
)

export default AllCommunities
