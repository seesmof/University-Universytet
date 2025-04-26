import { Bunch } from "./models/Bunch";

const user = "seesmof";
const password = "p0zBE5e|";
const uri = `mongodb+srv://${user}:${password}@cluster0.y7yhp7s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`;

mongoose.connect(uri);

const run = async () => {
  try {
    const bunch = await Bunch.create({
      grapesCount: 37,
      outsideDamaged: false,
      overlySoft: false,
      unstableForm: true,
      insectDamaged: false,
      sugarImbalanced: true,
    });
  } catch (err) {
    console.log(err);
  } finally {
    console.log(bunch);
  }
};

run();
