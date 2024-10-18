def calculate_love_score(name1, name2):
    # Combine the names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Initialize dictionaries to store counts
    true_counts = {letter: combined_names.count(letter) for letter in 'true'}
    love_counts = {letter: combined_names.count(letter) for letter in 'love'}

    # Calculate the total scores
    true_score = sum(true_counts.values())
    love_score = sum(love_counts.values())

    # Print each letter's count of true
    for letter, count in true_counts.items():
        print(f"{letter.upper()} occurs {count} times")
    print(f"Total {true_score}")

    # Print each letter's count of love
    for letter, count in love_counts.items():
        print(f"{letter.upper()} occurs {count} times")
    print(f"Total {love_score}")

    # Combine scores to make a two-digit number
    love_score_combined = str(true_score) + str(love_score)
    print(f"Love Score = {love_score_combined}")

# Calling function with hard coded names
calculate_love_score("Kanye West", "Kim Kardashian")