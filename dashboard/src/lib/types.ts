import { LucideIcon, User, BarChart3, Search, TrendingUp, Calculator, Archive, Globe, Sparkles, MonitorPlay } from 'lucide-react';

export interface Agent {
  id: string;
  name: string;
  description: string;
  persona: string;
  content: string;
}

export interface PortfolioHolding {
  ticker: string;
  name: string;
  shares: number;
  average_cost: number;
  total_value: number;
  allocation_pct: number;
  position_type?: 'LONG' | 'SHORT';
  thesis_id: string;
}

export interface Portfolio {
  portfolio_name: string;
  start_date: string;
  initial_nav: number;
  current_nav: number;
  daily_change_usd?: number;
  daily_change_pct?: number;
  currency: string;
  holdings: PortfolioHolding[];
  cash_balance: number;
  benchmark_vs_spy: number;
  weeks_alive: number;
  recommended_actions: string[];
  performance_history: {
    date: string;
    oman_return: number;
    spy_return: number;
  }[];
}

export interface UniverseItem {
  ticker: string;
  name: string;
  status: 'SELECTED' | 'PASSED' | 'DISQUALIFIED';
  reason: string;
  category: string;
}

export interface Universe {
  last_updated: string;
  items: UniverseItem[];
}

export interface Command {
  id: string;
  name: string;
  description?: string;
}

export const agentTheme: Record<string, { color: string; icon: LucideIcon }> = {
  oman: { color: 'from-blue-900 to-amber-600', icon: User },
  malli: { color: 'from-rose-500 to-pink-400', icon: Sparkles },
  fundamentokung: { color: 'from-emerald-900 to-teal-700', icon: BarChart3 },
  newwy: { color: 'from-red-700 to-rose-500', icon: Search },
  vera: { color: 'from-teal-600 to-emerald-400', icon: Calculator },
  reese: { color: 'from-stone-700 to-orange-200', icon: Archive },
  tubemaster: { color: 'from-red-600 to-red-400', icon: MonitorPlay },
  
  // Legacy backups for old logs
  earnchan: { color: 'from-orange-600 to-yellow-500', icon: TrendingUp },
  scout: { color: 'from-indigo-600 to-blue-400', icon: Globe },
};
