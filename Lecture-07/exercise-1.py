# Survey results (each list represents a participant's choice)
survey_results = [
    ["Python", "Javascript", "C++"],                   #Participant 1
    ["Python", "Javascript", "C#"],                    #Participant 2
    ["Python", "Java"],                                #Participant 3
    ["Python", "C++", "Javascript"],                   #Participant 4
    ["Python", "Javascript", "C++", "Java"],           #Participant 5
]

# 1. Identify the languages that were chosen by all participants.
# 2. Find the languages that were only chosen by a single participant.
# 3. Determine the number of unique languages mentioned in the survey.
# 4. List the languages that were chosen by at exactly two participants.
# 5. Find participants who have the exact same set of favorite languages.


languages_all_participants = set.intersection(*[set(participant) for participant in survey_results])
print("Languages chosen by all participants:", languages_all_participants)

# 1. Identify the languages that were chosen by all participants.


# 2. Find the languages that were only chosen by a single participant.


# 3. Determine the number of unique languages mentioned in the survey.


# 4. List the languages that were chosen by at exactly two participants.


# 5. Find participants who have the exact same set of favorite languages.
