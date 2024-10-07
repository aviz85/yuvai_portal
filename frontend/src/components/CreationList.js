import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Typography, List, ListItem, ListItemText, Button, Box } from '@mui/material';
import { fetchCreations } from '../api';

function CreationList() {
  const [creations, setCreations] = useState([]);

  useEffect(() => {
    fetchCreations().then(response => setCreations(response.data));
  }, []);

  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom>
        AI Creations
      </Typography>
      <List>
        {creations.map(creation => (
          <ListItem key={creation.id} divider>
            <ListItemText
              primary={<Link to={`/creation/${creation.id}`}>{creation.title}</Link>}
              secondary={`By: ${creation.creator.username} | Type: ${creation.creation_type}`}
            />
          </ListItem>
        ))}
      </List>
      <Button component={Link} to="/create" variant="contained" color="primary">
        Create New
      </Button>
    </Box>
  );
}

export default CreationList;