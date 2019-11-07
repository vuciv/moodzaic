//display errors maybe but like we can just not test this maybe

import React from 'react';
import ReactDOM from 'react-dom';
import SignUpForm from '../components/SignUp';

describe('SignUp', () => {
  //beforeEach stuff
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<SignUpForm />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
