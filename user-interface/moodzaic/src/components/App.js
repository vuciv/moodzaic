import React, { Component } from 'react';
// import '../App.css';
import LoginForm from './LogIn.js'
import ProfilePage from './ProfPage.js'
import MoodPage from './MoodInput.js'

class App extends Component {
  // constructor(props) {
  //   super(props)
  //   this.state = {
  //     LoggedIn: false,
  //     Name: '',
  //     Username: ''
  //   }
  //   this.toggleLogIn = this.toggleLogIn.bind(this)
  // this.handleChange = this.handleChange.bind(this);
  // this.handleSubmit = this.handleSubmit.bind(this);
  // };
  state = {
        LoggedIn: true,
        Name: '',
        Username: ''
  }

  toggleLogIn = () => {
      this.setState(prevState => ({
        LoggedIn: !prevState.LoggedIn
      }))
  }
  render() {
    return (
      <div>
      {console.log(this.state)}
        {this.state.LoggedIn ?
        <MoodPage /> :
        <LoginForm />}
      </div>
    )
  }

}
// function App() {
//   console.log("Hey");
//   return (
//     <LoginForm />
    // <FixedMenuLayout />

    // <div className="App">
      // <LoginPage />
      // <header className="App-header">
      //   <img src={logo} className="App-logo" alt="logo" />
      //   <p>
      //     Edit <code>src/App.js</code> and save to reload.
      //   </p>
      //   <a
      //     className="App-link"
      //     href="https://reactjs.org"
      //     target="_blank"
      //     rel="noopener noreferrer"
      //   >
      //     Learn React
      //   </a>
      // </header>
    // </ div>
//   );
// }


export default App;
