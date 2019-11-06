import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App';
import MoodPage from './components/MoodInput';
import ProfilePage from './components/ProfPage';
import CommunityPage from './components/Community';

import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
// ReactDOM.render((
//    <Router history = {browserHistory}>
//       <Route path = "/" component = {App}>
//          <IndexRoute component = {App} />
//          <Route path = "home" component = {App} />
//          <Route path = "mood input" component = {MoodPage} />
//          <Route path = "profile" component = {ProfilePage} />
//          <Route path = "communities" component = {CommunityPage} />
//       </Route>
//    </Router>
// ), document.getElementById('app'))
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
