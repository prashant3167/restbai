// import React from 'react';
import "./SecondPage.css";

import Container from '@material-ui/core/Container';
import CitiesSlider from './script';

import RowAndColumnSpacing from './Amm';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';






const DataModule = () => {
  const [data, setData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
 const {id} = useParams();
 console.log(id);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:8000/advert/'+id);
        const jsonData = await response.json();
        setData(jsonData);
        setIsLoading(false);
      } catch (error) {
        console.log('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
  if (isLoading) {
    return <p>Loading data...</p>;
  }
  return (
    <div>
    <h1 className="entry-title" itemProp="headline">{data.title}</h1>
      <CitiesSlider slides={data.images} />
      <Container className="spage" maxWidth="Lg">
      
      <h2 className="entry-title" itemProp="headline">{data.description}</h2>

      {data.length === 0 ? (
        <p>Loading data...</p>
      ) : (
        <div>
            <div>
            <RowAndColumnSpacing items={data.red} status='error'/>
            </div>
            <div>
            <RowAndColumnSpacing items={data.yellow} status='warning'/>
            </div>
            <div>
            <RowAndColumnSpacing items={data.green} status='success'/>
            </div>
        </div>
        
      )}
      </Container>
    </div>
  );
};

export default DataModule;
