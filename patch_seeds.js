const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

const newSeeds = fs.readFileSync('seeds.js', 'utf8');

// Replace everything between const SEED_DEFS = [ and ];
const replaceRegex = /const SEED_DEFS = \[\s*[\s\S]*?\];/;
let newHtml = html.replace(replaceRegex, newSeeds);

// Remove the old exponential loop since it's pre-calculated in seeds.js
const loopRegex = /\/\/ Économie Loi Exponentielle[\s\S]*?\}\);/;
newHtml = newHtml.replace(loopRegex, '');

// update default inventory
newHtml = newHtml.replace("inventory = { 't0': 5 };", "inventory = { 's1': 5 };");
newHtml = newHtml.replace("let selectedSeedId = 't0';", "let selectedSeedId = 's1';");

fs.writeFileSync('index.html', newHtml);
