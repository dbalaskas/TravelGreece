import React, { Component } from 'react';
import {v4 as uuid} from 'uuid';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import AddTodo from './components/AddTodo';
import Todos from './components/Todos';
import About from './components/pages/About';

class App extends Component {
  state = {
    todos: [
      {
        id: uuid(),
        title: 'Take out the trash',
        completed: false
      },
      {
        id: uuid(),
        title: 'Dinner with wife',
        completed: false
      },
      {
        id: uuid(),
        title: 'Meet the boss',
        completed: false
      }
    ]
  }

  // Toggle Complete
  markComplete = (id) => {
    this.setState({ todos: this.state.todos.map(todo => {
      if (todo.id === id) {
        todo.completed = !todo.completed
      }
      return todo;
    }) });
  }

  // Delete Todo
  delTodo = (id) => {
    this.setState({todos: [...this.state.todos.filter(todo => todo.id !== id)] });
  }

  // Add Todo
  addTodo = (title) => {
    const newTodo = {
      id: uuid(),
      title: title,
      completed: false
    }
    this.setState({todos: [...this.state.todos, newTodo] });
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Header />
          <div className="container" style={{ paddingTop: '70px', paddingBottom: '20px' }}>
            <Route exact path="/" render={props=> (
              <React.Fragment>
                  <AddTodo addTodo={this.addTodo} />
                  <Todos todos={ this.state.todos } markComplete={ this.markComplete } delTodo={this.delTodo} />
              </React.Fragment>
            )} />
            <Route path="/about" component={About} />
          </div>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;
