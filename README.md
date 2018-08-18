# ClickStreamAnalysis
## How to run this project?
### Change the DATAPATH to your current path and then run the function with the corresponding arguments
1. DataAnalysis.py
  Read the data in and participate the data by the date, thus we get 26 days data for 4 weeks. I saved them in the /DaySlice folder.
2. DataProcessing.py
  Calculate every user's activity record in the format of a m * n matrix (m = Number of Activity (13), n = Number of the day (26)), demonstrating how many times for each type of link the user has clicked everyday, and save them in the /GroupsData folder.
3. RemoveUseless.py
  Remove the users who don't appear in the Groups for ProjectA.txt since there are other students from another Project to choose this course.
4. GroupInfo.py
  Read the Groups for ProjectA.txt in and get the relation between each user and the group they belonging to. And create the directories for every groups in /GroupsPlot. And draw the daily click stream line plot for each group (calculated by the each group member's data) and save the plot in its corresponding group folder.
5. Plot.py
  Based on the group matrix and the UsersData, draw the click stream line plot for each user, named by the user's id, and save them in the corresponding group folder.
6. GroupBarPlot.py
  EasyBarPlot()
  Draw the group's clustered stack plot for the daily overall click. Name them by Overall Click Stack.png and save them in the corresponding group folder.
  DifficultBarPlot()
  Draw the each week's clustered stack plot to demonstrate how many and what type of clicks for each user have clicked. Named them by Week$n Clustered Stack.png and save them in corresponding folder.
