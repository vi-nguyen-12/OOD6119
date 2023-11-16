import React from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import { AiOutlineCheck } from "react-icons/ai";

const Book = () => {
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
          <tr>
            <td>1</td>
            <td>7478</td>
            <td>The Great Gasby</td>
            <td>FScott Fitzgerald</td>
            <td>Novel</td>
            <td>
              <AiOutlineCheck />
            </td>
            <td>Borrow</td>
          </tr>
          <tr>
            <td>2</td>
            <td>8782</td>
            <td>Little Red Riding Hood</td>
            <td>Charles Perrult</td>
            <td>Kids</td>
            <td>
              <AiOutlineCheck />
            </td>
            <td>Borrow</td>
          </tr>
          <tr>
            <td>3</td>
            <td>4625</td>
            <td>Elon Musk</td>
            <td>Walter Isaacson</td>
            <td>Biography</td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </Table>
    </Container>
  );
};

export default Book;
