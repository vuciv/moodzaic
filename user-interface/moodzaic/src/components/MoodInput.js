import React from 'react'
import logo from '../logo.png';
import {
  Container,
  Divider,
  Grid,
  Header,
  Image,
  List,
  Button,
  Form
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

class MoodPage extends React.Component {
  render() {
    return(
      <div>
        <MyMenu />
        <Container text style={{ marginTop: '7em' }}>
          <Header as='h1'>How are you feeling?</Header>
          <p>Some ~important~ questions for you about your mood today.</p>
          <Form>
            <Form.Field>
              <label>What did you eat for the last 3 meals?</label>
              <input />
            </Form.Field>
          </Form>
          <Form>
            <Form.Field>
              <label>What do you want from me????</label>
              <input />
            </Form.Field>
          </Form>
          <p>
            Anyways thats all have a nice day I guess
          </p>
          <Link to="/Profile">
            <Button color='teal' fluid size='large'>
              Submit
            </Button>
          </Link>
        </Container>
        <Footer />
      </div>
    )
  }
}

export default MoodPage;
