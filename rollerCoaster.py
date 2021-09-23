import pandas as pd
from matplotlib import pyplot as plt

wood_winners = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_winners = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
coaster_data = pd.read_csv('roller_coasters.csv')


wood_rankings = wood_winners[['Rank', 'Name', 'Park', 'Year of Rank']]
steel_rankings = steel_winners[['Rank', 'Name', 'Park', 'Year of Rank']]
    
# write function to plot rankings over time for 1 roller coaster
def PlotCoasterRankingOverTime(CoasterName, ParkName, Rankings, Type):
    CoasterRankings = Rankings[(Rankings.Name == CoasterName) & \
                               (Rankings.Park == ParkName)]
    ax = plt.subplot()
    plt.plot(range(len(CoasterRankings['Year of Rank'])), CoasterRankings.Rank, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title(CoasterName + ', ' + ParkName + ", " + Type + " Coaster")
    ax.invert_yaxis()
    ax.set_xticks(range(len(CoasterRankings['Year of Rank'])))
    ax.set_xticklabels(CoasterRankings['Year of Rank'])
    ax.set_yticks(CoasterRankings.Rank)
    plt.show()
    plt.clf()

# write function to plot rankings over time for 2 roller coasters
def PlotTwoCoasterRankingsOverTime(Coaster1Name, Park1Name, Coaster2Name, \
                                  Park2Name, Rankings, Type):
    #Find the rankings for the unique name/park pairs
    Coaster1Rankings = Rankings[(Rankings.Name == Coaster1Name) & \
                               (Rankings.Park == Park1Name)]
    Coaster2Rankings = Rankings[(Rankings.Name == Coaster2Name) & \
                               (Rankings.Park == Park2Name)]
    ax = plt.subplot()
    plt.plot(Coaster1Rankings['Year of Rank'], Coaster1Rankings.Rank, marker='o')
    plt.plot(Coaster2Rankings['Year of Rank'], Coaster2Rankings.Rank, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title(Coaster1Name + ' VS ' + Coaster2Name + ', ' + Type + " Coasters")
    plt.legend([Coaster1Name + ', ' + Park1Name, Coaster2Name + ', ' \
                + Park2Name], loc='best')
    ax.invert_yaxis()
    plt.show()
    plt.clf()
    
# write function to plot top n rankings over time
def PlotCoastersRankedOverNvsTime(n, Rankings):
    #save all coasters with a ranking <= n in new dataframe
    CoasterRankedOverN = Rankings[(Rankings.Rank <= n)].reset_index()
    ax = plt.subplot()
    #find all 'unique' coasters based on Name and Park pairs
    UniqueCoasters = CoasterRankedOverN.groupby(['Name','Park']).size().reset_index()
  
    for row in UniqueCoasters.index:
       CoasterRankings = CoasterRankedOverN[(CoasterRankedOverN['Name'] == \
                         UniqueCoasters['Name'][row]) & \
                         (CoasterRankedOverN['Park'] == \
                          UniqueCoasters['Park'][row])]
       plt.plot(CoasterRankings['Year of Rank'], CoasterRankings.Rank, \
               label=UniqueCoasters['Name'][row], marker='o')
    ax.invert_yaxis()
    plt.title('Coasters Ranked ' + str(n) + ' and Up')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend(loc='best')
    plt.show()
    plt.clf()
    
# write function to plot histogram of column values
def PlotRollerCoasterHistogram(data, column_name):
 
    plt.hist(data[column_name].dropna())
    plt.xlabel(column_name)
    plt.ylabel('Number Coasters')
    plt.title('Coaster Data Histogram')
    plt.show()
    plt.clf()
    
#plot the histogram for height
def PlotCoasterInversionsBarGraph(data, park_name):
    InversionsForPark = data[data.park == park_name]
    ax = plt.subplot()
    plt.bar(range(len(InversionsForPark.num_inversions)),InversionsForPark.num_inversions)
    plt.xlabel('Coasters')
    plt.ylabel('Number of Inversions')
    plt.title(park_name)
    ax.set_xticks(range(len(InversionsForPark.num_inversions)))
    ax.set_xticklabels(InversionsForPark.name, rotation=90)
    plt.show()
    plt.clf()

def PlotPieChartOfOpenClosedCoasterStatusAtAllParks(data):
    num_closed = data[data.status == 'status.closed.definitely'].status.count()
    num_open = data[data.status == 'status.operating'].status.count()
    plt.pie([num_open,num_closed], labels=['Operating','Closed'], autopct='%0.2f%%')
    plt.title('Percentage of Operating VS Closed Roller Coasters')
    plt.axis('equal')
    plt.show()
    plt.clf()
    
 
def PlotPieChartOfAllCoasterStatusAtAllParks(data):
    status_counts = data.groupby(['status']).name.count().reset_index()
 
    plt.pie(status_counts['name'])
    plt.title('Status Percentages for all Roller Coasters')
    #bbox_to_anchor moves legend off of pie chart
    plt.legend(status_counts['status'], bbox_to_anchor=(-0.1, 1.))
    plt.axis('equal')
    plt.show() 
    plt.clf()


def PlotScatterChartofTwoDataSets(data, col1_name, col2_name):
    plt.scatter(data[col1_name], data[col2_name])
    plt.title('Scatter Plot Comparing Coaster ' + col1_name + ' with ' + col2_name)
    plt.xlabel(col1_name)
    plt.ylabel(col2_name)
    plt.show()
    plt.clf()


def MostPopularSeatingsTypePieGraph(data):

    seating_types = data.groupby('seating_type').size().reset_index()
    
    seating_types.rename(columns={0:'Count'}, inplace=True)
    plt.figure(figsize=(8,8))
    plt.pie(seating_types.Count, labels=seating_types.seating_type,\
            rotatelabels=True, autopct='%0.1f%%', pctdistance=.95)
    plt.title('Most Popular Coaster Seating Types')
    plt.axis('equal')
    plt.show()
    plt.clf()
 

def PlotSeatingData(data, col_name):
    sit_down_data = data[(data.seating_type == 'Sit Down') & \
                        (data[col_name] != 0)].dropna().reset_index()
    inverted_data = data[(data.seating_type == 'Inverted') & \
                        (data[col_name] != 0)].dropna().reset_index()
    spinning_data = data[(data.seating_type == 'Spinning') & \
                        (data[col_name] != 0)].dropna().reset_index()
    ax = plt.subplot()
    plt.bar(range(3), [sit_down_data[col_name].mean(), inverted_data[col_name].mean(), spinning_data[col_name].mean()])
    plt.title('Roller Coaster Seating Types')
    plt.ylabel('Average ' + col_name)
    ax.set_xticks(range(3))
    ax.set_xticklabels(['Sit Down', 'Inverted', 'Spinning'])
    plt.show()
    plt.clf()
    
def PlotManufacturerData(data, builder):
    builder_data = data[data.manufacturer == builder]
    avg_height = builder_data.height.mean()
    avg_speed = builder_data.speed.mean()
    avg_length = builder_data.length.mean()
    avg_inversions = builder_data.num_inversions.mean()

    if avg_inversions < 1:
        avg_inversion_text = '< 1'
    else:
        avg_inversion_text = str(round(avg_inversions))
    ax = plt.subplot()
    plt.bar(range(4), [avg_height, avg_speed, avg_length, avg_inversions])
    
    ax.text(0, avg_height + 5, str(round(avg_height,2)), horizontalalignment='center', fontsize=12)
    ax.text(1, avg_speed + 5, str(round(avg_speed,2)), horizontalalignment='center', fontsize=12)
    ax.text(2, avg_length + 5, str(round(avg_length,2)), horizontalalignment='center', fontsize=12)
    ax.text(3, avg_inversions + 5, avg_inversion_text, horizontalalignment='center', fontsize=12)
    ax.set_xticks(range(4))
    ax.set_xticklabels(['Avg Height(m)', 'Avg Speed (kmh)', 'Avg Length (km)', 'Avg # of Inversions'], rotation=90)
    plt.title('Averages on ' + str(len(builder_data)) + ' Coasters for Manufacturer: ' + builder)
    plt.show()
    plt.clf()
    
def PlotTop20sByPark(data, col_name):
    
    park_data = data[data[col_name] != 0].groupby('park')[col_name].max().dropna().reset_index()
    
    top_20_park_data = park_data[col_name].nlargest(n=20).reset_index()

    top_20_park_names = []
    for row in range(len(top_20_park_data)):
        top_20_park_names.append(park_data.iloc[int(top_20_park_data['index'][row])].park)
    ax = plt.subplot()

    plt.plot(range(len(top_20_park_data)), top_20_park_data[col_name])
    ax.set_xticks(range(len(top_20_park_data)))
    ax.set_xticklabels(top_20_park_names, rotation = 90)
    plt.ylabel(col_name)

    if col_name == 'speed':
        plt.title('Top 20 Parks with Fastest Coasters')
    elif col_name == 'height':
        plt.title('Top 20 Parks with Heighest Coasters')
    elif col_name == 'length':
        plt.title('Top 20 Parks with Longest Coasters')
    else: 
        plt.title('Top 20 Parks with Coasters having most Inversions')
    plt.show()
    plt.clf()
      