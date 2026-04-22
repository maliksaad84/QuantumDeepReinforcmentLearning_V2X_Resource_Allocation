## 🔍 DRL (Multi-Layer Perceptron)


###  Multi-Layer Perceptron (MLP)


  - In this setting, we have classical encoder, which compresses the ouput to 4 latent vectors. Then, instead of quantuam variational circuit for the compareable perfromance we replace VQC witht the MLP. Then, These 4 features pass to the classical output head having 4D input features.

---
    


###  Results

- The results shows slow convergance and low average return reward. This slow convergance is due to MLP which struggles hard to learn the correlation among the features. It learnns witht the more number of episodes. We run the MLP for 3500 episode to observe the training trent.From the results, it is observed that it seems converge and there is no more performance gain with average reward return around 85. 


 ![convergennce plot of the DRL](drl_reward_3500.png)
