const mongoose = require("mongoose");
const uri =
  "mongodb+srv://seesmof:p0zBE5e|@cluster0.y7yhp7s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

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
