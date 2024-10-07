import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline, Container } from '@mui/material';
import CreationList from './components/CreationList';
import CreationDetail from './components/CreationDetail';
import CreateCreation from './components/CreateCreation';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Container maxWidth="lg">
          <Routes>
            <Route path="/" element={<CreationList />} />
            <Route path="/creation/:id" element={<CreationDetail />} />
            <Route path="/create" element={<CreateCreation />} />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

export default App;
