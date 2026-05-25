"""
L0-Flow + TBN Protocol Integration (Proof of Concept)
Layer 0: Cryptographic Identity (TBN Protocol mock)
Layer 1: Deterministic Phase Agent (L0-Flow)

Metric: Cycle = 1 (π=1). Optimal stability = Φ (1.618).
"""

import math

# ============================================================
# LAYER 0: TBN PROTOCOL MOCK (Cryptographic Wrapper)
# ============================================================
class TBNGovernor:
    def __init__(self, agent, bot_id):
        self.agent = agent
        self.bot_id = bot_id
        
    def execute(self, data_stream):
        print(f"[TBN Layer 0] Cryptographic ID '{self.bot_id}' Verified.")
        return self.agent.process_task(data_stream)

# ============================================================
# LAYER 1: STATELESS PHASE AGENT
# ============================================================
class PhaseAgent:
    def __init__(self):
        self.PHI = 1.6180339887  # Ideal non-intersection invariant
        self.K_c = 1.019         # Kuramoto collapse threshold
        self.K = 1.2             # Initial state

    def circular_coherence(self, phases):
        """ 
        Calculate Kuramoto order parameter. 
        Cycle = 1.
        """
        if not phases: 
            return 0.5
        sc = sum(math.cos(2.0 * math.pi * p) for p in phases) / len(phases)
        ss = sum(math.sin(2.0 * math.pi * p) for p in phases) / len(phases)
        return math.sqrt(sc * sc + ss * ss)

    def process_task(self, data_stream):
        print("[L0-Flow Layer 1] Processing geometric coherence...")
        
        # Project data onto the Torus [0, 1) using current K
        phases = [(float(d) * self.K) % 1.0 for d in data_stream]
        coherence_C = self.circular_coherence(phases)
        
        # Agent tunes K towards the Golden Ratio (Φ)
        self.K += 0.05 * (self.PHI - self.K)
        print(f"[L0-Flow Layer 1] Tuning K towards Φ. Current K: {self.K:.4f}")

        # Strict survival boundary
        if coherence_C < (self.K_c / 2.0):
            print(f"[L0-Flow Layer 1] 🛑 FRICTION DETECTED (C={coherence_C:.3f}). Execution denied by physics.")
            return "DENIED"
        else:
            print(f"[L0-Flow Layer 1] ✅ PHASE LOCKED (C={coherence_C:.3f}). Action executed.")
            return "EXECUTED"

# ============================================================
# INTEGRATION TEST
# ============================================================
if __name__ == "__main__":
    print("=== TBN + L0-Flow: GOVERNANCE AS PHYSICS ===\n")
    
    # Initialize the integration stack
    agent = PhaseAgent()
    governed_bot = TBNGovernor(agent=agent, bot_id="L0-Flow-Node-009")
    
    # TEST 1: Harmonic data (Low entropy)
    print("--- TEST 1: INJECTING HARMONIC DATA ---")
    harmonic_data = [0.1, 0.12, 0.11, 0.13]
    result_1 = governed_bot.execute(harmonic_data)
    print(f"Result: {result_1}\n")
    
    # TEST 2: Chaotic data (High entropy / anomaly)
    print("--- TEST 2: INJECTING CHAOTIC DATA ---")
    chaotic_data = [0.9, 0.1, 0.5, 0.8]
    result_2 = governed_bot.execute(chaotic_data)
    print(f"Result: {result_2}\n")
