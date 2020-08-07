import React, { Component } from 'react';
import Listings from '../listings/Listings';
import { fetchListings, fetchListing } from '../../api';
import { Container } from 'react-bootstrap';

export class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {
      listings: [],
      listing: {},
      current_listing_id: 0,
      is_creating: true,
      is_fetching: true
    }

    this.getData = this.getData.bind(this);
  }

  componentDidMount() {
    this.getData();
  }

  async getData() {
    let data = await fetchListings();
    this.setState({listings: data.results});
  }

  // Rent Listing
  rentedListing = (url) => {
    this.setState({listings: [...this.state.listings.filter(listing => listing.url !== url)] });
    alert('Rented Listing '+url)
  }

  render() {
      return (
        <React.Fragment>
        	<Container>
        		<h2 className="text-center">Best for you!</h2>
            <Listings listings={ this.state.listings } rented={ this.rentedListing } />
        	</Container>
        </React.Fragment>
  	)
  }
}

export default Home;
