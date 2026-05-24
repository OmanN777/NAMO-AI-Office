"use client";

import React, { useState, useEffect, use } from "react";
import Link from "next/link";
import { 
  ArrowLeft, 
  Target, 
  BarChart3, 
  TrendingUp, 
  Search, 
  FileText,
  AlertCircle,
  Shield,
  Calculator
} from "lucide-react";

interface StockData {
  ticker: string;
  thesis: string;
  brief: string;
  moat: string;
  financial: string;
  sentiment: string;
  segments: string;
  sourcesCount: number;
  sourceFiles: string[];
  lastUpdated: string;
}

export default function StockDetailPage({ params }: { params: Promise<{ ticker: string }> }) {
  const resolvedParams = use(params);
  const ticker = resolvedParams.ticker;
  const [data, setData] = useState<StockData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`/api/stock/${ticker}`);
        const result = await res.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching stock detail:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [ticker]);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center bg-slate-950">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (!data) return null;

  // Function to extract text after header
  const formatContent = (text: string) => {
    return text.split('\n').slice(1).join('\n').trim();
  };

  const getHypeLevel = (sentiment: string) => {
    if (sentiment.includes("EXTREME BULLISH")) return { label: "ร้อนแรงเกินไป (Overheated)", color: "text-red-500" };
    if (sentiment.includes("VERY BULLISH")) return { label: "ขาขึ้นชัดเจน (Strong Uptrend)", color: "text-orange-500" };
    if (sentiment.includes("BULLISH")) return { label: "แนวโน้มบวก (Positive Bias)", color: "text-emerald-500" };
    return { label: "ทรงตัว (Consolidating)", color: "text-slate-400" };
  };

  const hype = getHypeLevel(data.sentiment);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 p-6 md:p-12">
      <div className="max-w-6xl mx-auto space-y-12">
        {/* Back Button & Header */}
        <header className="flex flex-col gap-6">
          <Link 
            href="/" 
            className="flex items-center gap-2 text-slate-500 hover:text-blue-400 transition-colors group w-fit"
          >
            <ArrowLeft size={18} className="group-hover:-translate-x-1 transition-transform" />
            <span className="font-bold uppercase tracking-widest text-xs">กลับไปยังสำนักงาน</span>
          </Link>
          
          <div className="flex items-center gap-6">
            <div className="bg-blue-600 p-6 rounded-3xl shadow-2xl shadow-blue-500/20">
              <h1 className="text-5xl font-black tracking-tighter">{data.ticker}</h1>
            </div>
            <div>
              <p className="text-slate-500 font-bold uppercase tracking-widest text-xs mb-1">Stock Intelligence Report</p>
              <h2 className="text-2xl font-bold text-slate-200">บทวิเคราะห์และข่าวกรองเชิงลึก</h2>
            </div>
          </div>
        </header>

        {/* Main Intelligence Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          {/* Left Column: Thesis & Deep Dive */}
          <div className="lg:col-span-2 space-y-8">
            {/* Oman's Thesis Section */}
            <section className="bg-slate-900 rounded-[32px] border border-slate-800 p-8 shadow-xl relative overflow-hidden group">
              <div className="absolute -top-10 -right-10 opacity-5 group-hover:opacity-10 transition-opacity">
                <Target size={200} />
              </div>
              <div className="relative z-10">
                <div className="flex items-center gap-2 mb-6">
                  <Target className="text-blue-500" size={24} />
                  <h3 className="text-xl font-bold">สมมติฐานการลงทุน (Investment Thesis)</h3>
                </div>
                <div className="prose prose-invert prose-slate max-w-none">
                  <pre className="bg-slate-950/50 p-6 rounded-2xl border border-slate-800 text-sm overflow-x-auto whitespace-pre-wrap font-mono leading-relaxed text-slate-300">
                    {data.thesis}
                  </pre>
                </div>
              </div>
            </section>

            {/* Sub-agent Insight Blocks */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-slate-900 rounded-3xl border border-slate-800 p-6 hover:border-emerald-500/30 transition-colors">
                <div className="flex items-center gap-2 mb-4">
                  <BarChart3 className="text-emerald-500" size={20} />
                  <h4 className="font-bold text-sm uppercase tracking-wider text-emerald-400">Competitive Moat</h4>
                </div>
                <div className="text-xs text-slate-400 leading-relaxed whitespace-pre-wrap font-medium">
                  {data.moat ? formatContent(data.moat) : "กำลังรวบรวมข้อมูล..."}
                </div>
                <div className="mt-4 pt-4 border-t border-slate-800 flex items-center justify-between">
                  <span className="text-[9px] text-slate-500 font-bold uppercase">Analyst</span>
                  <span className="text-[9px] text-emerald-500 font-bold uppercase">Fundamentokung</span>
                </div>
              </div>

              <div className="bg-slate-900 rounded-3xl border border-slate-800 p-6 hover:border-orange-500/30 transition-colors">
                <div className="flex items-center gap-2 mb-4">
                  <TrendingUp className="text-orange-500" size={20} />
                  <h4 className="font-bold text-sm uppercase tracking-wider text-orange-400">Financials & KPIs</h4>
                </div>
                <div className="space-y-4">
                  <div className="text-xs text-slate-400 leading-relaxed whitespace-pre-wrap font-medium">
                    {data.financial ? formatContent(data.financial) : "กำลังวิเคราะห์งบการเงิน..."}
                  </div>
                  {data.segments && (
                    <div className="mt-4 pt-4 border-t border-slate-800">
                      <p className="text-[10px] text-slate-500 font-bold uppercase mb-2">Segment & Performance Analysis</p>
                      <div className="text-[11px] text-slate-300 leading-relaxed whitespace-pre-wrap font-mono bg-slate-950/50 p-3 rounded-xl border border-slate-800">
                        {formatContent(data.segments)}
                      </div>
                    </div>
                  )}
                </div>
                <div className="mt-4 pt-4 border-t border-slate-800 flex items-center justify-between">
                  <span className="text-[9px] text-slate-500 font-bold uppercase">Analyst</span>
                  <span className="text-[9px] text-orange-500 font-bold uppercase">Earnchan</span>
                </div>
              </div>
            </div>
          </div>

          {/* Right Sidebar: Sentiment & Sources */}
          <aside className="space-y-8">
            {/* Market Sentiment Card */}
            <div className="bg-slate-900 rounded-[32px] border border-slate-800 p-8 shadow-xl">
              <div className="flex items-center gap-2 mb-6">
                <Search className="text-red-500" size={20} />
                <h3 className="font-bold text-sm uppercase tracking-widest">Market Sentiment</h3>
              </div>
              <div className="space-y-6">
                <div className="bg-slate-950 p-6 rounded-2xl border border-slate-800 text-center shadow-inner">
                  <p className="text-[10px] uppercase text-slate-500 font-bold mb-1 tracking-[0.2em]">Hype-Meter</p>
                  <p className={`text-2xl font-black ${hype.color}`}>{hype.label}</p>
                </div>
                <div className="p-5 border-l-2 border-red-500 bg-red-500/5 rounded-r-2xl">
                  <div className="text-xs text-slate-300 leading-relaxed font-medium whitespace-pre-wrap italic">
                    {data.sentiment ? formatContent(data.sentiment).split('\n')[0] : "Newwy กำลังสแกนหาข่าวล่าสุด..."}
                  </div>
                </div>
                <div className="flex items-center justify-between px-2">
                  <span className="text-[9px] text-slate-500 font-bold uppercase text-red-500">Agent: Newwy</span>
                  <div className="w-2 h-2 rounded-full bg-red-500 animate-pulse" />
                </div>
              </div>
            </div>

            {/* Source Intelligence Card */}
            <div className="bg-slate-900 rounded-[32px] border border-slate-800 p-8 shadow-xl">
              <div className="flex items-center gap-2 mb-6">
                <FileText className="text-blue-400" size={20} />
                <h3 className="font-bold text-sm uppercase tracking-widest text-blue-400">แหล่งข้อมูลอ้างอิง</h3>
              </div>
              <div className="space-y-4">
                <div className="flex items-center justify-between bg-slate-950 p-4 rounded-xl border border-slate-800">
                  <span className="text-xs text-slate-400 font-medium italic">Verified Primary Files</span>
                  <span className="bg-blue-600/20 text-blue-400 px-3 py-1 rounded-full text-xs font-black border border-blue-500/30">{data.sourcesCount}</span>
                </div>
                {data.sourceFiles.length > 0 ? (
                  <div className="space-y-2 max-h-40 overflow-y-auto pr-2 custom-scrollbar">
                    {data.sourceFiles.map((file, i) => (
                      <div key={i} className="flex items-center gap-2 text-[10px] text-slate-500 font-mono py-1 border-b border-slate-800/50">
                        <div className="w-1 h-1 rounded-full bg-slate-700" />
                        {file}
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-[10px] text-slate-600 italic text-center py-4 bg-slate-950/50 rounded-xl">ไม่มีไฟล์ดิบในฐานข้อมูล (ใช้ Web Search)</p>
                )}
              </div>
            </div>

            {/* Warning Rule */}
            <div className="p-6 bg-amber-500/10 rounded-3xl border border-amber-500/20 flex gap-4 shadow-lg shadow-amber-500/5">
              <Shield className="text-amber-500 shrink-0" size={20} />
              <p className="text-[11px] text-amber-500/90 leading-relaxed font-bold uppercase tracking-tight">
                Simulated Data Only: Agent Oman ปฏิบัติตามกฎความลับ (Blindness Rule) ข้อมูลนี้ไม่ใช่คำแนะนำการลงทุนจริง
              </p>
            </div>
          </aside>

        </div>
      </div>
    </div>
  );
}
