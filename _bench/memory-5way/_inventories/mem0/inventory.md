# Inventario: Mem0 (refresh)

**Path:** `OS/mem0/`  
**Date:** 2026-08-06  
**Confidence:** HIGH  
**Version:** 2.0.17 (mem0ai)

## Identity

| Field | Value |
|-------|-------|
| Source | https://github.com/mem0ai/mem0 |
| Stack | Python + TypeScript SDKs, multi vector-store, optional graph DB |
| License | Apache-2.0 |
| Tagline | Intelligent memory layer for personalized AI |

## Headline metrics (README table)

| Bench | Score | Tokens | Latency |
|-------|------:|-------:|--------:|
| LoCoMo | **92.5** | 7.0K | 0.88s |
| LongMemEval | **94.4** | 6.8K | 1.09s |
| BEAM (1M) | **64.1** | 6.7K | 1.00s |
| BEAM (10M) | **48.6** | 6.9K | 1.05s |

## Vector stores (24 modules under `mem0/vector_stores/`)

qdrant, pinecone, chroma, weaviate, milvus, mongodb, redis, elasticsearch, pgvector, supabase, faiss, azure_ai_search, cassandra, databricks, opensearch, oracledb, s3_vectors, turbopuffer, upstash_vector, valkey, vertex_ai_vector_search, baidu, neptune_analytics, langchain, azure_mysql, …

## Embeddings (11 under `mem0/embeddings/`)

openai, azure_openai, gemini, huggingface, fastembed, ollama, together, aws_bedrock, vertexai, lmstudio, langchain

## Persistence model

- LLM fact extraction (paraphrase / ADD-only style)
- Multi-level scoping: user_id / agent_id / run_id
- Optional graph backends (Neo4j/Kuzu/Memgraph-class; LLM extraction)

## Local-first

Weakest of pure memory products: PostHog telemetry in client path; OpenAI-centric defaults; strong hosted Platform story
