//conditionally render form to send an invite, if iammod
//render correct community and list of members (?)
//that means rendering the name of the community as an h1
//at some point in the future, communities will need to maintain message list, but not for this iteration!!
import React from 'react';
import ReactDOM from 'react-dom';
import Community from '../components/Community';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";
import {configure, shallow} from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({adapter: new Adapter() })


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

describe('Community', function() {
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<Community />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
  it("Profile page initializes text properly", () => {
    act(() => {
      render(<Community communityName="Idontwantthat" Posts={["hello","hello2"]}/>, container);
    })
    expect(container.textContent).toBe("Idontwantthathellohello2");
    console.log("This is printing from ProfPage.test.js")
  });


})
