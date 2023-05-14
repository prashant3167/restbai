import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import MuiAlert from '@mui/material/Alert';
import Box from '@mui/material/Box';

const Item = styled(Paper)(({ theme }) => ({
//   backgroundColor: theme.palette.mode === 'dark' ? 'green' : 'red',
//   ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  fontSize: 'larger'
//   color: theme.palette.text.secondary,
}));

const Alert = React.forwardRef(function Alert(props, ref) {
    return <MuiAlert ref={ref}  {...props} />;
  });
        
        
{/* <Alert severity="success">{item}</Alert> */}

export default function RowAndColumnSpacing(props) {
  const { items,status } = props;
  return (
    (<Box sx={{ width: '100%', marginTop: '10px' }}>
      <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
        {items.map(l => <Grid item xs={3}><Item><Alert severity={status}>{l}</Alert> </Item></Grid>)}
      </Grid>
    </Box>)
  );
}