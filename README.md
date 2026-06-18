# Large Language Models (LLMs) - Complete Implementation Guide

A comprehensive collection of Large Language Model implementations, fine-tuning techniques, and advanced applications. This repository covers the full spectrum of LLM development from pretraining and fine-tuning to cutting-edge techniques like Retrieval-Augmented Generation (RAG), structured output generation, and evaluation frameworks.

## 🧠 Core Competencies

### 🚀 Pretraining & Fine-Tuning

- **Pretraining Pipeline**: Complete implementation of LLM pretraining from scratch, including data preparation, tokenization, and distributed training strategies.
- **Supervised Fine-Tuning (SFT)**: Instruction tuning using curated datasets to align models with specific tasks and behaviors.
- **Reinforcement Learning (RLHF)**: Implementation of Reinforcement Learning from Human Feedback using PPO (Proximal Policy Optimization).
- **Direct Preference Optimization (DPO)**: Advanced preference learning technique for more stable and efficient fine-tuning.

### 🔍 Advanced Retrieval & Search

- **Vector Embeddings**: Comprehensive guide to creating and using text embeddings for semantic search and retrieval.
- **Semantic Search**: Implementation of dense retrieval systems using vector databases and similarity search.
- **Retrieval-Augmented Generation (RAG)**: Complete RAG pipeline combining retrieval with generation for enhanced factual accuracy.
- **Weaviate Integration**: Vector database implementation for scalable semantic search applications.

### 📊 Structured Output & Control

- **Pydantic Integration**: Structured output generation using Pydantic models for type-safe, validated responses.
- **Tool Calling**: Implementation of function calling capabilities for LLMs to interact with external APIs and tools.
- **Output Parsing**: Advanced techniques for parsing and validating structured outputs from language models.

### 🧪 Evaluation & Testing

- **Comprehensive Testing Framework**: Automated testing suite for evaluating LLM performance across multiple metrics.
- **Hallucination Detection**: Techniques for identifying and measuring model hallucinations.
- **Performance Metrics**: Implementation of accuracy, coherence, and relevance metrics for model evaluation.

## 🛠 Technical Stack

- **Core Frameworks**: PyTorch, Transformers (Hugging Face), LangChain
- **Vector Databases**: Weaviate, FAISS
- **Data Processing**: NumPy, Pandas, Scikit-learn
- **Evaluation**: Custom evaluation frameworks, Pydantic for validation
- **Development**: Jupyter Notebooks, Python 3.13+

## 📂 Repository Structure

| Directory | Description | Key Components |
|-----------|-------------|----------------|
| **Pretraining_LLMs** | Complete pretraining pipeline | Data preparation, tokenization, distributed training |
| **Post_Training_LLMs** | Fine-tuning techniques | SFT, RLHF, DPO implementations |
| **RAG** | Retrieval-Augmented Generation | Vector embeddings, semantic search, Weaviate |
| **SemanticSearch** | Search and retrieval systems | Dense retrieval, similarity search |
| **Structured_Output** | Controlled generation | Pydantic models, tool calling, output parsing |
| **TextEmbeddings** | Embedding techniques | Text vectorization, semantic similarity |
| **Evaluation_LLMs** | Testing frameworks | Performance metrics, hallucination detection |
| **GRPO** | Advanced optimization | Group Relative Policy Optimization |
| **AgentMemory** | Memory systems | Context management, agent architectures |
| **Attention** | Attention mechanisms | Transformer architectures, attention variants |

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- PyTorch 2.0+
- Jupyter Notebook/Lab
- CUDA-compatible GPU (recommended for training)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/holaholu/llm.git
   cd llm
   ```

2. **Set up the environment**

   ```bash
   python -m venv llm_env
   source llm_env/bin/activate  # On Windows use `llm_env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Install additional dependencies**

   ```bash
   # For RAG and vector search
   pip install weaviate-client sentence-transformers
   
   # For evaluation frameworks
   pip install pytest pydantic
   ```

### Quick Start

1. **Explore Pretraining**: Start with `Pretraining_LLMs/1_Pretraining_Intro.ipynb`
2. **Fine-Tuning Basics**: Try `Post_Training_LLMs/Supervised_FineTuning.ipynb`
3. **RAG Implementation**: Build your first RAG system with `RAG/vector_embeddings.ipynb`
4. **Structured Output**: Generate structured data with `Structured_Output/Pydantic_Basics.ipynb`

## 📈 Key Projects

| Project | Description | Tech Stack |
|---------|-------------|-----------|
| **Complete Pretraining Pipeline** | End-to-end LLM pretraining with distributed training | `PyTorch`, `Transformers`, `Distributed` |
| **RAG System** | Retrieval-Augmented Generation with Weaviate | `Weaviate`, `Sentence-Transformers`, `LangChain` |
| **Structured Output Generator** | Type-safe structured generation using Pydantic | `Pydantic`, `Transformers`, `JSON Schema` |
| **Comprehensive Evaluation Suite** | Automated testing and metrics for LLMs | `Pytest`, `Custom Metrics`, `Pandas` |
| **Multi-Modal Agent** | Memory-enabled agent with tool calling | `LangChain`, `Custom Memory Systems` |

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# API Keys (optional for some examples)
OPENAI_API_KEY=your_openai_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here

# Vector Database
WEAVIATE_URL=your_weaviate_url
WEAVIATE_API_KEY=your_weaviate_key

# Model Paths
MODEL_CACHE_DIR=./models
EMBEDDING_CACHE_DIR=./embeddings
```

## 📚 Learning Path

1. **Foundation**: Start with `LLM_Tokenizers.ipynb` to understand tokenization
2. **Core Concepts**: Progress through `Pretraining_LLMs/` for fundamental understanding
3. **Advanced Techniques**: Explore `Post_Training_LLMs/` for fine-tuning methods
4. **Applications**: Build practical applications in `RAG/` and `Structured_Output/`
5. **Evaluation**: Learn to evaluate models with `Evaluation_LLMs/`

## 🤝 Contributing

This repository is actively maintained as a learning resource. Contributions are welcome in the form of:
- New implementation examples
- Performance improvements
- Additional evaluation metrics
- Documentation enhancements

## 📄 License

This project is provided for educational purposes. Please refer to individual project licenses for specific usage terms.

---

_This repository serves as a comprehensive guide to modern Large Language Model development, from foundational concepts to cutting-edge applications._
