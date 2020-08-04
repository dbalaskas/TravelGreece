import React from 'react';
// import { Navbar, Row } from 'react-bootstrap';
import { Container } from 'react-bootstrap';


function Footer() {
    return (
        <div id="main-footer" className="primary" style={footer}>
            <Container>
                <div className="text-center">&copy;{new Date().getFullYear()} TravelGreece - All Rights Reserved | Terms of service | Ptivacy</div>
            </Container>
        </div>
    )
}

export default Footer;

const footer = {
	color: '#fff',
	background: '#444',
	padding: '2em 0 0 0',
	possition: 'relative',
	bottom: '0',
	width: '100%'
}