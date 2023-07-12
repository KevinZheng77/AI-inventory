import React, {createContext, useContext, useReducer, useEffect} from "react";
import axios from 'axios';

//initial state
const initialState = {
    user: null,
    fetchingUser: true,
    Inventory: [],
}

//reducer
const globalReducer = (state, action) => {
    switch(action.type) {
        case "SET_USER":
            return{
                ...state,
                user: action.payload,
                fetchingUser: false,
            };
        case "SET_INVENTORY":
            return{
                ...state,
                Inventory: action.payload.returnInventory,
            };
        case "RESET_USER":
            return{
                ...state,
                user: null,
                fetchingUser: false,
                Inventory: [],
            };
        default: 
        return state;
    }
}


//create the context
export const GlobalContext = createContext(initialState);

//provider component 
export const GlobalProvider = (props) => {
    const [state, dispatch] = useReducer(globalReducer, initialState);

    useEffect(() =>{
        getCurrentUser();
    }, [])
    //action: get current user
    const getCurrentUser = async () =>{
        try{
            console.log("get user is working")
            const res = await axios.get("/api/auth/current");
            if(res.data){
                const Inventory = await axios.get("/api/inventory/current");
                if(Inventory.data){
                    dispatch({type: "SET_USER", payload: res.data});
                    dispatch({
                        type: "SET_INVENTORY",
                        payload: Inventory.data,
                        
                      });
                }
            }else{
                dispatch({type: "RESET_USER"});
            }
        }catch(error){
            console.log(error)
            dispatch({type: "RESET_USER"});
        }
    };

    const logoutfunction = async () =>{
        try{
            console.log("THIS CLICKED");
            await axios.put("/api/auth/logout");
            dispatch({type: "RESET_USER"})
        }catch(error){
            console.log(error)
            dispatch({type: "RESET_USER"})
        }
    };

    const value = {
        ...state,
        getCurrentUser,
        logoutfunction,
    };

    return(
        <GlobalContext.Provider value={value}>
            {props.children}
        </GlobalContext.Provider>
    );
}

export function useGlobalContext(){
    return useContext(GlobalContext);
}