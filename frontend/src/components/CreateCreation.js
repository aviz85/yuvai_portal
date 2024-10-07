import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Typography, Box, TextField, Button, MenuItem } from '@mui/material';
import { createCreation } from '../api';

function CreateCreation() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [creationType, setCreationType] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    createCreation({ title, description, creation_type: creationType })
      .then(response => {
        navigate(`/creation/${response.data.id}`);
      });
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Create New AI Creation
      </Typography>
      <TextField
        fullWidth
        label="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        margin="normal"
        required
      />
      <TextField
        fullWidth
        multiline
        rows={4}
        label="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        margin="normal"
        required
      />
      <TextField
        select
        fullWidth
        label="Creation Type"
        value={creationType}
        onChange={(e) => setCreationType(e.target.value)}
        margin="normal"
        required
      >
        <MenuItem value="APP">Application</MenuItem>
        <MenuItem value="IMG">Image</MenuItem>
        <MenuItem value="VID">Video</MenuItem>
        <MenuItem value="AUD">Audio</MenuItem>
        <MenuItem value="OTH">Other</MenuItem>
      </TextField>
      <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
        Create
      </Button>
    </Box>
  );
}

export default CreateCreation;