import React from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

const Borrow = () => {
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
          <tr>
            <th>1</th>
            <td>visitor1@gmail.com</td>
            <td>7876</td>
            <td>This is where it ends</td>
            <td>Cindy</td>
            <td>Novel</td>
            <td>Oct 1, 2023</td>
            <td>Oct 15, 2023</td>
            <td></td>
            <td>$5</td>
            <td className="d-flex">
              <Button className="primary mr-2 xs">Return</Button>
              <Button className="primary xs">Pay</Button>
            </td>
          </tr>
          <tr>
            <td>2</td>
            <td>user_test@gmail.com</td>
            <td>8487</td>
            <td>Diary of wimpy the kid</td>
            <td>Jeff</td>
            <td>Kids</td>
            <td>Nov 1</td>
            <td>Nov 16</td>
            <td></td>
            <td></td>
            <td>
              <Button variant="primary" className="mr-2 xs">
                Return
              </Button>
            </td>
          </tr>
        </tbody>
      </Table>
    </Container>
  );
};

export default Borrow;
