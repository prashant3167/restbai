import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Carousel from 'react-material-ui-carousel';
import { Paper } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  heading: {
    margin: theme.spacing(2),
  },
  carousel: {
    height: 300,
    margin: 'auto',
    width: '50%',
    [theme.breakpoints.down('sm')]: {
      width: '100%',
    },
  },
  description: {
    margin: theme.spacing(2),
  },
}));

const Listing = () => {
  const classes = useStyles();

  const carouselItems = [
    {
      img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/test/323570__000.jpg',
      description: 'Image 1',
    },
    {
      img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/test/323570__003.jpg',
      description: 'Image 2',
    },
    {
      img: 'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/test/323570__009.jpg',
      description: 'Image 3',
    },
  ];

  return (
    <div>
      <Typography variant="h4" className={classes.heading}>
        Heading
      </Typography>

      <Carousel className={classes.carousel}>
        {carouselItems.map((item, index) => (
          <Paper key={index}>
            <img src={item.img} alt={item.description} />
          </Paper>
        ))}
      </Carousel>

      <Typography variant="body1" className={classes.description}>
        Description
      </Typography>
    </div>
  );
};

export default Listing;
