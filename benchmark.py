import time
import statistics
import numpy as np

from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from agents.expert import ExpertAgent
from council.manager import CouncilManager

TEST_PROMPTS = [
    "Explain TCP vs UDP",
    "Design a URL shortener",
    "What is Raft consensus?",
    "Explain deadlock in operating systems",
    "What is consistent hashing?",
    "Design a distributed cache",
    "How does DNS work?",
    "What is CAP theorem?",
    "Explain multithreading vs multiprocessing",
    "Design a scalable chat application"
]

agents = [
    PlannerAgent(),
    CriticAgent(),
    ExpertAgent()
]

council = CouncilManager(agents)

latencies = []
response_lengths = []

print("Running Benchmark...\n")

for idx, prompt in enumerate(TEST_PROMPTS, start=1):

    start = time.perf_counter()

    response = council.convene(prompt)

    end = time.perf_counter()

    latency = end - start

    latencies.append(latency)
    response_lengths.append(len(str(response)))

    print(f"[{idx}/{len(TEST_PROMPTS)}] {latency:.2f}s")

avg_latency = statistics.mean(latencies)
p95_latency = np.percentile(latencies, 95)
throughput = len(TEST_PROMPTS) / sum(latencies)

print("\n" + "=" * 50)
print("Tiny Council Benchmark Results")
print("=" * 50)
print(f"Prompts Tested     : {len(TEST_PROMPTS)}")
print(f"Average Latency    : {avg_latency:.2f}s")
print(f"P95 Latency        : {p95_latency:.2f}s")
print(f"Throughput         : {throughput:.2f} req/s")
print(f"Avg Response Size  : {statistics.mean(response_lengths):.0f} chars")
print("=" * 50)