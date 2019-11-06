import React from 'react';
import ReactDOM from 'react-dom';
import App from '../components/App';
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

// describe('App Component', () => {
//
//     let wrapper;
//     beforeEach(() => {
//         const initialState = {
//             posts: [{
//                 title: 'Example title 1',
//                 body: 'Some text'
//             }, {
//                 title: 'Example title 2',
//                 body: 'Some text'
//             }, {
//                 title: 'Example title 3',
//                 body: 'Some text'
//             }]
//         }
//         wrapper = setUp(initialState);
//     });
//
//     it('Should render without errors', () => {
//         const component = findByTestAtrr(wrapper, 'appComponent');
//         expect(component.length).toBe(1);
//     });
//
//     it('exampleMethod_updatesState Method should update state as expected', () => {
//         const classInstance = wrapper.instance();
//         classInstance.exampleMethod_updatesState();
//         const newState = classInstance.state.hideBtn;
//         expect(newState).toBe(true);
//     });
//
//     it('exampleMethod_returnsAValue Method should return value as expected', () => {
//         const classInstance = wrapper.instance();
//         const newValue = classInstance.exampleMethod_returnsAValue(6);
//         expect(newValue).toBe(7);
//     });
//
//
// });

// let container = null;
// beforeEach(() => {
//   // setup a DOM element as a render target
//   container = document.createElement("div");
//   document.body.appendChild(container);
// });
//
// afterEach(() => {
//   // cleanup on exiting
//   unmountComponentAtNode(container);
//   container.remove();
//   container = null;
// });

describe('Things relating to the login screen', () => {
  //beforeEach stuff
  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<App />, div);
    ReactDOM.unmountComponentAtNode(div);
  });

  it("Entering correct username and password opens main page", () => {
    act(() => {
      render(<App />, container);
    });
    //expect();
  });
  it("Entering username and password updates state", () => {
      //update and expect
  });
})

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

//Outputs new username and password to backend as expected (backend will initialize new user)
//Load user profile information properly
//Switch to menu/input page
