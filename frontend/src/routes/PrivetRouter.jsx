import React, { useEffect } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { SidebarDemo } from '../components/home/SideBar';

const PrivetRouter = () => {
    const accessToken = localStorage.getItem('accessToken');
    const navigate = useNavigate();

    useEffect(() => {
        if (!accessToken) {
            navigate('/'); 
        }
    }, [accessToken, navigate]); 

    return accessToken ? (
        <SidebarDemo>
            <Outlet />
        </SidebarDemo>
    ) : null; 
};

export default PrivetRouter;
