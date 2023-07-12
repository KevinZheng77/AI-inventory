import React from 'react';
import { useGlobalContext } from '../context/Globalcontext';
import {useNavigate} from 'react-router-dom';
import Header from './Header';
import './dashboard.css';
const Dashboard = () => {

    const [userText, setUserText] = React.useState("");
    const { user, Inventory } = useGlobalContext();
    const navigate = useNavigate();
    console.log(Inventory);
    React.useEffect(()=> {
        if(!user && navigate){
            navigate("/");
        }
    }, [user, navigate]);

    return(
        <>
            <h2 className="inventoryTitle">Inventory Display</h2>
            <div className="inventory">
                {Array.isArray(Inventory) && Inventory.map((item, index) => (
                    <div key={index} className="inventoryItem">
                        <h3>{item.ProductName}</h3>
                        <p>Size: {item.Size}</p>
                        <p>Cost: {item.Cost}</p>
                        <p>Selling: {item.Selling}</p>
                    </div>
                ))}
            </div>
            <form>
                <div className="userText">
                    <label>Tell The AI What you would like to Add</label>
                    <input type="text" value={userText}
                        onChange={(e) => setUserText(e.target.value)}
                    />
                </div>
                <button type='submit'>Enter</button>
            </form>
            <Header/>
        </>
        
    )
}

export default Dashboard;