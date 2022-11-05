 import React from "react";
 import axios from "axios";

 export default class FloorList extends React.Component {
     state = {
         floors: [],
     };

componentDidMount(){
    axios.get(`https://unimaps-back.herokuapp.com/floor`).then(res => {
        console.log(res);
        res.data.map(andar=>{
            if(andar.number==this.props.andar){
                this.setState({floors: andar});
            }
        });
    });
}

render() {
    let floor=this.state.floors;
    return (
        <b>
            <b key={floor.building_id}>Numero de salas: {floor.room_quantity}</b>
        </b>
    )
}

 }