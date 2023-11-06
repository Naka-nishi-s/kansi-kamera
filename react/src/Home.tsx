import { Box, Button, Paper, Typography } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";

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
          <Typography variant="h5">Watch!</Typography>

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

          <Typography variant="h5">status:{statusMsg}</Typography>

          <Box sx={{ pt: 3 }}>
            <Typography variant="h5">Archives</Typography>
            {videoList.map((video) => (
              <div key={video.id}>
                <a
                  href={video.file_path}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {video.file_path}
                </a>
              </div>
              //   <div key={video.id}>
              //     <video width="320" height="240" controls>
              //       <source src={video.file_path} type="video/mp4" />
              //       Your browser does not support the video tag.
              //     </video>
              //   </div>
            ))}
          </Box>
        </Box>
      </Paper>
    </Box>
  );
};
