//conditionally render form to send an invite, if iammod
//render correct community and list of members (?)
//that means rendering the name of the community as an h1
//at some point in the future, communities will need to maintain message list, but not for this iteration!!
import React from 'react';
import ReactDOM from 'react-dom';
import Community from '../components/Community';

describe('Community', () => {
  //beforeEach stuff
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<Community />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
