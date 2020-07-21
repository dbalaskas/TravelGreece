import React, { Component } from 'react';

export class AddTodo extends Component {
    state = {
        title: ''
    }

    onSubmit = (e) => {
        e.preventDefault();
        this.props.addTodo(this.state.title);
        this.setState({title: ''})
    }

    onChange = (e) => this.setState({[e.target.name]: e.target.value});

    render() {
        return (
            <div style={{ marginBottom: '0.5rem'}}>
                <form style={{ display: 'flex'}} onSubmit={this.onSubmit}>
                    <input
                        type="text"
                        name="title"
                        style={{flex: '10', padding: '5px'}}
                        placeholder="Add todo..."
                        value={this.state.title}
                        onChange={this.onChange}
                    />
                    <input
                        type="submit"
                        value="Add"
                        className="btn"
                        style={{flex: '1'}}
                    />
                </form>
            </div>
        )
    }
}

export default AddTodo
