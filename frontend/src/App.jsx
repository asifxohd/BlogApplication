import LoginPage from "./pages/LoginPage"
import RegisterCard from "./components/auth/RegisterCard";
import { BrowserRouter, Navigate, Route, Routes, useNavigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PrivetRouter from "./routes/PrivetRouter";
import Blogs from "./components/home/Blog";
import MyBlogs from "./components/home/MyBlogs";
import CreatePost from "./components/home/CreatePost";
import Profile from "./components/home/Profile";

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<LoginPage />} />
				<Route path="register" element={<RegisterCard />} />
				<Route path="home" element={<PrivetRouter />}>
					<Route path="" element={<Blogs />} /> 
					<Route path="my-blogs" element={<MyBlogs />} /> 
					<Route path="create-post" element={<CreatePost />} /> 
					<Route path="profile" element={<Profile />} /> 
					{/* <Route path="logout" element={<LogoutModalConfirmation />} /> */}
				</Route>
			</Routes>
		</BrowserRouter>
	);
}

export default App
