const { MongoClient } = require('mongodb');

const uri = "YOUR_MONGODB_URI";
const client = new MongoClient(uri);

async function connectDB() {
  try {
    await client.connect();
    console.log("Connected to MongoDB");
  } catch (err) {
    console.error(err);
  }
}

module.exports = { connectDB };
