import React from 'react';
// import { Link } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';
import { faUserPlus, faSignInAlt } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";


function Header() {
    return (
        <Navbar bg="primary" expand="lg" variant="dark" fixed="top">
        <Navbar.Brand href="/">TravelGreece</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
                <Nav.Link href="/">Home</Nav.Link>
                <Nav.Link href="/about">About</Nav.Link>
            </Nav>
            <Nav>
                <Nav.Link href="/register"><FontAwesomeIcon icon={faUserPlus} /> Register</Nav.Link>
                <Nav.Link href="/login"><FontAwesomeIcon icon={faSignInAlt} /> Login</Nav.Link>
            </Nav>
        </Navbar.Collapse>
        </Navbar>
    )
}

export default Header;
