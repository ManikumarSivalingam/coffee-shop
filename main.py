import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("sqlitecloud://cp2dejwkvz.g5.sqlite.cloud:8860/coffee-shop?apikey=A0eyHwO1z6rgD77c5tRAZyb1bZ8LvJ75Vmlrnc9saAY")

df_users = pd.read_sql("SELECT * FROM users", engine)
print("Users DataFrame:")
print(df_users)
df_things = pd.read_sql("SELECT * FROM things", engine)
print("Things DataFrame:")
print(df_things)

# new_user = pd.DataFrame({
#     "firstname": "Alice",
#     "lastname": "Johnson",
#     "email": "alice.johnson@example.com",
#     "password": "alicepassword"
# }, index=[0])
# new_user.to_sql('users', engine, if_exists='append', index=False)

