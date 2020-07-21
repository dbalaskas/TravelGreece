import React from 'react';
import { Navbar, Container, Row } from 'react-bootstrap';


function Footer() {
    return (
        // <Navbar bg="primary" expand="lg" variant="dark" fixed="bottom">
        <div id="main-footer" className="primary">
            <Container>
                <h4 className="text-center">Copyright &copy;{new Date().getFullYear()} TravelGreece - All Rights Reserved</h4>
            </Container>
        </div>
        // </Navbar>
    )
}

export default Footer;
