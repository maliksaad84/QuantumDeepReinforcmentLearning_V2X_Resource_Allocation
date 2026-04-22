#  Quantum-Enhanced Multi-Agent Learning for Distributed Resource Allocation in NR-V2X

This repository presents the implementation and experimental evaluation of:

**"Quantum-Enhanced Multi-Agent Learning for Distributed Resource Allocation in NR-V2X: Opportunities, Challenges, and Future Directions"**

Submitted to **IEEE Communications Magazine**.

---

## 🚗 Overview

This work explores the integration of **Quantum-Enhanced Deep Reinforcement Learning (QDRL)** into **NR-V2X Mode 2** distributed resource allocation.

In NR-V2X Mode 2:

- Vehicles autonomously select sidelink resources  
- Semi-Persistent Scheduling (**SPS**) governs transmissions  
- Resource contention arises due to decentralized decision-making  

To address these challenges, we propose a **hybrid classical–quantum learning framework**, consisting of:

- **Classical Encoder** → compresses vehicular state into latent features  
- **Variational Quantum Circuit (VQC)** → enhances representation learning  
- **Classical Output Head** → maps features to resource allocation decisions  

Training follows a **Centralized Training and Distributed Execution (CTDE)** paradigm.

---

## 🧠 Learning Framework

Each vehicle observes:

- Local traffic density  
- Mobility features (speed, neighbors)  
- Temporal packet generation behavior  

Based on these observations, the agent selects:

- Resource blocks  
- Transmission intervals  
- Scheduling parameters  

### 🎯 Objective

Maximize:

- **Packet Delivery Ratio (PDR)**  
- **Freshness of Information (AoI)**  
- **Spectrum Efficiency**  

Minimize:

- Packet drops  
- Channel congestion  

---

## 📊 Performance Evaluation

We compare:

- **DRL (MLP-based baseline)**  
- **QDRL with different qubit configurations:**
  - ![2 Qubits](2Qubit_seq_concatenation_and_plain/)
    - Reuploading Method
    - Sequential Encoding & Concatenation    
  - ![4 Qubits](4qubit_5Doutput/)
    - with 4D Classical Output Head
    - with 5D Classical Output Head
  - ![5 Qubits](5_Qubit)  

---

## 📈 Convergence Behavior

![Convergence](figures/convergence_all.png)

### 🔍 Key Observations

- QDRL achieves **faster convergence** than DRL  
- 4-qubit and 5-qubit models converge around **~400 episodes**  
- DRL requires **~1500+ episodes**  
- 2-qubit model converges early but with **lower final reward**  

---

## 🔬 Representation Analysis (PCA)

### 🔍 ![Insights](pca_all)

- QDRL produces **structured and separable latent representations**  
- DRL representations are **scattered and less informative**  
- Quantum circuits improve **feature interaction via entanglement**  

---

## ⚡ Effect of Qubit Scaling

| Qubits | Observation |
|--------|-----------|
| **2 Qubits** | Fast convergence but limited performance (information bottleneck) |
| **4 Qubits** | Strong performance and stable learning |
| **5 Qubits** | Similar performance to 4Q (diminishing returns) |

---

## 🔁 DRL vs QDRL

| Aspect | DRL (MLP) | QDRL (VQC) |
|------|----------|-----------|
| Convergence Speed | Slow | Fast |
| Stability | Moderate | High |
| Representation Quality | Weak | Strong |
| Feature Interaction | Limited | Enhanced (Entanglement) |

---

## 🚀 Key Contributions

- First study of **quantum-enhanced DRL for NR-V2X Mode 2**  
- Hybrid classical–quantum architecture for resource allocation  
- Analysis of **qubit scalability effects**  
- PCA-based evaluation of latent representations  
- Practical insights for **6G quantum-enabled V2X systems**  

---

## 📌 Important Notes

- The environment models realistic NR-V2X sidelink communication  
- Vehicles operate in a **fully distributed manner**  
- Training is performed centrally using collected experience  

Full methodological details are provided in the paper.

---

## 🔮 Future Directions

- Quantum-aware explainability frameworks  
- Integration with **6G AI-native architectures**  
- Standardization of quantum-enhanced V2X  
- Deployment on real quantum hardware  

---

## 📬 Citation

```bibtex
(To be updated after publication)
