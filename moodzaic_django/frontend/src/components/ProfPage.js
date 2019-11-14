import React from 'react'
import {
  Container,
  Divider,
  Grid,
  Header,
  Image,
  List,
  Segment,
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';
import Reminders from './Reminders.js';

const ProfilePage = ({User}) => (
  <div>
    <MyMenu />
    <Grid columns={2}>
      <Grid.Column width = {10}>
        <Container text style={{ marginTop: '7em', marginLeft: '10em' }}>
          <Header as='h1'>{User.username}'s Profile</Header>
            <p>My name? <strong>{User.first_name} {User.last_name}</strong></p>
            <p>My age? <strong>{User.age}</strong></p>
            <p>My Gender? <strong>{User.gender}</strong></p>
            <p>
            Once you imput your mood, I can display your mood history here!
            </p>
          </Container>
        </Grid.Column>
        <Grid.Column width = {5}>
          <Reminders/>
        </Grid.Column>
      </Grid>
    <Footer />
  </div>
)

export default ProfilePage;
