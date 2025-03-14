import json
import random as rand

# Open Proverbs as Dict
with open('data/proverbs.json', 'r') as file:
    proverb_data = list(json.load(file))
    # for i in list:
    #     print(i)
    #     proverb_data = i
    
# Display Topic Prompt
print("===== Ancient Chinese Proverb Generator =====\n")
print("To randomly select a proverb, select a topic or select \'random\'")
topic_count = 1
print("0 - Random")
for topic in proverb_data:
    print(topic_count, "-", topic)
    topic_count += 1



wants_proverb = True

while True:
    # take topic input from user
    topic_choice = int(input("Enter choice (Life, Wisdom, ...): "))
    print(proverb_data[topic_choice][0])
    print(proverb_data)
    
    
    # check if choice is valid    
    if topic_choice == 0: 
        topic_choice = rand.randint(1, (len(proverb_data) + 1))
        
    # Select random proverb from chosen topic 
    if topic_choice <= (len(proverb_data) + 1) and topic_choice > 0:
        print("Generating random proverb from ", proverb_data[topic_choice])
        topic_proverbs = proverb_data[topic_choice]
        
        rand_proverb_item = topic_proverbs[rand.randint(1, len(proverb_data))]
        print(rand_proverb_item)
        
        # i = 0
        # for key, value in proverb_data.items():
        #     print(key, " --- ",value)
        #     if i == rand_proverb_idx:
        #         proverb = value
        #     i += 1
        
        # 
        # print(proverb)

        
    else:
        print("ERROR: Choice selected is out of bounds. Please select again.")
    
    # Display Topic Prompt
    print("=============================================")
    print("===== Ancient Chinese Proverb Generator =====\n")
    print("To randomly select a proverb, Enter a topic or \'random\'")
    print("0 - Random")
    topic_count = 1
    for topic in proverb_data:
        print(topic_count, "-", topic)
        topic_count += 1
