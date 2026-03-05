const fs = require('fs');

const behaviors = [
    'none', 'dance', 'hide', 'move', 'parasite',
    'magnet', 'shadow', 'explode', 'giant_low_drop', 'blackhole'
];

let seeds = [];
let baseCost = 10;
let baseDrops = [10, 15]; // Max drops to start
let sellMultiplier = 0.5;

const seedNames = [
    "Pousse Simple", "Herbe Dansante", "Pousse Couarde", "Liane Voyageuse", "Ronce Parasite",
    "Bourgeon Attractif", "Fleur Ombre", "Cristalline Piquante", "Orgueil Doré", "Singularité",
    "Fleur de Feu", "Cristal de Givre", "Racine Hurlante", "Tige de Fer", "Liane Électrique",
    "Lotus Sanguin", "Orchidée Fantôme", "Cactus Émeraude", "Rose des Vents", "Tulipe d'Obsidienne",
    "Graine Tempête", "Bourgeon Sombre", "Lys Solaire", "Pétale Lunaire", "Fleur Toxique",
    "Ronce d'Acier", "Lierre Épineux", "Jacinthe d'Eau", "Coquelicot Géant", "Iris Céleste",
    "Fougère Ancienne", "Baobab Nain", "Graine de Météore", "Pousse de Lave", "Herbe de Cristal",
    // 15 Exclusives (index 35 to 49)
    "Artefact Botanique", "Graine Stellaire", "Racine du Néant", "Fleur Temporelle", "Lotus Noir",
    "Orchidée Primordiale", "Rose de Cristal", "Bourgeon Divin", "Liane Dimensionnelle", "Tige Cosmos",
    "Fleur d'Ombre Pure", "Graine d'Éternité", "Pétale Chaos", "Lys de l'Aube", "Singularité Absolue"
];

for(let i = 0; i < 50; i++) {
    let cost = Math.round(baseCost * Math.pow(2.5, i));
    let sell = Math.round(cost * sellMultiplier * Math.pow(0.95, i));

    // As rarity goes up, max drops go down, min drops approach 1
    let maxDrop = Math.max(2, 15 - Math.floor(i / 3.5));
    let minDrop = Math.max(1, 10 - Math.floor(i / 2));

    // Assign random color
    let color = `hsl(${Math.random() * 360}, ${70 + Math.random() * 30}%, ${40 + Math.random() * 40}%)`;

    let behavior = behaviors[i % behaviors.length];

    // Specific overrides
    if(i === 8) behavior = 'giant_low_drop';
    if(i === 9) behavior = 'blackhole';

    seeds.push({
        id: `s${i+1}`,
        name: seedNames[i] || `Graine Inconnue ${i+1}`,
        color: color,
        cost: cost,
        sell: sell,
        lifespan: 5000 + Math.random() * 15000,
        drops: [minDrop, maxDrop],
        behavior: behavior,
        exclusive: i >= 35
    });
}

const jsContent = `const SEED_DEFS = ${JSON.stringify(seeds, null, 4)};`;
fs.writeFileSync('seeds.js', jsContent);
console.log("Generated seeds.js");
