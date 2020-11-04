import logo from './logo.png';
import './App.css';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import React from 'react';
import Autocomplete from '@material-ui/lab/Autocomplete';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
      width: '20ch',
    },
  },
}));

const tripType = [
  {
    value: 'oneWay',
    label: 'One Way'
  },
  {
    value: 'rounded',
    label: 'Round Trip'
  }
];


function App() {
  const classes = useStyles();
  const [currency, setCurrency] = React.useState('oneWay');

  const handleChange = (event) => {
    setCurrency(event.target.value);
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p> Fly At Will </p>
        </header>
        <form className={classes.root} noValidate autoComplete="on">
          <label><TextField id="outlined-basic" label="Departure" name="depart" variant="outlined" /></label>
          <label><TextField id="outlined-basic" label="Arrival" name="arrival" variant="outlined" /></label>
          <TextField name="out"
                       id="date"
                       label="Date Outward"
                       type="date"
                       className={classes.textField}
                       InputLabelProps={{
                       shrink: true,}}/>
          <TextField name="in"
                       id="date"
                       label="Date Inward"
                       type="date"
                       className={classes.textField}
                       InputLabelProps={{
                       shrink: true,}}/>
          <TextField name="trip"
            id="standard-select-currency"
            select
            label="Trip Type"
            value={currency}
            onChange={handleChange}
          >
            {tripType.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>
          <br/>
          <Button type="submit" variant="contained" color="primary">Submit</Button>
        </form>
    </div>
  );
}

export default App;
