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

const MyMenu = () => (
  <div>
    <Menu fixed='top' inverted>
      <Container>
        <Menu.Item as='a' header>
          <Image size='mini' src={logo} style={{ marginRight: '1.5em' }} />
        </Menu.Item>
        <Menu.Item as='a'>Record Mood</Menu.Item>
        <Menu.Item as='a'>My Moodzaic</Menu.Item>
        <Menu.Item as='a'>My Communities</Menu.Item>
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
