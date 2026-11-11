#!/usr/bin/env python3
"""Transparent helper for TPRM residual-risk calculations."""
from __future__ import annotations
import argparse
from dataclasses import dataclass

@dataclass(frozen=True)
class RiskResult:
    inherent: float
    residual: float
    rating: str

def rating(score: float) -> str:
    if score <= 4: return "Low"
    if score <= 9: return "Moderate"
    if score <= 16: return "High"
    return "Critical"

def calculate(likelihood: int, impact: int, control_effectiveness: float, evidence_confidence: float) -> RiskResult:
    if likelihood not in range(1, 6) or impact not in range(1, 6):
        raise ValueError("Likelihood and impact must be integers from 1 through 5.")
    for name, value in {"control_effectiveness": control_effectiveness, "evidence_confidence": evidence_confidence}.items():
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1.")
    inherent = likelihood * impact
    residual = round(inherent * (1 - control_effectiveness * evidence_confidence), 2)
    return RiskResult(float(inherent), residual, rating(residual))

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--likelihood', type=int, required=True)
    p.add_argument('--impact', type=int, required=True)
    p.add_argument('--control-effectiveness', type=float, required=True)
    p.add_argument('--evidence-confidence', type=float, required=True)
    a=p.parse_args()
    r=calculate(a.likelihood,a.impact,a.control_effectiveness,a.evidence_confidence)
    print(f"Inherent risk: {r.inherent:.2f}")
    print(f"Residual risk: {r.residual:.2f}")
    print(f"Residual rating: {r.rating}")
if __name__ == '__main__': main()
