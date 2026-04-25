# EURU_TOS — Official Schema for Governance Threshold Profiles
Version: 1.0
Status: Active
Owner: EURU Governance
Applies to:
- 00_GOVERNANCA/THRESHOLDS/
- euru_threshold_registry.py
- Friday cycle governance layer
- Score Engine
- all AI agents proposing threshold changes

---

## 1. Purpose

This document defines the official schema for versioned governance threshold profiles inside Euru_TOS.

The objective is to make governance thresholds:
- explicit
- versioned
- auditable
- comparable across periods
- machine-readable
- safe for controlled evolution

This schema is the source of truth for threshold versioning.

---

## 2. Core Principles

1. Every threshold profile must be a valid Markdown file (`.md`)
2. Every threshold profile must start with YAML front matter
3. YAML front matter is the machine-readable source of truth
4. Markdown body is the human-readable governance explanation
5. Every change must increment the profile version
6. Threshold changes must never overwrite historical versions
7. Only one active profile per scope should exist for a given effective date
8. Thresholds must be comparable across versions
9. Dates must use ISO 8601
10. Version numbers must use semantic versioning (`major.minor.patch`)

---

## 3. Folder Scope

Official folder:
`00_GOVERNANCA/THRESHOLDS/`

Recommended subfolders:
- `00_GOVERNANCA/THRESHOLDS/PROFILES/`
- `00_GOVERNANCA/THRESHOLDS/CHANGELOGS/`

---

## 4. File Naming Convention

### 4.1 Threshold profile
Pattern:
`THRESHOLDS_PROFILE_<scope>_<profile_id>_v<version>.md`

Examples:
- `THRESHOLDS_PROFILE_system_default_v1.0.0.md`
- `THRESHOLDS_PROFILE_system_default_v1.1.0.md`
- `THRESHOLDS_PROFILE_score_engine_baseline_v2.0.0.md`

### 4.2 Threshold changelog
Pattern:
`THRESHOLDS_CHANGELOG_<scope>_<profile_id>_v<from>_to_v<to>.md`

Example:
- `THRESHOLDS_CHANGELOG_system_default_v1.0.0_to_v1.1.0.md`

---

## 5. Official Enum Dictionary

### 5.1 Schema type
Allowed values:
- `governance_threshold_profile`
- `governance_threshold_changelog`

### 5.2 Scope
Allowed values:
- `system`
- `agent`
- `asset`
- `setup`
- `score_engine`
- `watchlist`
- `risk`

### 5.3 Profile status
Allowed values:
- `draft`
- `active`
- `deprecated`
- `archived`

### 5.4 Change type
Allowed values:
- `increase`
- `decrease`
- `added`
- `removed`
- `renamed`
- `clarified`
- `reclassified`

### 5.5 Approval status
Allowed values:
- `pending`
- `approved`
- `rejected`

### 5.6 Governance decision impact
Allowed values:
- `low`
- `medium`
- `high`
- `critical`

---

## 6. GOVERNANCE_THRESHOLD_PROFILE Schema

Every threshold profile file must follow this structure.

### 6.1 Required front matter fields

```yaml
---
schema_type: governance_threshold_profile
schema_version: 1.0

profile_id: default
scope: system
version: 1.0.0
status: active

effective_from: 2026-04-12
effective_to: null

owner: EURU Governance
change_reason: initial_baseline
approval_status: approved
approved_by: human_governance
approval_date: 2026-04-12

inherits_from: null
supersedes_version: null

thresholds:
  readiness:
    min_closed_trades: 20
    min_win_rate_pct: 50.0
    min_average_rr: 2.0
    min_expectancy: 0.01

  schema_quality:
    max_invalid_files: 0
    max_warning_files: 5
    block_on_invalid_schema: true
    block_on_warnings_in_strict_mode: true

  portfolio_risk:
    max_portfolio_risk_used_pct: 75.0
    max_single_asset_risk_pct: 20.0
    max_open_positions: 12

  score_engine:
    min_prediction_accuracy_pct: 60.0
    min_average_entry_score_winners: 7.0
    max_false_positive_rate_pct: 35.0

  watchlist:
    repeated_failure_block_after: 3
    repeated_failure_review_after: 2

  governance:
    human_review_required_for_strategy_change: true
    human_review_required_for_threshold_change: true
    immediate_block_on_critical_deviation: true

notes_tags:
  - baseline
  - simulate
  - governance
---
```

### 6.2 Required field definitions

#### Identity
- `schema_type`: must be `governance_threshold_profile`
- `schema_version`: current version is `1.0`
- `profile_id`: stable profile name within its scope
- `scope`: official scope enum
- `version`: semantic version
- `status`: lifecycle state of the profile

#### Effectivity
- `effective_from`: date when profile becomes valid
- `effective_to`: date when profile stops being valid, or `null`

#### Governance ownership
- `owner`
- `change_reason`
- `approval_status`
- `approved_by`
- `approval_date`

#### Version lineage
- `inherits_from`: optional parent profile version reference
- `supersedes_version`: previous version replaced by this one

#### Threshold map
- `thresholds`: nested dictionary of threshold groups and numeric/boolean settings

#### Classification
- `notes_tags`: list of tags

---

### 6.3 Threshold rules

1. Every threshold key must be stable across versions whenever possible
2. New keys may be added without breaking old versions
3. Existing keys must not be silently deleted without changelog explanation
4. Numeric values must be numeric
5. Boolean values must be boolean
6. Nested threshold groups are allowed and recommended
7. Historical threshold files must never be modified in place after approval
8. If a profile becomes obsolete, create a new version and deprecate the old one

---

### 6.4 Required body structure for threshold profiles

Use these exact headings:

```md
# Profile Summary

## Purpose
- What this threshold profile governs

## Threshold Rationale
- Why these values were chosen

## Changes vs Previous Version
- What changed
- If first version, write: `- initial baseline`

## Expected Operational Impact
- What should improve, tighten, or become more conservative

## Human Governance Notes
- Final comments, approvals, cautions
```

---

## 7. GOVERNANCE_THRESHOLD_CHANGELOG Schema

A changelog records the diff between two versions of the same profile.

### 7.1 Required front matter fields

```yaml
---
schema_type: governance_threshold_changelog
schema_version: 1.0

profile_id: default
scope: system
from_version: 1.0.0
to_version: 1.1.0
change_date: 2026-04-19

generated_by: euru_threshold_registry.py
approval_status: approved
impact_level: medium

changed_keys_count: 4
added_keys_count: 1
removed_keys_count: 0
---
```

### 7.2 Required body structure

```md
# Change Summary

## Version Transition
- from 1.0.0 to 1.1.0

## Added Keys
- ...
- If none, write: `- none`

## Removed Keys
- ...
- If none, write: `- none`

## Changed Values
- `path`: old -> new

## Governance Interpretation
- Why these changes matter

## Human Approval Notes
- ...
```

---

## 8. SemVer Policy

### 8.1 Major version (`X.0.0`)
Use when:
- governance logic changes significantly
- readiness philosophy changes
- breaking threshold structure changes occur
- old comparisons require migration logic

### 8.2 Minor version (`1.X.0`)
Use when:
- thresholds are tuned
- new groups or keys are added safely
- governance becomes stricter or looser without breaking schema

### 8.3 Patch version (`1.0.X`)
Use when:
- documentation is clarified
- typo or non-breaking metadata is corrected
- explanatory notes are improved without changing the operational value

---

## 9. Historical Comparison Rules

Every Friday cycle should be able to answer:
1. Which threshold profile was active during this period?
2. Which version changed compared with the previous week?
3. Did performance improve under stricter or looser thresholds?
4. Which rules were active when decisions were made?

Therefore:
- effective dates are mandatory
- version history is mandatory
- changelog generation is mandatory whenever threshold values change

---

## 10. Parser Contract

Threshold parsers must follow this exact order:
1. Parse YAML front matter
2. Validate `schema_type`
3. Validate `schema_version`
4. Validate scope and semantic version
5. Validate effective dates
6. Validate threshold map
7. Trust YAML as source of truth
8. Use Markdown body for governance explanation only

---

## 11. Official Threshold Profile Template

```md
---
schema_type: governance_threshold_profile
schema_version: 1.0

profile_id: default
scope: system
version: 1.0.0
status: draft

effective_from: 2026-04-12
effective_to: null

owner: EURU Governance
change_reason: threshold_update
approval_status: pending
approved_by: null
approval_date: null

inherits_from: null
supersedes_version: null

thresholds:
  readiness:
    min_closed_trades: 20
    min_win_rate_pct: 50.0
    min_average_rr: 2.0
    min_expectancy: 0.01

notes_tags: []
---

# Profile Summary

## Purpose
- ...

## Threshold Rationale
- ...

## Changes vs Previous Version
- ...

## Expected Operational Impact
- ...

## Human Governance Notes
- ...
```

---

## 12. Non-Negotiable Rules for All Agents

1. Never overwrite an approved threshold version in place
2. Never activate two overlapping profiles for the same scope and profile_id without explicit intent
3. Never change numeric thresholds without bumping version
4. Never omit effective dates
5. Never skip changelog generation when values change
6. Never guess approval metadata
7. Never use body text as replacement for YAML front matter
8. Never compare weekly performance without referencing the active threshold version

---

## 13. Final Authority

If there is any conflict between:
- old ad-hoc threshold notes
- agent assumptions
- unversioned governance rules
- implicit defaults

this schema wins.
