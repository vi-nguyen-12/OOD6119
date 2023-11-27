import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import { get_due_date, get_today_str } from "../../helper";

const Borrow = () => {
  const [books, setBooks] = useState([]);

  const return_book = (visitor_email, book_id) => async () => {
    try {
      const response = await fetch(
        `http://localhost:5000/api/visitors/return`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ visitor_email, book_id }),
        }
      );
      if (response.status !== 200) {
        throw new Error(response.error);
      }
      const data = await response.json();
      setBooks((prev) => {
        return prev.map((b) =>
          b.visitor_email === visitor_email && b.book_id === book_id
            ? { ...b, return_date: get_today_str() }
            : b
        );
      });
      alert(data.message);
    } catch {
      (err) => {
        alert(err.message);
      };
    }
  };
  useEffect(() => {
    const get_borrow_books = async () => {
      try {
        const response = await fetch(
          `http://localhost:5000/api/books/borrowed`
        );
        if (response.status !== 200) {
          throw new Error(response.error);
        }
        const data = await response.json();

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
            <th>Visitor email</th>
            <th>Book ID</th>
            <th>Title</th>
            <th>Author</th>
            <th>Category</th>
            <th>Borrowed Date</th>
            <th>Borrowed Due Date</th>
            <th>Return Date</th>
            <th>Late fee</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {books.map((b, idx) => (
            <tr key={idx}>
              <td>{idx + 1}</td>
              <td>{b.visitor_email}</td>
              <td>{b.book_id}</td>
              <td>{b.title}</td>
              <td>{b.author}</td>
              <td>{b.category}</td>
              <td>{b.borrow_date}</td>
              <td>{get_due_date(b.borrow_date)}</td>
              <td>{b.return_date}</td>
              <td>{b.late_fee}</td>
              <td className="d-flex">
                {!b.return_date && (
                  <>
                    {b.late_fee > 0 ? (
                      <Button
                        className="primary xs"
                        onClick={return_book(b.visitor_email, b.book_id)}
                      >
                        Pay & Return
                      </Button>
                    ) : (
                      <Button
                        className="primary xs"
                        onClick={return_book(b.visitor_email, b.book_id)}
                      >
                        Return
                      </Button>
                    )}
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Borrow;
