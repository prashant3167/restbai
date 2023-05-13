import React, { useState } from "react";
import "./App.css";
import AnimatedMulti from "./AnimatedMulti";
import optionsa from "./data.json";
import TextField from "@mui/material/TextField";


function App() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [propertyid, setpropertyid] = useState("");
  const [childData, setChildData] = useState({
    interior: [],
    kitchen: [],
    appliances: [],
    countbed: 1,
    countwash: 1,
    // Add more child components as needed
  });
  // console.log(optionsa);


  const handleDataChange = (childId, data) => {
    setChildData((prevData) => ({
      ...prevData,
      [childId]: data,
    }));
  };

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
  };
  const handleBedChange = (event) => {
    // setChildData(childId, event.target.value);
    setChildData((prevData) => ({
      ...prevData,
      countbed: event.target.value, // Update the value for the countbed key
    }));
  };
  const handleWashChange = (event) => {
    // setChildData(childId, event.target.value);
    setChildData((prevData) => ({
      ...prevData,
      countwash: event.target.value, // Update the value for the countbed key
    }));
  };
  const handlePropertyIdChange = (event) => {
    setpropertyid(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    console.log(childData);

    if (selectedFiles.length === 0) {
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append("files", selectedFiles[i]);
    }

    formData.append("name", propertyid);
    formData.append(
      "interior",
      childData.interior.map(({ value }) => value)
    );
    formData.append(
      "kitchen",
      childData.kitchen.map(({ value }) => value)
    );
    formData.append(
      "appliances",
      childData.appliances.map(({ value }) => value)
    );
    formData.append("totalBedroom", childData.countbed);
    formData.append("totalWashroom", childData.countwash);

    fetch("http://verifier:8000/upload", {
      method: "POST",
      body: formData,
      headers: {
        'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        "Accept": "*/*",
        },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <form className="file-upload-form" onSubmit={handleFormSubmit}>
      <div className="form-group">
        <label htmlFor="name">PropertyID:</label>
        <input
          type="text"
          id="name"
          value={propertyid}
          onChange={handlePropertyIdChange}
        />
      </div>

      <TextField
        childId="countbed"
        inputProps={{ inputMode: "numeric", pattern: "[0-9]*" }}
        id="demo-helper-text-misaligned"
        label="Bedrooms"
        onChange={handleBedChange}
      />
      <TextField
        childId="countwash"
        inputProps={{ inputMode: "numeric", pattern: "[0-9]*" }}
        label="Washrooms"
        onChange={handleWashChange}
      />
      <AnimatedMulti
        childId="bedroom"
        options={optionsa.interior}
        onChange={handleDataChange}
        placeholder={<div>Select Interior amenities</div>}
      />
      <AnimatedMulti
        childId="kitchen"
        options={optionsa.kitchen}
        onChange={handleDataChange}
        placeholder={<div>Select Kitchen amenities</div>}
      />
      <AnimatedMulti
        childId="appliances"
        options={optionsa.appliances}
        onChange={handleDataChange}
        placeholder={<div>Select appliances available</div>}
      />

      <div className="form-group">
        <label htmlFor="files">Select Property Images:</label>
        <input type="file" id="files" multiple onChange={handleFileChange} />
      </div>
      <button type="submit">Verify</button>
    </form>
  );
}

export default App;
