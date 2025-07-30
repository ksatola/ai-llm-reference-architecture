# FTI Architecture


## System View

![alt text](/images/ai_llm_system.png)


### Design objectives
Different subsystems (pipelines) are independent from others and can:
- Leverage different architectures (CPU, GPU, TPU).
- Use different tech stacks (tools, services).
- Have separate development team.
- Be developed, deployed, and scaled separately (independently).
- The data engineering team owns the Data Pipeline.
- The ML engineering team owns the FTI Pipelines.
- Interfaces between subsystems remain the same regardless of subsystems' internal complexity.


### Data Collection Pipeline (ETL)
- Extract raw data from different sources into a staging area.
- Link/align data from different sources to be used as a coherent data corpus.
- Standardize data structure, transform data and store for further processing.
- Tools: Snowflake, BigQuery, Mongo DB...


### Feature Pipeline
- Take raw data as input, processes it, and output the features and labels.
- Have data validation, data preparation steps.
- Tools: Pandas, Spark, DBT...
  

### Training Pipeline
- In the initial stage of model development, the data science team owns this step.
- Perform model evaluation and validation steps.
- Process data in batch mode rather than in near real-time.
- Tools: PyTorch, TensorFlow, Scikit-Learn...


### Inference (serving) Pipeline
- Take as input the features and labels from the feature store and the trained model from the model registry. With these two, make predictions in either batch or real-time mode.
- Tools: PyTorch, TensorFlow, Scikit-Learn...


### Feature Store
- Store, version, track, and share features.
- Keep the state of saved features.
- Version data.
- Help avoid training-serving skew.
- Tools: Feast, Tecton, SageMaker FS, Databrics FS, Vertex AI FS...


### Model Registry 
- Centralized repository that manages ML models throughout their lifecycle.
- Store models along with their metadata, version history, and performance metrics.
- Serve as a single source of truth. 
- Track, share, and document model versions.
- Facilitate team collaboration. 
- Fundamental element in the deployment process as it integrates with continuous integration and continuous deployment (CI/CD) pipelines.
- Tools: MLflow, AIM, HuggingFace...


## Additional Resources
- [From MLOps to ML Systems with Feature/Training/Inference Pipelines](https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines)
- [Building ML Systems the Right Way Using the FTI Architecture](https://medium.com/decodingml/building-ml-systems-the-right-way-using-the-fti-architecture-d9cc0cd29abf)

