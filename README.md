# 🩺 Diabetes Prediction Web App  

This is a **Streamlit-based web application** that predicts whether a person is likely to have diabetes or not based on several medical parameters.  
The app uses a trained **Machine Learning model** to make predictions in real-time from user inputs.

---

## 🚀 Features  

- 📋 User-friendly interface built with **Streamlit**  
- 🤖 Machine Learning–based prediction  
- 🧮 Takes 8 key health parameters as input  
- ⚡ Instant prediction results  
- 🌐 Runs directly in the browser — no setup required for the end user  

---

## 🧠 Input Parameters  

| Parameter | Description |
|------------|--------------|
| **Pregnancies** | Number of times the person has been pregnant |
| **Glucose** | Plasma glucose concentration (mg/dL) |
| **Blood Pressure** | Diastolic blood pressure (mm Hg) |
| **Skin Thickness** | Triceps skin fold thickness (mm) |
| **Insulin** | 2-hour serum insulin (mu U/ml) |
| **BMI** | Body Mass Index (weight in kg/(height in m)²) |
| **Diabetes Pedigree Function** | Function that scores likelihood of diabetes based on family history |
| **Age** | Age of the person (in years) |

---

## 🧩 How It Works  

1. The user enters all the required health details in the input fields.  
2. The app processes the input data and feeds it into a pre-trained **Machine Learning model** (e.g., Logistic Regression, Random Forest, etc.).  
3. The model predicts whether the person is **Diabetic** or **Non-Diabetic**.  
4. The prediction result is displayed instantly on the screen.

---

## 🛠️ Technologies Used  

- **Python** 🐍  
- **Streamlit** – for web app UI  
- **Scikit-learn / Pickle** – for loading and using the ML model  
- **Pandas & NumPy** – for data processing  

---

## ▶️ How to Run the App  

1. **Clone the repository**
   ```bash
   git clone https://github.com/GaganYadav20/Diabetes_Prediction.git
   cd Diabetes_Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to 👉 [http://localhost:8501](http://localhost:8501)

---


## 🧾 Output Example  

✅ **Result:** “The person is not Diabetic.”  
❌ **Result:** “The person is likely to be Diabetic.”

---

## 👨‍💻 Author  

**Gagan Yadav**  
📧 [Gaganyadav2094@gmail.com](mailto:Gaganyadav2094@gmail.com)  
🌐 [GitHub Profile](https://github.com/GaganYadav20)
