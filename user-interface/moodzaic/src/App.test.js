import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import renderer from 'react-test-renderer';
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";

/* Component hierarchy for reference
* App
* 1. LoginPage
*   a. LoginInstruction
    b. MakeAccount
*     i. NewUsernameForm
*     ii. NewPasswordForm
*   b. LoginForm
*     i. UsernameForm
*     ii. PasswordForm
* 2. Menu
* 3. MoodInputPage
* 4. ProfilePage
* 5. CommunityPage
*/

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

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

//example
/*it("renders with or without a name", () => {
  act(() => {
    render(<Hello />, container);
  });
  expect(container.textContent).toBe("Hey, stranger");

  act(() => {
    render(<Hello name="Jenny" />, container);
  });
  expect(container.textContent).toBe("Hello, Jenny!");

  act(() => {
    render(<Hello name="Margaret" />, container);
  });
  expect(container.textContent).toBe("Hello, Margaret!");
});*/

//Outputs existing username and password to backend as expected
it("Entering username and password updates state", () => {
  act(() => {
    render(<App />, container);
  });
});
//Outputs new username and password to backend as expected (backend will initialize new user)
//Load user profile information properly
//Switch to menu/input page
