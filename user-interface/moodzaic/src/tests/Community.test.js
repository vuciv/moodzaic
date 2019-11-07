//render correct community and existing posts
//that means rendering the name of the community as an h1
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
