import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import './App.css';
import { fetchListing, addListing } from './api';

import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import SearchBar from './components/layout/SearchBar';
import DatePicker from './components/partials/DatePicker.js';

import Home from './components/pages/Home';
import About from './components/pages/About';
import Register from './components/pages/Register';
import Login from './components/pages/Login';
import Search from './components/pages/Search';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      listings: [],
      listing: {},
      current_listing_id: 0,
      is_creating: true,
      is_fetching: true
    }

    this.handleItemClick = this.handleItemClick.bind(this);
    this.handleAddListing = this.handleAddListing.bind(this);
    this.handleSaveListing = this.handleSaveListing.bind(this);
    // this.handleData = this.handleData.bind(this);
    this.handleOnChange = this.handleOnChange.bind(this);
  }

  async handleItemClick(id) {
    let selected_listing = await fetchListing(id);

    this.setState({
      is_creating: false, 
      current_listing_id: id, 
      listing: selected_listing
    });
  }

  handleAddListing() {
    this.setState((prevState) => {
      return {is_creating: true}
    });
  }

  async handleSaveListing(data) {
    await addListing(data);
    await this.getData(); 
  }

  handleData(data) {
    let result = JSON.parse(data);

    let current_listing = this.state.listing;
    if (current_listing.id === result.id) {
      this.setState({listing: result}); 
    }
  }

  handleOnChange(e) {
    let content = e.target.value;
    let current_listing = this.state.listing;
    current_listing.content = content;

    this.setState({
      listing: current_listing
    });

    const socket = this.refs.socket;
    socket.state.ws.send(JSON.stringify(current_listing));
  }

  render() {
    return (
      <Router>
        <div className="page-container">
          <div className="content-wrap">
            <Header />
            <div style={{ paddingTop: '56px', paddingBottom: '20px' }}>
              <Route exact path="/" render={props=> (
                <React.Fragment>
                  <SearchBar />
                  <hr />
                  <Home />       
                </React.Fragment>
              )} />
              <Route path="/about" component={About} />
              <Route path="/register" component={Register} />
              <Route path="/login" component={Login} />
              <Route path="/search" component={Search} />
              <Route path="/date" component={DatePicker} />
            </div>
          </div>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;
