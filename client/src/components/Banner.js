import React from "react";
import { useNavigate } from "react-router-dom";

const Banner = () => {
  const navigate = useNavigate();

  return (
    <h1
      style={{ color: "red" }}
      className="mt-4 ml-4 fixed-top cursor-pointer"
      onClick={() => navigate("/")}
    >
      Houston Library
    </h1>
  );
};

export default Banner;
