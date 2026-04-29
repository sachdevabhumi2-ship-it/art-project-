import streamlit as st
import pandas as pd

st.set_page_config(page_title="FinTechChain", page_icon="💳", layout="wide")

st.title("💳 FinTechChain")
st.subheader("Blockchain Startup Design Project - FinTech")

st.markdown("---")

# Startup Table
st.header("📌 Startup Table")

startup = pd.DataFrame({
    "Item": [
        "Startup Name",
        "Business Problem",
        "Target Customer",
        "How Blockchain is Used",
        "Main Actors",
        "Product / Service",
        "Benefit of Blockchain",
        "Risk / Challenge"
    ],
    "Details": [
        "FinTechChain",
        "Slow payments, fraud, high transaction fees",
        "Customers, banks, businesses",
        "Secure peer-to-peer blockchain payment system",
        "Customer, Bank, Merchant, Platform",
        "Blockchain payment and lending platform",
        "Fast payments, low cost, better security",
        "Users may not understand wallets and regulations"
    ]
})

st.table(startup)

# Flow Table
st.header("⛓️ Mini Blockchain Flow")

flow = pd.DataFrame({
    "Block": [1,2,3,4],
    "Actor": ["Customer","Platform","Bank","Merchant"],
    "Activity": [
        "Initiated payment",
        "Verified transaction",
        "Transferred funds",
        "Received payment"
    ]
})

st.table(flow)

# Token
st.header("🪙 Token Utility")

token = pd.DataFrame({
    "Token Name": ["FinCoin"],
    "Purpose": ["Rewards users, cashback, transaction fees"]
})

st.table(token)

# Explanation
st.header("📖 How Blockchain Improves This Business")

st.write("""
Blockchain improves FinTech businesses by making financial transactions faster,
safer, and more transparent. Traditional payment systems can be slow and involve
high fees because multiple intermediaries are used.

FinTechChain uses blockchain to allow secure peer-to-peer transactions. Every
transaction is recorded on a digital ledger, reducing fraud and increasing trust.

Customers can send money quickly with lower fees. Businesses receive payments
faster. Smart contracts can automate loans, insurance claims, and settlements.

Banks and financial companies benefit from lower costs and better efficiency.
Overall, blockchain modernizes financial services with speed, security,
and transparency.
""")

st.success("✅ FinTech Blockchain Project Ready")
