import React from 'react'
import { Button, Form, Grid, Header, Image, Message, Segment } from 'semantic-ui-react'
import logo from '../logo.png'
import {createUser} from '../integration_funcs.js';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
const handleSubmit = (event) => {
  const [username, password, confirm_password] = event.target.map(t => t.value);

  if (password === confirm_password) {
    console.log([username, password]);
  }
  console.log(username)
}
const SignUpForm = () => {

  
  
  return <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
    <Grid.Column style={{ maxWidth: 450 }}>
      <Header as='h2' color='teal' textAlign='center'>
        <Image src={logo} /> Sign up for an account
      </Header>
      <Form size='large' onSubmit={createUser} >
        <Segment stacked>
          <Form.Input fluid icon='user' iconPosition='left' placeholder='Username' />
          <Form.Input
            fluid
            icon='lock'
            iconPosition='left'
            placeholder='Password'
            type='password'
          />
          <Form.Input
            fluid
            icon='lock'
            iconPosition='left'
            placeholder='Confirm Password'
            type='password'
          />
          <Link to='/Welcome'>
            <Button color='teal' fluid size='large'>
              Sign Up
            </Button>
          </Link>
        </Segment>
      </Form>
      <Message>
        Already have an account? <Link to='/'>Log In</Link>
      </Message>
    </Grid.Column>
  </Grid>
};

export default SignUpForm
