好，给你一个**具体到每周**的RDKit学习计划，6-8月执行。

---

## 前置条件

- Python基础（你会，没问题）
- 建议用conda管理环境（避免包冲突）

```bash
# 创建独立环境
conda create -n rdkit python=3.10
conda activate rdkit
conda install -c conda-forge rdkit jupyter pandas matplotlib seaborn
```

---

## 6月：RDKit基础操作

### Week 1：分子表示与可视化

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 学SMILES | 理解SMILES语法规则，能手写简单分子 | 笔记 |
| RDKit读分子 | `Chem.MolFromSmiles()`, `Chem.MolToSmiles()` | notebook |
| 分子画图 | `Draw.MolToImage()`, `Draw.MolsToGridImage()` | 10个分子的可视化图 |
| 分子属性 | 分子量、分子式、环数 | 属性表 |

**练习**：
- 找10个常见药物（阿司匹林、布洛芬等），画出它们的结构
- 比较它们的SMILES表示，观察规律

---

### Week 2：分子描述符计算

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 物理化学描述符 | `Descriptors.MolWt`, `MolLogP`, `TPSA`, `NumHDonors`, `NumHAcceptors` | 描述符计算函数 |
| 结构描述符 | `NumRotatableBonds`, `NumAromaticRings`, `NumAliphaticRings` | 结构特征表 |
| Lipinski五规则 | 实现判断函数（MW<<500, LogP<<5, HBD<<5, HBA<<10） | 类药性筛选工具 |

**练习**：
- 下载DrugBank的"small molecule"数据集（约2000个）
- 计算所有分子的描述符，画分布图（histogram/boxplot）
- 标记哪些符合Lipinski规则，哪些不符合

---

### Week 3：子结构与匹配

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 子结构搜索 | `Chem.MolFromSmarts()`, `HasSubstructMatch()` | 子结构匹配函数 |
| 常见药效团 | 苯环、羧基、酰胺、磺酰胺等 | 药效团匹配工具 |
| 分子片段分解 | `rdMMPA`（Matched Molecular Pair Analysis）入门 | 片段分析notebook |

**练习**：
- 定义5个常见子结构（如：苯环、羧酸、伯胺）
- 在DrugBank数据集中统计每个子结构的出现频率
- 找出"同时含苯环和羧酸"的分子（模拟NSAIDs的共同特征）

---

### Week 4：分子相似性与聚类

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 指纹计算 | Morgan指纹（ECFP）, `AllChem.GetMorganFingerprintAsBitVect()` | 指纹生成函数 |
| 相似性计算 | Tanimoto系数, `DataStructs.TanimotoSimilarity()` | 相似性矩阵 |
| 聚类分析 | 用指纹+Tanimoto做层次聚类, 画dendrogram | 分子聚类图 |

**练习**：
- 选100个COX-2抑制剂（可从ChEMBL下载）
- 计算它们的Morgan指纹，做聚类
- 观察：结构相似的分子是否聚在一类？

**6月底产出**：一个GitHub仓库，包含4个notebook（可视化→描述符→子结构→相似性）

---

## 7月：ADMET数据与建模基础

### Week 5-6：MoleculeNet数据探索

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 下载数据 | ESOL（溶解度）, FreeSolv（水合自由能）, Lipophilicity（油水分配系数） | 数据集 |
| 数据清洗 | 去重、处理缺失值、异常值检测 | 清洗脚本 |
| EDA | 描述符分布、相关性矩阵、与目标变量的关系 | EDA报告 |

**关键学习点**：
- 理解这三个任务分别对应ADMET的哪个字母（A=Absorption, D=Distribution, M=Metabolism, E=Excretion, T=Toxicity）
- ESOL→A（溶解度影响吸收）, Lipophilicity→A/D

---

### Week 7：传统机器学习基线

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 特征工程 | 用RDKit计算全套描述符作为特征 | 特征矩阵 |
| 模型训练 | 随机森林, XGBoost, 用scikit-learn | 训练脚本 |
| 评估 | R², RMSE, 5-fold交叉验证 | 结果表 |

**练习**：
- 在ESOL数据集上，用分子描述符训练随机森林
- 记录验证集R²，作为后续GNN的对比基准

---

### Week 8：模型解释与错误分析

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 特征重要性 | 随机森林的`feature_importances_`, SHAP值 | 重要特征图 |
| 错误分析 | 找出预测误差最大的分子，观察结构规律 | 错误分析笔记 |
| 可视化 | 预测值vs真实值的散点图，按误差大小着色 | 分析图 |

**7月底产出**：
- 一个完整的"ESOL溶解度预测"项目（数据→特征→模型→评估→解释）
- 技术博客草稿："用RDKit和随机森林预测分子溶解度"

---

## 8月：图神经网络入门（GNN）

### Week 9-10：分子图表示

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 图表示 | 分子→图：原子=节点，键=边 | 图转换函数 |
| 节点特征 | 原子类型、度、电荷、芳香性等 | 节点特征编码 |
| 边特征 | 键类型（单/双/三/芳香）、是否共轭 | 边特征编码 |

**技术栈**：PyTorch + PyTorch Geometric (PyG)

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install torch-geometric torch-scatter torch-sparse
```

---

### Week 11：GNN模型训练

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 模型搭建 | GCN或GIN（Graph Isomorphism Network） | 模型代码 |
| 训练流程 | 数据划分、训练循环、早停 | 训练脚本 |
| 对比实验 | 与随机森林的R²对比 | 结果表 |

**关键学习点**：
- 理解为什么GNN适合分子：分子天然是图结构
- 理解消息传递（message passing）机制

---

### Week 12：项目收尾与展示

| 任务 | 具体内容 | 产出 |
|:---|:---|:---|
| 完整对比 | 传统ML vs GNN在ESOL上的性能对比 | 对比表+图 |
| 案例分析 | 挑3-5个分子，对比两种模型的预测 | 案例分析 |
| 文档整理 | README、requirements、运行说明 | 可复现仓库 |

**8月底产出**：
- GitHub仓库："Molecular-ADMET-Prediction"
- 结构：data/ notebooks/ src/ README.md requirements.txt
- 能一键运行（至少核心流程）

---

## 每周时间分配建议

| 活动 | 时间 | 说明 |
|:---|:---|:---|
| 学习新内容 | 5-6h | 看文档、教程、运行代码 |
| 动手练习 | 4-5h | 自己写代码，不要只抄 |
| 整理笔记 | 2h | 写进notebook，配markdown说明 |
| 复盘/debug | 2-3h | 解决报错，记录坑和解决方案 |
| **总计** | **13-16h/周** | 约每天2h，周末多补 |

---

## 关键检查点

| 时间 | 检查内容 | 通过标准 |
|:---|:---|:---|
| 6月底 | RDKit基础 | 能独立画出10个药物结构，计算描述符 |
| 7月底 | 传统ML基线 | ESOL上随机森林R² > 0.7（文献基准约0.8） |
| 8月底 | GNN入门 | GNN跑通，有结果，不管好坏 |

**如果7月底R² < 0.5**：检查特征工程，或换Lipophilicity数据集（更简单）
**如果8月底GNN跑不通**：先保证传统ML项目完整，GNN可以延后

---

## 学习资源清单

| 类型 | 资源 | 用途 |
|:---|:---|:---|
| 官方文档 | RDKit Cookbook (https://www.rdkit.org/docs/Cookbook.html) | 查API |
| 教程 | Pat Walters的RDKit博客 (practicalcheminformatics.com) | 学思路 |
| 数据集 | MoleculeNet (http://moleculenet.ai) | 下载数据 |
| GNN教程 | PyG官方示例 (github.com/pyg-team/pytorch_geometric) | 学GNN |
| 书籍 | 《Deep Learning for the Life Sciences》(O'Reilly) | 备用参考 |

---

**下一步**：你需要我帮你**写Week 1的具体代码模板**（SMILES读取+画图），还是**推荐DrugBank/ChEMBL数据的下载方式**？