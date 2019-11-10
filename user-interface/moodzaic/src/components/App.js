import React, { Component } from 'react';
// import '../App.css';
import LoginForm from './LogIn.js'
import ProfilePage from './ProfPage.js'
import MoodPage from './MoodInput.js'
import CommunityPage from './CommunityPage.js'
import Community from './Community.js'
import SignUpForm from './SignUp.js'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

class App extends Component {

  state = {
        LoggedIn: false,
        Name: 'TestName',
        Username: 'TestUsername',
        MyCommunityList: [],
        MyObservationList: [],
        LastObservationTime: '',
        Age: 0,
        Gender: 'Ambidextrous',
        ProgressScore: 0
  }

  toggleLogIn = () => {
      this.setState(prevState => ({
        LoggedIn: !prevState.LoggedIn
      }))
  }
  render() {
    return (
      <div>
        <Router>
          <Switch>
            <Route path="/signup">
              <SignUpForm />
            </Route>
            <Route path="/MyMood">
              <MoodPage />
            </Route>
            <Route path="/Profile">
              <ProfilePage Username={this.state.Username} Name={this.state.Name}
                Age={this.state.Age} Gender={this.state.Gender}
                ProgressScore={this.state.ProgressScore}/>
            </Route>
            <Route path="/Communities">
              <CommunityPage />
            </Route>
            <Route path="/">
              {this.state.LoggedIn ?
                <Community /> :
                <LoginForm />}
            </Route>
          </Switch>
        </Router>
      </div>
    )
  }
}


export default App;
