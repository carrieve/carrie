(function () {
  const el = document.getElementById('save-instructions');
  if (!el) return;

  // Inject styles
  const style = document.createElement('style');
  style.textContent = `
    .si-wrap { margin-bottom: 16px; }
    .si-heading { font-size: 0.95rem; font-weight: 700; color: #111; margin-bottom: 14px; }
    .si-heading span { color: #8B2FC9; }
    .si-tabs { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 18px; }
    .si-tab { padding: 8px 14px; border-radius: 20px; border: 1.5px solid #e5e7eb; background: #fff; font-size: 0.84rem; font-weight: 600; cursor: pointer; font-family: inherit; color: #6b7280; transition: all 0.15s; }
    .si-tab:hover { border-color: #8B2FC9; color: #8B2FC9; }
    .si-tab.si-active { background: #8B2FC9; color: #fff; border-color: #8B2FC9; }
    .si-content { display: none; }
    .si-content.si-active { display: block; }
    .si-steps { display: flex; flex-direction: column; gap: 10px; margin-bottom: 10px; }
    .si-step { display: flex; align-items: flex-start; gap: 10px; }
    .si-num { width: 24px; height: 24px; border-radius: 50%; background: #f3e8ff; color: #6b1fa0; font-size: 0.72rem; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; }
    .si-text { font-size: 0.9rem; color: #111; line-height: 1.55; }
    .si-text a { color: #8B2FC9; text-decoration: none; }
    .si-tip { font-size: 0.8rem; color: #7a5800; background: #fffbeb; border-radius: 8px; padding: 9px 12px; margin-top: 10px; line-height: 1.5; }
    .si-toggle { background: none; border: none; color: #6b7280; font-size: 0.8rem; cursor: pointer; font-family: inherit; padding: 0; text-decoration: underline; text-underline-offset: 3px; margin-top: 10px; display: block; }
    .si-secondary { margin-top: 12px; padding-top: 12px; border-top: 1px solid #e5e7eb; }
  `;
  document.head.appendChild(style);

  el.innerHTML = `
    <div class="si-wrap">
      <p class="si-heading">Step 1 — Pick where to save it. <span>Do this once and your AI always knows.</span></p>
      <div class="si-tabs">
        <button class="si-tab si-active" onclick="siTab('claude',this)">🟠 Claude</button>
        <button class="si-tab" onclick="siTab('chatgpt',this)">🟢 ChatGPT</button>
        <button class="si-tab" onclick="siTab('gemini',this)">🔵 Gemini</button>
        <button class="si-tab" onclick="siTab('grok',this)">⚫ Grok</button>
        <button class="si-tab" onclick="siTab('copilot',this)">🟣 Copilot</button>
      </div>

      <div class="si-content si-active" id="si-claude">
        <div class="si-steps">
          <div class="si-step"><span class="si-num">1</span><span class="si-text">Go to <a href="https://claude.ai" target="_blank">claude.ai</a> → click <strong>Projects</strong> in the left sidebar → <strong>New Project</strong></span></div>
          <div class="si-step"><span class="si-num">2</span><span class="si-text">Give the project a name (e.g. "My Executive") → click <strong>Continue</strong></span></div>
          <div class="si-step"><span class="si-num">3</span><span class="si-text">Click <strong>Add instructions</strong> → paste your briefing → save</span></div>
          <div class="si-step"><span class="si-num">4</span><span class="si-text">Start every chat from inside that project — Claude already knows your executive</span></div>
        </div>
        <p class="si-tip">⚠️ Paste into <strong>Add instructions</strong> — not the chat box. The chat box only lasts one conversation. Instructions stick permanently.</p>
      </div>

      <div class="si-content" id="si-chatgpt">
        <div class="si-steps">
          <div class="si-step"><span class="si-num">1</span><span class="si-text">Go to <a href="https://chatgpt.com" target="_blank">chatgpt.com</a> → profile icon → <strong>Settings → Personalization → Custom Instructions</strong></span></div>
          <div class="si-step"><span class="si-num">2</span><span class="si-text">Paste your prompt into the top box → save</span></div>
          <div class="si-step"><span class="si-num">3</span><span class="si-text">Applies to every new chat automatically</span></div>
        </div>
      </div>

      <div class="si-content" id="si-gemini">
        <div class="si-steps">
          <div class="si-step"><span class="si-num">1</span><span class="si-text">Go to <a href="https://gemini.google.com" target="_blank">gemini.google.com</a> → <strong>Gems</strong> → <strong>New Gem</strong></span></div>
          <div class="si-step"><span class="si-num">2</span><span class="si-text">Paste your prompt into the instructions box → save</span></div>
          <div class="si-step"><span class="si-num">3</span><span class="si-text">Open that Gem any time — it knows your executive</span></div>
        </div>
      </div>

      <div class="si-content" id="si-grok">
        <div class="si-steps">
          <div class="si-step"><span class="si-num">1</span><span class="si-text">Go to <a href="https://grok.com" target="_blank">grok.com</a> → <strong>Settings → Custom Instructions</strong></span></div>
          <div class="si-step"><span class="si-num">2</span><span class="si-text">Paste your prompt → save</span></div>
        </div>
      </div>

      <div class="si-content" id="si-copilot">
        <div class="si-steps">
          <div class="si-step"><span class="si-num">1</span><span class="si-text">Go to <a href="https://copilot.microsoft.com" target="_blank">copilot.microsoft.com</a> → start a new chat</span></div>
          <div class="si-step"><span class="si-num">2</span><span class="si-text">Paste your prompt and say: <em>"This is my executive's profile — refer to it whenever you help me."</em></span></div>
        </div>
      </div>
    </div>
  `;

  window.siTab = function (name, btn) {
    document.querySelectorAll('.si-tab').forEach(b => b.classList.remove('si-active'));
    document.querySelectorAll('.si-content').forEach(c => c.classList.remove('si-active'));
    btn.classList.add('si-active');
    document.getElementById('si-' + name).classList.add('si-active');
  };
})();
