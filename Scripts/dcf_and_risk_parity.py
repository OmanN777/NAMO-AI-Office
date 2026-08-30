import os
import sys
import math

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def calculate_scenario_dcf(fcf_current, growth_bull=0.25, growth_base=0.15, growth_bear=0.05, discount_rate=0.10, terminal_growth=0.03, years=5):
    """
    Computes 3-scenario DCF (Bull, Base, Bear) to derive Fair Value range.
    """
    scenarios = {
        'Bull (Aggressive)': growth_bull,
        'Base (Consensus)': growth_base,
        'Bear (Conservative)': growth_bear
    }
    
    results = {}
    for name, g in scenarios.items():
        pv_fcf = 0
        fcf = fcf_current
        for t in range(1, years + 1):
            fcf *= (1 + g)
            pv_fcf += fcf / ((1 + discount_rate) ** t)
        
        # Terminal Value
        terminal_fcf = fcf * (1 + terminal_growth)
        terminal_val = terminal_fcf / (discount_rate - terminal_growth)
        pv_terminal = terminal_val / ((1 + discount_rate) ** years)
        
        enterprise_val = pv_fcf + pv_terminal
        results[name] = round(enterprise_val, 2)
        
    return results

def calculate_risk_parity_weights(volatilities):
    """
    Computes inverse-volatility weights for portfolio allocation (Risk-Parity).
    volatilities: dict of ticker -> annualized volatility (e.g. {'AVGO': 0.28, 'VRT': 0.45})
    """
    inv_vols = {t: 1.0 / max(v, 0.01) for t, v in volatilities.items()}
    total_inv = sum(inv_vols.values())
    weights = {t: round((iv / total_inv) * 100, 2) for t, iv in inv_vols.items()}
    return weights

if __name__ == '__main__':
    print('=== 1. Scenario-Based DCF Example (CRM / Salesforce) ===')
    fcf = 12.0 # $12B FCF
    dcf_res = calculate_scenario_dcf(fcf, growth_bull=0.20, growth_base=0.12, growth_bear=0.05)
    for s, v in dcf_res.items():
        print(f'{s}: Fair Enterprise Value = ${v}B')
        
    print('\n=== 2. Risk-Parity Allocation Example (Master Universe) ===')
    sample_vols = {'AVGO': 0.28, 'CRM': 0.22, 'PLTR': 0.42, 'VRT': 0.48, 'CCJ': 0.35, 'GOOGL': 0.24}
    weights = calculate_risk_parity_weights(sample_vols)
    for t, w in sorted(weights.items(), key=lambda x: x[1], reverse=True):
        print(f'{t}: Recommended Weight = {w}%')
