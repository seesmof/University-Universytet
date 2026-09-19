import express from "express";
import cors from "cors";
import env from "dotenv";
import { createClient } from "@supabase/supabase-js";

env.config();

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_KEY,
);

const app = express();
const port = process.env.PORT;

app.use(cors());

app.get("/", (req, res) => {
  return res.status(200).json({ message: "Jesus is LORD" });
});

app.get("/posts", async (req, res) => {
  try {
    const { data, error } = await supabase.from("posts").select();
    console.log(data);
    return res.send(data);
  } catch (error) {
    return res.send({ error });
  }
});

app.post("/posts", async (req, res) => {
  try {
    console.log(req.body);
    const { data, error } = await supabase.from("posts").insert(req.body);
    if (error) {
      return res.status(400).json(error);
    }
    return res.status(200).json(req.body);
  } catch (error) {
    return res.send({ error });
  }
});

app.get("/posts/:id", async (req, res) => {
  try {
    const { data, error } = await supabase
      .from("posts")
      .select()
      .eq("id", req.params.id);
    console.log(data);
    return res.send(data);
  } catch (error) {
    return res.send({ error });
  }
});

app.listen(port, () =>
  console.log(`Listening on port ${port}: http://localhost:${port}`),
);
