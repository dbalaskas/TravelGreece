import React from 'react';
import { Container } from 'react-bootstrap';
import '../../css/style.css';


function SearchBar() {
    return (
  			<div id="showcase">
	    		<Container>
	    			<div className="text-center">
	    				<div className="home-search p-4">
				        <div className="overlay p-4">
				          <h1 className="display-6 mb-4">Find your room!</h1>
			    				<div className="search">
				            <form action="...">
				              <div className="form-row">
				                <div className="col-md-4 mb-3">
				                  <label className="sr-only">City</label>
				                  <input type="text" name="city" className="form-control" placeholder="City" />
				                </div>
				                <div className="col-md-4 mb-3">
				                  <label className="sr-only">State</label>
				                  <select name="visitors" className="form-control">
				                    <option selected="true" disabled="disabled">Number of visitors</option>
				                    {Visitors.map((visitor) => {
				                      return <option value={ visitor }>{ visitor }</option>
				                    })}
				                  </select>
				                </div>
				               </div>
				              <button className="btn btn-primary btn-block mt-4" type="submit">Search</button>
				            </form>
				          </div>
			    			</div>
		    			</div>
	    			</div>
	    		</Container>
	    	</div>
        // <Navbar bg="primary" expand="lg" variant="dark" fixed="top">
        // <Navbar.Brand href="/">TravelGreece</Navbar.Brand>
        // <Navbar.Toggle aria-controls="basic-navbar-nav" />
        // <Navbar.Collapse id="basic-navbar-nav">
        //     <Nav className="mr-auto">
        //         <Nav.Link href="/">Home</Nav.Link>
        //         <Nav.Link href="/about">About</Nav.Link>
        //     </Nav>
        //     <Nav>
        //         <Nav.Link href="/register"><FontAwesomeIcon icon={faUserPlus} /> Register</Nav.Link>
        //         <Nav.Link href="/login"><FontAwesomeIcon icon={faSignInAlt} /> Login</Nav.Link>
        //     </Nav>
        // </Navbar.Collapse>
        // </Navbar>
    )
}

const Visitors = [1,2,3,4,5,6,7,8,9,10];

export default SearchBar;