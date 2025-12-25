<h1 align="center">🛡️ AI-Based Scam Detection System</h1>

<p align="center">
  <b>An end-to-end Machine Learning & NLP project for detecting scam messages using Python and Streamlit.</b>
</p>

<hr/>

<h2>📌 Project Overview</h2>

<p>
Scam and spam messages have become increasingly common across digital platforms.
This project focuses on building an <b>automated scam detection system</b> using
<b>Natural Language Processing (NLP)</b> and <b>Machine Learning</b>.
</p>

<p>
The system classifies a given text message as <b>Scam</b> or <b>Not Scam</b> and provides
real-time predictions through an interactive web interface.
</p>

---

<h2>🧠 Machine Learning Approach</h2>

<ul>
  <li><b>Text Vectorization:</b> CountVectorizer (Bag-of-Words model)</li>
  <li><b>Classifier:</b> Multinomial Naive Bayes</li>
  <li><b>Problem Type:</b> Binary text classification</li>
</ul>

<p>
Multinomial Naive Bayes was selected due to its efficiency and strong performance
on text-based classification problems such as spam detection.
</p>

---

<h2>⚙️ How the System Works</h2>

<ol>
  <li>Load labeled text data from the dataset</li>
  <li>Convert raw text into numerical features using NLP techniques</li>
  <li>Train a supervised machine learning model</li>
  <li>Serialize the trained model for reuse</li>
  <li>Accept user input via a Streamlit-based interface</li>
  <li>Predict whether the message is Scam or Safe</li>
</ol>

---

<h2>📂 Project Structure</h2>

<pre>
├── app.py              # Streamlit web application
├── train_model.py      # Model training pipeline
├── spam.csv            # Dataset (labeled messages)
├── spam_model.pkl      # Trained ML model
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime version
└── README.md           # Project documentation
</pre>

---

<h2>🖥️ Running the Project Locally</h2>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/Nidhs01/&lt;repository-name&gt;.git
cd &lt;repository-name&gt;
</pre>

<h3>2️⃣ Create and Activate Virtual Environment</h3>

<pre>
py -3.11 -m venv venv
venv\Scripts\activate
</pre>

<h3>3️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Run the Application</h3>

<pre>
streamlit run app.py
</pre>

<p>
The application will be available at:
<b>http://localhost:8501</b>
</p>

---

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>Python 3.11</li>
  <li>scikit-learn</li>
  <li>NumPy</li>
  <li>pandas</li>
  <li>Streamlit</li>
  <li>Natural Language Processing (NLP)</li>
  <li>Git & GitHub</li>
</ul>

---

<h2>🔍 Key Technical Highlights</h2>

<ul>
  <li>End-to-end NLP-based text classification pipeline</li>
  <li>Efficient model persistence using pickle</li>
  <li>Separation of training and inference logic</li>
  <li>Environment and dependency management</li>
  <li>Interactive ML-powered user interface</li>
</ul>

---

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Advanced preprocessing (stemming, lemmatization)</li>
  <li>Model comparison with Logistic Regression and SVM</li>
  <li>Expanded dataset for improved accuracy</li>
  <li>REST API integration using FastAPI</li>
</ul>

---

<h2>👤 Author</h2>

<p>
<b>Nidhs01</b><br/>
Machine Learning & AI Enthusiast
</p>

<hr/>

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>
