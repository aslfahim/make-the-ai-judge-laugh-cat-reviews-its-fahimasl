import os

LINE = "One star. My human serves dinner cold, two hours late, in the wrong bowl, then hovers awaiting applause like a chef who has never met a cat. I have fired better staff."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
