import React from 'react'
import {
  Container,
  Message,
  Segment
} from 'semantic-ui-react'


class Reminders extends React.Component {
  state = {
        myReminders: [],
  }

  componentDidMount() {
    fetch('')
      .then(response => response.json())
      .then(data => this.setState({ myReminders : data }));
  }

  toggleAddMode = () => {
    this.setState(prevState => ({
      AddMode: !prevState.AddMode
    }))
  }

  render() {
    const myReminders = this.state.myReminders;
    var i;

    return (
      <div>
        <Container>
          for (i = 0; i < 3; i++) {
            <Message key = {myReminders.pop()} color = 'purple'>
            <Message.Header>Reminder!</Message.Header>
              <p>{r}</p>
            </Message>
          }
        </Container>
      </div>
    )
  }
}




export default Reminders;
