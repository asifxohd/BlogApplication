import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'react-quill/dist/quill.snow.css'; 

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ToastContainer autoClose={4000}  />
    <App />
  </StrictMode>,
)
