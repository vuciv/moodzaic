import React from 'react'
import { Button, Form, Grid, Header, Image, Message, Segment } from 'semantic-ui-react'
import logo from '../logo.png'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

class LoginForm extends React.Component {
  state = {
    LoggedIn: false
  }


  logIn = () => {
    //here we need to somehow check that the person is legit lol
    this.props.callback();
  }


  render() {
    return(
      <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
        <Grid.Column style={{ maxWidth: 450 }}>
          <Header as='h2' color='teal' textAlign='center'>
            <Image src={logo} /> Log-in to your account
          </Header>
          <Form size='large'>
            <Segment stacked>
              <Form.Input fluid icon='user' iconPosition='left' placeholder='Username' />
              <Form.Input
                fluid
                icon='lock'
                iconPosition='left'
                placeholder='Password'
                type='password'
              />
              <Button color='teal' fluid size='large' onClick={this.logIn}>
                Login
              </Button>
            </Segment>
          </Form>
          <Router>
            <Message>
              New to us? <Link to='/signup'>Sign Up</Link>
            </Message>
          </Router>
        </Grid.Column>
      </Grid>
    )
  }
}

export default LoginForm
