import React, {useState} from 'react';
//import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import '../App.css';



class LoginInstruction extends React.Component {
  render() {
    return(
      <h2>Please enter your username and password</h2>
    );
  }
}


class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}


class LoginPage extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        Username: '',
        Password: ''
      };

      this.handleUsernameChange = this.handleUsernameChange.bind(this);
      this.handlePasswordChange = this.handlePasswordChange.bind(this);
    }

    handleUsernameChange(username) {
      this.setState({
        Username: username
      });
    }

    handlePasswordChange(password) {
      this.setState({
        Passowrd: password
      });
    }

    render() {
      return (
        <div>
          <LoginInstruction />
          <LoginForm />
        </div>
      );
    }
  }


export default LoginPage;
