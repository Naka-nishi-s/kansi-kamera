import { Box, Button, Typography } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";

type VideoList = {
  id: string;
  file_path: string;
};

function App() {
  const [isRunning, setIsRunning] = useState(false);
  const [videoList, setVideoList] = useState<VideoList[]>([]);

  useEffect(() => {
    axios
      .get("/api/videos/")
      .then((response) => {
        setVideoList(response.data);
      })
      .catch((error) => console.error("Get Videolist Error", error));
  }, []);

  /**
   * Start Watch Room
   */
  const startWatchRoom = () => {
    axios
      .post("/api/start-camera")
      .then((res) => {
        setIsRunning(res.data.isRunning);
        console.log(res.data.status);
      })
      .catch((e) => console.error(e));
  };

  /**
   * Stop Watch Room
   */
  const stopWatchRoom = () => {
    axios
      .post("/api/stop-camera")
      .then((res) => {
        setIsRunning(res.data.isRunning);
        console.log(res.data.status);
      })
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
        <Button
          variant="contained"
          onClick={startWatchRoom}
          disabled={isRunning}
        >
          Start!
        </Button>
        <Button
          variant="contained"
          onClick={stopWatchRoom}
          disabled={!isRunning}
        >
          Stop!
        </Button>
      </Box>
      <Box>
        <Typography variant="h5">Archives</Typography>
        {videoList.map((video) => (
          <div key={video.id}>
            <a
              href={`/media/${video.file_path}`}
              target="_blank"
              rel="noopener noreferrer"
            >
              {video.file_path}
            </a>
          </div>
        ))}
      </Box>
    </Box>
  );
}

export default App;
