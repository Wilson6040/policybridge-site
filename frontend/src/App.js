import { useEffect, useState } from "react";
import "@/App.css";
import axios from "axios";
import {
  FileText, Download, FileType, ShieldCheck, Loader2, ExternalLink, CheckCircle2, AlertCircle,
} from "lucide-react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const DocCard = ({ doc }) => {
  const [busy, setBusy] = useState(null);
  const [status, setStatus] = useState(null); // {type:'ok'|'err', text}

  const download = async (f) => {
    setBusy(f.ext);
    setStatus(null);
    try {
      // Fetch the bytes and download via a local blob URL — works in any
      // browser/tab and isn't affected by download/popup blockers.
      const res = await axios.get(
        `${API}/documents/download/${encodeURIComponent(f.filename)}`,
        { responseType: "blob" }
      );
      const blob = new Blob([res.data], {
        type: res.headers["content-type"] || "application/octet-stream",
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = f.filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 5000);
      setStatus({ type: "ok", text: `Saved ${f.filename} to your Downloads.` });
    } catch (e) {
      setStatus({
        type: "err",
        text: "Download failed. Open this page in a new browser tab (button at the top), then try again.",
      });
    } finally {
      setBusy(null);
    }
  };

  return (
    <div
      data-testid={`doc-card-${doc.id}`}
      className="group relative flex flex-col rounded-xl bg-white border border-slate-200 shadow-sm hover:shadow-xl transition-shadow duration-300 overflow-hidden"
    >
      <div className="h-1.5 w-full" style={{ backgroundColor: doc.accent }} />
      <div className="p-6 flex flex-col flex-1">
        <div className="flex items-start gap-3 mb-3">
          <div
            className="shrink-0 grid place-items-center h-11 w-11 rounded-lg"
            style={{ backgroundColor: `${doc.accent}1A`, color: doc.accent }}
          >
            <FileText size={22} strokeWidth={2} />
          </div>
          <div>
            <h3 className="text-[17px] font-semibold text-slate-900 leading-tight">{doc.title}</h3>
            <p className="text-xs font-medium tracking-wide uppercase mt-0.5" style={{ color: doc.accent }}>
              {doc.subtitle}
            </p>
          </div>
        </div>
        <p className="text-[13.5px] leading-relaxed text-slate-600 flex-1">{doc.description}</p>

        <div className="mt-5 flex flex-wrap gap-2.5">
          {doc.formats.map((f) => (
            <button
              key={f.ext}
              data-testid={`download-${doc.id}-${f.ext}`}
              onClick={() => download(f)}
              disabled={busy === f.ext}
              className={`inline-flex items-center gap-2 rounded-lg px-3.5 py-2 text-sm font-semibold transition-all duration-200 active:scale-[0.98] disabled:opacity-70 ${
                f.ext === "docx" ? "text-white hover:brightness-110" : "bg-slate-100 text-slate-700 hover:bg-slate-200"
              }`}
              style={f.ext === "docx" ? { backgroundColor: doc.accent } : {}}
            >
              {busy === f.ext ? (
                <Loader2 size={16} className="animate-spin" />
              ) : f.ext === "docx" ? (
                <Download size={16} />
              ) : (
                <FileType size={16} />
              )}
              {f.ext === "docx" ? "Word (.docx)" : "PDF"}
              <span className="text-[11px] font-normal opacity-80">{f.size_kb} KB</span>
            </button>
          ))}
          {doc.formats.map((f) => (
            <a
              key={`open-${f.ext}`}
              href={`${API}/documents/download/${encodeURIComponent(f.filename)}`}
              target="_blank"
              rel="noopener noreferrer"
              data-testid={`open-${doc.id}-${f.ext}`}
              className="inline-flex items-center gap-1.5 rounded-lg px-2.5 py-2 text-xs font-medium text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition-colors"
              title={`Open ${f.ext.toUpperCase()} in a new tab`}
            >
              <ExternalLink size={13} /> open {f.ext}
            </a>
          ))}
        </div>

        {status && (
          <div
            data-testid={`status-${doc.id}`}
            className={`mt-3 flex items-start gap-2 text-[12.5px] rounded-lg px-3 py-2 ${
              status.type === "ok" ? "bg-emerald-50 text-emerald-800" : "bg-red-50 text-red-700"
            }`}
          >
            {status.type === "ok" ? <CheckCircle2 size={15} className="mt-px shrink-0" /> : <AlertCircle size={15} className="mt-px shrink-0" />}
            <span>{status.text}</span>
          </div>
        )}
      </div>
    </div>
  );
};

const Home = () => {
  const [docs, setDocs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get(`${API}/documents`)
      .then((res) => setDocs(res.data.documents || []))
      .catch(() => setError("Could not load documents."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-50" data-testid="document-centre">
      <header className="bg-[#0B2A45] text-white">
        <div className="max-w-5xl mx-auto px-6 py-10">
          <div className="flex items-center gap-2 text-[#62c7f0] text-sm font-semibold tracking-wide">
            <ShieldCheck size={18} /> TOKIO MARINE HCC
          </div>
          <h1 className="mt-3 text-3xl sm:text-4xl font-bold tracking-tight">Document Centre</h1>
          <p className="mt-2 text-slate-300 max-w-2xl text-[15px]">
            Media &amp; Entertainment — download your branded, market-ready documents below: the new
            coverage comparison &amp; gap-fill strategy (TMHCC vs five competitors), plus the
            Media &amp; Music Combined (0526) wording set. Word files open and edit directly in
            Microsoft Word; PDFs are ready to share.
          </p>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-6 py-10">
        <div
          data-testid="open-new-tab-banner"
          className="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 rounded-xl border border-amber-200 bg-amber-50 px-4 py-3"
        >
          <p className="text-[13.5px] text-amber-900">
            <span className="font-semibold">Best results:</span> open this page in its own browser tab,
            then click a button — the file saves straight to your Downloads. Each card also has a small
            “open” link to view the file in a new tab.
          </p>
          <a
            href={window.location.href}
            target="_blank"
            rel="noopener noreferrer"
            data-testid="open-new-tab-btn"
            className="inline-flex shrink-0 items-center gap-2 rounded-lg bg-amber-500 px-3.5 py-2 text-sm font-semibold text-white hover:bg-amber-600 transition-colors"
          >
            <ExternalLink size={16} /> Open in a new tab
          </a>
        </div>

        {loading && (
          <div className="flex items-center gap-2 text-slate-500" data-testid="loading-state">
            <Loader2 className="animate-spin" size={18} /> Loading documents…
          </div>
        )}
        {error && (
          <div className="text-red-600 bg-red-50 border border-red-200 rounded-lg px-4 py-3" data-testid="error-state">
            {error}
          </div>
        )}
        {!loading && !error && (
          <div className="space-y-10" data-testid="documents-grid">
            {Array.from(new Set(docs.map((d) => d.group || "Documents"))).map((group) => (
              <section key={group} data-testid={`doc-group-${group}`}>
                <h2 className="text-[13px] font-bold uppercase tracking-wider text-[#00648B] mb-1">
                  {group}
                </h2>
                <div className="h-px w-full bg-gradient-to-r from-[#00648B]/40 to-transparent mb-5" />
                <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                  {docs
                    .filter((d) => (d.group || "Documents") === group)
                    .map((d) => (
                      <DocCard key={d.id} doc={d} />
                    ))}
                </div>
              </section>
            ))}
          </div>
        )}

        <div className="mt-10 rounded-xl border border-slate-200 bg-white p-5 text-[13.5px] text-slate-600">
          <p className="font-semibold text-slate-800 mb-1">Keeping the files</p>
          To keep the whole project (including these documents) in your own GitHub, use the
          <span className="font-semibold text-slate-800"> “Save to GitHub” </span>
          option in the chat input and download them from your repository.
        </div>
      </main>
    </div>
  );
};

function App() {
  return <Home />;
}

export default App;
