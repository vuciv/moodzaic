//make a dummy struct with all the info and test that given that struct,
//it writes those thing
//probably name as an h1 and the other stuff as ps?

import React from 'react';
import ProfilePage from '../components/ProfPage';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";

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


it("Profile page initializes text properly", () => {
  act(() => {
    render(<ProfilePage Name="Jack" Username="GiveMeTheSalt" Gender="M" ProgressScore="0.33" />, container);
  })
  expect(container.textContent).toBe("Profile: Jack 'GiveMeTheSalt'");
  console.log("This is printing from ProfPage.test.js")
})

//{Name, Username, Age, Gender, ProgressScore}
