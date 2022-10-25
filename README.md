# Predict Stroke with Unbalanced Data and Create a Web App

In the first part I considered many ML models to choose the best. I evaluated the models using balanced accuracy and recall. The best recall metrics go up to 92%.
In opposite to that, preсision is extremely low. But it's better to be overdressed than underdressed. For example, Over-sampling using SMOTE and cleaning using ENN strategy + Logistic regression gives recall: 0.92, preсision: 0.17 as a result f1 very low: 0.29.

In the second part, I create a web app using Streamlit. It's a simple questionnaire where only 6 features are left:  
'gender', 'age', 'hypertension', 'heart_disease', 'bmi' and 'smoking_status'.
In result the web app then returns a probality of having a stroke.

![Example](https://github.com/VolkhinD/stroke_prediction/blob/main/Screen%20Shot%202022-10-15%20at%2020.47.52.png)
