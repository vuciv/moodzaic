import React from 'react'
import {
  Container,
  Header,
  Form,
  Grid,
} from 'semantic-ui-react'
import CommunityService from '../CommunityService.js';




class MakeCommunity extends React.Component {
  state = {
    name: ''
  }

  handleChange = (e, { name, value }) => this.setState({ [name]: value })

  handleSubmit = () => {
      CommunityService.createCommunity(this.state.name); //but actually some community object with that name
      //at least, I think. I don't fucking know. it's almost 2 am im dead and also still dying somehow
      this.props.callback();
  }


  render() {
    return(
      <div>
        <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
          <Grid.Column style={{ maxWidth: 1000 }}>
            <Container text style={{ marginTop: '7em' }}>
              <Header as='h1' color='teal'>Creating A New Community</Header>
              <p>Your community needs a name to get started.
              After your community is created, anyone can join and post!
              </p>
              <Form>
                  <Form.Field onChange={this.handleChange}>
                    <label>Name of Community</label>
                    <input />
                  </Form.Field>
                  <Form.Button color='teal' onClick={this.handleSubmit}>
                    Create Community
                  </Form.Button>
              </Form>
            </Container>
          </Grid.Column>
        </Grid>
      </div>
    )
  }
}

export default MakeCommunity;
