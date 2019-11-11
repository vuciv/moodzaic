//testing nothing for unit tests bc it takes in nothing
//renders a different page if username and password approved by backend?
import React from 'react';
import ReactDOM from 'react-dom';
import LoginForm from '../components/LogIn';

describe('LogIn', () => {
  //beforeEach stuff
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<LoginForm />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
