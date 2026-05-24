"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { ArrowLeft, User, Shield, Target, Lightbulb, Zap, Rocket, FileText } from "lucide-react";
import { Agent } from "@/lib/types";

export default function AboutOmanPage() {
  const [profile, setProfile] = useState<string>("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchAbout() {
      try {
        const res = await fetch("/api/agents");
        const agents: Agent[] = await res.json();
        const oman = agents.find((a) => a.id === "oman");
        setProfile(oman?.content || "");
      } catch (error) {
        console.error("Error fetching Oman profile:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchAbout();
  }, []);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center bg-slate-950">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 p-6 md:p-12 selection:bg-blue-500/30">
      <div className="max-w-4xl mx-auto space-y-12">
        {/* Navigation */}
        <Link 
          href="/" 
          className="flex items-center gap-2 text-slate-500 hover:text-blue-400 transition-colors group w-fit"
        >
          <ArrowLeft size={18} className="group-hover:-translate-x-1 transition-transform" />
          <span className="font-bold uppercase tracking-widest text-xs">กลับไปยังสำนักงาน</span>
        </Link>

        {/* Hero Section */}
        <header className="relative py-12 px-8 rounded-[40px] bg-gradient-to-br from-blue-900/40 to-slate-900 border border-blue-500/20 overflow-hidden shadow-2xl shadow-blue-500/5">
          <div className="absolute top-0 right-0 p-12 opacity-5">
            <User size={300} />
          </div>
          <div className="relative z-10 space-y-6">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-blue-500/10 rounded-full border border-blue-500/20">
              <div className="w-1.5 h-1.5 rounded-full bg-blue-500 animate-pulse" />
              <span className="text-[10px] font-black uppercase tracking-widest text-blue-400">ระบบจำลองการลงทุน</span>
            </div>
            <h1 className="text-6xl font-black tracking-tighter">Agent <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-amber-400">Oman</span></h1>
            <p className="text-xl text-slate-400 max-w-2xl leading-relaxed font-medium italic">
              &quot;Agent จำลองการเทรดตามสไตล์ CEO (OmanN777) บริหารพอร์ตจำลองมูลค่า $30,000 ด้วยวินัยทางวิศวกรรม&quot;
            </p>
          </div>
        </header>

        {/* Core Identity Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          
          {/* Philosophy Card */}
          <section className="bg-slate-900/50 rounded-3xl border border-slate-800 p-8 hover:border-blue-500/30 transition-colors">
            <div className="flex items-center gap-3 mb-6 text-amber-400">
              <Lightbulb size={24} />
              <h3 className="text-xl font-bold">ปรัชญาการลงทุน</h3>
            </div>
            <ul className="space-y-4">
              {[
                { icon: Zap, text: "เน้น Aggressive Growth ในกลุ่มเทคโนโลยี" },
                { icon: Target, text: "ความเป็นเลิศทางวิศวกรรมและความสามารถในการสเกล" },
                { icon: Rocket, text: "สมมติฐานหลัก: AI-Energy Convergence" }
              ].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-slate-300 font-medium">
                  <item.icon size={16} className="text-slate-500" />
                  <span>{item.text}</span>
                </li>
              ))}
            </ul>
          </section>

          {/* Privacy Card */}
          <section className="bg-slate-900/50 rounded-3xl border border-slate-800 p-8 hover:border-red-500/30 transition-colors">
            <div className="flex items-center gap-3 mb-6 text-red-400">
              <Shield size={24} />
              <h3 className="text-xl font-bold">โปรโตคอลความเป็นส่วนตัว</h3>
            </div>
            <div className="p-4 bg-red-500/5 border border-red-500/10 rounded-2xl">
              <p className="text-xs font-bold uppercase tracking-widest text-red-500 mb-2">กฎความลับ (The Blindness Rule)</p>
              <p className="text-sm text-slate-400 leading-relaxed font-medium italic">
                Oman ถูกสั่งห้ามไม่ให้เข้าถึง หรือวิเคราะห์ข้อมูลพอร์ตการลงทุนจริงของเจ้าของโดยเด็ดขาด
              </p>
            </div>
          </section>
        </div>

        {/* Detailed Logs/Content */}
        <section className="bg-slate-900 rounded-[40px] border border-slate-800 overflow-hidden shadow-xl">
          <div className="p-8 border-b border-slate-800 bg-slate-900/50 flex items-center justify-between">
            <h3 className="font-bold text-lg flex items-center gap-2">
              <FileText size={20} className="text-blue-500" />
              โปรโตคอลหลักของ Agent (เอกสาร)
            </h3>
            <span className="text-[10px] text-slate-500 font-bold uppercase tracking-widest">v1.2 Stable</span>
          </div>
          <div className="p-8 prose prose-invert prose-slate max-w-none">
            <pre className="bg-slate-950 p-8 rounded-3xl border border-slate-800 text-sm overflow-x-auto whitespace-pre-wrap font-mono leading-relaxed text-slate-400">
              {profile.split('---').pop()?.trim()}
            </pre>
          </div>
        </section>

        {/* Footer Note */}
        <footer className="text-center py-12 border-t border-slate-900">
          <p className="text-xs text-slate-600 font-bold uppercase tracking-[0.2em]">สร้างโดยระบบบริหารจัดการพอร์ต Gemini-CLI</p>
        </footer>
      </div>
    </div>
  );
}
