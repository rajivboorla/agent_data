
# Input = {'Product1':{ 'metal':['gold']}, 'Product2' :{ 'metal':['Zinc','Gold','Silver']}}

# # Output = {'Product1':{ 'metal':'GOLD'}, 'Product2' :{ 'metal':'GOLD|SILVER|ZINC'}}

# def transform_products(input_dict):
#     output_dict = {}
#     for product, attributes in input_dict.items():
#         output_dict[product] = {}
#         for attr, values in attributes.items():
#             upper_values = [value.upper() for value in values]
#             combined_values = '|'.join(sorted(upper_values))
#             output_dict[product][attr] = combined_values
#     return output_dict

# transform_products(Input)



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

from database import SessionLocal
from models.agent import Agent
from routers import agents

def test_db_connection():
    try:
        db = SessionLocal()
        # Try to query the database to ensure the connection works
        # agents = db.query(Agent).all()
        agents = [
                    Agent(name="Rajesh Kumar", age=28, city="Hyderabad", area="Madhapur", phone="9876543210"),
                    Agent(name="Suresh Reddy", age=35, city="Hyderabad", area="Gachibowli", phone="9876543211"),
                    Agent(name="Anita Sharma", age=30, city="Bangalore", area="Whitefield", phone="9876543212"),
                    Agent(name="Vikram Singh", age=40, city="Chennai", area="T Nagar", phone="9876543213"),
                    Agent(name="Pooja Verma", age=26, city="Mumbai", area="Andheri", phone="9876543214"),
                    Agent(name="Arjun Rao", age=32, city="Hyderabad", area="Kukatpally", phone="9876543215"),
                    Agent(name="Neha Patel", age=29, city="Pune", area="Hinjewadi", phone="9876543216"),
                    Agent(name="Kiran Yadav", age=38, city="Delhi", area="Dwarka", phone="9876543217"),
                    Agent(name="Meera Nair", age=27, city="Chennai", area="Velachery", phone="9876543218"),
                    Agent(name="Ravi Teja", age=33, city="Hyderabad", area="Banjara Hills", phone="9876543219"),
                    Agent(name="Sneha Iyer", age=31, city="Bangalore", area="Electronic City", phone="9876543220"),
                    Agent(name="Amit Joshi", age=45, city="Mumbai", area="Borivali", phone="9876543221"),
                    Agent(name="Lakshmi Devi", age=36, city="Hyderabad", area="Secunderabad", phone="9876543222"),
                    Agent(name="Rahul Mehta", age=28, city="Pune", area="Wakad", phone="9876543223"),
                    Agent(name="Divya Kapoor", age=34, city="Delhi", area="Saket", phone="9876543224"),
                    Agent(name="Naveen Kumar", age=29, city="Hyderabad", area="LB Nagar", phone="9876543225"),
                    Agent(name="Priya Reddy", age=41, city="Chennai", area="Anna Nagar", phone="9876543226"),
                    Agent(name="Manoj Das", age=37, city="Bangalore", area="Marathahalli", phone="9876543227"),
                    Agent(name="Swathi Rao", age=24, city="Hyderabad", area="Uppal", phone="9876543228"),
                    Agent(name="Karthik Sharma", age=39, city="Mumbai", area="Powai", phone="9876543229"),
                
                 ]

        db.add_all( agents)
        db.commit()
        print("Database connection successful. Number of agents:", len(agents))

    except Exception as e:
        print("Database connection failed:", str(e))
    finally:
        db.close()