import React from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";

const Borrow = () => {
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
          <tr>
            <td>1</td>
            <td>8832</td>
            <td>This is where it ends</td>
            <td>Cindy K. Sporles</td>
            <td>Novel</td>
            <td>Oct 1, 2023</td>
            <td>Oct 15, 2023</td>
            <td>Oct 14, 2023</td>
            <td></td>
          </tr>
          <tr>
            <td>2</td>
            <td>4532</td>
            <td>Akira</td>
            <td>Katsuhiro Atomo</td>
            <td>Comics</td>
            <td>Oct 2, 2023</td>
            <td>Oct 16, 2023</td>
            <td></td>
            <td>$5</td>
          </tr>
        </tbody>
      </Table>
    </Container>
  );
};

export default Borrow;
