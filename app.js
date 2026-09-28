const fs = require('fs');

function displayKnowledge(filePath) {
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  console.log(`Name: ${data.name}`);
  console.log(`Job: ${data.jobTitle} at ${data.worksFor.name}`);
  console.log(`Email: ${data.email}`);
}

displayKnowledge('knowledge.okf.json');
