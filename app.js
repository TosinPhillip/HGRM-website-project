const express = require("express");
const ejs = require("ejs");
const app = express();

// Set EJS as the view engine
app.set("view engine", "ejs");
app.set("views", __dirname + "/public/views");
app.use(express.static(__dirname + "/public/images"));


// Route for rendering index.html
app.get("/", (req, res) => {
  res.render("index.html");
});

app.get("/doctrine", (req, res) => {
  res.render("doctrine.html");
});

app.get("/executives", (req, res) => {
  res.render("execs.html");
});

app.get("/staff_advisers", (req, res) => {
  res.render("staff_advisers.html");
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
