# Setup Environment
conda create --name main-ds python=3.11
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit 

# Run Steamlit App
streamlit run dashboard.py