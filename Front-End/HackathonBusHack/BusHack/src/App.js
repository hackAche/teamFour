import React, { Component } from 'react';
import FloorList from "./FloorList";
import Modal from "react-modal";
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect
} from "react-router-dom";



class MapScreen extends Component {
  componentDidMount() {
    window.wheelzoom(this.e, { zoom: 0.1, maxZoom: 10 })
  }
  render() {
    let custom={content:{top:"50%", left:"50%", right:"auto", bottom:"auto", marginRight: "-50%", transform: 'translate(-50%, -50%)'}}
    let andar = this.props.match.params.id;
    const max = 4, min = 1;
    if (this.e) {
      window.triggerEvent(this.e, 'wheelzoom.destroy');
    }
    window.wheelzoom(this.e, { zoom: 0.1, maxZoom: 10 })
    return (<div>
      <Modal isOpen={this.state.open} onRequestClose={() => this.setState({ open: false })} style={custom}>
        <p>
          Sobre: Aplicativo web desenvolvido no Hackathon Ache.io, aplicativo para rastreio do fluxo de usuarios dos ônibus da UFPel. 
        </p>
      </Modal>
      <Modal isOpen={this.state.open2} onRequestClose={() => this.setState({ open2: false })} style={custom}>
          
          <form>
          <span>
          Contato:
          </span>
          <input></input>
          <br></br>
          <br></br>
          <span>
          Mensagem:
          </span>
          <input></input>
          </form>
          
      </Modal>
      <div id="sidebar" className={this.state.menu && "active"}>



        <div className="opcoes">
          <div className="toggle-btn" onClick={() => this.toggleSidebar()}>
            <i className="fa fa-bars"></i>
          </div>

          <form action="">
            <i className="fa fa-search"></i>
            <div className="dropdown">
              <button className="dropbtn">
                Pelotas
              </button>
              <div className="dropdown-content">
                <div className="submenu"><button className="dropbtn" >Quinze</button></div>
                <div className="submenu"><button className="dropbtn" >Mercado Publico</button></div>
                <div className="submenu"><button className="dropbtn" >Odontologia</button></div>
                <div className="submenu"><button className="dropbtn" >Campus 2</button> </div>
              </div>
            </div>
          </form>


        </div>


        <ul>
          <div className="brand-logo">
            <img src="/images/Logo.png" />
          </div>
          <li className="menu"><a href="">Home</a></li>
          <li className="menu"><a onClick={()=>this.setState({ open: true })}>Sobre</a></li>
          <li className="menu"><a onClick={()=>this.setState({ open2: true })}>Contato</a></li>
          <li className="footer">&copy;2022</li>
        </ul>
      </div>

      <div className="mapa">
        <img src={"/images/Maps.png"} ref={(e) => this.e = e} style={{ width: "100%", height: "99.6vh" }} />
      </div>

 
    </div>)
  }
  state = { menu: false, andar: 1, bottom: false }

  toggleSidebar() {
    this.setState({ menu: !this.state.menu })
  }
}



class App extends Component {

  render() {
    return (
      <Router>
        <Route path="/" exact> <Redirect from="/" to="/andar/1" /> </Route>
        <Route path="/andar/:id" component={MapScreen} />
      </Router>

    );
  }
}



export default App;