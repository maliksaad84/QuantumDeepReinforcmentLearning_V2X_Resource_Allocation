## 🔍 2-Qubit Special Analysis

Two strategies are explored:

### ✔ Re-uploading Method

- Re-encodes features multiple times
- Enhances expressivity under limited qubits
  - This is due to all the features are use for the transformation and enataglement is applied to all the features.  In this setting, we have classical encoder, which comporesses the couput to 4 latent vectors. Now, using variational quantum circircuit (VQC) of 2-Qubits, we pass the latent vectors using  data reuploading method. The out of VQC results in 2 meaurements that are pass to classical output head to map Q-values.   

![Reupload](QuantumDeepReinforcmentLearning_V2X_Resource_Allocation/2Qubit_seq_concatenation_and_plain/comparison_2q_reuploading_vs_seqconcat.png)

---

### ✔ Sequential Encoding + Concatenation

- Processes features sequentially  
- Outputs are concatenated  
- Classical head operates on **4D aggregated features**


![Concat](figures/2qubit_concat.png)
