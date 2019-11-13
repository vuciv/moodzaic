import React from 'react'
import logo from '../logo.png';
import {
  Header,
  Form,
  Comment
} from 'semantic-ui-react'
import PostService from '../PostService.js';
// import { getPosts, sendPost } from '../integration_funcs.js'


class Community extends React.Component {
  state = {
    message: '',
    now: '',
    posts: []
  }

  componentDidMount() {
    PostService.getCommunityPosts().then(function (result) {
        this.setState({ posts:  result.data, nextPageURL:  result.nextlink})
        //yeah so like?? pretending this is a function??? hopefully it can be?????
    });
  }

  handleChange = (e, { message, value }) => this.setState({ [message]: value })

  handleSubmit = () => {
    PostService.createPost({
      message: this.state.message,
      community: this.props.myCommunity,
      poster: this.props.username,
      time: this.state.now, //or like probably userService.getUser by username somehow
    });
    this.setState({ message: '' });
  }

  setTime = (time) => {
    this.setState({ now: time });
  }

  render() {
    const { message } = this.state
    const community = this.props.myCommunity;
    const username = this.props.username;
    const posts = this.state.posts;

    var today = new Date();
    var date = (today.getMonth()+1)+'-'+today.getDate()+'/'+today.getFullYear();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var now = date+' '+time;

    this.setTime(now);


    // heyyyyyyy soooooo printing posts is not gonna work like this and idk how it will work
    //big oof for the ladies in the back
    //may help if we can get
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
