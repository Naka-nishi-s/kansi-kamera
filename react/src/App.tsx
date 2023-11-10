import RemoveRedEyeIcon from "@mui/icons-material/RemoveRedEye";
import { Box, Typography } from "@mui/material";
import { Route, Routes } from "react-router-dom";
import { Home } from "./Home";
import { Login } from "./Login";
import { Video } from "./Video";

function App() {
  return (
    <Box
      sx={{
        width: "80%",
        maxWidth: "1200px",
        m: "0 auto",
        pt: 4,
      }}
    >
      <Box sx={{ display: "flex", alignItems: "center", gap: 2 }}>
        <RemoveRedEyeIcon />
        <Typography variant="h4">Kanshi-Kamera</Typography>
      </Box>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/video/:videoId" element={<Video />} />
      </Routes>
    </Box>
  );
}

export default App;
