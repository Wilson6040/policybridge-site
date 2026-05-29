import { useEffect, useState } from "react";
import "@/App.css";
import axios from "axios";
import { FileText, Download, FileType, ShieldCheck, Loader2 } from "lucide-react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const DocCard = ({ doc }) => {
  const download = (filename) => {
    window.location.href = `${API}/documents/download/${encodeURIComponent(filename)}`;
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
              onClick={() => download(f.filename)}
              className={`inline-flex items-center gap-2 rounded-lg px-3.5 py-2 text-sm font-semibold transition-all duration-200 active:scale-[0.98] ${
                f.ext === "docx"
                  ? "text-white hover:brightness-110"
                  : "bg-slate-100 text-slate-700 hover:bg-slate-200"
              }`}
              style={f.ext === "docx" ? { backgroundColor: doc.accent } : {}}
            >
              {f.ext === "docx" ? <Download size={16} /> : <FileType size={16} />}
              {f.ext === "docx" ? "Word (.docx)" : "PDF"}
              <span className="text-[11px] font-normal opacity-80">{f.size_kb} KB</span>
            </button>
          ))}
        </div>
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
      .catch((e) => setError("Could not load documents."))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-slate-50" data-testid="document-centre">
      {/* Header */}
      <header className="bg-[#0B2A45] text-white">
        <div className="max-w-5xl mx-auto px-6 py-10">
          <div className="flex items-center gap-2 text-[#62c7f0] text-sm font-semibold tracking-wide">
            <ShieldCheck size={18} /> TOKIO MARINE HCC
          </div>
          <h1 className="mt-3 text-3xl sm:text-4xl font-bold tracking-tight">Document Centre</h1>
          <p className="mt-2 text-slate-300 max-w-2xl text-[15px]">
            Media &amp; Music Combined (0526) — download your branded, market-ready documents below.
            Word files open and edit directly in Microsoft Word; PDFs are ready to share.
          </p>
        </div>
      </header>

      {/* Body */}
      <main className="max-w-5xl mx-auto px-6 py-10">
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
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5" data-testid="documents-grid">
            {docs.map((d) => (
              <DocCard key={d.id} doc={d} />
            ))}
          </div>
        )}

        <div className="mt-10 rounded-xl border border-slate-200 bg-white p-5 text-[13.5px] text-slate-600">
          <p className="font-semibold text-slate-800 mb-1">Tip: editing the Word files</p>
          When you open the new wording in Microsoft Word, the table of contents page numbers and footer
          numbers are already set. To keep the whole project (including these files), use the
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
