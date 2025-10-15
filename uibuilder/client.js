// Recebe mensagens do Node-RED via uibuilder e atualiza a UI
uibuilder.onChange('msg','', (msg) => {
  if (!msg || !msg.payload) return;
  const p = msg.payload;
  if (p.tipo === 'update_batch') updateBatch(p.dados);
});

function updateBatch(dados){
  const cards = document.getElementById('cards');
  cards.innerHTML = '';
  dados.forEach(d => {
    const el = document.createElement('div');
    el.className = 'card';
    el.innerHTML = `
      <h2>${d.paciente}</h2>
      <p>Batimentos: <strong>${d.batimentos} bpm</strong></p>
      <p>Temp.: <strong>${d.temperatura.toFixed(1)} °C</strong></p>
      <p>SpO2: <strong>${d.spo2}%</strong></p>
      <p>PA: <strong>${d.pa.sistolica}/${d.pa.diastolica} mmHg</strong></p>
    `;
    cards.appendChild(el);
  });
}

// Indicador de ligação
uibuilder.onChange('clientStatus', '', (st) => console.log('uibuilder status', st));
