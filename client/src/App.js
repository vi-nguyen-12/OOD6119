import React, { useState, useEffect } from "react";
import Banner from "./components/Banner";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import VisitorLogin from "./pages/visitor/Login";
import VisitorBook from "./pages/visitor/Book";
import VisitorBorrow from "./pages/visitor/Borrow";
import VisitorSubscribe from "./pages/visitor/Subscribe";
import VisitorHome from "./pages/visitor/Home";
import AdminHome from "./pages/admin/Home";
import AdminBook from "./pages/admin/Book";
import AdminBorrow from "./pages/admin/Borrow";
import Home from "./pages/Home";

const App = () => {
  useEffect(() => {
    const getBooks = async () => {
      try {
        const result = await fetch("http://localhost:5000/api/books");
        const data = await result.json();
        console.log(data);
      } catch (err) {
        console.log("error");
        console.log(err);
      }
    };
    getBooks();
  }, []);
  return (
    <div>
      <Banner />
      <BrowserRouter>
        <Routes>
          <Route path="/visitor/login" element={<VisitorLogin />} />
          <Route path="/visitor" element={<VisitorHome />}>
            <Route path="books" element={<VisitorBook />} />
            <Route path="borrow" element={<VisitorBorrow />} />
            <Route path="subscribe" element={<VisitorSubscribe />} />
          </Route>
          <Route path="/admin" element={<AdminHome />}>
            <Route path="books" element={<AdminBook />} />
            <Route path="borrow" element={<AdminBorrow />} />
          </Route>

          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};
export default App;
