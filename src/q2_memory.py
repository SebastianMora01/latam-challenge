from typing import List, Tuple
import re
def extract_emojis(text: str) -> List[str]:
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "]+", flags=re.UNICODE)
    return emoji_pattern.findall(text)

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_count = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            emojis = extract_emojis(tweet['content'])
            for emoji in emojis:
                emoji_count[emoji] += 1

    top_10_emojis = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_emojis

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
