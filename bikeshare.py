import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello our dear! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            city=str(input('would you like to see data for chicago,new york,or washington?\n')).lower()
            if city in CITY_DATA:
                break
            else:
                print('Sorry invalid input x_x:try again')
                
        except:
            print('sorry x_x:try again')

   
    while True:
        try:
            month=str(input('would you like to filter the data by month (yes or no)?\n')).lower()
            if month in['no','yes']:
                month='all'
                break
            elif month =='yes':
                while True:
                    month=str(input('which month?January,February,March,April,May,or June?\n')).title()
                    if month in months:
                        break
                    else:
                        print('sorry invalid input x_x:try again')
                 break
                
            else:
                print('sorry invalid input x_x:try again')
                
         except:
            print('sorry invalid input x_x:try again')
     
    while True:
        try:
            day=str(input('would you like to filter the data(yes or no)?\n')).lower()
            if day in['yes','no']:
                if day=='no':
                    day='all'
                    break
                    
                elif day =='yes':
                    while True:
                        day=str(input('which day?Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,or Saturday\n')).title()
                        if day in days:
                            break
                        else:
                            print('sorry invalid input x_x:try again')
                    break
             else:
                print('sorry invalid input x_x:try again')
                
           except:
            print('sorry invalid input x_x:try again')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    #convert to data time
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    #create month column
    df['month']=df['Start Time'].dt.month
    
    #create day column
    df['hour']=df['Start Time'].dt.hour
    
    if month != 'all':
        month=months.index.index(month.title())+1
        df=df[df['month'] ==month]
    if day != 'all':
        df=df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    most_common_month=df['month'].mode()[0]
    count_most_common_month=df['month'].value_counts()
[most_common_month]


     
    most_common_day=df['day'].mode()[0]
    count_most_common_day=df['day'].value_counts()
[most_common_day]

    
    most_common_hour=df['hour'].mode()[0]
    count_most_common_hour=df['hour'].value_counts()
[most_common_hour]
    print("The mostcommon month:{},count{}\nThe most common day:{}".format(month[most_common_month],count_most_common_month,most_common_day,count_most_common_day,most_common_hour,count_most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     
    most_start_station=df['Start Station'].ode()[0]
    count_most_start_station=df['Start Station'].value_counts()[most_start_station]


    
    most_end_station=df['End station'].mode()[0]
    count_most_end_station=df['End Station'].value_counts()
    [most_end_station]

     
    most_start_and_end_station=df[['Start Station','End Station']].mode().iloc[0]
    print("The most common start station:{},count{} \nThe most common end station:{},count{} \nThe most frequent combination of start station: {} and end station: {} trip".format(most_start_station,count_most_start_station,most_end_station,count_most_end_station,most_start_and_end_station['Start Station'],most_start_and_end_station['End Station']))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     
    total_travel_time=df['Trip Duration'].sum()

     
    mean_travel_time=df['Trip Duration'].mean()
    
    print("Trip Duration: {},mean travel time{}".format(total_travel_time,mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    counts_user_types=df['User Type'].value_counts()


     
    count_of_gender=df['Gender'].value_counts()


     
    earliest_birth_year=df['Birth Year'].min()
    most_recent_birth_year=df['Birth Year'].max()
    most_common_birth_year=df['Birth Year'].mode()[0]
    print("counts of user types \n{}\ncounts of gender \n{}\nThe earliest birth year is: {}\nThe most recent birth year is {}\nThe most common birth year is {}.format(counts_user_types,count_of_gender,earliest_birth_year,most_recent_birth_year,most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
          
        if  'Gender' in df:
             user_stats(df)
        head=0
        size=4
          
        while True:
            try:
               view_trip_data=str(input('Would you like to view individual trip data?(yes or no)\n')).lower()
               if view_trip_data in ['yes','no']:
                  if view_trip_data == 'yes':
                     print(df.loc[head:head+size])
                     head+=size+1
                  else:
                      break
              else:
                  print('sorry invalid input x_x:try again')
            except:
                 print('sorry invalid input x_x:try again')
          
        check=0
       

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
