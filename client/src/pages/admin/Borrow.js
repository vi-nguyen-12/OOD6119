import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import { get_due_date, get_today_str } from "../../helper";
import axios from "axios";
import { AiOutlineCheck } from "react-icons/ai";

const Borrow = () => {
  const [books, setBooks] = useState([]);

  const return_book = (transaction_id) => async () => {
    try {
      const response = await axios.post(
        `http://localhost:5000/api/visitors/return`,
        { transaction_id }
      );
      if (response.status !== 200) {
        throw new Error(response.error);
      }

      setBooks((prev) => {
        return prev.map((b) =>
          b.transaction_id == transaction_id
            ? { ...b, return_date: get_today_str() }
            : b
        );
      });
      alert(response.data.message);
    } catch {
      (err) => {
        alert(err.message);
      };
    }
  };
  useEffect(() => {
    const get_borrow_books = async () => {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/books/borrowed`
        );

        console.log(response.data);
        setBooks(response.data);
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
            <th>Membership</th>
            <th>Book ID</th>
            <th>Title, Author,Category</th>
            <th>Best seller</th>

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
              <td>{b.is_member ? <AiOutlineCheck /> : ""}</td>
              <td>{b.book_id}</td>
              <td>
                <div>{b.title}</div>

                <div style={{ fontSize: "0.8rem", marginTop: "7px" }}>
                  {b.author}
                </div>
                <div style={{ fontSize: "0.7rem" }}> {b.category}</div>
              </td>
              <td>{b.is_bestseller ? <AiOutlineCheck /> : ""}</td>

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
                        onClick={return_book(b.transaction_id)}
                      >
                        Pay & Return
                      </Button>
                    ) : (
                      <Button
                        className="primary xs"
                        onClick={return_book(b.transaction_id)}
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
