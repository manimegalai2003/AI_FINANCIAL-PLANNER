🚀 AI-Based Financial Planner 📈
An interactive AI-powered financial planning tool built with Streamlit, leveraging machine learning (Linear Regression) to analyze stock prices, predict future trends, and provide investment insights based on risk tolerance.

🌟 Features
✅ Fetches real-time stock market data using yfinance
✅ Stock price prediction using Linear Regression
✅ Investment insights (Market Cap, 52-Week High/Low, Current Price)
✅ Interactive charts (Historical prices, Moving Averages, Volatility Analysis)
✅ Personalized investment recommendations based on risk tolerance

📌 Technologies Used
Python
Streamlit (for interactive UI)
yfinance (for real-time stock data)
Matplotlib (for data visualization)
Scikit-Learn (for machine learning)
Pandas & NumPy (for data processing)

🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-financial-planner.git
cd ai-financial-planner

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit app
streamlit run app.py
📌 Replace app.py with your actual Python script name

🖥️ How It Works
1️⃣ Enter a stock ticker (e.g., AAPL, TSLA)
2️⃣ Select investment horizon (Short-Term, Mid-Term, Long-Term)
3️⃣ Adjust risk tolerance (Low to High)
4️⃣ View stock insights & price predictions
5️⃣ Get AI-driven investment recommendations

🛠️ Future Improvements
🔹 Enhance prediction model with LSTMs / Time-Series ML models
🔹 Add Sentiment Analysis using financial news
🔹 Implement Portfolio Optimization strategies
