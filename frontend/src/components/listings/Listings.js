import React, { Component } from 'react';
import Listing from './Listing';
import PropTypes from 'prop-types';

export class Listings extends Component {
    render() {
        return this.props.listings.map((listing) => (
            <Listing key={ listing.id } listing={ listing } rented={ this.props.rented } />
        ));
    }
}

// PropTypes
Listings.propTypes = {
    listings: PropTypes.array.isRequired
}

export default Listings;