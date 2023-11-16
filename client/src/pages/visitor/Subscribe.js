import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

const Subscribe = () => {
  return (
    <Container className="mt-5">
      <h5 className="color-blue mt-5">
        You have subscribed for the updates of new books at Houston Library
      </h5>
      <Button variant="primary">Unsubscribe!</Button>
    </Container>
  );
};

export default Subscribe;
