data = """
A Review on Weather Forecasting Techniques
A Real-Time Weather Forecasting and Analysis
Local Temperature Forecasts Based on Statistical Post-Processing of Numerical Weather Prediction Data
Precision Agriculture Through Weather Forecasting
Visibility Forecasting Using Autoregressive Integrated Moving Average (ARIMA) Models
The Role of Statistical Methods and Tools for Weather Forecasting and Modeling
Weather Prediction: Improving Accuracy Using Data Mining And Forecasting Techniques
Short-Term Temperature Forecasts Using A Convolutional Neural Network
Improving Time Series Forecasting Using ARIMA Based on Moving-Average Filter and EMD Decomposition
Streaming Dynamic Mode Decomposition For Short-Term Forecasting In Wind Farms
Efficient IoT based Weather Station
Low-Cost Automatic Weather Stations in the Internet of Things
Implementation Of A Weather Station And Forecasting Weather Using IoT
Automated Weather Station
Local Weather Station Design and Development for Cost-Effective Environmental Monitoring and Real-Time Data Sharing
An Adaptive Outlier Detection and Processing Approach Towards Time Series Sensor Data
Single Layer & Multi-layer Long Short-Term Memory (LSTM) Model with Intermediate Variables for Weather Forecasting
Weather Forecasting Using Quantum-Based Lstm: A Comparative Analysis
SARIMA Model: An Efficient Machine Learning Technique for Weather Forecasting
Beyond The Horizon: A Comprehensive Analysis Of Artificial Intelligence-Based Weather Forecasting Models
Weather Forecasting In A Changing Climate: The Rise Of AI And Machine Learning
A IoT-Based Smart Irrigation For Olive Farming: Real-Time Water Quality Monitoring And LSTM Forecasting
Time Series Forecasting Based On Multi-Criteria Optimization For Model And Filter Selection Applied To Hydroelectric Power Plants
Compact Transformer Variants For Synthetic Time Series Forecasting
A Hybrid Approach To Time Series Forecasting: Integrating ARIMA And Prophet For Improved Accuracy
Gap filling crowdsourced air temperature data in cities using data-driven approaches
Short-Term Temperature Forecasts Using A Convolutional Neural Network — An Application To Different Weather Stations In Germany
A Yield Classification Prediction Framework Based On Intelligent Agricultural Sensor Data And Meta Heuristic Optimization Ensemble Learning
Investigation Of Machine Learning Based Techniques For Crop Yield Estimation Of Corn And Cotton Using Multi-Sensor Data Fusion
IoT-Driven Real-Time Weather Measurement And Forecasting Mobile Application With Machine Learning Integration
A 30-Yr High-Resolution Weather Research And Forecasting Model Downscaling Data Over California And Nevada
Hailstorm Prediction And Loss Assessment Using High-Resolution Hazard And Claims Data
Machine Learning Approaches For Imputing Missing Meteorological Data In Senegal
""".strip()

lines = data.split("\n")
original_length = len(lines)

unique_lines = set(lines)
unique_length = len(unique_lines)

print("All are unique" if original_length == unique_length else "Not all are unique")
