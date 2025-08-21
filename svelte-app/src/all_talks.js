import { data } from "./index.js";
export const all_talks = new Set(
  data.map((record) => {
    return record.label;
  })
);
// console.log(all_talks)
