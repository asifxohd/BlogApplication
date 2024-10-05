import React, { useState } from "react";
import { Link, useNavigate } from 'react-router-dom';
import { useFormik } from 'formik';
import { toast } from 'react-toastify';
import { loginValidationSchema } from "../../utils/validations/auth";
import { loginUser } from '../../services/api/Login';


const LoginCard = () => {
    const [error, setError] = useState('')
    const navigate = useNavigate();
    const formik = useFormik({
        initialValues: {
            username: '',
            password: '',
        },
        validationSchema: loginValidationSchema,
        onSubmit: async (values) => {

            try {
                const response = await loginUser(values)
                console.log(response);
                navigate('home')
                toast.success("login SuccessFull")
            } catch (error) {
                console.error('Login failed:', error?.response?.data);
                setError(error?.response?.data?.detail)
                toast.error('Login failed. Please try again.');
            }
        },
    });



    return (
        <div className="h-screen bg-gray-50">
            <div className="flex min-h-screen w-full items-center justify-center text-gray-600 bg-gray-50">
                <div className="relative">
                    <div className="hidden sm:block h-56 w-56 text-indigo-300 absolute a-z-10 -left-20 -top-20">
                    </div>
                    <div className="hidden sm:block h-28 w-28 text-indigo-300 absolute a-z-10 -right-20 -bottom-20">
                    </div>
                    <div className="relative flex flex-col sm:w-[30rem] rounded-lg border-gray-400 bg-white shadow-lg px-4">
                        <div className="flex-auto p-6">
                            <div className="mb-10 flex flex-shrink-0 flex-grow-0 items-center justify-center overflow-hidden">
                                <a href="#" className="flex cursor-pointer items-center gap-2 text-indigo-500 no-underline hover:text-indigo-500">
                                    <span className="flex-shrink-0 text-3xl font-black tracking-tight opacity-100">
                                        Blog Application
                                    </span>
                                </a>
                            </div>

                            <form onSubmit={formik.handleSubmit} className="mb-4">

                                <div className="mb-4">
                                    <label htmlFor="username" className="mb-2 inline-block text-xs font-medium uppercase text-gray-700">Username</label>
                                    <input
                                        type="text"
                                        id="username"
                                        name="username"
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        value={formik.values.username}
                                        className={`block w-full cursor-text appearance-none rounded-md border ${formik.touched.username && formik.errors.username
                                                ? 'border-red-500'
                                                : 'border-gray-400'
                                            } bg--100 py-2 px-3 text-sm outline-none focus:border-indigo-500 focus:bg-white focus:text-gray-600 focus:shadow`}
                                        placeholder="Enter your username"
                                        autoComplete="username"
                                    />
                                    {formik.touched.username && formik.errors.username ? (
                                        <div className="text-red-500 text-xs">{formik.errors.username}</div>
                                    ) : null}
                                </div>
                                <div className="mb-4">
                                    <div className="flex justify-between">
                                        <label className="mb-2 inline-block text-xs font-medium uppercase text-gray-700" htmlFor="password">Password</label>
                                    </div>
                                    <div className="relative flex w-full flex-wrap items-stretch">
                                        <input
                                            type="password"
                                            id="password"
                                            name="password"
                                            onChange={formik.handleChange}
                                            onBlur={formik.handleBlur}
                                            value={formik.values.password}
                                            className={`block w-full cursor-text appearance-none rounded-md border ${formik.touched.password && formik.errors.password
                                                    ? 'border-red-500'
                                                    : 'border-gray-400'
                                                } bg--100 py-2 px-3 text-sm outline-none focus:border-indigo-500 focus:bg-white focus:text-gray-600 focus:shadow`}
                                            placeholder="Enter your password"
                                            autoComplete="current-password"
                                        />
                                        {formik.touched.password && formik.errors.password ? (
                                            <div className="text-red-500 text-xs">{formik.errors.password}</div>
                                        ) : null}

                                    </div>
                                </div>

                                <div className="mb-4">
                                    <button className="grid w-full cursor-pointer select-none rounded-md border border-indigo-400 bg-indigo-400 py-2 px-5 text-center align-middle text-sm text-white shadow hover:border-indigo-600 hover:bg-indigo-600 hover:text-white focus:border-indigo-600 focus:bg-indigo-600 focus:text-white focus:shadow-none" type="submit">
                                        Sign in
                                    </button>
                                </div>
                                {error ? (
                                    <div className=" text-center text-red-500 text-xs">{error}</div>
                                ) : null}
                            </form>
                            <p className="mb-4 text-center">
                                Don't Have An Account?
                                <Link to="/register" className="cursor-pointer text-blue-500 no-underline hover:text-blue-500"> Create an account</Link>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default LoginCard;
