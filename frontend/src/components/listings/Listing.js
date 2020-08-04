import React, { Component } from 'react';
import PropTypes from 'prop-types';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Row, Col } from 'react-bootstrap';

export class Listing extends Component {
    getStyle = () => {
        return {
            backgroundColor: '#f4f4f4',
            padding: '10px',
            borderBottom: '1px #ccc dotted',
            textDecoration: this.props.listing.completed ? 'line-through' : 'none',
        }
    }

    render() {
        const { url, title } = this.props.listing;
        return (
            <div style={ this.getStyle() }>
                <Row>
                    <Col xs={8}>
                        <h3>
                            { title }
                        </h3>
                    </Col>
                    <Col xs={4}>
                        <button style={btnStyle} onClick={this.props.rented.bind(this, url)}>Rent!</button>
                    </Col>
                </Row>
            </div>
        )
    }
}

// PropTypes
Listing.propTypes = {
    listing: PropTypes.object.isRequired
}

const btnStyle = {
    background: '#ff0000',
    color: '#fff',
    border: 'none',
    padding: '5px 9px',
    borderRadius: '50%',
    cursor: 'pointer',
    float: 'right'
}

export default Listing;
