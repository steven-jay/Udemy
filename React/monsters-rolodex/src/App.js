
import './App.css';

const React = require('react');
const { CardList } = require('./Components/CardList/card-list.component')
const { SearchBox } = require('./Components/search-box/search-box.component')

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      monsters: [],
      searchField: '',
    }
    this._setChars = this._setChars.bind(this);
    this._getChars = this._getChars.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  async _getChars() {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const monsterData = await response.json();
    return monsterData
  }

  async _setChars() {
    // alternative way to write this is:
    // setChars().then(data => this.setState({ monsters: data }));
    this.setState({ monsters: await this._getChars() })
  }

  componentDidMount() {
    this._setChars();
  }

  handleChange(e) { this.setState({ searchField: e.target.value }, () => console.log(this.state.searchField)) }
  /* alternatively, use arrow function notation i.e. const handleChange = e => { blah blah } to auto bind to whatever declared the function
  i.e. App class */

  render() {
    const { monsters, searchField } = this.state;
    const filteredMonsters = monsters.filter(monster => monster.name.toLowerCase().includes(searchField.toLowerCase()))
    return (
      <div className="App">
        <h1>Monsters Rolodex</h1>
        <SearchBox placeholder='search monsters' handleChange={e => this.setState({ searchField: e.target.value }, () => console.log(this.state.searchField))} />
        {/* second argument in setState function is a callback function that runs once state has been updated, 
        allowing you to run a function as soon as the state has updated. This is because setState is an async function */}
        <CardList monsters={filteredMonsters} />
      </div>
    );
  };
}

export default App;
