import React from 'react'
import logo from '../logo.png';
import {
  Header,
  Form,
  Comment
} from 'semantic-ui-react'
import { getPosts, sendPost } from '../integration_funcs.js'



// class FormExampleClearOnSubmit extends React.Component {
//   state = {}
//
//   handleChange = (e, { name, value }) => this.setState({ [name]: value })
//
//   handleSubmit = () => this.setState({ email: '', name: '' })
//
//   render() {
//     const { name, email } = this.state
//
//     return (
//       <Form onSubmit={this.handleSubmit}>
//         <Form.Group>
//           <Form.Input
//             placeholder='Name'
//             name='name'
//             value={name}
//             onChange={this.handleChange}
//           />
//           <Form.Input
//             placeholder='Email'
//             name='email'
//             value={email}
//             onChange={this.handleChange}
//           />
//           <Form.Button content='Submit' />
//         </Form.Group>
//       </Form>
//     )
//   }
// }

class Community extends React.Component {
  state = {}

  handleChange = (e, { message, value }) => this.setState({ [message]: value })

  handleSubmit = () => {
    // sendPost({poster: u,
    //           message: m,
    //           time: t,
    //           comment_list: []
    //         });
    this.setState({ message: '' });
  }

  render() {
    const { message } = this.state
    const community = this.props.myCommunity;
    const username = this.props.username;
    const posts = getPosts(community);

    var today = new Date();
    var date = (today.getMonth()+1)+'-'+today.getDate()+'/'+today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var now = date+' '+time;

    // function printComments(comments) {
    //   return (
    //     comments.map((c, i) => {
    //       return(
    //         <Comment key = {i}>
    //           <Comment.Avatar src={logo} />
    //           <Comment.Content>
    //             <Comment.Author as='a'>{c.poster}</Comment.Author>
    //             <Comment.Text>{c.message}</Comment.Text>
    //           </Comment.Content>
    //         </Comment>
    //       )
    //     })
    //   )
    // }

    const printPosts = posts.map((post, i) => {
      return (
        <Comment key = {i} >
          <Comment.Avatar src={logo} />
          <Comment.Content>
            <Comment.Author as='a'>{post.poster.name}</Comment.Author>
            <Comment.Metadata>
              <div>{post.time}</div>
            </Comment.Metadata>
            <Comment.Text>{post.message}</Comment.Text>
            <Comment.Actions>
              <Comment.Action>Reply</Comment.Action>
            </Comment.Actions>
          </Comment.Content>
          {post.comment_list.empty ? '' :
          <Comment.Group>
            {printPosts(post.comment_list)}
          </Comment.Group>
          }
        </Comment>
      )
    })

    return (
      <div>
        <Comment.Group>
          <Header as='h3' dividing>
            {community}
          </Header>

          {printPosts}

          <Form onSubmit={this.handleSubmit}>
            <Form.TextArea
              placeholder='Say something to the community!'
              name='message'
              value={message}
              onChange={this.handleChange}
            />
            <Form.Button
              content='Post'
              labelPosition='left'
              icon='edit' primary
            />
          </Form>
        </Comment.Group>
      </div>
    )
  }
}

// const CommentExampleComment = () => (
// <Comment.Group>
//   <Header as='h3' dividing>
//     Comments
//   </Header>
//
//   <Comment>
//     <Comment.Avatar src={logo} />
//     <Comment.Content>
//       <Comment.Author as='a'>Matt</Comment.Author>
//       <Comment.Metadata>
//         <div>Today at 5:42PM</div>
//       </Comment.Metadata>
//       <Comment.Text>How artistic!</Comment.Text>
//       <Comment.Actions>
//         <Comment.Action>Reply</Comment.Action>
//       </Comment.Actions>
//     </Comment.Content>
//   </Comment>
//
//   <Comment>
//     <Comment.Avatar src='/images/avatar/small/elliot.jpg' />
//     <Comment.Content>
//       <Comment.Author as='a'>Elliot Fu</Comment.Author>
//       <Comment.Metadata>
//         <div>Yesterday at 12:30AM</div>
//       </Comment.Metadata>
//       <Comment.Text>
//         <p>This has been very useful for my research. Thanks as well!</p>
//       </Comment.Text>
//       <Comment.Actions>
//         <Comment.Action>Reply</Comment.Action>
//       </Comment.Actions>
//     </Comment.Content>
//     <Comment.Group>
//       <Comment>
//         <Comment.Avatar src={logo} />
//         <Comment.Content>
//           <Comment.Author as='a'>Jenny Hess</Comment.Author>
//           <Comment.Metadata>
//             <div>Just now</div>
//           </Comment.Metadata>
//           <Comment.Text>Elliot you are always so right :)</Comment.Text>
//           <Comment.Actions>
//             <Comment.Action>Reply</Comment.Action>
//           </Comment.Actions>
//         </Comment.Content>
//       </Comment>
//     </Comment.Group>
//   </Comment>
//
//   <Comment>
//     <Comment.Avatar src={logo} />
//     <Comment.Content>
//       <Comment.Author as='a'>Joe Henderson</Comment.Author>
//       <Comment.Metadata>
//         <div>5 days ago</div>
//       </Comment.Metadata>
//       <Comment.Text>Dude, this is awesome. Thanks so much</Comment.Text>
//       <Comment.Actions>
//         <Comment.Action>Reply</Comment.Action>
//       </Comment.Actions>
//     </Comment.Content>
//   </Comment>
//
//   <Form reply>
//     <Form.TextArea />
//     <Button content='Add Reply' labelPosition='left' icon='edit' primary />
//   </Form>
// </Comment.Group>
// )



export default Community
