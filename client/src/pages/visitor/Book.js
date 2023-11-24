import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import { AiOutlineCheck } from "react-icons/ai";

const Book = () => {
  const [books, setBooks] = useState([]);

  const borrow_book = (id) => () => {
    const borrow = async () => {
      // try {
      //   const response = await fetch(
      //     `http://localhost:5000/api/books/${id}/borrow`,
      //     {
      //       method: "GET",
      //       headers: {
      //         authorization: `Bearer ${localStorage.getItem("email")}`,
      //       },
      //     }
      //   );
      //   if (!response.ok) {
      //     throw new Error(response.error);
      //   }
      //   const data = await response.json();
      //   console.log(data);
      //   setBooks(data);
      // } catch (err) {
      //   alert(err);
      // }
      console.log("ok borrow");
    };
    if (window.confirm("Are you sure you want to borrow this book?")) {
      borrow();
    }
  };
  useEffect(() => {
    const get_books = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/books");

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
            <th>Available</th>
            <th>Action</th>
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
              <td>{book.is_available && <AiOutlineCheck />}</td>
              <td>
                {" "}
                <u className="cursor-pointer" onClick={borrow_book(book._id)}>
                  {book.is_available && "Borrow"}
                </u>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Book;
