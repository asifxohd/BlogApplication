import axios from "axios"
import { BASE_URL } from "../../constents"

export const loginUser = async (data) => {
    try {
        const response = await axios.post(`${BASE_URL}auth/login/`, data)
        // collecting access token and refersh token
        const { access, refresh } = response.data;
        localStorage.setItem('accessToken', access);
        localStorage.setItem('refreshToken', refresh);
        return response.data

    } catch (error) {
        throw error;
    }
};