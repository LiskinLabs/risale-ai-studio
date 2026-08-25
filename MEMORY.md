# Risale AI Studio — Project Memory & DevSecOps Architecture

## 📌 Project Overview
- **Repository:** `LiskinLabs/risale-ai-studio`
- **Tech Stack:** Next.js, Tauri, TypeScript, Rust, Biome, pnpm monorepo.
- **Purpose:** Next-generation AI-assisted reader & study platform for Risale-i Nur.

---

## 🛡️ DevSecOps & CI/CD Pipeline Matrix (All-Green Standard)
| Workflow | File | Triggers | Description |
| :--- | :--- | :--- | :--- |
| **PR & Code Verification** | `.github/workflows/pull-request.yml` | `push`, `pull_request` | Monorepo linting, typechecking, and package building |
| **CodeQL Advanced SAST** | `.github/workflows/codeql.yml` | `push`, `pull_request`, weekly | Static code security analysis for TypeScript/JavaScript/Rust |
| **Scorecard Supply-Chain** | `.github/workflows/scorecard.yml` | `push`, `branch_protection` | OpenSSF Scorecard supply-chain security evaluation |

---
*Updated: 2026-08-25 | Liskin Labs Engineering*
