import os
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("BASE_URL"))


query = '感冒吃什么药效果好？可以吃阿莫西林吗？'

# 查询语句向量化
query_resp = client.embeddings.create(
    model=os.getenv("MODEL_EMBEDDING"),
    input=query
)

query_vec = np.array(query_resp.data[0].embedding)

# print(query_vec)

# 备选文本向量化
question_texts = [
    '什么叫感冒? / 感冒是一种什么病？',
    '感冒一般是由什么引起的？/ 什么会导致感冒？',
    '感冒会有哪些症状？/ 感冒有哪些临床表现？',
    '感冒吃什么药好得快？/ 感冒怎么治？',
    '得了感冒去医院挂什么科室的号？',
    '感冒要怎么预防？',
    '感冒换着有什么禁忌？/ 感冒不能吃什么？',
    '感冒要做哪些检查？',
    '感冒能治好吗？/ 感冒治好的几率有多大？',
    '感冒的并发症有哪些？',
    '阿莫西林能治那些病？'
]

question_resp = client.embeddings.create(
    model=os.getenv("MODEL_EMBEDDING"),
    input=question_texts
)

question_vecs = []
for item in question_resp.data:
    question_vecs.append(np.array(item.embedding))

# print(len(question_vecs))


# 计算欧式距离，距离越小，相似度越高
l2_distances = np.linalg.norm(query_vec - question_vecs, axis=1)

closest_indices = np.argsort(l2_distances)[:3]
# print(closest_indices)

for idx in closest_indices:
    print(question_texts[idx])

