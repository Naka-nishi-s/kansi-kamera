import { Box, Button, Paper, Typography } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

type VideoList = {
  id: string;
  file_path: string;
};

export const Home = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [statusMsg, setStatusMsg] = useState("");
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
        setStatusMsg(res.data.status);
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
        setStatusMsg(res.data.status);
      })
      .catch((e) => console.error(e));
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Paper elevation={3}>
        <Box sx={{ textAlign: "center", p: 6 }}>
          <Typography variant="h4">Watch</Typography>

          <Box
            sx={{ pt: 2, display: "flex", gap: 1, justifyContent: "center" }}
          >
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

          <Typography variant="h5">status: {statusMsg}</Typography>

          <Box sx={{ pt: 3 }}>
            <Typography variant="h4">Archives</Typography>
            {videoList.map((video) => (
              <Box key={video.id} sx={{ pt: 1 }}>
                <Link to={`/video/${video.id}`}>{video.file_path}</Link>
              </Box>
            ))}
          </Box>
        </Box>
      </Paper>
    </Box>
  );
};
