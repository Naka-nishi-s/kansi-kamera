import { Box, Button, Typography } from "@mui/material";
import axios from "axios";

function App() {
  /**
   * Start Watch Room
   */
  const startWatchRoom = () => {
    axios
      .post("/api/start-camera")
      .then((res) => console.log(res.data))
      .catch((e) => console.error(e));
  };

  /**
   * Stop Watch Room
   */
  const stopWatchRoom = () => {
    axios
      .post("/api/stop-camera")
      .then((res) => console.log(res.data))
      .catch((e) => console.error(e));
  };

  return (
    <Box
      sx={{
        width: "80%",
        maxWidth: "1200px",
        m: "0 auto",
        pt: 4,
        textAlign: "center",
      }}
    >
      <Typography variant="h4">Kanshi-Kamera</Typography>
      <Box sx={{ pt: 4, display: "flex", gap: 2, justifyContent: "center" }}>
        <Button variant="outlined" onClick={startWatchRoom}>
          Start!
        </Button>
        <Button variant="contained" onClick={stopWatchRoom}>
          Stop!
        </Button>
      </Box>
    </Box>
  );
}

export default App;
