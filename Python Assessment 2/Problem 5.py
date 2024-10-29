matrix = {
    20 : [100, 96.8, 92.6, 86.7, 78.8, 68.2, 54.4, 37.5, 21.3, 8.3],
    19 : [96.1, 93.3, 89.2, 83.9, 76.7, 66.6, 53.5, 37.3, 21, 8.3],
    18 : [92.2, 89.6, 85.9, 81.1, 74.2, 65, 52.7, 36.9, 21, 8.3],
    17 : [88.2, 85.7, 82.5, 77.9, 71.7, 63.3, 51.6, 36.6, 21, 8.3],
    16 : [84.1, 81.8, 79, 74.7, 69.1, 61.3, 50.4, 36.2, 20.8, 8.3],
    15 : [79.9, 77.9, 75.3, 71.6, 66.4, 59.2, 49.1, 35.7, 20.8, 8.3],
    14 : [75.4, 73.7, 71.4, 68, 63.4, 56.9, 47.7, 35.2, 20.8, 8.3],
    13 : [71, 69.4, 67.3, 64.5, 60.4, 54.4, 46.1, 34.5, 20.7, 8.3],
    12 : [66.4, 65, 63.3, 60.6, 57.1, 51.9, 44.3, 33.6, 20.5, 8.3],
    11 : [61.7, 60.4, 59, 56.7, 53.7, 49.1, 42.4, 32.7, 20.3, 8.3],
    10 : [56.7, 55.8, 54.4, 52.7, 50, 46.1, 40.3, 31.6, 20.1, 8.3],
    9 : [51.8, 51.1, 49.8, 48.4, 46.1, 42.8, 37.8, 30.2, 19.8, 8.3],
    8 : [46.6, 45.9, 45.1, 43.8, 42, 39.4, 35.2, 28.6, 19.3, 8.3],
    7 : [41.3, 40.8, 40.1, 39.2, 37.8, 35.5, 32.2, 26.9, 18.6, 8.3],
    6 : [35.9, 35.5, 35, 34.3, 33.2, 31.4, 29, 24.6, 17.8, 8.1],
    5 : [30.4, 30, 29.7, 29.2, 28.4, 27.2, 25.3, 22.1, 16.6, 8.1],
    4 : [24.6, 24.4, 24.2, 23.9, 23.3, 22.4, 21.2, 18.9, 14.8, 8],
    3 : [18.7, 18.6, 18.4, 18.2, 18, 17.5, 16.8, 15.4, 12.7, 7.4],
    2 : [12.7, 12.5, 12.5, 12.4, 12.4, 12, 11.7, 11, 9.7, 6.5],
    1 : [6.4, 6.4, 6.4, 6.4, 6.4, 6.2, 6.2, 6, 5.7, 4.4]
}
# y = overs available, x = wickets loss
#team 2 score = team 1 score * (team 2 resources / team 1 resources)
t1_overs = int(input('Number of overs played by Team 1: '))
#using " and ' interchangebly due to need of ' in some inputs
t1_score = int(input("Team 1's total run: "))
t1_loss = int(input("Team 1's wicket loss: "))
t2_Aovers = int(input('Number of available overs for Team 2: '))
#we are assuming team two has not played yet so losses = 0
t2_loss = 0
#calculates the resources of both teams, using the matrix values as the columns of the table, and the matrix keys as the rows of the table
# this is can be done without editing the numbers since losses start at 0, which is the same as list indexing
t1_resources = matrix[t1_overs][t1_loss]
t2_resources = matrix[t2_Aovers][t2_loss]
print(f" Team 1's resources = {t1_resources}, Team 2's resources (the chasing team) = {t2_resources}")
#Using the provided formula to calculate the revised target of team 2 i.e the chasing team
t2_score = t1_score * (t2_resources / t1_resources)
print(f'Revised target for chasing team in 20 over games = {round(t2_score)} (rounded to nearest whole number)')
