import React from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import { useLocation, useNavigate, Outlet } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { pathname } = location;
  const isActive = pathname.split("/")[2];

  const handleClick = (page) => () => {
    navigate(`/admin/${page}`);
  };

  return (
    <Container className="text-center mt-5">
      <h5 className="d-flex justify-content-end">Admin Email</h5>
      <h6 className="d-flex justify-content-end">admin_test@gmail.com</h6>
      <Nav
        fill
        variant="tabs"
        defaultActiveKey="/visitor/books"
        className="mt-5 mb-5"
      >
        <Nav.Item
          className={isActive === "books" ? "is-active" : "not-active"}
          onClick={handleClick("books")}
        >
          <Nav.Link>Books</Nav.Link>
        </Nav.Item>
        <Nav.Item
          className={isActive === "borrow" ? "is-active" : "not-active"}
          onClick={handleClick("borrow")}
        >
          <Nav.Link>Borrow books</Nav.Link>
        </Nav.Item>
      </Nav>
      <Outlet />
    </Container>
  );
};

export default Home;
