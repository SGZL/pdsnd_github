import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june']
days =['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def breakline():
    print('-'*40)

def salutations():
    print('Hello! Let\'s explore some US bikeshare data!')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    salutations()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
        if city in CITY_DATA:
            break
        else:
            print('You entered an invalid city\n')
            continue


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter by month or all? enter month or all for all months\n').lower()
        if month == 'month':
            while True:
                month = input('which month?\n').lower()
                if month in months:
                    break
                else:
                    print('You entered an invalid month\n')
                    continue
            break
        elif month == 'all':
            break
        else:
            print('You entered an invalid filter option')
            continue
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('which day or all ? enter the day or all for all days of the week etc\n').lower()
        if day in days:
            break
        elif day == 'all':
            break            
        else:
            print('You entered an invalid day\n')
            continue


    breakline()
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
    #load data file into dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    #convert the start time column into  datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    #extract month from Start Time to create new column
    df['month']=df['Start Time'].dt.month
    
    #extract day from Start Time to create to new column
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    #extract hour from Start Time to create to new column
    df['hour']=df['Start Time'].dt.hour
    
    #filter by month
    if month !='all':
        month = months.index(month)+1
        df=df[df['month']==month]
    
    #filter by weekday
    if day !='all':
        df=df[df['day_of_week']==day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = months[int(df['month'].mode()[0])-1].title()
    print("The most common month is {}\n".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print("The most common day of week is {}\n".format(most_common_weekday))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour is {}\n".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    breakline()


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}\n".format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}\n".format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station']+' --AND-- '+df['End Station']
    most_common_start_end_station = df['start_end_station'].mode()[0]
    print("The most common end station is {}\n".format(most_common_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    breakline()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time is: {}\n".format(total_travel_time))
    


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time is: {}\n".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    breakline()


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)       
    


    # TO DO: Display counts of gender    
    if 'Gender' in df.columns:
        gender=df['User Type'].value_counts()
        print(gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth=df['Birth Year'].dropna(axis=0)
        earliest_birth = birth.min()
        recent_birth = birth.max()
        most_common_year = birth.mode()[0]
        print('earliest year of birth: {}'.format(earliest_birth))
        print('most recent year of birth: {}'.format(recent_birth))
        print('most_common_year: {}'.format(most_common_year))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    breakline()

def display_rows(df):
    """Display data in rows of fives"""
    i=0
    while True:    
        display=input('Type YES to see initial five data rows/five more rows else press No\n').lower()
        if display== 'yes':
            print(df.iloc[i:i+5])
            i+=5
        else:
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
