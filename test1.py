from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors

# ==================== 1. SMILES 读取 ====================
smiles_list = [
    "CCO",           # 乙醇
    "c1ccccc1",      # 苯
    "CC(=O)Oc1ccccc1C(=O)O",  # 阿司匹林
    "InvalidSMILES", # 错误示例
]

for smi in smiles_list:
    mol = Chem.MolFromSmiles(smi)
    
    if mol is None:
        print(f"❌ 无效 SMILES: {smi}")
        continue
    
    # 基础信息提取
    print(f"\n✅ 有效分子: {smi}")
    print(f"   分子式: {Chem.rdMolDescriptors.CalcMolFormula(mol)}")
    print(f"   分子量: {Descriptors.MolWt(mol):.2f}")
    print(f"   重原子数: {mol.GetNumHeavyAtoms()}")
    print(f"   环数: {Chem.rdMolDescriptors.CalcNumRings(mol)}")