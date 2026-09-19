import express from "express";
import cors from "cors";

const app = express();
const port = 8080;

app.use(cors());

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Jesus is LORD" });
});

app.listen(port, () =>
  console.log(`Listening on port ${port}: http://localhost:${port}`),
);
