//make a dummy struct with all the info and test that given that struct,
//it writes those thing
//probably name as an h1 and the other stuff as ps?

import React from 'react';
import ProfilePage from '../components/ProfPage';
import App from '../components/App';
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


describe('Profile tests', function() {

  it("Profile page initializes text properly", () => {
    act(() => {
      render(<ProfilePage Name="Jack" Username="GiveMeTheSalt" Gender="M" ProgressScore={33} />, container);
    })
    expect(container.textContent).toBe("Profile: Jack 'GiveMeTheSalt'");
    console.log("This is printing from ProfPage.test.js")
  });

  //This passes when App renders a ProfilePage!
  it("Shallow test", () => {
    const wrapper = shallow(<App />)
    expect(wrapper
    .find('ProfilePage').debug())
    .toEqual('<ProfilePage />');
  });

})
//{Name, Username, Age, Gender, ProgressScore}
