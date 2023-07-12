import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';  // Import your App component
import { BrowserRouter } from 'react-router-dom';
import { GlobalProvider } from "./context/Globalcontext";
ReactDOM.render(
  <React.StrictMode>
  <GlobalProvider>
      <BrowserRouter>
          <App />
      </BrowserRouter>
  </GlobalProvider>
  </React.StrictMode>,
  document.getElementById('root')  
)