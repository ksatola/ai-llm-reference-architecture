FTI Architecture


System View

Design objectives
- Differents subsystems (pipelines) are independent from others and can:
  - Leverage different architectures and compute components (CPU, GPU, TPU), 
  - Use different tech stacks (tools, services),
  - Have separate dev team,
  - Be developed, deployed, scaled separately (independently)
- Interfaces between subsystems remain the same regardless their complexity
- Data Collection Pipeline can:
  - Get raw data from different sources
  - Standardize data structure, transform data and store for further processing
- Feature Pipeline can:
  - Include data validation step...
  - Be run on CPU-based machines
  - Tools: Pandas, Spark, DBT...
- Training Pipeline can:
  - Include data evaluation step...
  - Process data in batch mode rather than in near real-time
  - Be run on GPU/TPU-based machines
  - Tools: PyTorch, TensorFlow, Scikit-Learn
- Inference (serving) Pipeline can:
  - Process data in near real-time or batch mode
  - Be run on GPU/TPU-based machines
  - Tools: PyTorch, TensorFlow, Scikit-Learn
- Feature Store can:
  - Allow data versioning
  - Help avoid training-serving skew
  - Tools: Feast, Tecton, SageMaker FS, Databrics FS, Vertex AI FS...
- Model Registry can: 
  - Store versioned models along with their metadata
  - Allow models tracking, monitoring and performance comparison
  - Tools: MLflow, AIM, HuggingFace

====

TW architecture will be based on FTI pattern with the scope of:
- Ingesting, cleaning, and validating fresh data
- Training and inference setups
- Compute and serve features in the right environment
- Serve the model in a cost-effective way
- Version, track, be able to reproduce, and share the datasets and models
- Monitor your infrastructure and models
- Deploy the model on a scalable infrastructure
- Automate the deployments and training

Following the [FTI pattern](https://medium.com/decodingml/building-ml-systems-the-right-way-using-the-fti-architecture-d9cc0cd29abf), any ML system can be divided into 3 pipelines:
- Feature training 
- Model training
- Inference (model serving)

![alt text](/images/AI_LLM_Ref_Arch_System.png)

[More info](https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines)