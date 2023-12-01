import React, { useState, useEffect } from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";

const Catalog = () => {
  const [logs, setLogs] = useState([]);
  useEffect(() => {
    const get_logs = async () => {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/admins/logger`
        );

        setLogs(response.data);
      } catch (err) {
        alert(err.message);
      }
    };
    get_logs();
  }, []);
  return (
    <div>
      <h4>Admin Logger</h4>
      <Table striped className="mt-5">
        <thead>
          <tr>
            <th>#</th>
            <th>Activity</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{log}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Catalog;
