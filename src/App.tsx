import { useState } from 'react';
import {
  TrendingUp,
  Package,
  Settings,
  Activity,
  AlertTriangle,
  Clock,
  Euro,
  Plus
} from 'lucide-react';

// --- Types ---
export interface ProductLine {
  id: string;
  name: string;
  buyPrice: number;
  partsCost: number;
  sellPrice: number;
  laborTimeMinutes: number; // in minutes
  stock: number;
}

export interface Sale {
  id: string;
  lineId: string;
  lineName: string;
  profit: number;
  timestamp: number;
}

// --- Initial Data ---
const INITIAL_LINES: ProductLine[] = [
  {
    id: '1',
    name: 'Manettes (Ex: PS5 Drift)',
    buyPrice: 0,
    partsCost: 5,
    sellPrice: 25,
    laborTimeMinutes: 20,
    stock: 3,
  },
  {
    id: '2',
    name: 'Thermostats Connectés',
    buyPrice: 15,
    partsCost: 0,
    sellPrice: 45,
    laborTimeMinutes: 15,
    stock: 5,
  },
  {
    id: '3',
    name: 'Modules IoT',
    buyPrice: 5,
    partsCost: 2,
    sellPrice: 20,
    laborTimeMinutes: 10,
    stock: 10,
  }
];

const START_CAPITAL = 500;
const REVOLVING_LIMIT = 1000;
const GOAL = 30000;

function App() {
  const [lines, setLines] = useState<ProductLine[]>(INITIAL_LINES);
  const [sales, setSales] = useState<Sale[]>([]);
  const [capital, setCapital] = useState<number>(START_CAPITAL);
  const [startDate] = useState<number>(() => Date.now() - 30 * 24 * 60 * 60 * 1000); // Mock started 30 days ago
  const [currentDate, setCurrentDate] = useState<number>(() => Date.now());

  const totalProfit = sales.reduce((sum, sale) => sum + sale.profit, 0);
  const daysActive = Math.max(1, Math.floor((currentDate - startDate) / (1000 * 60 * 60 * 24)));
  const velocity = totalProfit / daysActive;
  const progressPercent = Math.min(100, (capital / GOAL) * 100);

  const tiedUpCapital = lines.reduce((sum, line) => sum + ((line.buyPrice + line.partsCost) * line.stock), 0);
  const capitalLimitPercent = Math.min(100, (tiedUpCapital / REVOLVING_LIMIT) * 100);

  const [isAddingLine, setIsAddingLine] = useState(false);
  const [newLineData, setNewLineData] = useState<Partial<ProductLine>>({
    name: '', buyPrice: 0, partsCost: 0, sellPrice: 0, laborTimeMinutes: 0, stock: 0
  });

  const handleAddLine = () => {
    if (!newLineData.name) return;
    const newLine: ProductLine = {
      id: crypto.randomUUID(),
      name: newLineData.name,
      buyPrice: newLineData.buyPrice || 0,
      partsCost: newLineData.partsCost || 0,
      sellPrice: newLineData.sellPrice || 0,
      laborTimeMinutes: newLineData.laborTimeMinutes || 0,
      stock: newLineData.stock || 0
    };
    setLines(prev => [...prev, newLine]);
    setIsAddingLine(false);
    setNewLineData({ name: '', buyPrice: 0, partsCost: 0, sellPrice: 0, laborTimeMinutes: 0, stock: 0 });
  };

  const handleAddStock = (lineId: string) => {
    setLines(prev => prev.map(l =>
      l.id === lineId ? { ...l, stock: l.stock + 1 } : l
    ));
  };

  const handleSimulateSale = (lineId: string) => {
    const line = lines.find(l => l.id === lineId);
    if (!line || line.stock <= 0) return;

    const profit = line.sellPrice - (line.buyPrice + line.partsCost);

    setLines(prev => prev.map(l =>
      l.id === lineId ? { ...l, stock: l.stock - 1 } : l
    ));

    setCapital(prev => prev + line.sellPrice);

    const newSale: Sale = {
      id: crypto.randomUUID(),
      lineId: line.id,
      lineName: line.name,
      profit: profit,
      timestamp: Date.now()
    };

    setCurrentDate(newSale.timestamp);

    setSales(prev => [newSale, ...prev]);
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 p-4 md:p-8 font-sans">
      <div className="max-w-6xl mx-auto space-y-6">
        <header className="flex items-center justify-between border-b border-zinc-800 pb-4">
          <div className="flex items-center gap-3">
            <Settings className="w-8 h-8 text-indigo-400" />
            <h1 className="text-2xl font-bold tracking-tight">Micro-Maintenance OS</h1>
          </div>
          <div className="text-zinc-400 text-sm">
            Système de Gestion de Flux & Rentabilité
          </div>
        </header>

        <main className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 space-y-6">
            {/* Dashboard */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 shadow-sm">
              <div className="flex items-center gap-2 mb-6">
                <TrendingUp className="text-emerald-500 w-5 h-5" />
                <h2 className="text-lg font-semibold">Tableau de Bord & Objectif</h2>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div className="bg-zinc-950 p-4 rounded-lg border border-zinc-800/50">
                  <div className="text-sm text-zinc-400 mb-1">Capital Actuel</div>
                  <div className="text-2xl font-bold font-mono text-zinc-100">{capital.toFixed(2)} €</div>
                </div>
                <div className="bg-zinc-950 p-4 rounded-lg border border-zinc-800/50">
                  <div className="text-sm text-zinc-400 mb-1">Bénéfice Total</div>
                  <div className="text-2xl font-bold font-mono text-emerald-400">+{totalProfit.toFixed(2)} €</div>
                </div>
                <div className="bg-zinc-950 p-4 rounded-lg border border-zinc-800/50">
                  <div className="text-sm text-zinc-400 mb-1 flex items-center gap-1">
                    <Activity className="w-3 h-3" /> Vélocité
                  </div>
                  <div className="text-2xl font-bold font-mono text-indigo-400">{velocity.toFixed(2)} € <span className="text-sm font-normal text-zinc-500">/ jour</span></div>
                </div>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-zinc-400">Progression vers 30 000 €</span>
                  <span className="font-mono">{progressPercent.toFixed(1)}%</span>
                </div>
                <div className="h-3 bg-zinc-950 rounded-full overflow-hidden border border-zinc-800">
                  <div
                    className="h-full bg-indigo-500 transition-all duration-1000 ease-out"
                    style={{ width: `${progressPercent}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Lines Manager */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 shadow-sm">
              <div className="flex items-center justify-between mb-6">
                <div className="flex items-center gap-2">
                  <Settings className="text-indigo-400 w-5 h-5" />
                  <h2 className="text-lg font-semibold">Gestionnaire de Lignes & ROTI</h2>
                </div>
                <button
                  onClick={() => setIsAddingLine(!isAddingLine)}
                  className="flex items-center gap-1 text-sm bg-indigo-500/10 text-indigo-400 hover:bg-indigo-500/20 px-3 py-1.5 rounded-lg transition-colors"
                >
                  <Plus className="w-4 h-4" />
                  Nouvelle Ligne
                </button>
              </div>

              {isAddingLine && (
                <div className="bg-zinc-950 p-4 rounded-lg border border-indigo-500/30 mb-4 space-y-4">
                  <div className="text-sm font-medium text-indigo-400 mb-2">Ajouter une nouvelle catégorie</div>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <input
                      type="text"
                      placeholder="Nom de la ligne"
                      className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                      value={newLineData.name}
                      onChange={e => setNewLineData({...newLineData, name: e.target.value})}
                    />
                    <div className="grid grid-cols-2 gap-2">
                      <input
                        type="number"
                        placeholder="Achat moyen"
                        className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                        value={newLineData.buyPrice || ''}
                        onChange={e => setNewLineData({...newLineData, buyPrice: parseFloat(e.target.value)})}
                      />
                      <input
                        type="number"
                        placeholder="Coût pièces"
                        className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                        value={newLineData.partsCost || ''}
                        onChange={e => setNewLineData({...newLineData, partsCost: parseFloat(e.target.value)})}
                      />
                    </div>
                    <div className="grid grid-cols-3 gap-2 md:col-span-2">
                      <input
                        type="number"
                        placeholder="Revente"
                        className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                        value={newLineData.sellPrice || ''}
                        onChange={e => setNewLineData({...newLineData, sellPrice: parseFloat(e.target.value)})}
                      />
                      <input
                        type="number"
                        placeholder="Temps (min)"
                        className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                        value={newLineData.laborTimeMinutes || ''}
                        onChange={e => setNewLineData({...newLineData, laborTimeMinutes: parseInt(e.target.value)})}
                      />
                      <input
                        type="number"
                        placeholder="Stock init."
                        className="bg-zinc-900 border border-zinc-800 rounded p-2 text-sm text-zinc-100"
                        value={newLineData.stock || ''}
                        onChange={e => setNewLineData({...newLineData, stock: parseInt(e.target.value)})}
                      />
                    </div>
                  </div>
                  <div className="flex justify-end gap-2 mt-4">
                    <button onClick={() => setIsAddingLine(false)} className="text-sm px-3 py-1.5 text-zinc-400 hover:text-zinc-200">Annuler</button>
                    <button onClick={handleAddLine} className="text-sm px-3 py-1.5 bg-indigo-500 hover:bg-indigo-600 text-white rounded">Ajouter</button>
                  </div>
                </div>
              )}

              <div className="space-y-4">
                {lines.map(line => {
                  const netMargin = line.sellPrice - (line.buyPrice + line.partsCost);
                  const roti = line.laborTimeMinutes > 0 ? (netMargin / (line.laborTimeMinutes / 60)) : 0;

                  return (
                    <div key={line.id} className="bg-zinc-950 p-4 rounded-lg border border-zinc-800/50">
                      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                        <div className="font-medium text-zinc-200">{line.name}</div>
                        <div className="flex gap-4 text-sm">
                          <div className="flex items-center gap-1">
                            <span className="text-zinc-500">Marge:</span>
                            <span className="font-mono text-emerald-400">{netMargin.toFixed(2)} €</span>
                          </div>
                          <div className="flex items-center gap-1">
                            <span className="text-zinc-500">ROTI:</span>
                            <span className="font-mono text-indigo-400">{roti.toFixed(2)} €/h</span>
                          </div>
                        </div>
                      </div>

                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div>
                          <label className="block text-zinc-500 mb-1 text-xs uppercase tracking-wider">Achat moyen</label>
                          <div className="font-mono">{line.buyPrice.toFixed(2)} €</div>
                        </div>
                        <div>
                          <label className="block text-zinc-500 mb-1 text-xs uppercase tracking-wider">Coût pièces</label>
                          <div className="font-mono">{line.partsCost.toFixed(2)} €</div>
                        </div>
                        <div>
                          <label className="block text-zinc-500 mb-1 text-xs uppercase tracking-wider">Revente</label>
                          <div className="font-mono">{line.sellPrice.toFixed(2)} €</div>
                        </div>
                        <div>
                          <label className="block text-zinc-500 mb-1 text-xs uppercase tracking-wider">Main d'œuvre</label>
                          <div className="font-mono flex items-center gap-1">
                            <Clock className="w-3 h-3 text-zinc-400" /> {line.laborTimeMinutes} min
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          <div className="space-y-6">
            {/* Stock Management */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 shadow-sm">
              <div className="flex items-center gap-2 mb-6">
                <Package className="text-blue-400 w-5 h-5" />
                <h2 className="text-lg font-semibold">Stock & BFR</h2>
              </div>

              <div className="mb-6 p-4 bg-zinc-950 rounded-lg border border-zinc-800/50">
                <div className="flex justify-between items-end mb-2">
                  <div>
                    <div className="text-sm text-zinc-400">Capital Immobilisé</div>
                    <div className="text-xl font-bold font-mono text-zinc-100">{tiedUpCapital.toFixed(2)} €</div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm text-zinc-400">Limite Tournant</div>
                    <div className="text-sm font-mono text-zinc-500">{REVOLVING_LIMIT.toFixed(2)} €</div>
                  </div>
                </div>
                <div className="h-2 bg-zinc-900 rounded-full overflow-hidden border border-zinc-800">
                  <div
                    className={`h-full transition-all duration-500 ease-out ${capitalLimitPercent > 90 ? 'bg-red-500' : capitalLimitPercent > 75 ? 'bg-amber-500' : 'bg-blue-500'}`}
                    style={{ width: `${capitalLimitPercent}%` }}
                  />
                </div>
                {capitalLimitPercent > 90 && (
                  <div className="mt-3 flex items-center gap-1.5 text-xs text-red-400 bg-red-500/10 p-2 rounded">
                    <AlertTriangle className="w-4 h-4" /> Attention: Limite de BFR presque atteinte
                  </div>
                )}
              </div>

              <div className="space-y-3">
                {lines.map(line => (
                  <div key={`stock-${line.id}`} className="flex items-center justify-between p-3 bg-zinc-950 rounded border border-zinc-800/30">
                    <div className="text-sm truncate pr-4 text-zinc-300 flex-1">{line.name}</div>
                    <div className="flex items-center gap-3">
                      <div className="text-xs text-zinc-500 font-mono hidden md:block">
                        {((line.buyPrice + line.partsCost) * line.stock).toFixed(2)} €
                      </div>
                      <div className={`font-mono font-medium px-2 py-0.5 rounded text-xs ${line.stock === 0 ? 'bg-red-500/10 text-red-400' : line.stock < 3 ? 'bg-amber-500/10 text-amber-400' : 'bg-zinc-800 text-zinc-300'}`}>
                        {line.stock} en stock
                      </div>
                      <button
                        onClick={() => handleAddStock(line.id)}
                        className="p-1 hover:bg-zinc-800 rounded text-zinc-400 hover:text-zinc-200"
                        title="Ajouter au stock"
                      >
                        <Plus className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Activity Log */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-6 shadow-sm">
              <div className="flex items-center justify-between mb-6">
                <div className="flex items-center gap-2">
                  <Activity className="text-zinc-400 w-5 h-5" />
                  <h2 className="text-lg font-semibold">Journal & Simulation</h2>
                </div>
              </div>

              <div className="mb-6">
                <div className="text-sm text-zinc-500 mb-2">Simuler une vente rapide :</div>
                <div className="flex flex-wrap gap-2">
                  {lines.map(line => (
                    <button
                      key={`btn-${line.id}`}
                      onClick={() => handleSimulateSale(line.id)}
                      disabled={line.stock <= 0}
                      className="text-xs flex items-center gap-1 bg-zinc-800 hover:bg-zinc-700 disabled:opacity-50 disabled:cursor-not-allowed text-zinc-300 px-3 py-1.5 rounded transition-colors"
                    >
                      <Euro className="w-3 h-3 text-emerald-400" />
                      {line.name}
                    </button>
                  ))}
                </div>
              </div>

              <div className="space-y-4">
                <h3 className="text-sm font-medium text-zinc-400 border-b border-zinc-800 pb-2">Dernières ventes</h3>
                <div className="space-y-3">
                  {sales.length === 0 ? (
                    <div className="text-sm text-zinc-600 italic">Aucune vente enregistrée</div>
                  ) : (
                    sales.slice(0, 5).map(sale => (
                      <div key={sale.id} className="flex items-center justify-between text-sm">
                        <div>
                          <div className="text-zinc-300">{sale.lineName}</div>
                          <div className="text-xs text-zinc-500">
                            {new Date(sale.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                          </div>
                        </div>
                        <div className="font-mono text-emerald-400 font-medium">+{sale.profit.toFixed(2)} €</div>
                      </div>
                    ))
                  )}
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
