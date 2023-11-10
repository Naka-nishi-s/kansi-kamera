import {
  Box,
  Button,
  Container,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";
import { FormEvent, useState } from "react";

export const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (event: FormEvent) => {
    event.preventDefault();

    console.log(username);
    console.log(password);

    const response = await axios.post("/api/login", { username, password });
    console.log(response);
  };

  return (
    <Container>
      <Paper elevation={6} sx={{ p: 4, textAlign: "center" }}>
        <Typography variant="h4">Login</Typography>

        <form onSubmit={handleLogin}>
          <Box sx={{ display: "flex", flexDirection: "column" }}>
            <TextField
              variant="outlined"
              margin="normal"
              id="username"
              label="User Name"
              name="username"
              autoComplete="username"
              required
              autoFocus
              onChange={(e) => setUsername(e.currentTarget.value)}
            />
            <TextField
              variant="outlined"
              margin="normal"
              id="password"
              label="Password"
              name="password"
              required
              autoComplete="new-password"
              onChange={(e) => setPassword(e.currentTarget.value)}
            />
            <Button type="submit">Go!</Button>
          </Box>
        </form>
      </Paper>
    </Container>
  );
};
