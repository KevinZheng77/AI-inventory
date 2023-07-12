const aiplatform = require('@google-cloud/aiplatform');
const express = require('express');
const router = express.Router();
const requireAuth = require('../middleware/permission');
const { route } = require('./auth');
const {PredictionServiceClient} = require('@google-cloud/automl').v1;
require('dotenv').config();
const path = require('path');


const keyFilename = path.join(__dirname, "../keys/serviceAccountKey.json");
const client = new aiplatform.PredictionServiceClient({
    keyFilename: keyFilename
});
// Create client for prediction service.
const predictionClient = new PredictionServiceClient();
//project information
const projectId = process.env.PROJECT_ID;
const location = 'us-central1';  // Make sure to replace with your location if different
const endpointId = process.env.ENDPOINT_ID;


async function predict(userText) {
console.log(projectId,endpointId);
console.log(userText);
const endpointPath = `projects/${projectId}/locations/${location}/endpoints/${endpointId}`;

const request = {
    endpoint: endpointPath,  // The path to your endpoint
    instances: [
      {
        content: userText,  // The text content for prediction
        mimeType: 'text/plain',  // The MIME type of the content
      },
    ],
  };
  

  const [response] = await client.predict(request);

  return response;
}


// @route GET  /api/google/test
// @desc  Test the google Route
// @access Public
router.get('/test', (req, res) =>{
    res.send('Google route is working')
});


router.post('/predict', async (req, res) => {
    const userText = req.body.userText;
    try {
      const prediction = await predict(userText);
      res.json(prediction);
    } catch (error) {
      res.status(500).send(error.toString());
    }
  });

  module.exports = router;