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

const ProfilePage = ({Name, Username, Age, Gender, ProgressScore, Notifications}) => (
  <div>
    <MyMenu />
    <Grid columns={2}>
      <Grid.Column width = {10}>
        <Container text style={{ marginTop: '7em', marginLeft: '10em' }}>
          <Header as='h1'>{Username}'s Profile</Header>
            <p>{Notifications}</p>
            <p>My name? <strong>{Name}</strong></p>
            <p>My age? <strong>{Age}</strong></p>
            <p>My Gender? <strong>{Gender}</strong></p>
            <p>My progress score towards my big goal: <strong>{ProgressScore}</strong></p>
            <p>
            Once we've built up some data in the backend, I can display your mood history here!
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
