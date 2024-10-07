import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Typography, Box, TextField, Button, List, ListItem, ListItemText } from '@mui/material';
import { fetchCreation, addComment } from '../api';

function CreationDetail() {
  const [creation, setCreation] = useState(null);
  const [comment, setComment] = useState('');
  const { id } = useParams();

  useEffect(() => {
    fetchCreation(id).then(response => setCreation(response.data));
  }, [id]);

  const handleCommentSubmit = (e) => {
    e.preventDefault();
    addComment(id, { content: comment })
      .then(response => {
        setCreation({
          ...creation,
          comments: [...creation.comments, response.data]
        });
        setComment('');
      });
  };

  if (!creation) return <Typography>Loading...</Typography>;

  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom>
        {creation.title}
      </Typography>
      <Typography variant="subtitle1" gutterBottom>
        By: {creation.creator.username}
      </Typography>
      <Typography variant="subtitle2" gutterBottom>
        Type: {creation.creation_type}
      </Typography>
      <Typography variant="body1" paragraph>
        {creation.description}
      </Typography>
      <Typography variant="h6" gutterBottom>
        Comments
      </Typography>
      <List>
        {creation.comments.map(comment => (
          <ListItem key={comment.id} divider>
            <ListItemText
              primary={comment.content}
              secondary={`By: ${comment.author.username}`}
            />
          </ListItem>
        ))}
      </List>
      <Box component="form" onSubmit={handleCommentSubmit} sx={{ mt: 2 }}>
        <TextField
          fullWidth
          multiline
          rows={3}
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          label="Add a comment"
          variant="outlined"
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary">
          Add Comment
        </Button>
      </Box>
    </Box>
  );
}

export default CreationDetail;