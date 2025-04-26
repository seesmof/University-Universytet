import mongoose from "mongoose";
const { Schema, model } = mongoose;

const bunchSchema = new Schema({
  grapesCount: Number,
  outsideDamaged: Boolean,
  overlySoft: Boolean,
  unstableForm: Boolean,
  insectDamaged: Boolean,
  sugarImbalanced: Boolean,
});

const Bunch = model("Bunch", bunchSchema);
export default Bunch;
