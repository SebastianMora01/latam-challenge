from typing import List, Tuple
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_count = defaultdict(int)
    with open(file_path, 'r', encoding='utf-8') as file:
        tweets = [json.loads(line) for line in file]

    for tweet in tweets:
        emojis = extract_emojis(tweet['content'])
        for emoji in emojis:
            emoji_count[emoji] += 1

    top_10_emojis = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_emojis
