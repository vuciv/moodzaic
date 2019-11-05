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
  Form
} from 'semantic-ui-react'
import MyMenu from './Menu.js';
import Footer from './Footer.js';


const MoodPage = () => (
  <div>
    <MyMenu />
    <Container text style={{ marginTop: '7em' }}>
      <Header as='h1'>Semantic UI React Fixed Template</Header>
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
    </Container>
    <Footer />
  </div>
)

export default MoodPage;
