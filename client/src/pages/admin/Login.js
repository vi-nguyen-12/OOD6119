import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/esm/Button";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const onSubmit = async () => {
    if (email === "admin@gmail.com") {
      return navigate("/admin/home");
    }
    alert("Please enter admin email to login");
  };
  return (
    <Container className="d-flex flex-column align-items-center justify-content-center">
      <h2 className="mb-5">Visitor</h2>
      <h4 className="mt-5">Log in</h4>
      <label> Please enter your email to login:</label>
      <input
        type="text"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <Button variant="primary" className="mt-3" onClick={onSubmit}>
        {" "}
        Submit
      </Button>
    </Container>
  );
};

export default Login;
