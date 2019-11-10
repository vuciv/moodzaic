import React from 'react'
import {
  Container,
  Button,
} from 'semantic-ui-react'
import { addCommunity, isMyCommunity } from '../integration_funcs.js'

function AllCommunities({allCommunities}) {
  const communities = allCommunities.map((com, i) => {
    return <Button
              color='teal' fluid size='large'
              key = {i}
              onClick = {addCommunity(com)}>
              {com}: {isMyCommunity(com) ? 'added!' : 'add?'}
            </ Button>;
  })

  return (
    <div>
      <Container text style={{ marginTop: '7em' }}>
        <p> should show all the communities and allow you to select any to join</p>
        {communities}
      </Container>
    </div>
  )
}


export default AllCommunities
