import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import { AiOutlineCheck } from "react-icons/ai";

const Book = () => {
  const [books, setBooks] = useState([]);
  useEffect(() => {
    const get_books = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/books");
        const data = await response.json();
        console.log(data);
        setBooks(data);
      } catch {
        (err) => alert(err.message);
      }
    };
    get_books();
  }, []);
  return (
    <Container>
      <h3 className="color-blue mt-5 ">List of books</h3>
      <Table striped className="mt-5">
        <thead>
          <tr>
            <th>#</th>
            <th>Book ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Category</th>
            <th>Best seller</th>
            <th>Available</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{book._id}</td>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.category}</td>
              <td>{book.is_bestseller && <AiOutlineCheck />}</td>
              <td>{book.is_available && <AiOutlineCheck />}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Book;
