import React from 'react';
import ReactDOM from 'react-dom';
import MoodPage from '../components/MoodInput';
import { unmountComponentAtNode } from "react-dom";

let container = null;
beforeEach(() => {
  // setup a DOM element as a render target
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  // cleanup on exiting
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

describe('MoodInput', () => {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<MoodPage />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
  it("Entering username and password updates state", () => {
      //update and expect
  });
})
