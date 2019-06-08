import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

    async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }
    constructor(props) {
    super(props);
    this.state = {
      city: []
    };
  }

  List(){
    return $.getJSON('http://127.0.0.1:8000/api/')
    .then(function(data) {
      return data.results;
    });
  }

  render() {
    this.List().then(function(res){
      this.state = {city: res};
    });
    return (
      <div id="layout-content" className="layout-content-wrapper">
        <div city="panel-list">
          {this.state.city((item, i) =>{
            return(
              <h1>{city}</h1>
              <span>{item.date},{item.highp},{item.lowp}</span>
            )
          })}
        <div>
      </div>
    )
  }
}
}

export default App;
