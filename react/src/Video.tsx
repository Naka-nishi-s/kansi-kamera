import { Box } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export const Video = () => {
  const { videoId } = useParams();
  const [videoSrc, setVideoSrc] = useState("");
  console.log(videoId);

  useEffect(() => {
    axios
      .get(`/api/videos/${videoId}`)
      .then((res) => {
        setVideoSrc(res.data.filePath);
      })
      .catch((err) => {
        console.error("Error fetching video", err);
      });
  }, []);

  console.log(videoSrc);

  return (
    <Box>
      {videoSrc && (
        <video width="320" height="240" controls>
          <source src={`/${videoSrc}`} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      )}
    </Box>
  );
};
