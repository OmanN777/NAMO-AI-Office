"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { Agent, Portfolio, Command, Universe, agentTheme } from "@/lib/types";
import { 
  Users, 
  User,
  LayoutDashboard, 
  ChevronRight, 
  Target, 
  AlertCircle,
  Code2,
  FileText,
  Clock,
  TrendingUp,
  Globe,
  Info,
  Shield,
  Lightbulb,
  Calendar
} from "lucide-react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Dashboard() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [globalCommands, setGlobalCommands] = useState<Command[]>([]);
  const [portfolio, setPortfolio] = useState<Portfolio | null>(null);
  const [universe, setUniverse] = useState<Universe | null>(null);
  const [selectedAgent, setSelectedAgent] = useState<Agent | null>(null);
  const [loading, setLoading] = useState(true);
  const [currentDate, setCurrentDate] = useState("2026-05-28");
  const [activeTab, setActiveTab] = useState<'dashboard' | 'about'>('dashboard');
  
  const availableDates = ["2026-05-19", "2026-05-21", "2026-05-23", "2026-05-28"];

  useEffect(() => {
    async function fetchData() {
      try {
        const [agentsRes, portfolioRes, commandsRes, universeRes] = await Promise.all([
          fetch("/api/agents", { cache: "no-store" }),
          fetch(`/api/portfolio?date=${currentDate}`, { cache: "no-store" }),
          fetch("/api/commands", { cache: "no-store" }),
          fetch("/api/universe", { cache: "no-store" })
        ]);
        const agentsData = await agentsRes.json();
        const portfolioData = await portfolioRes.json();
        const commandsData = await commandsRes.json();
        const universeData = await universeRes.json();
        
        setAgents(agentsData);
        setPortfolio(portfolioData);
        setGlobalCommands(commandsData);
        setUniverse(universeData);
        
        if (!selectedAgent) {
          const oman = agentsData.find((a: Agent) => a.id === "oman");
          if (oman) setSelectedAgent(oman);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [currentDate, selectedAgent]);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center bg-slate-950">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  const agentCommands = selectedAgent ? globalCommands.filter(cmd => cmd.id.startsWith(selectedAgent.id)) : [];

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-900 border-r border-slate-800 flex flex-col">
        <div className="p-6 border-b border-slate-800 flex items-center gap-3">
          <div className="bg-blue-600 p-2 rounded-lg">
            <LayoutDashboard size={20} />
          </div>
          <h1 className="font-bold text-lg tracking-tight uppercase">Namo Executive Office</h1>
        </div>
        
        <nav className="flex-1 overflow-y-auto p-4 space-y-2">
          <div className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-2 px-2">
            ทีมงาน AI (Staff)
          </div>
          {agents.map((agent) => {
            const ThemeIcon = agentTheme[agent.id]?.icon || Users;
            const isSelected = selectedAgent?.id === agent.id;
            const isOman = agent.id === 'oman';
            const isMalli = agent.id === 'malli';
            
            return (
              <button
                key={agent.id}
                onClick={() => {
                  setSelectedAgent(agent);
                  if (agent.id !== 'oman') setActiveTab('dashboard');
                }}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all ${
                  isSelected 
                    ? "bg-slate-800 text-blue-400 shadow-sm" 
                    : "text-slate-200 hover:bg-slate-800/50 hover:text-white"
                }`}
              >
                <ThemeIcon size={18} className={isOman ? "text-blue-500" : isMalli ? "text-rose-400" : "text-slate-400"} />
                <span className={`text-sm font-medium capitalize ${isOman ? "font-bold" : ""}`}>
                  {isOman ? 'Oman (พอร์ตจำลอง)' : isMalli ? 'Malli (เลขาบริหาร)' : agent.id === 'scout' ? 'Scout (ผู้เสาะหา)' : agent.id}
                </span>
                {isSelected && <ChevronRight size={14} className="ml-auto" />}
              </button>
            );
          })}
        </nav>

        <div className="p-4 border-t border-slate-800">
          <div className="bg-slate-800/50 rounded-lg p-3 border border-slate-700/50">
            <p className="text-[10px] text-slate-500 uppercase font-bold mb-1">โปรไฟล์ CEO</p>
            <p className="text-sm font-medium">Namo</p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto bg-slate-950 p-8">
        {selectedAgent && (
          <div className="max-w-7xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-500">
            
            {/* Header / Tabs & Metadata for Oman */}
            {selectedAgent.id === "oman" ? (
              <div className="flex flex-col md:flex-row md:items-end justify-between border-b border-slate-800 pb-4 mb-8">
                <div className="flex items-end gap-4">
                  <div className="flex gap-4">
                    <button 
                      onClick={() => setActiveTab('dashboard')}
                      className={`px-6 py-3 rounded-t-xl font-bold transition-colors ${
                        activeTab === 'dashboard' ? "bg-slate-800 text-white border-t border-x border-slate-700" : "text-slate-500 hover:text-slate-300"
                      }`}
                    >
                      แดชบอร์ดพอร์ตจำลอง
                    </button>
                    <button 
                      onClick={() => setActiveTab('about')}
                      className={`px-6 py-3 rounded-t-xl font-bold transition-colors ${
                        activeTab === 'about' ? "bg-slate-800 text-white border-t border-x border-slate-700" : "text-slate-500 hover:text-slate-300"
                      }`}
                    >
                      เกี่ยวกับโปรเจกต์
                    </button>
                  </div>

                  {/* Timeline Switcher */}
                  <div className="flex items-center gap-2 mb-2 px-4 py-1.5 bg-slate-900/50 rounded-full border border-slate-800 ml-4">
                    <Calendar size={12} className="text-blue-500" />
                    <span className="text-[10px] font-bold text-slate-500 uppercase mr-2">Timeline:</span>
                    {availableDates.map(date => (
                      <button
                        key={date}
                        onClick={() => setCurrentDate(date)}
                        className={`text-[10px] px-3 py-1 rounded-full font-black transition-all ${
                          currentDate === date 
                            ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20" 
                            : "text-slate-500 hover:text-slate-300"
                        }`}
                      >
                        {date === "2026-05-28" ? "LIVE" : date.split('-').slice(1).join('/')}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="flex items-center gap-6 mb-2">
                  <div className="flex items-center gap-4 px-4 py-2 bg-slate-900 rounded-2xl border border-slate-800 shadow-inner">
                    <div className="text-right border-r border-slate-800 pr-4">
                      <p className="text-[8px] text-slate-500 font-bold uppercase tracking-widest mb-0.5">Cash Balance</p>
                      <p className="text-sm font-black text-blue-400 italic">${portfolio?.cash_balance?.toLocaleString(undefined, {minimumFractionDigits: 2})}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-[8px] text-slate-500 font-bold uppercase tracking-widest mb-0.5">Net Asset Value</p>
                      <div className="flex items-center gap-1.5 justify-end">
                        <div className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                        <p className="text-xl font-black text-white italic">
                          ${portfolio?.current_nav?.toLocaleString()}
                        </p>
                      </div>
                    </div>
                  </div>
                  <div className={`px-4 py-2 h-[52px] flex flex-col justify-center rounded-2xl border ${
                    portfolio && portfolio.current_nav >= portfolio.initial_nav 
                      ? "bg-emerald-500/10 border-emerald-500/20 text-emerald-400" 
                      : "bg-red-500/10 border-red-500/20 text-red-400"
                  }`}>
                    <p className="text-[8px] font-bold uppercase tracking-tighter">Total Return</p>
                    <p className="text-lg font-black tracking-tight">
                      {portfolio && portfolio.current_nav >= portfolio.initial_nav ? '+' : ''}
                      {portfolio ? (((portfolio.current_nav - portfolio.initial_nav) / portfolio.initial_nav) * 100).toFixed(2) : 0}%
                    </p>
                  </div>
                </div>
              </div>
            ) : (
              <div className="flex items-center justify-between border-b border-slate-800 pb-8 mb-8">
                <div>
                  <h2 className="text-4xl font-black tracking-tighter flex items-center gap-4">
                    <span className="text-slate-500">Agent</span>
                    <span className="text-white capitalize">{selectedAgent.id}</span>
                  </h2>
                  <p className="text-slate-400 mt-2 font-medium italic">&quot;{selectedAgent.description}&quot;</p>
                </div>
                <div className="px-6 py-3 bg-slate-900 rounded-2xl border border-slate-800 flex items-center gap-4">
                  <div className="text-right">
                    <p className="text-[10px] text-slate-500 font-bold uppercase tracking-widest">Team Status</p>
                    <p className="text-sm font-bold text-emerald-400">ONLINE</p>
                  </div>
                  <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-500">
                    <Shield size={20} />
                  </div>
                </div>
              </div>
            )}

            {/* Content for Oman Dashboard */}
            {selectedAgent.id === "oman" && activeTab === 'dashboard' && portfolio && (
              <div className="space-y-8">
                {/* Top Row: Performance Chart & Actions */}
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                  <div className="lg:col-span-2">
                    <section className="bg-slate-900 rounded-3xl border border-slate-800 p-8 shadow-lg">
                      <div className="flex items-center justify-between mb-8">
                        <div className="flex items-center gap-2">
                          <TrendingUp className="text-blue-500" size={18} />
                          <h3 className="font-bold">Performance History</h3>
                        </div>
                        <div className="flex items-center gap-4 text-[10px] font-bold uppercase tracking-widest">
                          <div className="flex items-center gap-1.5">
                            <div className="w-2 h-2 rounded-full bg-blue-500" />
                            <span className="text-slate-300">Oman Portfolio</span>
                          </div>
                          <div className="flex items-center gap-1.5">
                            <div className="w-2 h-2 rounded-full bg-slate-700" />
                            <span className="text-slate-500">S&P 500 (Benchmark)</span>
                          </div>
                        </div>
                      </div>
                      <div className="h-64 w-full">
                        <ResponsiveContainer width="100%" height="100%">
                          <LineChart data={portfolio.performance_history}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                            <XAxis 
                              dataKey="date" 
                              stroke="#64748b" 
                              fontSize={10} 
                              tickLine={false} 
                              axisLine={false}
                              tickFormatter={(val) => val.split('-').slice(1).join('/')}
                            />
                            <YAxis 
                              stroke="#64748b" 
                              fontSize={10} 
                              tickLine={false} 
                              axisLine={false}
                              tickFormatter={(val) => `${val}%`}
                            />
                            <Tooltip 
                              contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '12px' }}
                              itemStyle={{ fontSize: '10px', fontWeight: 'bold' }}
                            />
                            <Line 
                              type="monotone" 
                              dataKey="oman_return" 
                              stroke="#3b82f6" 
                              strokeWidth={3} 
                              dot={{ fill: '#3b82f6', r: 4 }}
                              activeDot={{ r: 6, strokeWidth: 0 }}
                            />
                            <Line 
                              type="monotone" 
                              dataKey="spy_return" 
                              stroke="#334155" 
                              strokeWidth={2} 
                              strokeDasharray="5 5"
                              dot={false}
                            />
                          </LineChart>
                        </ResponsiveContainer>
                      </div>
                    </section>
                  </div>

                  <div className="lg:col-span-1">
                    <section className="bg-slate-900 rounded-3xl border border-slate-800 p-6 shadow-lg h-full flex flex-col">
                      <div className="flex items-center gap-2 mb-6">
                        <AlertCircle className="text-orange-500" size={18} />
                        <h3 className="font-bold text-sm">การดำเนินการของ Oman</h3>
                      </div>
                      <div className="space-y-4 flex-1 overflow-y-auto pr-2 custom-scrollbar">
                        {portfolio.recommended_actions.slice(-4).reverse().map((action, idx) => (
                          <div key={idx} className="p-4 bg-slate-950 border border-slate-800 rounded-2xl flex items-start gap-3">
                            <div className="w-1.5 h-1.5 rounded-full bg-blue-500 mt-1.5 shrink-0" />
                            <p className="text-[11px] text-slate-300 leading-relaxed font-medium">{action}</p>
                          </div>
                        ))}
                      </div>
                    </section>
                  </div>
                </div>

                {/* Middle Section: Full-width Holdings */}
                <section className="bg-slate-900 rounded-3xl border border-slate-800 p-8 shadow-lg overflow-hidden">
                  <div className="flex items-center justify-between mb-8">
                    <h3 className="font-bold text-lg flex items-center gap-2 text-white">
                      <Target size={20} className="text-blue-500" />
                      หุ้นในพอร์ตปัจจุบัน
                    </h3>
                  </div>
                  <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
                      {portfolio.holdings.map((h) => {
                        const currentValue = h.total_value;
                        const costBasis = h.average_cost * h.shares;
                        const plValue = currentValue - costBasis;
                        const plPercent = costBasis !== 0 ? (plValue / costBasis) * 100 : 0;
                        const isProfit = plValue >= 0;

                        return (
                          <Link 
                            key={h.ticker} 
                            href={`/stock/${h.ticker}`}
                            className="flex items-center justify-between p-4 bg-slate-950 border border-slate-800 rounded-2xl hover:border-blue-500/50 transition-all group"
                          >
                            <div className="flex items-center gap-3">
                              <div className={`w-1 h-8 rounded-full ${h.position_type === 'SHORT' ? 'bg-red-500' : 'bg-emerald-500'}`} />
                              <div>
                                <p className="font-bold text-white text-sm group-hover:text-blue-400 transition-colors">
                                  {h.ticker}
                                  <span className={`ml-2 text-[8px] px-1.2 py-0.5 rounded border ${
                                    h.position_type === 'SHORT' 
                                      ? 'text-red-400 border-red-500/30 bg-red-500/10' 
                                      : 'text-emerald-400 border-emerald-500/30 bg-emerald-500/10'
                                  }`}>
                                    {h.position_type || 'LONG'}
                                  </span>
                                </p>
                                <div className="mt-1 flex flex-col gap-0.5">
                                  <div className="flex items-center gap-1.5">
                                    <p className="text-[10px] font-bold text-white">${ (h.total_value / h.shares).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2}) }</p>
                                    <p className="text-[8px] text-slate-500 font-medium uppercase tracking-tighter">Market Price</p>
                                  </div>
                                  <div className="flex items-center gap-1.5">
                                    <p className="text-[10px] font-bold text-slate-400">${h.average_cost.toLocaleString()}</p>
                                    <p className="text-[8px] text-slate-600 font-medium uppercase tracking-tighter">Avg Cost</p>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div className="text-right flex flex-col items-end">
                              <p className="text-sm font-black text-white leading-none">${h.total_value.toLocaleString()}</p>
                              <div className={`mt-1 flex flex-col items-end`}>
                                <p className={`text-[10px] font-black leading-none ${isProfit ? 'text-emerald-500' : 'text-red-500'}`}>
                                  {isProfit ? '+' : ''}{plPercent.toFixed(2)}%
                                </p>
                                <p className={`text-[8px] font-bold leading-tight ${isProfit ? 'text-emerald-600/70' : 'text-red-600/70'}`}>
                                  {isProfit ? '+' : ''}${plValue.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}
                                </p>
                              </div>
                            </div>
                          </Link>
                        );
                      })}
                  </div>
                </section>

                {/* Bottom Row: Universe */}
                <section className="bg-slate-900 rounded-3xl border border-slate-800 overflow-hidden shadow-lg">
                  <div className="p-6 border-b border-slate-800 bg-slate-900/50 flex items-center justify-between">
                    <h3 className="font-bold flex items-center gap-2">
                      <Globe size={18} className="text-emerald-500" />
                      จักรวาลหุ้นที่พิจารณา (The Universe)
                    </h3>
                  </div>
                  <div className="p-6">
                    <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4">
                      {universe?.items.map((item) => (
                        <Link 
                          key={item.ticker} 
                          href={`/stock/${item.ticker}`}
                          className="bg-slate-800/40 rounded-2xl border border-slate-700/50 p-4 hover:border-blue-500/50 transition-all group flex flex-col justify-between cursor-pointer"
                        >
                          <div>
                            <div className="flex items-center justify-between mb-3">
                              <div>
                                <h4 className="font-bold text-white text-base group-hover:text-blue-400 transition-colors">{item.ticker}</h4>
                                <p className="text-[9px] text-slate-500 font-bold uppercase">{item.name}</p>
                              </div>
                              <span className={`px-2 py-0.5 rounded-full text-[7px] font-black tracking-widest ${
                                item.status === 'SELECTED' ? 'bg-emerald-500/20 text-emerald-400' :
                                item.status === 'DISQUALIFIED' ? 'bg-red-500/20 text-red-400' : 'bg-slate-500/20 text-slate-400'
                              }`}>
                                {item.status}
                              </span>
                            </div>
                            <p className="text-[10px] text-slate-400 leading-relaxed line-clamp-3">
                              {item.reason}
                            </p>
                          </div>
                        </Link>
                      ))}
                    </div>
                  </div>
                </section>
              </div>
            )}

            {/* Redesigned About Oman View */}
            {selectedAgent.id === "oman" && activeTab === 'about' && (
              <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
                {/* Left Column: Avatar & Profile */}
                <div className="md:col-span-1 space-y-6">
                  <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-lg flex flex-col items-center text-center">
                    <div className="w-32 h-32 bg-blue-900/30 rounded-2xl border-2 border-blue-500/30 flex items-center justify-center mb-4 relative overflow-hidden">
                      <User size={64} className="text-blue-500/50" />
                      <div className="absolute inset-0 bg-gradient-to-t from-blue-900/50 to-transparent" />
                    </div>
                    <h2 className="text-2xl font-black italic">Oman</h2>
                    <p className="text-[10px] text-slate-500 font-bold uppercase tracking-widest mt-2">Portfolio Manager</p>
                    <div className="mt-4 space-y-2 w-full">
                      <div className="px-3 py-2 bg-slate-950 rounded-xl border border-slate-800 text-left">
                        <p className="text-[8px] text-slate-500 font-bold uppercase">Budget</p>
                        <p className="text-sm font-bold text-blue-400">$30,000 USD</p>
                      </div>
                      <div className="px-3 py-2 bg-slate-950 rounded-xl border border-slate-800 text-left">
                        <p className="text-[8px] text-slate-500 font-bold uppercase">Status</p>
                        <p className="text-sm font-bold text-emerald-400">Active</p>
                      </div>
                      <div className="px-2 py-1 bg-red-500/10 text-red-400 text-[9px] font-black tracking-widest rounded-md mt-2 uppercase border border-red-500/20">
                        Blindness Rule Active
                      </div>
                    </div>
                  </div>

                  {/* System Identity / Specifications */}
                  <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-lg">
                    <h4 className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-4">System Specifications</h4>
                    <div className="space-y-4">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-lg bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
                          <Code2 size={16} />
                        </div>
                        <div>
                          <p className="text-[10px] text-slate-500 font-bold uppercase">Decision Logic</p>
                          <p className="text-xs font-bold">Rule-based Engineering</p>
                        </div>
                      </div>
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
                          <Target size={16} />
                        </div>
                        <div>
                          <p className="text-[10px] text-slate-500 font-bold uppercase">Risk Tolerance</p>
                          <p className="text-xs font-bold">Aggressive / High-Conviction</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Right Column: Narrative & Identity */}
                <div className="md:col-span-3 space-y-8">
                  <section className="bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-lg relative overflow-hidden group">
                    <div className="absolute top-0 right-0 p-8 opacity-5 group-hover:scale-110 transition-transform duration-700">
                      <Shield size={200} />
                    </div>
                    <div className="relative z-10">
                      <div className="flex items-center gap-3 mb-6">
                        <div className="p-2 bg-blue-500/10 rounded-xl text-blue-400 border border-blue-500/20">
                          <Shield size={20} />
                        </div>
                        <h3 className="text-xl font-bold">The Blindness Rule</h3>
                      </div>
                      <p className="text-slate-300 leading-relaxed font-medium text-lg italic bg-slate-950/50 p-6 rounded-2xl border border-slate-800">
                        &quot;Oman ถูกสั่งห้ามไม่ให้เข้าถึง หรือวิเคราะห์ข้อมูลพอร์ตการลงทุนจริงของเจ้าของโดยเด็ดขาด 
                        เพื่อรักษาความบริสุทธิ์ของกลยุทธ์จำลองและความเป็นส่วนตัวสูงสุด&quot;
                      </p>
                    </div>
                  </section>

                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <section className="bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-lg">
                      <div className="flex items-center gap-3 mb-6">
                        <div className="p-2 bg-amber-500/10 rounded-xl text-amber-400 border border-amber-500/20">
                          <Lightbulb size={20} />
                        </div>
                        <h3 className="text-xl font-bold">ปรัชญาการลงทุน</h3>
                      </div>
                      <ul className="space-y-4">
                        {[
                          "เน้น Aggressive Growth ในกลุ่มเทคโนโลยี",
                          "คัดเลือกเฉพาะบริษัทที่มี Engineering Strength",
                          "สมมติฐานหลัก: AI-Energy Convergence",
                          "เน้น Scalability ของโมเดลธุรกิจ"
                        ].map((text, i) => (
                          <li key={i} className="flex items-start gap-3">
                            <div className="w-1.5 h-1.5 rounded-full bg-amber-500 mt-2 shrink-0" />
                            <span className="text-slate-300 font-medium">{text}</span>
                          </li>
                        ))}
                      </ul>
                    </section>

                    <section className="bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-lg">
                      <div className="flex items-center gap-3 mb-6">
                        <div className="p-2 bg-rose-500/10 rounded-xl text-rose-400 border border-rose-500/20">
                          <Info size={20} />
                        </div>
                        <h3 className="text-xl font-bold">การบริหารจัดการ</h3>
                      </div>
                      <div className="space-y-4 text-sm text-slate-400 leading-relaxed font-medium">
                        <p>ควบคุมพอร์ตผ่านคำสั่ง CLI โดยตรง ทุกการตัดสินใจต้องบันทึกลงใน Investment Thesis เพื่อใช้ในการเรียนรู้ย้อนหลัง</p>
                        <div className="p-4 bg-slate-950 rounded-2xl border border-slate-800">
                          <p className="text-[10px] text-slate-500 font-bold uppercase mb-2">Primary Sources Only</p>
                          <p className="text-xs italic text-slate-300">
                            &quot;เชื่อในข้อมูลดิบ เช่น 10-K และ Earnings Transcript มากกว่าการคาดเดาจากแหล่งข่าวลอยๆ&quot;
                          </p>
                        </div>
                      </div>
                    </section>
                  </div>

                  {/* Available Commands Section for Oman */}
                  <section className="bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-lg">
                    <div className="flex items-center gap-3 mb-6">
                      <div className="p-2 bg-blue-500/10 rounded-xl text-blue-400 border border-blue-500/20">
                        <Code2 size={20} />
                      </div>
                      <h3 className="text-xl font-bold">คำสั่งเฉพาะ (Available Commands)</h3>
                    </div>
                    {agentCommands.length > 0 ? (
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {agentCommands.map((cmd) => (
                          <div key={cmd.id} className="p-4 bg-slate-950 rounded-2xl border border-slate-800 hover:border-blue-500/50 transition-colors">
                            <p className="font-mono text-sm font-bold text-blue-400 mb-2">{cmd.name}</p>
                            <p className="text-xs text-slate-400 font-medium leading-relaxed">{cmd.description || "ไม่มีคำอธิบาย"}</p>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <p className="text-sm text-slate-500 italic">ไม่มีคำสั่งเฉพาะสำหรับ Agent นี้</p>
                    )}
                  </section>
                </div>
              </div>
            )}

            {/* Standard Agent Protocols View (For other agents) */}
            {selectedAgent.id !== "oman" && (
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div className="lg:col-span-2 space-y-8">
                  <section className="bg-slate-900 rounded-3xl border border-slate-800 p-8 shadow-lg">
                    <div className="flex items-center gap-2 mb-6">
                      <FileText size={18} className="text-blue-500" />
                      <h3 className="font-bold">Agent Protocols & Logic</h3>
                    </div>
                    <pre className="bg-slate-950 p-6 rounded-2xl border border-slate-800 text-xs overflow-x-auto whitespace-pre-wrap font-mono leading-relaxed text-slate-300">
                      {selectedAgent.content.split('---').pop()?.trim()}
                    </pre>
                  </section>
                </div>

                <div className="space-y-8">
                  <div className="bg-slate-900 rounded-3xl border border-slate-800 p-6 shadow-lg">
                    <div className="flex items-center gap-2 mb-4">
                      <User size={18} className="text-blue-500" />
                      <h3 className="font-bold text-sm">Persona</h3>
                    </div>
                    <p className="text-sm italic text-slate-400 leading-relaxed bg-slate-950 p-4 rounded-xl border border-slate-800">
                      &quot;{selectedAgent.persona || "No persona defined."}&quot;
                    </p>
                  </div>

                  <div className="bg-slate-900 rounded-3xl border border-slate-800 p-6 shadow-lg flex-1">
                    <div className="flex items-center gap-2 mb-6">
                      <Clock size={18} className="text-blue-500" />
                      <h3 className="font-bold text-sm">Recent Activity</h3>
                    </div>
                    <div className="space-y-4">
                      {/* Placeholder for real commands log */}
                      {[
                        "ตรวจสอบข้อมูลตลาดล่าสุด",
                        "สรุปรายงานประจำวัน",
                        "วิเคราะห์ปัจจัยพื้นฐานหุ้นกลุ่มใหม่"
                      ].map((activity, i) => (
                        <div key={i} className="flex items-center gap-3">
                          <div className="w-1.5 h-1.5 rounded-full bg-blue-500/50" />
                          <p className="text-xs text-slate-400 font-medium">{activity}</p>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Available Commands Section for other agents */}
                  <div className="bg-slate-900 rounded-3xl border border-slate-800 p-6 shadow-lg flex-1 mt-8">
                    <div className="flex items-center gap-2 mb-6">
                      <Code2 size={18} className="text-blue-500" />
                      <h3 className="font-bold text-sm">Available Commands</h3>
                    </div>
                    {agentCommands.length > 0 ? (
                      <div className="space-y-4">
                        {agentCommands.map((cmd) => (
                          <div key={cmd.id} className="p-4 bg-slate-950 rounded-xl border border-slate-800 hover:border-blue-500/30 transition-colors">
                            <p className="font-mono text-xs font-bold text-blue-400 mb-1">{cmd.name}</p>
                            <p className="text-[10px] text-slate-400 font-medium">{cmd.description || "No description"}</p>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <p className="text-xs text-slate-500 italic">No specific commands available.</p>
                    )}
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}
