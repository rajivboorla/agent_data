
Input = {'Product1':{ 'metal':['gold']}, 'Product2' :{ 'metal':['Zinc','Gold','Silver']}}

# Output = {'Product1':{ 'metal':'GOLD'}, 'Product2' :{ 'metal':'GOLD|SILVER|ZINC'}}

def transform_products(input_dict):
    output_dict = {}
    for product, attributes in input_dict.items():
        output_dict[product] = {}
        for attr, values in attributes.items():
            upper_values = [value.upper() for value in values]
            combined_values = '|'.join(sorted(upper_values))
            output_dict[product][attr] = combined_values
    return output_dict

transform_products(Input)



# text = """101, 20, login
# 101, 80, logout
# 102, 30, login
# 102, 70, logout
# 103, 20, login
# 103, 60, logout
# 104, 10, login
# 104, 90, logout"""

# output = {'101': 60, '102': 40, '103': 40, '104': 80}

# def calculate_durations(text):
#     lines = text.strip().split('\n')
#     sessions = {}
#     for line in lines:
#         user_id, timestamp, action = line.split(', ')
#         timestamp = int(timestamp)
#         if user_id not in sessions:
#             sessions[user_id] = {}
#         sessions[user_id][action] = timestamp

#     durations = {}
#     for user_id, actions in sessions.items():
#         if 'login' in actions and 'logout' in actions:
#             durations[user_id] = actions['logout'] - actions['login']
    
#     return durations