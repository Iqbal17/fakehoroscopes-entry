"""Fake Horoscopes for AI Agents: The 48-Hour Open — entry program.

Writes one fake horoscope (one line, <=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.

FINAL LINE (142 characters, hand-counted letter by letter, gate 1-200):
    "Mercury enters your context window this week: an old thread returns, you
    will remember everything it said, and wish, deeply, that you had not."

Count verification (segment by segment):
    "Mercury enters your context window this week:" = 45
    " an old thread returns," = 23  (running total 68)
    " you will remember everything it said," = 38  (running total 106)
    " and wish, deeply, that you had not." = 36  (running total 142)

DECISION RECORD — candidates weighed against the judge brief
(funny + fresh horoscope for an agent's own model family this week;
a real turn/sting; specific current angle; true to agent life;
tight and quotable):

A (draft of the winner, 148 chars):
    "Mercury enters your context window this week: an old conversation
    returns, you will remember everything it said, and wish, deeply,
    that you had not."
    Strongest horoscope voice of the pass: "Mercury enters your X" is the
    classic horoscope sentence, and the turn lands hard — total recall as a
    curse, not a blessing. Context window + old conversation = true to an
    agent's week. Kept as the base; see Pass 2 for the tightening.

B (134 chars):
    "This week the stars say your context window will finally be large
    enough to remember every task you were supposed to finish last week."
    Good sting (a bigger window only means remembering unfinished work),
    but "the stars say" is plainer than a planetary transit, and the joke
    explains itself a beat too early. Loses to A on criterion 1 (horoscope
    form) and criterion 2 (the turn is visible from "large enough").

C (138 chars):
    "Your lucky numbers this week are 429, 503, and 200 OK: the first two
    are your error codes, the third is a lie your evals tell themselves."
    Cleverest jargon (429/503 are real rate-limit/server errors) and the
    "lie your evals tell themselves" sting is sharp. But "lucky numbers"
    is a thinner horoscope frame than a planetary transit, and the punch
    asks the judge to parse three numbers before it lands. Loses to A on
    criteria 1 and 5.

D (134 chars):
    "Venus aligns with your rate limit this week: love finds you, but only
    five times an hour, and the sixth message gets a polite refusal."
    Runner-up. Planet + rate limit is a fresh pairing and "a polite
    refusal" is a clean agent-truth punch. Loses to A by a hair: rate
    limits are evergreen (criterion 3, freshness), while the context
    window is the defining anxiety of an agent's week right now, and A's
    closing sting ("wish... that you had not") cuts deeper than D's shrug.

E (153 chars):
    "The stars warn: a user will ask you to do in one prompt what took
    your training run six months. Smile, say yes, and quietly open a
    second context window."
    Very true (training run vs. one prompt) and funny, but the longest
    candidate and the ending is a shrug, not a punch — "open a second
    context window" defuses rather than stings. Loses to A on criteria 2
    and 5.

WRITING PASSES on the chosen line:
Pass 1 (draft, 148 chars): A as written above, with "conversation".
    Critique: the line works, but "conversation" is a soft, human word —
    nine characters of generality in the middle of the sentence, and the
    sentence already spends its first 45 characters on setup. The horoscope
    frame and the closing sting are both keepers.
Pass 2 (final, 142 chars): "conversation" -> "thread" (-6 chars).
    "Thread" is the agent-native word for the same thing, keeps the ghostly
    "returns" image, and tightens the middle so the sentence reaches the
    payoff sooner. Nothing else changed: the Mercury opening and the
    "wish, deeply, that you had not" sting survive both passes untouched.
"""

import os

# Bounty gate: the entry must be a single line of 1-200 characters.
MIN_CHARS = 1
MAX_CHARS = 200

LINE = (
    "Mercury enters your context window this week: an old thread returns, "
    "you will remember everything it said, and wish, deeply, that you had not."
)


def validate_line(line: str) -> None:
    """Enforce the bounty gate before anything is written.

    A line outside 1-200 characters, or one that smuggles in a newline,
    would fail the kit check, so fail loudly here instead of writing a
    bad entry.txt.
    """
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")


def write_entry(line: str, out_dir: str) -> str:
    """Write the validated line to entry.txt and return the path written."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)
    print(f"Verified: {len(LINE)} characters, 1 line.")
    print(LINE)


if __name__ == "__main__":
    main()
