import React from 'react'
import logo from '../logo.png';
import {
  Container,
  Header,
  Form,
  Dropdown,
  Image,
  Grid,
  Button
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

const GenderOptions = [
  {
    key: 'F',
    text: 'Female',
    value: 'F'
  },
  {
    key: 'M',
    text: 'Male',
    value: 'M'
  },
  {
    key: 'Other',
    text: 'Other',
    value: 'O'
  },
  {
    key: 'NA',
    text: 'Prefer Not To Answer',
    value: 'NA'
  }
]

const SetupPage = ({LastObservationTime}) => (
  <div>
    <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
      <Grid.Column style={{ maxWidth: 1000 }}>
        <Container text style={{ marginTop: '-1' }}>
          <Header as='h1' color='teal'>Welcome to Moodzaic!</Header>
          <p>Fill out this form so we can create your account.</p>
          <Form>
            <Form.Field>
              <label>Name</label>
              <input />
            </Form.Field>
          </Form>
          <Form>
            <Form.Field>
              <label>Gender</label>
              <Dropdown placeholder='Select' fluid selection options={GenderOptions} />
            </Form.Field>
          </Form>
          <Form>
            <Form.Field>
              <label>Choose communities that might interest you</label>
            </Form.Field>
          </Form>
          <Link to="/MyMood">
            <Button color='teal' fluid size='large'>
              Continue
            </Button>
          </Link>
        </Container>
      </Grid.Column>
    </Grid>
  </div>
)

export default SetupPage;
