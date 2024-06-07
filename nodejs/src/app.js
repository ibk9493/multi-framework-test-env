const express = require('express');
const app = express();
const port = 8000;

app.get('/', (req, res) => {
  res.send('Node.js code runs successfully!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
 