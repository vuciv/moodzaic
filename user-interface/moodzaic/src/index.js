import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import FixedMenuLayout from './FixedMenuLayout';
import * as serviceWorker from './serviceWorker';
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css" />


ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
