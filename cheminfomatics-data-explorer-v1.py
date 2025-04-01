import streamlit as st
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from rdkit.Chem import rdMolDescriptors
import sqlite3

# App Title
st.title("Cheminformatics Data Explorer")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Task", ["Database Explorer", "Molecular Analysis", "Chemical Space Exploration"])

# Database connection (Example using SQLite)
conn = sqlite3.connect("cheminformatics.db")
cursor = conn.cursor()

# Ensure a sample table exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS molecules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    smiles TEXT
)
''')
conn.commit()

# 1. Database Explorer
if page == "Database Explorer":
    st.header("Cheminformatics Database")

    # Display existing data
    df = pd.read_sql_query("SELECT * FROM molecules", conn)
    st.dataframe(df)

    # Add new molecules
    with st.form("add_molecule"):
        name = st.text_input("Molecule Name")
        smiles = st.text_input("SMILES Notation")
        submit = st.form_submit_button("Add to Database")
        
        if submit and name and smiles:
            try:
                mol = Chem.MolFromSmiles(smiles)
                if mol:
                    cursor.execute("INSERT INTO molecules (name, smiles) VALUES (?, ?)", (name, smiles))
                    conn.commit()
                    st.success(f"Added {name} to the database.")
                else:
                    st.error("Invalid SMILES notation.")
            except Exception as e:
                st.error(f"Error adding molecule: {e}")

# 2. Molecular Analysis
elif page == "Molecular Analysis":
    st.header("Molecular Property Calculator")

    smiles_input = st.text_area("Enter SMILES string(s)", height=100)
    
    if st.button("Analyze"):
        smiles_list = smiles_input.split("\n")
        results = []
        
        for smi in smiles_list:
            smi = smi.strip()
            mol = Chem.MolFromSmiles(smi)
            if mol:
                mol_img = Draw.MolToImage(mol)
                mol_weight = Descriptors.MolWt(mol)
                logp = Descriptors.MolLogP(mol)
                hbd = rdMolDescriptors.CalcNumHBD(mol)
                hba = rdMolDescriptors.CalcNumHBA(mol)
                
                st.subheader(f"Molecule: {smi}")
                st.image(mol_img, caption="Structure")
                st.write(f"**Molecular Weight:** {mol_weight}")
                st.write(f"**LogP:** {logp}")
                st.write(f"**H-bond Donors:** {hbd}")
                st.write(f"**H-bond Acceptors:** {hba}")
            else:
                st.warning(f"Invalid SMILES: {smi}")

# 3. Chemical Space Exploration
elif page == "Chemical Space Exploration":
    st.header("Chemical Space Enumeration")

    base_smiles = st.text_input("Enter Base SMILES for Enumeration")
    
    if st.button("Generate Analogues"):
        mol = Chem.MolFromSmiles(base_smiles)
        if mol:
            # Simple enumeration (add common functional groups)
            fragments = ["CC", "C=O", "C#N", "CCl", "CO", "CN"]
            new_molecules = []

            for frag in fragments:
                new_smiles = base_smiles + frag
                new_mol = Chem.MolFromSmiles(new_smiles)
                if new_mol:
                    new_molecules.append((new_smiles, Draw.MolToImage(new_mol)))
            
            for smi, img in new_molecules:
                st.subheader(f"Variant: {smi}")
                st.image(img, caption=smi)
        else:
            st.error("Invalid base SMILES notation.")

# Close the database connection
conn.close()
