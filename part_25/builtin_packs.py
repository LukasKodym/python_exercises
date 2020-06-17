# %%
##
import calendar as cal
from datetime import date as dt

# %%
##
s = cal.calendar(2020)

print(s)

# %%
##
s = cal.month(2020, 6)

print(s)

# %%
##
d_1 = dt.date(2020, 6, 1)
d_2 = dt.date(2020, 7, 18)

print(d_2 - d_1)


# %%
##
