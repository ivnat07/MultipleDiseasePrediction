
# 🧠 Disease Prediction Application

A web-based application built using **React.js** and **Flask** that empowers users with personalized health insights and disease risk predictions based on their symptoms and medical history. The application leverages machine learning algorithms to classify and predict potential diseases, improving health awareness and early diagnosis.

## 🚀 Features

- **User-Friendly Interface**: Clean, responsive front-end built using React.js.
- **Disease Prediction**: Predicts disease outcomes based on input symptoms using ML models.
- **Multiple Model Support**: Compares performance across Logistic Regression, Random Forest, and SVC.
- **Data Visualization**: Showcases trends and correlations using Matplotlib and Seaborn.
- **API Integration**: Flask API for model interaction and real-time prediction.
- **Interactive Insights**: Allows users to view model output with confidence scores.

## 🧪 Machine Learning Models

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | ~85%     |
| Random Forest       | ~90%     |
| Support Vector Classifier (SVC) | ~88%     |

## 📊 Tech Stack

- **Frontend**: React.js, Bootstrap, JavaScript
- **Backend**: Flask, Python
- **ML Libraries**: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib
- **Data**: Publicly available healthcare dataset

## 📁 Folder Structure

```
disease-prediction-app/
│
├── client/                      # React frontend
│   ├── src/
│   └── public/
│
├── server/                      # Flask backend
│   ├── app.py
│   ├── model/
│   └── utils/
│
├── dataset/                     # Processed health data
├── requirements.txt
└── README.md
```

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/disease-prediction-app.git
   cd disease-prediction-app
   ```

2. **Install backend dependencies**:
   ```bash
   cd server
   pip install -r requirements.txt
   ```

3. **Start the Flask server**:
   ```bash
   python app.py
   ```

4. **Run the React frontend**:
   ```bash
   cd ../client
   npm install
   npm start
   ```

5. **Open your browser**:  
   Go to `http://localhost:3000`

## 📈 Sample Predictions

- User enters symptoms such as fatigue, chest pain, and high BP.
- Backend model processes input and returns disease risk probabilities.
- Results are shown along with suggested next steps.

## 🤝 Contributions

Open to collaboration! If you'd like to contribute or improve this app, feel free to fork and open a PR.

## 🧑‍💻 Author

**Tanvi Kulkarni**  
[LinkedIn](https://www.linkedin.com/in/tanvi-amol-kulkarni) | [Portfolio](https://ivnat07.github.io/MyPortfolio/) | [GitHub](https://github.com/ivnat07)

## 📄 License

MIT License – free for personal or commercial use.
