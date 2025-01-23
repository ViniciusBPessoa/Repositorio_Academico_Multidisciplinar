import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nome: "Vinicius",
      novoNome: ""
    };
  }

  handleChange = (event) => {
    this.setState({ novoNome: event.target.value });
  }

  handleClick = () => {
    this.setState({ nome: this.state.novoNome });
  }

  render() {
    return (
      <div>
        <p>Olá, {this.state.nome}!</p>
        <input type="text" value={this.state.novoNome} onChange={this.handleChange} />
        <button onClick={this.handleClick}>Alterar Nome</button>
      </div>
    );
  }
}

export default App;