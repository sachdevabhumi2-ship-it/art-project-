Use this code in your **app.py** file because your topic is **Art**.

```python id="z8q1n5"
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ArtChain", page_icon="🎨", layout="wide")

st.title("🎨 ArtChain")
st.subheader("Blockchain Startup Design Project - Art")

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
        "ArtChain",
        "Fake artworks, ownership disputes, lack of transparency",
        "Artists, collectors, galleries, buyers",
        "Each artwork gets a digital certificate on blockchain",
        "Artist, Gallery, Buyer, Auction House",
        "Blockchain art authentication marketplace",
        "Prevents forgery, proves ownership, builds trust",
        "Users may not understand wallets or digital certificates"
    ]
})

st.table(startup)

# Blockchain Flow
st.header("⛓️ Mini Blockchain Flow")

flow = pd.DataFrame({
    "Block": [1,2,3,4],
    "Actor": ["Artist","Platform","Gallery","Buyer"],
    "Activity": [
        "Created original artwork",
        "Generated blockchain certificate",
        "Displayed artwork for sale",
        "Purchased and ownership transferred"
    ]
})

st.table(flow)

# Token Utility
st.header("🪙 Token Utility")

token = pd.DataFrame({
    "Token Name": ["ArtCoin"],
    "Purpose": ["Rewards buyers, royalty payments, platform fees"]
})

st.table(token)

# Explanation
st.header("📖 How Blockchain Improves This Business")

st.write("""
Blockchain improves the art business by creating trust, transparency,
and secure ownership records. In the traditional art market, fake
paintings and duplicate copies are often sold as originals.

ArtChain solves this issue by giving every artwork a unique digital
certificate stored on the blockchain. This certificate proves authenticity
and cannot be easily changed.

Whenever the artwork is sold, ownership is transferred through blockchain,
creating a permanent history of transactions. Buyers can verify if the
artwork is genuine and who owned it previously.

Artists also benefit because smart contracts can automatically pay
royalties whenever the artwork is resold. Overall, blockchain reduces
fraud, increases trust, and ensures fair rewards for creators.
""")

st.success("✅ Art Blockchain Project Ready")
```

