//selectively displays either community component or mycommunities component
import React from 'react';
import ReactDOM from 'react-dom';
import CommunityPage from '../components/CommunityPage';

describe('CommunityPage', () => {
  //beforeEach stuff
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<CommunityPage />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
