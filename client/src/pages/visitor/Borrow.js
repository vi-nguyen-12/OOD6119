import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import { get_due_date } from "../../helper";

const Borrow = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const email = localStorage.getItem("email");
    const get_borrow_books = async () => {
      try {
        const response = await fetch(
          `http://localhost:5000/api/visitors/${email}/books/borrowed`
        );
        if (response.status !== 200) {
          throw new Error(response.error);
        }
        const data = await response.json();
        console.log(data);
        setBooks(data);
      } catch (err) {
        alert(err);
      }
    };
    get_borrow_books();
  }, []);
  return (
    <Container>
      <h3 className="color-blue mt-5 ">List of borrow books</h3>
      <Table striped className="mt-5">
        <thead>
          <tr>
            <th>#</th>
            <th>Book ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Category</th>
            <th>Borrowed Date</th>
            <th>Borrowed Due Date</th>
            <th>Return Date</th>
            <th>Late fee</th>
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
              <td>{book.borrow_date}</td>
              <td>{get_due_date(book.borrow_date)}</td>
              <td>{book.return_date}</td>
              <td>{book.late_fee}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Borrow;
