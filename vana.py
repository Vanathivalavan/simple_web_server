from http.server import HTTPServer,BaseHTTPRequestHandler
content = '''<html>

<head>
    <meta charset="UTF-8" />
    <title>Funky To-Do List</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!-- Handwritten fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Patrick+Hand:wght@400&family=Gloria+Hallelujah&display=swap"
        rel="stylesheet">
    <style>
        :root {
            --bg: #b9a8ff;
            /* soft purple background */
            --card: #ffffff;
            --ink: #2a2a2a;
            --muted: #7a7a7a;
            --accent: #2ee6c9;
            /* minty cyan */
            --accent-dark: #1fb7a2;
            --pink-dash: #e88ad9;
            --ring: rgba(46, 230, 201, .35);
            --shadow: 0 16px 40px rgba(75, 64, 133, .35);
            --radius: 22px;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            background:
                radial-gradient(80vmax 60vmax at 10% -20%, #cfc6ff 0%, transparent 60%),
                radial-gradient(80vmax 60vmax at 110% 120%, #d8b8ff 0%, transparent 60%),
                var(--bg);
            font: 16px/1.5 "Patrick Hand", "Gloria Hallelujah", system-ui, -apple-system, Segoe UI, Roboto, Arial;
            color: var(--ink);
            padding: 28px 16px;
        }

        .sheet {
            width: min(920px, 92vw);
            background: var(--card);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            border: 2px solid #eee;
            position: relative;
            overflow: hidden;
            /* dotted notebook background */
            background-image:
                radial-gradient(#d6d9e6 1px, transparent 1px);
            background-size: 18px 18px;
        }

        .sheet::after {
            /* inner rounded edge to mimic paper */
            content: "";
            position: absolute;
            inset: 0;
            border-radius: calc(var(--radius) - 2px);
            box-shadow: inset 0 0 0 2px rgba(0, 0, 0, .04);
            pointer-events: none;
        }

        header {
            padding: 26px 26px 0;
            text-align: center;
        }

        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            flex-wrap: wrap;
        }

        /* Simple hand-drawn laptop illustration */
        .laptop {
            width: 56px;
            height: 56px;
            filter: drop-shadow(0 2px 0 rgba(0, 0, 0, .1));
        }

        .title-badge {
            display: inline-block;
            background: var(--accent);
            color: #0a1a18;
            padding: .35rem .8rem;
            border-radius: 12px;
            font-weight: 700;
            border: 2px solid var(--accent-dark);
            transform: rotate(-2deg);
        }

        .subtitle {
            margin: 6px 0 12px;
            color: #4a4a4a;
            font-size: 20px;
        }

        .pink-rule {
            height: 0;
            border: none;
            border-top: 3px dashed var(--pink-dash);
            margin: 8px auto 20px;
            width: calc(100% - 64px);
        }

        /* Form row */
        .row {
            display: flex;
            gap: 10px;
            padding: 0 22px 18px;
            justify-content: center;
        }

        .field {
            position: relative;
            flex: 1;
            max-width: 720px;
        }

        .input {
            width: 100%;
            background: #fff;
            border: 2px solid #e9e9f2;
            border-radius: 14px;
            padding: 12px 46px 12px 14px;
            outline: none;
            box-shadow: 0 3px 0 #d8d8ea;
            font-family: inherit;
            transition: box-shadow .15s, border-color .15s;
        }

        .input:focus {
            border-color: var(--accent);
            box-shadow: 0 3px 0 #19a995, 0 0 0 4px var(--ring);
        }

        .submit-sticker {
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%) rotate(3deg);
            background: #fff;
            border: 2px solid #c9d1d9;
            padding: 4px 8px;
            border-radius: 8px;
            box-shadow: 0 3px 0 #d7d7d7;
            font-size: 14px;
            color: #3b3b3b;
            pointer-events: none;
        }

        .btn {
            border: none;
            cursor: pointer;
            font-family: inherit;
            background: var(--accent);
            border: 2px solid var(--accent-dark);
            color: #0a1a18;
            font-weight: 700;
            padding: 12px 16px;
            border-radius: 14px;
            box-shadow: 0 4px 0 var(--accent-dark);
            transform: rotate(-1.5deg);
            transition: transform .05s;
        }

        .btn:active {
            transform: translateY(1px) rotate(-1.5deg);
        }

        /* List */
        ul.list {
            list-style: none;
            margin: 0;
            padding: 8px 18px 24px;
        }

        .item {
            display: grid;
            grid-template-columns: auto 1fr auto;
            gap: 10px;
            align-items: center;
            margin: 10px auto;
            padding: 10px 12px;
            width: calc(100% - 20px);
            background: #fff;
            border: 2px solid #e6e6f0;
            border-radius: 14px;
            box-shadow: 0 3px 0 #d9d9ea;
            transition: transform .06s;
        }

        .item:active {
            transform: translateY(1px);
        }

        .check {
            appearance: none;
            width: 22px;
            height: 22px;
            border-radius: 6px;
            border: 2px solid #9cc9c1;
            background: #fff;
            cursor: pointer;
            display: grid;
            place-items: center;
        }

        .check:checked {
            background: var(--accent);
            border-color: var(--accent-dark);
        }

        .check:checked::after {
            content: "✓";
            font-weight: 700;
            color: #0a1a18;
            transform: translateY(-1px);
        }

        .text {
            padding: 6px 8px;
            font-size: 18px;
        }

        .text.done {
            color: #9aa0a6;
            text-decoration: line-through;
        }

        .actions {
            display: flex;
            gap: 8px;
        }

        .icon {
            border: 2px solid #cfd3e6;
            background: #fff;
            color: #333;
            cursor: pointer;
            border-radius: 10px;
            padding: 6px 10px;
            font-size: 15px;
            box-shadow: 0 3px 0 #dcdff2;
        }

        .icon:hover {
            filter: brightness(0.98);
        }

        .icon.delete {
            border-color: #ffb0b0;
            box-shadow: 0 3px 0 #ffb0b0;
        }

        .icon.save {
            border-color: #8de3cf;
            box-shadow: 0 3px 0 #8de3cf;
        }

        .icon.cancel {
            border-color: #cfd3e6;
        }

        .edit-input {
            width: 100%;
            padding: 8px 10px;
            border: 2px solid #e9e9f2;
            border-radius: 10px;
            outline: none;
            font-family: inherit;
            font-size: 18px;
        }

        .empty {
            text-align: center;
            color: var(--muted);
            padding: 6px 16px 26px;
            font-size: 18px;
        }

        footer {
            padding: 10px 22px 26px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            color: #505050;
            font-size: 18px;
        }

        .export {
            text-decoration: none;
            color: #087d6e;
            border-bottom: 2px dotted #0aa08c;
        }

        /* small helper */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0
        }
    </style>
</head>

<body>
    <main class="sheet" aria-labelledby="title">
        <header>
            <div class="header-row">
                <!-- Cute line-art laptop (inline SVG so no files needed) -->
                <img class="laptop" src="notebook.svg" alt="Illustration" />
                <span class="title-badge">To-Do List</span>
            </div>
            <p class="subtitle">~ Today I need to ~</p>
            <hr class="pink-rule">
        </header>

        <!-- Add Row -->
        <form id="addForm" class="row" autocomplete="off">
            <div class="field">
                <input id="newTask" class="input" type="text" placeholder="Type a task and press Add or Enter…"
                    aria-label="New task">
            </div>
            <button class="btn" type="submit">Add</button>
        </form>

        <!-- Task List -->
        <ul id="list" class="list" aria-live="polite"></ul>
        <div id="empty" class="empty">Nothing here yet. Add your first task above!</div>

        <footer>
            <span>Tip: Double-click a task to edit • Enter to save, Esc to cancel</span>
            <a id="exportBtn" class="export" href="#">Export JSON</a>
        </footer>

        <div id="live" class="sr-only" aria-live="polite"></div>
    </main>

    <script>
        // ======= Behavior: Add • Edit • Delete • Complete • LocalStorage =======
        const STORAGE_KEY = 'funky.todo.v1';
        /** @type {{id:string, text:string, done:boolean}[]} */
        let tasks = load();
        let editing = null; // { id, li, input }

        const els = {
            form: document.getElementById('addForm'),
            input: document.getElementById('newTask'),
            list: document.getElementById('list'),
            empty: document.getElementById('empty'),
            live: document.getElementById('live'),
            exportBtn: document.getElementById('exportBtn')
        };

        render();

        // ADD
        els.form.addEventListener('submit', (e) => {
            e.preventDefault();
            const text = els.input.value.trim();
            if (!text) return;
            tasks.push({ id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now() + Math.random()), text, done: false });
            els.input.value = '';
            save(); render(); say('Task added');
        });

        // Toggle / Edit / Delete (event delegation)
        els.list.addEventListener('change', (e) => {
            const li = e.target.closest('li.item'); if (!li) return;
            if (e.target.matches('.check')) {
                const t = tasks.find(t => t.id === li.dataset.id);
                if (t) { t.done = e.target.checked; save(); render(); say(t.done ? 'Completed' : 'Marked active'); }
            }
        });

        els.list.addEventListener('click', (e) => {
            const li = e.target.closest('li.item'); if (!li) return;
            const id = li.dataset.id;

            if (e.target.matches('.delete')) {
                tasks = tasks.filter(t => t.id !== id);
                save(); render(); say('Task deleted');
            }

            if (e.target.matches('.edit')) {
                startEdit(li, id);
            }
            if (e.target.matches('.save')) {
                commitEdit(li, id);
            }
            if (e.target.matches('.cancel')) {
                cancelEdit();
            }
        });

        // Double-click text to edit
        els.list.addEventListener('dblclick', (e) => {
            const textEl = e.target.closest('.text'); if (!textEl) return;
            const li = textEl.closest('li.item');
            startEdit(li, li.dataset.id);
        });

        // Export JSON
        els.exportBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const blob = new Blob([JSON.stringify(tasks, null, 2)], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url; a.download = 'todos.json'; a.click();
            URL.revokeObjectURL(url);
        });

        // ---- Edit helpers ----
        function startEdit(li, id) {
            if (editing && editing.id !== id) commitEdit(editing.li, editing.id);
            const t = tasks.find(t => t.id === id); if (!t) return;

            const textEl = li.querySelector('.text');
            const input = document.createElement('input');
            input.className = 'edit-input';
            input.value = t.text;
            input.setAttribute('aria-label', 'Edit task');
            textEl.replaceWith(input);

            const actions = li.querySelector('.actions');
            actions.innerHTML = `
        <button class="icon save">💾</button>
        <button class="icon cancel">❌</button>
      `;

            editing = { id, li, input };
            input.focus(); input.selectionStart = input.selectionEnd = input.value.length;

            const onKey = (e) => {
                if (e.key === 'Enter') commitEdit(li, id);
                else if (e.key === 'Escape') cancelEdit();
            };
            input.addEventListener('keydown', onKey);
            input.addEventListener('blur', () => commitEdit(li, id));
        }

        function commitEdit(li, id) {
            if (!editing || editing.id !== id) return;
            const t = tasks.find(t => t.id === id); if (!t) return;
            const v = editing.input.value.trim();
            if (!v) {
                tasks = tasks.filter(x => x.id !== id);
                say('Empty text — task deleted');
            } else {
                t.text = v; say('Task edited');
            }
            editing = null; save(); render();
        }

        function cancelEdit() {
            editing = null; render();
        }

        // ---- Render & storage ----
        function render() {
            els.list.innerHTML = '';
            tasks.forEach(t => {
                const li = document.createElement('li');
                li.className = 'item';
                li.dataset.id = t.id;
                li.setAttribute('role', 'listitem');
                li.innerHTML = `
          <input class="check" type="checkbox" ${t.done ? 'checked' : ''} aria-label="Toggle completion">
          <div class="text ${t.done ? 'done' : ''}">${escapeHtml(t.text)}</div>
          <div class="actions">
            <button class="icon edit">✏</button>
            <button class="icon delete">🗑</button>
          </div>
        `;
                els.list.appendChild(li);
            });

            els.empty.style.display = tasks.length ? 'none' : 'block';
            save(); // keep storage synced
        }

        function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks)); }
        function load() { try { const raw = localStorage.getItem(STORAGE_KEY); return raw ? JSON.parse(raw) : []; } catch { return []; } }
        function say(msg) { els.live.textContent = msg; }
        function escapeHtml(str) { return str.replace(/[&<>"']/g, s => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[s])); }
    </script>
</body>

</html>'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
