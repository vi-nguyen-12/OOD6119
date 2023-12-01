import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import { AiOutlineCheck } from "react-icons/ai";
import axios from "axios";

const Book = () => {
  const [books, setBooks] = useState([]);
  const [showCreateBookModal, setShowCreateBooModal] = useState(false);
  const [newBookValue, setNewBookValue] = useState({
    title: "",
    author: "",
    category: "",
    is_bestseller: false,
    age_range: "",
    technology: "",
    awards: "",
    challenges: "",
    subject: "",
    artists: "",
  });

  const handleShowCreateBookModal = () => {
    setShowCreateBooModal(!showCreateBookModal);
  };

  const handleChange = (e) => {
    if (e.target.name === "is_bestseller") {
      setNewBookValue((prev) => ({
        ...prev,
        [e.target.name]: e.target.checked,
      }));
      return;
    }
    setNewBookValue((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const createBook = async () => {
    try {
      let data = {
        title: newBookValue.title,
        author: newBookValue.author,
        category: newBookValue.category,
        is_bestseller: newBookValue.is_bestseller,
        // is_bestseller: "tye",
      };
      switch (newBookValue.category) {
        case "Kids":
          data = { ...data, age_range: newBookValue.age_range };
          break;
        case "ScienceFiction":
          data = { ...data, technology: newBookValue.technology };
          break;
        case "Literary":
          data = { ...data, awards: newBookValue.awards };
          break;
        case "Adventure":
          data = { ...data, challenges: newBookValue.challenges };
          break;
        case "Biography":
          data = { ...data, subject: newBookValue.subject };
          break;
        case "Comics":
          data = { ...data, artists: newBookValue.artists };
          break;
        default:
      }
      const response = await axios.post(
        "http://localhost:5000/api/books/add",
        data,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      alert(response.data.message);
      handleShowCreateBookModal();
      setNewBookValue(() => ({
        title: "",
        author: "",
        category: "",
        is_bestseller: false,
        age_range: "",
        technology: "",
        awards: "",
        challenges: "",
        subject: "",
        artists: "",
      }));
    } catch {
      (err) => {
        alert(err.message);
      };
    }
  };

  useEffect(() => {
    const get_books = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/books");

        setBooks(response.data);
      } catch {
        (err) => alert(err.message);
      }
    };
    get_books();
  }, []);
  return (
    <Container>
      <div className="mt-5 position-relative">
        <div className="position-absolute start-0">
          <Button onClick={handleShowCreateBookModal}>Create new book</Button>
        </div>
        <h3 className="color-blue">List of books</h3>
      </div>

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
              <td>{book.is_bestseller ? <AiOutlineCheck /> : ""}</td>
              <td>{book.is_available ? <AiOutlineCheck /> : ""}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      <Modal show={showCreateBookModal} onHide={handleShowCreateBookModal}>
        <Modal.Header closeButton>Create new book</Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group htmlFor="title">
              <Form.Label>Title</Form.Label>
              <Form.Control
                type="text"
                name="title"
                value={newBookValue.title}
                onChange={handleChange}
              ></Form.Control>
            </Form.Group>
            <Form.Group htmlFor="author">
              <Form.Label>Author</Form.Label>
              <Form.Control
                type="text"
                name="author"
                value={newBookValue.author}
                onChange={handleChange}
              ></Form.Control>
            </Form.Group>
            <Form.Group htmlFor="category" className="mt-3">
              <Form.Label>Category</Form.Label>
              <Form.Select
                className="ml-2"
                name="category"
                onChange={handleChange}
              >
                <option>Open this select menu</option>
                <option value="Kids">Kids</option>
                <option value="ScienceFiction">Science Fiction</option>
                <option value="Literary">Literary</option>
                <option value="Adventure">Adventure</option>
                <option value="Biography">Biography</option>
                <option value="Comics">Comics</option>
              </Form.Select>
            </Form.Group>

            {newBookValue.category === "Kids" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Age Range</Form.Label>
                <Form.Control
                  type="text"
                  name="age_range"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            {newBookValue.category === "ScienceFiction" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Technology</Form.Label>
                <Form.Control
                  type="text"
                  name="technology"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            {newBookValue.category === "Literary" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Awards</Form.Label>
                <Form.Control
                  type="text"
                  name="awards"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            {newBookValue.category === "Adventure" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Challenges</Form.Label>
                <Form.Control
                  type="text"
                  name="challenges"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            {newBookValue.category === "Biography" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Subject</Form.Label>
                <Form.Control
                  type="text"
                  name="subject"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            {newBookValue.category === "Comics" && (
              <Form.Group htmlFor="additional_field">
                <Form.Label>Artist</Form.Label>
                <Form.Control
                  type="text"
                  name="artists"
                  value={newBookValue.additional_field}
                  onChange={handleChange}
                ></Form.Control>
              </Form.Group>
            )}
            <Form.Group htmlFor="is_bestseller" className="mt-3">
              <Form.Check
                name="is_bestseller"
                label="Is book best seller ?"
                checked={newBookValue.is_bestseller}
                onChange={handleChange}
              ></Form.Check>
            </Form.Group>
          </Form>
          <Button variant="primary" onClick={createBook}>
            Submit
          </Button>
        </Modal.Body>
      </Modal>
    </Container>
  );
};

export default Book;
