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


function addCommunity(c) {
  //add the community c to the list of all communities in the overall data
  //unless it's already added lol
}

function isMyCommunity(c) {
  //check if the community c is in your personal list of communities
}

function AllCommunities({allCommunities}) {
  const communities = allCommunities.map((com, i) => {
    return <Button
              color='teal' fluid size='large'
              key = {i}
              onClick = {addCommunity(com)}>
              {com}: {isMyCommunity(com) ? 'added!' : 'add?'}
            </ Button>;
  })

  return (
    <div>
      <Container text style={{ marginTop: '7em' }}>
        <p> should show all the communities and allow you to select any to join</p>
        {communities}
      </Container>
    </div>
  )
}


export default AllCommunities
