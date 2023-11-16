import React from "react";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/esm/Button";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  return (
    <>
      <Col className="d-flex justify-content-center mt-5">
        <h4>You are</h4>
      </Col>
      <Col className="d-flex justify-content-center mt-4">
        <Button
          variant="primary"
          className="mr-5 py-3 px-5"
          onClick={() => navigate("/visitor/login")}
        >
          {" "}
          Visitor
        </Button>
        <Button variant="primary" className="ml-5 py-3 px-5">
          Admin
        </Button>
      </Col>
    </>
  );
};

export default Home;
