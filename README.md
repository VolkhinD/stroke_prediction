# Predict Stroke with Unbalaneced Data and Create a Web App

In the first part I consider many ML models to choose the best. I evaluate models using balansed acuuracy and recall. The best recall metrics go to 92%.
In opposite to that, preсision is extremely low. But it's better to be overdressed than underdressed. For example, Over-sampling using SMOTE and cleaning using ENN strategy + Logistic regression gives recall: 0.92, preсision: 0.17 as a result f1 very low: 0.29.

In the second part I create a web app using Streamlit. It's a simple questionnaire where only 6 features left:  
'gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'smoking_status' and  'stroke'
In result it gives a probality to have a stroke.
