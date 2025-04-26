const mongoose = require("mongoose");
const user = "seesmof";
const password = "p0zBE5e|";
const uri = `mongodb+srv://${user}:${password}@cluster0.y7yhp7s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;

const run = async () => {
  try {
    await mongoose.connect(uri);
    await mongoose.connection.db.admin().command({ ping: 1 });
    console.log("Pinged deployment");
  } finally {
    await mongoose.disconnect();
  }
};
run().catch(console.dir);
