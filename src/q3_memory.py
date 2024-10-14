from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_count = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            if 'mentionedUsers' in tweet:
                for mention in tweet['mentionedUsers']:
                    mention_count[mention['username']] += 1

    top_10_users = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_users