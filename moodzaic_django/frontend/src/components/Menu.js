import React from 'react'
import logo from '../logo.png';
import {
  Container,
  Divider,
  Dropdown,
  Grid,
  Header,
  Image,
  List,
  Menu,
  Segment,
} from 'semantic-ui-react'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

const MyMenu = () => (
  <div>
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as={Link} to="/MyMood" header>
          <Image size='mini' src={logo} style={{ marginRight: '1.5em' }} />
        </Menu.Item>
        <Menu.Item as={Link} to="/MyMood">Record Mood</Menu.Item>
        <Menu.Item as={Link} to="/Profile">My Moodzaic</Menu.Item>
        <Menu.Item as={Link} to="/Communities">My Communities</Menu.Item>
      </Container>
    </Menu>
  </div>
)

export default MyMenu;

// <Dropdown item simple text='Dropdown'>
//   <Dropdown.Menu>
//     <Dropdown.Item>List Item</Dropdown.Item>
//     <Dropdown.Item>List Item</Dropdown.Item>
//     <Dropdown.Divider />
//     <Dropdown.Header>Header Item</Dropdown.Header>
//     <Dropdown.Item>
//       <i className='dropdown icon' />
//       <span className='text'>Submenu</span>
//       <Dropdown.Menu>
//         <Dropdown.Item>List Item</Dropdown.Item>
//         <Dropdown.Item>List Item</Dropdown.Item>
//       </Dropdown.Menu>
//     </Dropdown.Item>
//     <Dropdown.Item>List Item</Dropdown.Item>
//   </Dropdown.Menu>
// </Dropdown>
