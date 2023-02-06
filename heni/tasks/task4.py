# flights connects to planes via a single variable, tailnum.
# flights connects to airlines through the carrier variable.
# flights connects to airports in two ways: via the origin and dest variables.
# flights connects to weather via origin (the location), and year, month, day, and hour (the time).
#
#Task 1:
#Inner Join: will return all rows matching in both tables
#Left Join: will return all rows from left table -no matter if there is a match or not-
#Right Join: will return all rows from right table -no matter if there is a match or not-
#Full Join: will return all rows from BOTH tables 
#
#Task 2:
#Add full airline name to the flights dataframe and show the arr_time, origin, dest and the name of the airline.
#Filter resulting data.frame to include only flights containing the word JetBlue
#Summarise the total number of flights by origin in ascending.
#Filter resulting data.frame to return only origins with more than 100 flights.
#
import pandas as pd

flights = pd.read_csv("heni/resources/flights.csv")
airports = pd.read_csv("heni/resources/airports.csv")
weather = pd.read_csv("heni/resources/weather.csv")
airlines = pd.read_csv("heni/resources/airlines.csv")

join = airlines.join( flights.set_index( [ 'carrier' ] ),on=[ 'carrier' ], how='right' )

jetblue = join.query("name.str.contains('JetBlue')")

group = jetblue.groupby(['origin'])['origin'].count().reset_index(name='numFlights').sort_values(['numFlights'], ascending=True)

last = group.query("numFlights > 100")
last.to_csv("output_task4.csv", index=False)