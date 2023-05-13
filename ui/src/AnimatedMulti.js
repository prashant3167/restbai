import React from "react";
// import { useState } from 'react';
import Select from "react-select";
import makeAnimated from "react-select/animated";

const animatedComponents = makeAnimated();

export default function AnimatedMulti(props) {
  const { childId, options, onChange, placeholder } = props;

  const handleSelectChange = (selectedOptions) => {
    onChange(childId, selectedOptions);
  };

  return (
    <Select
      closeMenuOnSelect={false}
      components={animatedComponents}
      isMulti
      options={options}
      onChange={handleSelectChange}
      placeholder={placeholder}
    />
  );
}
