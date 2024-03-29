import React from 'react'
import { Button, Form, Grid, Header, Image, Message, Segment } from 'semantic-ui-react'
import logo from '../logo.png'
import {getUserByUsername} from '../integration_funcs';

import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

class LoginForm extends React.Component {
  state = {
    LoggedIn: false,
    username: '',
    password: ''
  }


  logIn = (u) => {
    const user = getUserByUsername(u.username);
    if (user) {
      this.props.callback(user);
    }
  }

  handleChange = (e, { name, value }) => this.setState({ [name]: value })


  handleSubmit = () => {
    // let username = event.target[0].value;
    // let password = event.target[1].value;
    getUserByUsername(this.state.username).then(user => {
      console.log(user);
      if (user && (this.state.password === user.password)) {
        this.logIn(user);
      }
    });


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
              <Form.Input fluid
                name='username'
                icon='user'
                iconPosition='left'
                placeholder='Username'
                onChange={this.handleChange}/>
              <Form.Input
                fluid
                name='password'
                icon='lock'
                iconPosition='left'
                placeholder='Password'
                type='password'
                onChange={this.handleChange}
              />
              <Button color='teal' type='submit' fluid size='large' onClick={this.handleSubmit}> {/*<onClick={this.logIn}>*/}
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
