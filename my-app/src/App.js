import logo from './logo.png';
import bgimg from './pic2.jpg'
import './App.css';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import React from 'react';
import 'fontsource-roboto';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
      width: '20ch',
    },
  },
}));

const tripType = [
  { value: 'oneWay', label: 'One Way' },
  { value: 'rounded',label: 'Round Trip'}
];

const packages = [
  { value: 'CZ', label: '南航随心飞'},
  { value: 'CA', label: '国航随便飞'},
  { value: 'MU', label: '东航悠闲飞'}
];

function App() {
  const classes = useStyles();
  const [trip, setTrip] = React.useState('oneWay');
  const [airlines, setAirlines] = React.useState('CZ');

  const handleChange = (event) => {
    setTrip(event.target.value);
  };
  const handleChange2 = (event) => {
    setAirlines(event.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="bg-box"><img src={bgimg} className="bg_img" /></div>
        <div className="logo-box"><img src={logo} className="logo_img" /></div>
        <div className="text-box"><p>Fly At Will Tool</p></div>
      </header>
      <div className="form-class">
        <form className={classes.root} noValidate autoComplete="on">
          <TextField id="outlined-basic" label="Departure" name="depart" variant="outlined" />
          <TextField id="outlined-basic" label="Arrival" name="arrival" variant="outlined" />
          <TextField name="out"
                       id="date"
                       label="Departure Date"
                       type="date"
                       InputLabelProps={{
                       shrink: true,}}/>
          <TextField name="in"
                       id="date"
                       label="Return Date"
                       type="date"
                       InputLabelProps={{
                       shrink: true,}}/>

          <TextField name="trip"
            select
            label="Trip Type"
            value={trip}
            onChange={handleChange}
          >
            {tripType.map((option) => (<MenuItem key={option.value} value={option.value}> {option.label} </MenuItem>))}
          </TextField>

          <TextField name="airline"
            select
            label="Package"
            value={airlines}
            onChange={handleChange2}
          >
            {packages.map((option) => (<MenuItem key={option.value} value={option.value}> {option.label} </MenuItem>))}
          </TextField>
          <br/>
          <Button type="submit" variant="contained" color="primary">Submit</Button>
        </form>
      </div>
    </div>
  );
}

export default App;
