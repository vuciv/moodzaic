import React, { Component } from 'react';
// import '../App.css';
import LoginForm from './LogIn.js'
import ProfilePage from './ProfPage.js'
import MoodPage from './MoodInput.js'
import CommunityPage from './CommunityPage.js'
import SignUpForm from './SignUp.js'
import SetupPage from './AccountSetup.js'

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

class App extends Component {

  state = {
        LoggedIn: false,
        Name: 'TestName',
        user: {
          username: '',
          password: '',
          email: '',
          first_name: '',
          last_name: ''
        },
        MyCommunityList: [],
        MyObservationList: [],
        LastObservationTime: '',
        Age: 0,
        Gender: 'F',
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
            <Route path="/Welcome">
              <SetupPage />
            </Route>
            <Route path="/Profile">
              <ProfilePage Username={this.state.user.username} Name={this.state.Name}
                Age={this.state.Age} Gender={this.state.Gender}
                ProgressScore={this.state.ProgressScore}/>
            </Route>
            <Route path="/Communities">
              <CommunityPage username={this.state.user}/>
            </Route>
            <Route path="/">
              {this.state.LoggedIn ?
                <ProfilePage Username={this.state.user.username} Name={this.state.Name}
                  Age={this.state.Age} Gender={this.state.Gender}
                  ProgressScore={this.state.ProgressScore}/> :
                <LoginForm callback = {this.toggleLogIn} />}
            </Route>
          </Switch>
        </Router>
      </div>
    )
  }
}


export default App;
// import React from "react";
// import ReactDOM from "react-dom";
// import DataProvider from "./DataProvider";
// import Table from "./Table";
// const App = () => (
//   <DataProvider endpoint="api/community/"
//                 render={data => <Table data={data} />} />
// );
// const wrapper = document.getElementById("app");
// wrapper ? ReactDOM.render(<App />, wrapper) : null;
