import express from "express";
import cors from "cors";

const app = express();

const PORT = 8080;

app.use(cors());
app.use(express.json());

app.get("/", (_req, res) => {
  res.status(200).json({ message: "Jesus is LORD" });
});

app.listen(PORT, () => {
  console.log(`The app is running on port ${PORT}: http://localhost:${PORT}`);
});
