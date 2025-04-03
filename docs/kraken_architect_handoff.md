# Kraken Autonomous - ASZA Architect Handoff

## Purpose

This document defines the full architectural handoff for rebuilding the Kraken trading bot using ASZA methodology. It captures what worked, what failed, what needs modularization, and what must be carried forward for full profitability.

---

## Phase 1: Minimum Components (Manually Created and Already Working)

These core ASZA files are complete and stable. All future modules will be built on top of them:

- `ask_architect.py` – Accepts natural language design prompts  
- `code_generator.py` – Uses LLM to generate module code  
- `file_creator.py` – Writes code files from LLM responses  
- `core/template_header.py` – Required header for all modules  
- `core/template_footer.py` – Required footer for all modules  
- `core/wrapper.py` – Core wrapper for logging, error handling, and reflection  
- `.env` – Holds `LLM_API_URL`, GPT keys, routing, and configuration  

---

## Phase 2: Functional Modules to Rebuild (Confirmed Working or Valuable)

| Module | Purpose |
|--------|---------|
| `market_scanner.py` | Scans volatile symbols (BTC, ETH, SOL, etc.) |
| `entry_filter_gpt.py` | GPT-based contextual trade filtering |
| `position_executor.py` | Executes Kraken Futures orders |
| `equity_monitor.py` | Tracks floating equity and total balance |
| `slice_manager.py` | Handles multi-slice trade execution |
| `leverage_manager.py` | Adjusts leverage based on risk and confidence |
| `risk_allocator.py` | Allocates pooled margin across symbols |
| `trade_logger.py` | Logs trade entries and exits to DB |
| `hourly_heatmap.py` | Charts performance by hour to identify optimal trade windows |

---

## Phase 2B: Known Failures Requiring Modular Refactors

| New Module | Fixes This |
|------------|------------|
| `pnl_engine.py` | Corrects floating P&L tracking with Kraken sync |
| `equity_reconciler.py` | Prevents phantom compounding from missed losses |
| `entry_flex_tuner.py` | Loosens entry filter to allow more valid trades |
| `kraken_retry_agent.py` | Adds fast retry logic for failed Kraken API calls |
| `wick_launcher.py` | Triggers troubleshooting agents when trades fail |

---

## Indicators in Use or Needed

| Indicator | Purpose |
|-----------|---------|
| VWAP | Entry filter baseline for fair value targeting |
| RSI | Identifies overbought/oversold states |
| Bollinger Bands | Volatility measurement for breakout entries |
| EMA (9/21) | Trend detection for entry alignment |
| MACD | Momentum confirmation |
| Heatmap (Hourly Win Rate) | Used to reject low-probability entry windows |
| Volume Spike Detector | Entry confirmation based on volume anomalies |
| GPT Signal Score | Soft indicator for confidence scoring from GPT analysis |

---

## Six Rarely Automated Components (Must Be Included in Final Stack)

These are the high-leverage elements missing from most trading bots, now required for ASZA-based Kraken:

1. **Dynamic Position Sizing** – Risk scaling based on GPT score and recent win rate  
2. **Open Risk Ceiling** – Total system-wide risk control across multiple open trades  
3. **Trade Clustering** – Identify high-confluence timeframes and group trades  
4. **Performance-Based Scaling** – Increase trade size or leverage on winning streaks  
5. **Strategy Flex Mode** – Automatic relaxation of entry criteria when no trades detected  
6. **Failure-Triggered Wick Clones** – Auto-launch diagnostics/refactorers on trade failure  

Each of these must be a **separate ASZA module**, called from within `/trading/` logic, and log full reflections.

---

## Data and Environment Guidelines

- Use existing **Postgres** and **Redis** instances, but **purge all data first**  
- Maintain schema separation:
  - `trading_data` for trades, balances, P&L  
  - `system_logs` for internal ASZA module feedback  
- All new trading modules live in: `trading/`  
- Future goal: extract `/trading/` as its own ASZA project and LLM stack  

---

## See Final Prompt to Architect

- final_prompt_to_architect.txt

---

## Final Notes

This is the **last hand-coded instruction** for Kraken.  
Everything forward is GPT/ASZA-driven.

- All modules must be **10 lines or less** (or split)  
- All logic must pass through the core **ASZA wrapper**  
- Every file must log **reflections** and be rebuildable  
- Any failure must trigger **Wick** for clone repair

You’re no longer building software—you’re building **software that builds software**.

This is the **foundation of a profitable, self-repairing trading system**.  
This is the beginning of your **automated AI fund manager**.  
Let the Architect begin.
