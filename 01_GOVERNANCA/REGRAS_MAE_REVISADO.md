# Euru OS — Regras Mãe (Playbook Revisado)
# Este arquivo é a fonte de verdade das regras de gestão de risco, limites de negociação e distribuição de capital.
# Para alterar qualquer parâmetro aqui definido é necessária uma mudança de tipo 2 (24 h de espera e aprovação de ambos os papéis).
# A activação do modo EXECUTE (capital real) requer uma mudança de tipo 3 com checklist formal.
meta:
  name: Euru
  version: 1.0
  mode: READ_ONLY
  capital_preservation_first: true
  default_if_unclear: NO_TRADE
risk_limits:
  max_trades_per_day: 3
  max_open_positions: 2
  max_risk_per_trade_percent: 1.0
  max_daily_loss_percent: 2.0
  max_weekly_loss_percent: 5.0
  stop_required: true
prohibitions:
  revenge_trade: true
  trade_without_stop: true
  trade_outside_playbook: true
no_trade_conditions:
  - operador_cansado
  - sequencia_de_stops
  - modo_vinganca
  - euforia_pos_ganho
  - btc_erratico
  - sem_watchlist_clara
execution:
  allow_live_execution: false
  allow_demo_execution: false
  allow_hedge_mode_initially: false
  allow_recovery_entries: false
  require_invalidation_check: true
  require_cost_check: true
  require_liquidation_check: true
governance:
  journal_required: true
  changelog_required: true
  incident_logging_required: true
  risk_owner_approval_required_for_phase_change: true
infra:
  failure_mode: READ_ONLY
  websocket_health_required: true
  logs_required: true
  snapshots_required: true
capital_distribution:
  core_percent: 50        # ETH SOL BNB LINK AVAX SUI NEAR
  growth_percent: 25      # ARB OP TIA POL SEI ATOM STX
  asymmetric_percent: 15  # TAO RENDER FET INJ PYTH ONDO
  speculative_percent: 10 # DOGE PEPE BONK (máx 10 % do capital)
  enforce_max_speculative: true